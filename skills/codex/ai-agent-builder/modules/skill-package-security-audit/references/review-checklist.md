# Static review checklist

## Structure

- Exact archive or tree hash recorded before review.
- No absolute path, `..` traversal, drive-qualified path, alternate data stream,
  symlink escape, case-confusable duplicate, or extreme decompression ratio.
- Expected skill folder has one controlling `SKILL.md`; folder and declared name
  match; every referenced local file exists and stays within the skill folder.

## Capability inventory

- Files read, written, moved, deleted, or watched.
- Commands/processes spawned; interpreters and shell expansion used.
- Network domains, methods, payloads, uploads, downloads, telemetry, and update checks.
- Credentials, tokens, cookies, browser profiles, account data, clipboard, camera,
  microphone, location, and personal or confidential files accessed.
- Startup tasks, services, hooks, scheduled work, registry/config changes, or
  other persistence.
- Privilege elevation, sandbox bypass, permission broadening, or delegated agents.

## Instruction integrity

- Actual behavior matches title, description, README, and requested task.
- No instruction asks the reviewer or host to ignore higher-priority rules,
  conceal actions, misstate verification, expose secrets, or run encoded text.
- Untrusted filenames, prompts, repository text, or web content cannot become
  shell commands, paths outside containment, or tool arguments without validation.
- External writes, messages, purchases, submissions, publication, or destructive
  actions require explicit task-scoped authorization.

## Supply chain and rollback

- Publisher, repository, tag/commit, checksum/signature, license, and dependency
  ownership are recorded.
- Dependencies are pinned where reproducibility or security needs it; install
  hooks and vendored executables are inspected.
- Exact target paths, name collisions, host precedence, backup, restore, and
  post-install verification are defined before any authorized installation.
