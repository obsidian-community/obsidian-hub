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
