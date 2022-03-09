---
aliases:
- 
tags:
- 
---

# GitHub Actions for the Hub

One GitHub Action that combines updating theme download counts, adds new plugins, themes and authors, [[Updating MOC files|updates MOC files]], updates the [tree of directories in Contributing](https://github.com/obsidian-community/obsidian-hub/blob/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.01%20Structure/Hub%20Tree%20Structure.md) and [[Adding footers|adds footers]] is the [[update_hub GitHub Action]].   ^3df057

## Potentially automatable

There are some maintenance steps that are currently done manually, and that could be run automatically, either on a cron schedule, or upon changes to the main branch.

This work is being tracked in [Automate (some) scripts with GitHub Actions · Issue #153](https://github.com/obsidian-community/obsidian-hub/issues/153)

- Updating theme download counts
  - Part of [[Updating Extensions]]
- Adding new theme, plugin and people pages
    - Part of [[Updating Extensions]]
- Generating the MOCs
  - [[Updating MOC files]]
- Sorting lists
  - [[Content Lists]]
- Running the Python tests
  - [[Testing Python Code with Approval Tests]]
- Updating "[Structure of the Community Vault](https://publish.obsidian.md/hub/CONTRIBUTING#Structure+of+the+Community+Vault)" IN CONTRIBUTING
    - The comments in the source file show the `tree` command-line args
    - There could be a script which ran the tree command automatically, and saved the output to a file
    - That file could then be `![[]]` embedded inside the CONTRIBUTING page


## Not yet automatable

- Updating existing theme, plugin and people pages
- Publishing

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.03%20Scripts%20and%20Automation/GitHub%20Actions%20for%20the%20Hub.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.03%20Scripts%20and%20Automation/GitHub%20Actions%20for%20the%20Hub.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
