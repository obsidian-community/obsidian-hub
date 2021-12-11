## Sorting of lists, to aid readability

### Decisions and conclusions

- Sort on Alias, not Plugin ID
- Avoid comment markers
- Find sections based on headers - and maybe location files and folders
- This is doable by GitHub action
- Update scripts that generate lists, to sort in the first place - e.g. Uncategorised plugins

### The Problem

For example, I find it hard to glance at the category pages and see what I'm after.

Compare these two:

![task-plugins-sorted](attachments/images/task-plugins-sorted.png)

### Suggestions

For machine generated text, e.g. lists of plugins and themes in People pages, make the python code sort these lists by plugin/theme name.

For human-edited lists, e.g. categories:

Introduce a standard delimiter to mark lists that should be sorted by the text the link, case-insensitively, e.g. 

```markdown
## Plugins in this category

%% Hub Content: Start of auto-sorted section - please retain this comment  %%

- [[slated-obsidian|Slated]]
- [[todoist-sync-plugin|Todoist Sync Plugin]]
- [[obsidian-day-planner|Day Planner]]

%% Hub Content: End of auto-sorted section - please retain this comment  %%
```

Then add a script to sort the content of all manually-maintained lists.

