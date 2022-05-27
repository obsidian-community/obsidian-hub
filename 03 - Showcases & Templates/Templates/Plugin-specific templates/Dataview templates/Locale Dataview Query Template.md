---
aliases: 
- 
tags:
- seedling
publish: true
---

# Locale Dataview Query Template

> Dataview Query Template that lists out [[Locale Template|Locale Notes]] with useful information and sorted in the order I may need while DMing.

**Note:** `"[[#" + alias + "|#]]"` uses the alias of the [[Locale Template]], displayed as a hastag symbol `#` to take me down the page where this query resides to a heading with more info for my session.
%% Paste your template below %%

````markdown

```dataview
TABLE WITHOUT ID "**" + link(file.link, alias) + "** " + "<span style='border-bottom: 2px solid var(--interactive-accent);'>" + "[[#" + alias + "|#]]" AS Locales, Description, Notes AS NOTES
FROM (#Location & !#Location/City) & #Campaign/Lost-Mine-Of-Phandelver
SORT Number
```

````

Image using the [[All Alternate Themes (ITS Theme)#D D WOTC\|D&D WOTC]] Alternate Theme Snippet.

[![](https://raw.githubusercontent.com/SlRvb/Obsidian--ITS-Theme/main/Images/Note-Showcase/T-DnD--Locale-Query.png)](https://raw.githubusercontent.com/SlRvb/Obsidian--ITS-Theme/main/Images/Note-Showcase/T-DnD--Locale-Query.png)

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/03%20-%20Showcases%20%26%20Templates/Templates/Plugin-specific%20templates/Dataview%20templates/Locale%20Dataview%20Query%20Template.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/03%20-%20Showcases%20%26%20Templates/Templates/Plugin-specific%20templates/Dataview%20templates/Locale%20Dataview%20Query%20Template.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
