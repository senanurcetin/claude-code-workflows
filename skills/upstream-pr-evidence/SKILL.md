---
name: upstream-pr-evidence
description: Prepare, update or answer review on a pull request to a third-party open-source repository with reproducible evidence. Use when fixing a bug upstream, responding to maintainer review, or deciding whether a red CI check is caused by your change.
---

# Upstream PR with evidence

The goal is a pull request a maintainer can merge without re-doing your work, and an honest record of what was and was not verified.

## 1. Before writing code
- Find the issue. If none exists, open one or ask in an existing one whether the change is wanted.
- **Wait for a maintainer to agree on the scope before opening the PR.** Many projects (for example skrub and pyjanitor) state this in their contributing guide and close PRs that skipped it, even correct ones. Asking and then opening the PR straight away does not count.
- Do not open unsolicited PRs in a repository where you already have two or more open PRs.
- Read `CONTRIBUTING.md`, the PR template and the lint/format config (line length, tool versions).
- Check out the exact upstream base commit and record its SHA.

## 2. Red, then green
1. Reproduce the defect on the pinned base.
2. Add a regression test that fails on the base. Run it and keep the failure output.
3. Make the smallest change that makes it pass.
4. Run the targeted test file, then the neighbouring test modules that exercise the same code path.
5. Run the repository's own linters with its own configuration.

## 3. Interpreting red CI
Before changing code because a check is red, establish the cause:
- Is the same job red on the upstream default branch? (`gh api repos/OWNER/REPO/commits/main/statuses`) If yes, it is pre-existing; say so and do not "fix" it in your PR.
- Did the job run at all? Check-run annotations such as "job was not acquired by Runner" are infrastructure, not test failures.
- Does `mergeable` say CONFLICTING, or is that an old snapshot? Re-query before rebasing.
- Never push empty or trigger-only commits to re-run CI, and never bypass `action_required` approval for forks. Re-runs belong to maintainers.

## 4. Responding to review
- Confirm the finding against the current head, not the head the review was written on (compare `review.commit_id` with `git log`).
- If it is already fixed by a later commit, reply in the thread with the commit SHA and the test that covers it.
- If it is valid and unfixed: add a test for the reviewer's scenario first, then fix.
- Thank the reviewer; keep replies short and factual.

## 5. What to report
Use this block in the PR description or review reply:

```
Verified at <short SHA> (<OS>, <Python/Node version>):
- <command> -> <N passed / exit 0>
- <linter> (<config>) -> clean
Not verified: <full suite / other platforms / upstream CI>
AI assistance: <tool> used for <what>; a human reviewed <what>.
```

Report only checks you actually ran. "Not run" is a valid and useful answer.

## Anti-patterns
- Many small PRs to one repository in a short time.
- A docs-only PR that papers over a code problem (for example documenting a wrong return type instead of fixing the dtype handling).
- Counting open PRs as contributions.
- Claiming a test pass from a run that crashed before collecting tests (for example a temp-directory permission error).
