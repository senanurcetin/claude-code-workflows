"""Validate skill frontmatter and relative Markdown links. Standard library only."""
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
errors = []

for skill in sorted(root.glob("skills/*/SKILL.md")):
    text = skill.read_text(encoding="utf-8")
    match = re.match(r"---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        errors.append(f"{skill}: missing YAML frontmatter")
        continue
    fields = dict(
        line.split(":", 1) for line in match.group(1).splitlines() if ":" in line
    )
    fields = {k.strip(): v.strip() for k, v in fields.items()}
    if fields.get("name") != skill.parent.name:
        errors.append(f"{skill}: name must equal folder name '{skill.parent.name}'")
    if not fields.get("description"):
        errors.append(f"{skill}: description is empty")

link = re.compile(r"\]\(([^)\s]+)\)")
fence_open = re.compile(r"(`{3,}|~{3,})")


def outside_fences(text):
    """The lines of a Markdown text that are not inside a fenced code block. A fence opens on a line starting
    with three or more backticks or tildes and closes on a line starting with at least as many of the same."""
    fence = None
    for line in text.splitlines():
        stripped = line.lstrip()
        if fence is None:
            opened = fence_open.match(stripped)
            if opened:
                fence = opened.group(1)
            else:
                yield line
        elif stripped.startswith(fence[0] * len(fence)) and not stripped.strip(fence[0]):
            fence = None


for md in sorted(root.rglob("*.md")):
    # templates/ holds fill-in placeholders such as [#N](link).
    if ".git" in md.parts or "templates" in md.parts:
        continue
    for target in (t for line in outside_fences(md.read_text(encoding="utf-8")) for t in link.findall(line)):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        path = target.split("#", 1)[0]
        if path and not (md.parent / path).exists():
            errors.append(f"{md.relative_to(root)}: broken link {target}")

for err in errors:
    print(err)
print("OK" if not errors else f"{len(errors)} problem(s)")
sys.exit(1 if errors else 0)
