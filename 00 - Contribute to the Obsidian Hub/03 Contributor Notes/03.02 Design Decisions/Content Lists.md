## Sorting of lists, to aid readability

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

**Rejected**: For human-edited lists, e.g. categories: Introduce standard comment delimiters to mark lists that should be sorted by the text the link, case-insensitively, e.g. 

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

