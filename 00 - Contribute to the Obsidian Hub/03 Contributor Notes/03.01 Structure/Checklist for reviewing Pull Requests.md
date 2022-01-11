---
aliases:
- 
tags:
- 
---

# Checklist for reviewing Pull Requests

An optional checklist of things that might be worth checking when reviewing pull requests.

When reviewing:

- If possible, try to view the PR content in Obsidian
- Does it add any text inside commented-out sections?
- Does it add any text inside machine-generated content (that could be moved to a separate section)
- Does it add any new dangling links?
- If files have been added
   - Do all the new files have file extensions?
- If files have been renamed
    - Has the title been updated?
    - Have the linked mentions been updated?
    - Have the aliases in linked mentions been updated
- If a template has been renamed
    - Has the matching counterpart been renamed?
        - `.github/scripts/templates`
        - `00 - Contribute to the Obsidian Hub/01 Templates`

After merging:

- Do the MOCs need updating? See [[Updating MOC files]]
- Does the [tree of directories in Contributing](https://github.com/obsidian-community/obsidian-hub/blob/main/CONTRIBUTING.md#structure-of-the-community-vault) need to be updated? See comments in the source of that file.
- If a directory was renamed (rare), check to see if you need delete the previous MOC
