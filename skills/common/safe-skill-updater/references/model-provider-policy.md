# Model and Provider Policy

## Shared Core

- Use the active host's model and tools.
- Do not auto-switch providers, models, or reasoning levels.
- Do not invent "latest" model names or derive them from naming patterns.
- If a capability is unavailable, use a documented fallback or state the limitation.

## Platform Overlays

- Keep Codex/OpenAI configuration in a Codex-specific overlay.
- Keep Claude model/runtime fields in a Claude-specific overlay.
- Keep OpenCode provider selection dynamic because it can host many vendors.
- Do not migrate model strings across providers by search-and-replace.

## Verification

Before changing a model string:

1. identify the file's actual runtime and whether the string controls behavior or is only factual/example text;
2. verify the current valid identifier from official provider documentation or the live runtime;
3. change only the same runtime's active configuration;
4. leave historical examples, comparisons, fixtures, and unrelated fallbacks unchanged unless they are the task;
5. record skipped and unresolved strings.

Prefer capability language such as "the active model's supported reasoning levels" over fixed names when exact identity is not essential.
