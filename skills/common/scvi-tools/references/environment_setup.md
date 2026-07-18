# scvi-tools Environment Contract

Verify the current official installation guidance before creating or changing an environment. scvi-tools evolves with Python, PyTorch, GPU, and optional-dependency compatibility; do not paste historical CUDA wheels, global upgrades, or fixed versions into a working analysis environment.

## Safe sequence

1. Inspect the operating system, Python version, existing environment manager, GPU/driver availability, project lock files, and current package versions.
2. Create a fresh, project-local or named isolated environment only after the user approves environment changes. Do not modify the system Python or an unrelated environment.
3. Select CPU, CUDA, or platform support from current official documentation and the actual hardware. Install PyTorch first only when the official compatibility path requires it.
4. Record the exact resolved versions, solver/channel/index choices, device check, and a minimal import/test result.
5. Treat an upgrade as a separate experiment: preserve the working environment, test with a small representative dataset, and promote only after validation.

## Common checks

- Confirm raw count requirements and AnnData/MuData format before model setup.
- Check package versions and device availability from inside the selected environment.
- Keep notebook kernels and CLI commands pointed at the same environment.
- Keep data, models, outputs, and environment metadata separate.

Use the official current installation documentation for commands and support matrices. Do not use this reference to justify a global install, a silent upgrade, or a CUDA change.
