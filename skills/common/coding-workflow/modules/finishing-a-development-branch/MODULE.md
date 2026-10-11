# Module: finishing-a-development-branch

> Part of `coding-workflow`. Paths are relative to `modules/finishing-a-development-branch/`.
> Trigger: Branch integration or workspace cleanup is requested or relevant after implementation. Turkish: geliştirme dalını bitir, merge/PR/temizlik seçenekleri.

# Finish a Development Branch

Verify the changed state, preserve original workspace identity, execute the authorized integration action, and clean up only an exactly identified owned workspace.

## 1. Inspect verification evidence

Reuse valid post-change checks from the current task; run missing repository-required checks appropriate to this change. A documentation edit need not run an unrelated application suite. Investigate failures with [systematic-debugging](../systematic-debugging/MODULE.md).

Unresolved required-check failures block merging and a passing claim. They do not block inspecting state, preserving a branch, or creating an explicitly authorized draft PR that discloses failures. Do not hand back a fixable test failure without investigation.

## 2. Capture identity before changing directory or branch

The following examples are **Bash**. In PowerShell use `$variable = ...`, `Set-Location`, and check `$LASTEXITCODE` after each Git command. Never paste Bash substitutions, `||`, or heredocs into an incompatible shell.

```bash
ORIGINAL_WORKTREE=$(git rev-parse --show-toplevel)
ORIGINAL_BRANCH=$(git symbolic-ref --quiet --short HEAD) # empty = detached HEAD
ORIGINAL_HEAD=$(git rev-parse HEAD)
ORIGINAL_GIT_DIR=$(git rev-parse --absolute-git-dir)
ORIGINAL_COMMON_DIR=$(git rev-parse --path-format=absolute --git-common-dir)
ORIGINAL_SUPERPROJECT=$(git rev-parse --show-superproject-working-tree)
git status --short
git worktree list --porcelain
OWNED_WORKTREE=false
# Set true only from this task's creation record or explicit user ownership grant.
```

Save these values and ownership evidence in task state BEFORE moving to the base worktree. Do not recompute the cleanup target from the new current directory.

- Equal original Git/common directories: normal repository; never remove its working directory.
- Different directories with no superproject: linked worktree. A submodule is not proof of a linked worktree.
- Detached HEAD: branch identity is absent; ownership is still independent of this fact.
- A path under `.worktrees`, `worktrees`, or a familiar configuration folder does **not** prove ownership.

Choose a verified integration worktree (`MAIN_ROOT`) from `git worktree list --porcelain`, not by appending `/..` to the common Git directory. Inspect its branch and working-tree status. Do not disturb unrelated user edits or change a branch checked out in another worktree.

Determine the actual base from PR/repository metadata or explicit instructions. Check `git merge-base <verified-base> ORIGINAL_HEAD`; do not guess main/master when multiple bases are plausible.

## 3. Resolve integration intent

Execute an already-authorized choice without another approval loop. If intent is unspecified, offer concise **named** actions:

- Merge locally into the verified base.
- Push and create a PR (draft when unresolved checks must be disclosed).
- Keep the branch/workspace as-is.
- Discard explicitly identified task work, with destructive confirmation.

Dispatch by action name, not menu number. Detached HEAD menus must not accidentally call another numbered action.

### Detached HEAD

Preserve the original commit and all uncommitted work. For an authorized merge/PR, create a non-conflicting named branch at the captured `ORIGINAL_HEAD` first. Recheck that current HEAD has not moved. Never push/delete an empty branch name. If naming a branch is not authorized or the harness owns the workspace, preserve it and report its commit/path; do not reset or remove it.

## 4. Execute the chosen action

### Merge locally

Ensure authorized changes are committed and the integration worktree is clean. Do not automatically commit unrelated/uncommitted user work. `FEATURE_BRANCH`, `BASE_BRANCH`, and `MAIN_ROOT` below must be verified values, not inferred placeholders.

```bash
cd "$MAIN_ROOT" || exit 1
git switch "$BASE_BRANCH" || exit 1
# Fetch/update only when needed and authorized; no unconditional git pull.
git merge "$FEATURE_BRANCH" || exit 1
# Run the repository's applicable checks on the merged state; stop cleanup on failure.
```

Inspect each command result. A failed merge/check never licenses removal or force reset. After successful integration and checks, cleanup an owned linked worktree as in Step 5. Delete only the confirmed original named feature branch with `git branch -d -- "$FEATURE_BRANCH"`, after it is no longer checked out. If an external worktree still uses it, keep the branch.

### Push and create PR

Verify remote, base, head, and publishing authorization. Search repository PR templates; summarize the actual diff and checks. Use available GitHub tooling or [github-cli-workflows](../github-cli-workflows/MODULE.md) when a CLI workflow is requested. A supported `gh` example:

```bash
git push -u origin "$FEATURE_BRANCH" || exit 1
gh pr create --base "$BASE_BRANCH" --head "$FEATURE_BRANCH" --title "<title>" --body "<summary and actual checks>"
# Add --draft when appropriate and disclose failing/missing checks.
```

Keep the worktree after PR creation unless separate cleanup was authorized. Report the actual PR URL and status, not a planned result.

### Keep as-is

Report the captured branch or detached commit, exact path, and check status. Leave workspace and branch intact.

### Discard

Show exact task branch/commits/path and any uncommitted/untracked files that would be lost. Obtain specific destructive confirmation unless that exact discard was already explicitly authorized. Never equate a general “finish” request with permission to discard.

For a normal repository, preserve user changes and switch to the verified base before deleting the confirmed task branch. For a linked worktree, require Step 5 ownership and path checks first. Detached HEAD has no branch to delete. Do not remove externally managed workspaces. If non-force removal fails because files remain, report those files and request a precise decision rather than escalating automatically.

## 5. Exact-path cleanup

Only a successfully verified merge or explicitly confirmed discard can reach cleanup. A PR or keep action preserves the workspace by default.

1. Use saved `ORIGINAL_WORKTREE`, branch/HEAD, Git directories, and ownership; never the post-`cd` working directory.
2. Require `OWNED_WORKTREE=true` with evidence and a registered linked worktree matching the saved exact path. A submodule or primary repository is never a removal target.
3. Recheck its current registration, HEAD/branch, status, and files. Unexpected changes block cleanup only; preserve them.
4. Move to the verified directory outside the target and remove without force:

```bash
cd "$MAIN_ROOT" || exit 1
git worktree remove "$ORIGINAL_WORKTREE" || exit 1
git worktree list --porcelain
```

5. Verify only the exact registration is gone. Do not run broad `git worktree prune`; removal unregisters this worktree itself.
6. Delete the confirmed named feature branch only when allowed and no worktree still uses it; use `-d` after merge. `-D` is for specifically confirmed discard only.

For harness/external ownership, use a supported workspace-exit operation if appropriate; otherwise leave it intact. Preserve original identity evidence in the final summary.

## Related modules

- [verification-before-completion](../verification-before-completion/MODULE.md)
- [using-git-worktrees](../using-git-worktrees/MODULE.md)
- [git-commit](../git-commit/MODULE.md)
