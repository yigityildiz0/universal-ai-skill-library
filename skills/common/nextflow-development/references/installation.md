# Nextflow and nf-core Environment Contract

Use current official documentation for installation commands, supported runtime versions, and container/HPC configuration. This reference deliberately does not embed a pipe-to-shell installer, a global package command, or a self-update command.

## Before changing an environment

1. Identify operating system, scheduler/container runtime, Java/runtime version, existing Nextflow/nf-core versions, project configuration, and storage/cache policy.
2. Preserve a working analysis environment. Create a separate test environment or module before changing versions.
3. Obtain installers/images only from official sources, inspect the artifact/URL, and ask before running install, sudo, service, group, shell-profile, or network-changing commands.
4. Record exact version, repository/tag, profile, config, container digest, reference build, samplesheet, and test result.

## Validate before full data

- Use the selected pipeline's documented test profile with a fresh, dedicated output directory.
- Check generated report, trace/timeline, logs, output tree, resource use, and expected sample count.
- Verify schema changes and parameter compatibility for a new release before promoting it to production analysis.
- Pin the exact passing tag/config; never infer compatibility from a version number alone.

## HPC and containers

Follow the institution's approved scheduler, container, cache, quota, and data-governance path. Do not change Docker permissions, system services, shell profiles, or shared module trees without the responsible administrator's approval.
