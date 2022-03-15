---
aliases:
- 
tags:
- 
---

# Content: Comments

## Agree a standard for optional text, that is commented out and then enabled...

Suggested standard:

**Note:** *See the other files in this folder for progress on implementing this in each of the types of notes (namely, Plugin, Theme and Author/Person).*

- `%% .... %%` for instructions and comments to maintainers
- `<!-- .... -->` for things that may be activated (either on one line, or split, depending on context)
    - Never use this for multi-line sections, where activating individual lines means moving some text up or down.
    - Instead, comment out each individual line separately
- `<https://>` as a placeholder for a commented-out URL
    - So it's obvious where the URL goes, and that it can be pasted in directly
    - and this will make it more likely that `^` marker will be retained
    - It's important that there are no spaces after the `^`marker, for it to work and display correctly

## Agree a standard begin/end prefix for marking 'do not edit' sections

**Note:** *See [Agree a standard begin/end prefix for marking 'do not edit' sections · Issue #351](https://github.com/obsidian-community/obsidian-hub/issues/351) for discussion and implementation progress on this.*

In various parts of the Hub, we use  markers to highlight sections which should not be edited manually because they are instead created or updated automatically by our [[GitHub Actions for the Hub]].

We use these markers in Author pages, and they do not seem to be well-understood: occasionally people add new text inside these matching pairs of comments.

```markdown
## Author of

%% Begin Hub: Released contributions %%

<!--
### Plugins
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

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.02%20Design%20Decisions/Content%20Comments.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.02%20Design%20Decisions/Content%20Comments.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
