---
aliases: 
- 
tags:
- seedling
publish: true
---

# Center Tables

> Adds a cssclass so that all tables in your notes are centered.

The `.t-c` CSS Class is from the [[ITS Theme]]. If you're using that theme, you don't need to add this as a snippet, you can just add it to the cssclass field in the [[YAML frontmatter]]. Otherwise this snippet should be compatible with most other themes. 

---
Feel free to change `.t-c` to something else if you prefer to use a different class name.

%% Paste your template below %%

```css
.t-c table {
    margin-left: auto;
    margin-right: auto
}
```

[![](https://i.imgur.com/4ywZHK1.png)](https://i.imgur.com/4ywZHK1.png)
