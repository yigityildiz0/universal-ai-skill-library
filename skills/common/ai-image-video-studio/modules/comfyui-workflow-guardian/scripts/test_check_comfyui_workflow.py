"""Offline regression checks; no ComfyUI, GPU, models or network required."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from check_comfyui_workflow import validate, resolve_existing_file


class WorkflowChecks(unittest.TestCase):
    def ui(self):
        return {"nodes": [{"id": 1, "type": "Source", "outputs": [{"links": [7]}]},
                          {"id": 2, "type": "Sink", "inputs": [{"link": 7}]}],
                "links": [[7, 1, 0, 2, 0, "IMAGE"]]}

    def api(self):
        return {"1": {"class_type": "Source", "inputs": {}},
                "2": {"class_type": "Sink", "inputs": {"image": ["1", 0]}}}

    def test_recognized_valid_formats(self):
        for data, fmt in ((self.ui(), "ui"), (self.api(), "api"), ({"prompt": self.api()}, "api")):
            result = validate(data, structure_only=True)
            self.assertEqual((result["format"], result["nodes"], result["exit_code"]), (fmt, 2, 0))
            self.assertFalse(result["runtime_validated"])

    def test_empty_unknown_and_invalid_node(self):
        for data in ({}, [], {"nodes": []}, {"arbitrary": 3}, {"nodes": [None]}, {"nodes": "bad"}):
            self.assertEqual(validate(data, structure_only=True)["exit_code"], 1)

    def test_bad_api_links_and_types(self):
        for link in (["404", 0], ["1", -1], ["1", True], ["1"], ["1", 0, 1]):
            data = self.api()
            data["2"]["inputs"]["image"] = link
            self.assertEqual(validate(data, structure_only=True)["exit_code"], 1)
        data = self.api()
        data["2"]["inputs"] = []
        self.assertEqual(validate(data, structure_only=True)["exit_code"], 1)

    def test_bad_ui_links(self):
        for mutate in (lambda d: d["links"][0].__setitem__(1, 404),
                       lambda d: d["links"][0].__setitem__(2, 8),
                       lambda d: d["nodes"][1]["inputs"][0].__setitem__("link", 99),
                       lambda d: d["nodes"][1].__setitem__("id", 1),
                       lambda d: d["links"].append(copy.deepcopy(d["links"][0]))):
            data = self.ui()
            mutate(data)
            self.assertEqual(validate(data, structure_only=True)["exit_code"], 1)

    def test_ui_v1_link_records_and_nested_groups(self):
        data = self.ui()
        data["links"] = [dict(zip(("id", "origin_id", "origin_slot", "target_id", "target_slot", "type"), data["links"][0]))]
        data["groups"] = [{"id": 1, "bounding": [0, 0, 100, 100]}, {"id": 2, "bounding": [1, 1, 10, 10]}]
        result = validate(data, structure_only=True)
        self.assertEqual(result["exit_code"], 0)
        self.assertEqual(result["group_overlaps"], 1)

    def test_file_coverage_and_ambiguity(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            model = root / "models/checkpoints/a/model.safetensors"
            model.parent.mkdir(parents=True)
            model.write_bytes(b"mock")
            roots = ("models/checkpoints",)
            self.assertEqual(resolve_existing_file("a/model.safetensors", root, roots)["status"], "resolved")
            self.assertEqual(resolve_existing_file("model.safetensors", root, roots)["status"], "basename_only")
            other = root / "models/checkpoints/b/model.safetensors"
            other.parent.mkdir()
            other.write_bytes(b"mock")
            self.assertEqual(resolve_existing_file("model.safetensors", root, roots)["status"], "ambiguous")
            self.assertEqual(resolve_existing_file("a", root, roots)["status"], "missing")
            self.assertEqual(resolve_existing_file("../escape", root, roots)["status"], "invalid_path")
            graph = {"1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "a/model.safetensors"}}}
            self.assertEqual(validate(graph, root)["exit_code"], 0)
            graph["1"]["inputs"]["ckpt_name"] = "missing.safetensors"
            self.assertEqual(validate(graph, root)["exit_code"], 1)
            graph["1"]["class_type"] = "CustomModelLoader"
            self.assertEqual(validate(graph, root)["exit_code"], 2)
            self.assertEqual(validate(graph)["model_reference_status"], "not_checked")

    def test_cli_exit_codes(self):
        script = Path(__file__).with_name("check_comfyui_workflow.py")
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "workflow.json"
            for data, code in ((self.api(), 0), ({}, 1)):
                path.write_text(json.dumps(data), encoding="utf-8")
                result = subprocess.run([sys.executable, "-B", str(script), str(path), "--structure-only", "--json"], capture_output=True, text=True)
                self.assertEqual(result.returncode, code, result.stderr)
                self.assertEqual(json.loads(result.stdout)["exit_code"], code)
            path.write_text("{broken", encoding="utf-8")
            self.assertEqual(subprocess.run([sys.executable, "-B", str(script), str(path), "--json"], capture_output=True).returncode, 2)


if __name__ == "__main__":
    unittest.main()
