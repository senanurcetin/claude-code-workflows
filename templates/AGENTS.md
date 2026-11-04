# AGENTS.md

Instructions for AI coding agents (Claude Code, Codex, ...) and humans working in this repository.
Adapted from the one used in [offline-jsonl-workshop](https://github.com/senanurcetin/offline-jsonl-workshop/blob/main/AGENTS.md).

## Project contract
- <What the project must never do: e.g. no network calls, no new dependencies, no credentials.>
- <Privacy rule: e.g. never print input records; error messages must not leak data.>

## Commands (run from repository root)
```sh
<test command>
<lint / type-check command>
<any release or integrity check>
git diff --check
```

## Rules
- For a behaviour defect, add a failing regression test first, then the smallest fix.
- Use synthetic fixtures only. No private data, tokens or backup files.
- Do not edit generated checksums or snapshots to hide an unexplained failure.
- Disclose AI assistance in the PR description and in `docs/AI_ASSISTANCE_LOG.md`.
- Report only checks you actually ran; write "not run" for the rest.
