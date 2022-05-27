---
aliases:
- 
tags:
- 
---

# Tip for Keeping Hub TODO lists

## Target Audience

This tip is really intended for anyone doing largish amounts of tidying up or handle-turning in the Hub content, which is cloned on their own machine.

## Scenario

I am making a series of small changes in the vault (like adding 20 missing notes).

- Maybe I want to save a screenshot or two of the things I am improving as well
- I would like to have a markdown note in the vault, so that I can keep a checklist of things to do

I want to **make it impossible for me to accidentally add those files** in a git commit.

An example might be:

```
Pages to create:

- [ ] [[Anthony Gold]]  
- [ ] [[Francesco D'Alessio]]  - need to work out naming convention with apostrophes
- [ ] [[Justin DiRose]]  
- [ ] [[Note-taking for University Students]]  - waiting for news from OCT
- [ ] [[Phnx]]  - note the lower-case equivalent below
- [ ] [[Tane Piper]]  
- [ ] [[apolaine]]  
- [ ] [[obsidian-drag-and-drop-blocks]]  
- [ ] [[phnx]]  
- [ ] [[placeholder/link]]  - these are actually URLs to add, not pages to create
- [ ] [[quick-monsters-5e]]  - need a system for managing plugins not yet in community list
- [ ] [[uwi]]
```

In Obsidian, I can test my progress by previewing that note, and seeing which links are still dangling, which is very useful.

## Steps

1. Create a directory at the top level called `DO NOT COMMIT`. The capitalisation and spaces matter.
2. Any files you put in `DO NOT COMMIT` directory will be ignored by git, and by the script that creates MOC files.

You can now put your own temporary notes and images in to `DO NOT COMMIT/`, confident that they will never be checked in.

## Alternative approaches

- It's also possible to add `- [ ]` checklists in GitHub issues and pull requests, as in this example: [issue #65](https://github.com/obsidian-community/obsidian-hub/issues/65).
    - **advantages**
        - the lists are public, and other people can see the progress, and may even be able to help
    - **disadvantages**
        - it is not easy to edit those lists in Obsidian
        - they cannot contain internal Obsidian wiki links (as used 

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/Tip%20for%20Keeping%20Hub%20TODO%20lists.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/Tip%20for%20Keeping%20Hub%20TODO%20lists.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
