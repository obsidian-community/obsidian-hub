---
aliases: 
- 
tags:
- seedling
publish: true
---

# Button Action & Trait Templates

These are mini templates utilized by the [[DnD Character Sheet]] Template to easily add multiple traits/actions with formatting already in place.

These use the [[buttons]] plugin to insert the template using `^button-name` on other templates. I usually have 1 note with a whole list of button codeblock to point to for my other templates that use [[buttons]].

%% Paste your template below %%

###### Trait
````markdown
```button
name Add Trait
type prepend template
action Path/To/Trait Template
```
^button-trait
````

```markdown
###### Trait
**Description of trait**

- Bullet list of what traits do
```

###### Actions
````markdown
```button
name Add Action
type prepend template
action Path/To/Actions Template
```
^button-action
````


```markdown
###### Name

Type | To Hit | Hit | Reach | Targets |
---|:---:|:---:|---|:---:|
**==Weapon/Feat Type==** |||||

```

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/03%20-%20Showcases%20%26%20Templates/Templates/TTRPG%20notes/Button%20Action%20%26%20Trait%20Templates.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/03%20-%20Showcases%20%26%20Templates/Templates/TTRPG%20notes/Button%20Action%20%26%20Trait%20Templates.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
