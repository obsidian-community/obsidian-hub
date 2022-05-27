---
aliases: 
- 
tags:
- seedling
---

# Tooltips for Literature Notes with Supercharged Links

![[Tooltips-for-Literature-Notes-with-Supercharged-Links.gif]]

Don't forget to add "title" (or whichever yaml key you use) to the "tag attributes for styling" in the [[supercharged-links-obsidian|Supercharged Links]] settings.

```css
/* change "#pdf-annotations" to the tag of your literature notes */
/* change "title" in "data-link-title" to the yaml key of your title */

.data-link-text[data-link-tags*="#pdf-annotations" i]:hover::after{
    content: "\""attr(data-link-title)"\""; 
    position: absolute;
    background-color: var(--background-secondary);
    padding: 8px;
    font-size: 0.9rem;
    max-width: 350px;
    color: var(--text-normal);
}
```

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/03%20-%20Showcases%20%26%20Templates/Plugin%20Showcases/Tooltips%20for%20Literature%20Notes%20with%20Supercharged%20Links.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/03%20-%20Showcases%20%26%20Templates/Plugin%20Showcases/Tooltips%20for%20Literature%20Notes%20with%20Supercharged%20Links.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
