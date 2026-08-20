# Architecture Design — Extended Guidance

### Step 6: Define Architecture Fitness Functions

Fitness functions are automated checks that verify the architecture stays within its design constraints.

**Dependency Rule Fitness Function** (Python with pytest):

```python
# tests/architecture/test_dependency_rules.py
import ast
import os
from pathlib import Path

LAYER_ORDER = ["presentation", "application", "domain", "infrastructure"]

def get_imports(filepath: str) -> list[str]:
    """Extract all import module paths from a Python file."""
    with open(filepath) as f:
        tree = ast.parse(f.read())
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.append(node.module)
    return imports

def layer_of(module_path: str) -> int | None:
    """Return the layer index for a module, or None if not in a layer."""
    for i, layer in enumerate(LAYER_ORDER):
        if f".{layer}." in module_path or module_path.startswith(layer):
            return i
    return None

def test_no_upward_dependencies():
    """Domain must not import from application or presentation.
    Application must not import from presentation."""
    violations = []
    for py_file in Path("src").rglob("*.py"):
        file_layer = layer_of(str(py_file))
        if file_layer is None:
            continue
        for imp in get_imports(str(py_file)):
            imp_layer = layer_of(imp)
            if imp_layer is not None and imp_layer < file_layer:
                violations.append(
                    f"{py_file} (layer {LAYER_ORDER[file_layer]}) "
                    f"imports {imp} (layer {LAYER_ORDER[imp_layer]})"
                )
    assert not violations, (
        "Upward dependency violations:\n" + "\n".join(violations)
    )

def test_domain_has_no_framework_imports():
    """Domain layer must not depend on any framework or infrastructure."""
    FORBIDDEN = {"flask", "django", "fastapi", "sqlalchemy", "boto3", "redis"}
    violations = []
    for py_file in Path("src/domain").rglob("*.py"):
        for imp in get_imports(str(py_file)):
            root_package = imp.split(".")[0]
            if root_package in FORBIDDEN:
                violations.append(f"{py_file} imports {imp}")
    assert not violations, (
        "Domain layer framework violations:\n" + "\n".join(violations)
    )
```

**Coupling Metrics Fitness Function** (Java with ArchUnit):

```java
// src/test/java/com/example/architecture/ArchitectureTest.java
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;
import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.*;
import static com.tngtech.archunit.library.Architectures.layeredArchitecture;

public class ArchitectureTest {

    @Test
    void layered_architecture_is_respected() {
        ArchRule rule = layeredArchitecture()
            .consideringAllDependencies()
            .layer("Presentation").definedBy("..presentation..")
            .layer("Application").definedBy("..application..")
            .layer("Domain").definedBy("..domain..")
            .layer("Infrastructure").definedBy("..infrastructure..")
            .whereLayer("Presentation").mayNotBeAccessedByAnyLayer()
            .whereLayer("Application").mayOnlyBeAccessedByLayers("Presentation")
            .whereLayer("Domain").mayOnlyBeAccessedByLayers(
                "Application", "Infrastructure")
            .whereLayer("Infrastructure").mayNotBeAccessedByAnyLayer();

        rule.check(new ClassFileImporter()
            .importPackages("com.example"));
    }

    @Test
    void domain_does_not_depend_on_spring() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("org.springframework..")
            .check(new ClassFileImporter()
                .importPackages("com.example.domain"));
    }
}
```

**Cyclic Dependency Check** (generic, CI-friendly):

```bash
#!/usr/bin/env bash
# scripts/check-cyclic-deps.sh
# Fails CI if circular package dependencies are detected.

set -euo pipefail

echo "Checking for cyclic dependencies..."

# Python projects
if command -v pydeps &> /dev/null; then
    pydeps src --no-show --no-output --check-circular
    echo "No circular dependencies found (Python)."
fi

# Java/Gradle projects
if [ -f "build.gradle" ]; then
    ./gradlew dependencyInsight --configuration compileClasspath \
      | grep -i "circular" && { echo "FAIL: Circular dependency detected"; exit 1; }
    echo "No circular dependencies found (Java)."
fi

# Node.js projects
if command -v madge &> /dev/null; then
    CYCLES=$(madge --circular --extensions ts,js src/)
    if [ -n "$CYCLES" ]; then
        echo "FAIL: Circular dependencies detected:"
        echo "$CYCLES"
        exit 1
    fi
    echo "No circular dependencies found (Node.js)."
fi
```
