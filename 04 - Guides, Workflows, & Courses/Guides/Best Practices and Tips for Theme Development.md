---
aliases: 
- 
tags:
- seedling
publish: true
---

# Best Practices and Tips for Theme Development

This note serves as a collection of tips and best practices for theme development which are too small to be their own guide.

- Name the font-faces in your theme's CSS differently from the one you installed on your system to prevent potential issues with fonts from going unnoticed. 
    By naming your base64-encoded font-faces (`@font-face`) the same as the font you installed on your system, you will never actually see how the fonts are rendered for other users, since Obsidian will prefer the system font when there are multiple fonts with the same name available (one via base64-encoded CSS, one on the system).
- Prefer `woff2` over `ttf` as font format, since the former has a far smaller file size.
- if you ever need more specificity than adding a `body` at the start of your selectors, you can double the targeted class, like so:
	- `body .timer-start-button.timer-start-button { --button-fill-inner: white; }`
	- The usecase for this is, for example, when an element uses those `.svelte-xyz` generated classes, which gives the rule more specificity, and just adding a `body` is not enough to override it. You can double or triple the class selector you're targeting, which gives it enough specificity for css to read it as more important.
		- **Caution:** directly using the `.element.svelte-xyz` type of classes in a CSS snippet will make it stop working if there's a change to the plugin, and so it's best to not include the `.svelte-xyz` parts themselves (so just the element class), and then add more specificity if required. The `.svelte-xyz` classes are randomly generated, they work in the original style because they're being added through a variable. Always only target classes that look like they were made by a human (even if that may be `.hd-2`).
	- You could also achieve more specificity by adding more elements before the targeted class, like `body .workspace-leaf-content .timer-start-button`, but an advantage of `body .timer-start-button.timer-start-button` is that it's not dependent on any other classes - if `.workspace-leaf-content` changed at some point, or the timer start button was used outside it, the custom style would still work if you just doubled its class.
- You can enter `process.versions.chrome` in the console to get the current Chrome version utilized by Obsidian to render CSS. CSS documentation pages like [MDN](https://developer.mozilla.org/en-US/) or [W3-Schools](https://www.w3schools.com/cssref/css3_pr_overflow-y.asp) usually document which Chrome version is required for a certain CSS feature at the bottom of the feature's documentation page.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Best%20Practices%20and%20Tips%20for%20Theme%20Development.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Best%20Practices%20and%20Tips%20for%20Theme%20Development.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>