---
aliases: 
- 
tags:
- seedling
---

# Tooltips for Literature Notes with Supercharged Links

![Screen Recording 2022-01-04 at 20 36 17](https://user-images.githubusercontent.com/73286100/148116001-8800ba0e-f24e-48f7-8bdf-87b30e6f0bb9.gif)

Don't forget to add "title" (or whichever yaml key you use) to the "tag attributes for styling" in the Supercherged Links settings.

```css
/* change "#pdf-annotations" to the tag of your literatur notes */
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
