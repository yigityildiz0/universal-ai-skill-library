# Module: result

> Upstream parallel-web/parallel-agent-skills skill, unchanged. Paths are relative to this module folder.
> Original trigger scope: Get completed research task result by run ID

# Get Research Result

## Run ID: $ARGUMENTS

```bash
parallel-cli research poll "$ARGUMENTS" --json
```

Present results in a clear, organized format.

If CLI not found, tell user to run `/parallel:parallel-cli-setup`.
