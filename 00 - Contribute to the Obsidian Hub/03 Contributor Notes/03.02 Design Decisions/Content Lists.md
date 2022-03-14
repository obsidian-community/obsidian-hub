---
aliases:
- 
tags:
- 
---

# Content: Lists

## Sorting of lists, to aid readability

**Status:** Agreed, and being tracked in [Implement automated sorting of some lists on links · Issue #282](https://github.com/obsidian-community/obsidian-hub/issues/282)

### Decisions and conclusions

- Sort by Alias, not Plugin ID
- Do not implement the "standard comment delimiters" suggestion, as it adds complexity, confusion and clutter for contributors
- Find sections based on headers - and maybe location files and folders
- This is doable by GitHub action
- Update scripts that generate lists, to sort in the first place - e.g. Uncategorised plugins

### The Problem

For example, I find it hard to glance at the category pages and see what I'm after.

Compare these two:

![[task-plugins-sorted.png]]

### Suggestions

**Agreed**: For machine generated text, e.g. lists of plugins and themes in People pages, make the python code sort these lists by plugin/theme name.

**Rejected**: For human-edited lists, e.g. categories: Introduce standard comment delimiters to mark lists that should be sorted by the Alias in the link, case-insensitively, e.g. 

```markdown
## Plugins in this category

%% Hub Content: Start of auto-sorted section - please retain this comment  %%

- [[slated-obsidian|Slated]]
- [[todoist-sync-plugin|Todoist Sync Plugin]]
- [[obsidian-day-planner|Day Planner]]

%% Hub Content: End of auto-sorted section - please retain this comment  %%
```

**Agreed**: Add a script to sort the content of all manually-maintained lists.

This will need to do something like:

- Know which files contain lists that should be sorted (e.g. which folders contain files with lists to sort)
- How to recognise chunks of text that are lists to sort (likely a regular expression looking for `-` or `*` followed by internal links with aliases `[[...|...]]`)


%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.02%20Design%20Decisions/Content%20Lists.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.02%20Design%20Decisions/Content%20Lists.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
