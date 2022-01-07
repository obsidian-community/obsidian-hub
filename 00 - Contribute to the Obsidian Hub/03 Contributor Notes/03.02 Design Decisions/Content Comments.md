---
aliases:
- 
tags:
- 
---

# Content: Comments

## Agree a standard for optional text, that is commented out and then enabled...

Suggested standard:

- `%% .... %%` for instructions and comments to maintainers
- `<!-- .... -->` for things that may be activated (either on one line, or split, depending on context)
    - Never use this for multi-line sections, where activating individual lines means moving some text up or down.
    - Instead, comment out each individual line separately
- `<https://>` as a placeholder for a commented-out URL
    - So it's obvious where the URL goes, and that it can be pasted in directly
    - and this will make it more likely that `^` marker will be retained
    - It's important that there are no spaces after the `^`marker, for it to work and display correctly

## Agree a standard begin/end prefix for marking 'do not edit' sections

We use these markers in Author pages, and they do not seem to be well-understood:

```markdown
## Author of

%% Begin Hub: Released contributions %%

<!--
### Plugins

- 
-->

<!--markdown
### Themes

- 
-->

%% End Hub: Released contributions %%
```

In the new MOC files, we use this:

```markdown
%% Hub MOCs: Don’t edit below  %%
...
%% Hub MOCs: Don’t edit above  %%
```

Example idea: standardise on:

```markdown
%% Hub Content: Don’t edit below  %%
...
%% Hub Content: Don’t edit above  %%
```

And then use that pair in all boundaries of machine-generated text.
