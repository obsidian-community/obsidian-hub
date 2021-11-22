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
