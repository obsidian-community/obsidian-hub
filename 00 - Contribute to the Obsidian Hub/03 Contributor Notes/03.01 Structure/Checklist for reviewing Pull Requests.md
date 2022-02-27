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

- Run the [[update_hub GitHub Action]]. See here [[GitHub Actions for the Hub#^3df057|what it does]].
- If a directory was renamed (rare), check to see if you need delete the previous MOC

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.01%20Structure/Checklist%20for%20reviewing%20Pull%20Requests.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.01%20Structure/Checklist%20for%20reviewing%20Pull%20Requests.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
