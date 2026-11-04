# Claude Code workflows

How I use [Claude Code](https://claude.com/claude-code) for open-source and data/ML engineering work, with links to public evidence you can check. Everything here is reusable under the MIT license.

## Contents

| Path | What it is |
| --- | --- |
| [`skills/upstream-pr-evidence/SKILL.md`](skills/upstream-pr-evidence/SKILL.md) | A Claude Code skill for preparing upstream PRs and answering review: red/green tests, diagnosing red CI before touching code, honest verification reports. |
| [`templates/AGENTS.md`](templates/AGENTS.md) | Agent instructions template (project contract, commands, rules). |
| [`templates/AI_ASSISTANCE_LOG.md`](templates/AI_ASSISTANCE_LOG.md) | Per-PR log of AI-assisted changes with verified results. |

Install the skill for your user:

```sh
mkdir -p ~/.claude/skills/upstream-pr-evidence
curl -fsSL https://raw.githubusercontent.com/senanurcetin/claude-code-workflows/main/skills/upstream-pr-evidence/SKILL.md \
  -o ~/.claude/skills/upstream-pr-evidence/SKILL.md
```

## Public evidence

**A small project built with Claude Code, end to end:** [offline-jsonl-workshop](https://github.com/senanurcetin/offline-jsonl-workshop) — a dependency-free UTF-8 JSONL validator. Its [AI assistance log](https://github.com/senanurcetin/offline-jsonl-workshop/blob/main/docs/AI_ASSISTANCE_LOG.md) links each Claude Code change to its PR and CI result, including one mistake (committed `.pyc` files) and its fix.

**Contributions to the Claude Agent SDK** (open, under review):
- [anthropics/claude-agent-sdk-python#1421](https://github.com/anthropics/claude-agent-sdk-python/pull/1421) — interpret naive transcript timestamps as UTC.
- [anthropics/claude-agent-sdk-python#1468](https://github.com/anthropics/claude-agent-sdk-python/pull/1468) — sidechain flag parity between the disk fast path and in-memory session folding.

**Upstream data/ML contributions:** merged PRs to xarray, pyjanitor, scipy, Altair, DuckDB docs and plotly.py. Live list: [merged PRs outside my own repositories](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+is%3Amerged+-user%3Asenanurcetin&type=pullrequests).

**Read-only CI evidence tool:** [nexus-devops-intelligence](https://github.com/senanurcetin/nexus-devops-intelligence) — reports GitHub check/status records for one exact commit SHA, with explicit unknown states.

## Principles
- Tests before claims: a change is "done" when a regression test fails before and passes after.
- A red check is investigated before code is changed; pre-existing and infrastructure failures are named as such.
- AI assistance is disclosed; only checks that actually ran are reported.

## License
[MIT](LICENSE)
