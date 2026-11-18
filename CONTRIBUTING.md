# Contributing

Contributions are welcome: a fix to a skill, a new workflow you have used on real work, or a correction to a template.

## What fits here
- Skills and templates you have actually used, with a link to public evidence (a PR, a CI run, a log).
- Changes that make an existing skill clearer, shorter or more correct.
- Reports where a skill gave wrong advice, with the situation and what happened.

Not a fit: untested prompt collections, or content copied from elsewhere without a compatible license.

## Adding or changing a skill
1. Put it in `skills/<name>/SKILL.md`. The frontmatter `name` must equal the folder name and `description` must not be empty.
2. Keep relative links valid.
3. Run the same check as CI:

   ```sh
   python scripts/check_repo.py
   ```

4. In the PR, say how you used the skill and link the evidence. Disclose AI assistance and report only checks you ran.

## Questions and ideas
Open an issue with one of the forms. Contributions are accepted under the [MIT license](LICENSE).
