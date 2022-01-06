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
- Prefer `woff2` over `ttf` as font format, since the former have a far smaller file size.
- if you ever need more specificity than adding a `body` at the start of your selectors, you can double the targeted class, like so:
	- `body .timer-start-button.timer-start-button { --button-fill-inner: white; }`
	- The usecase for this is, for example, when an element uses those `.svelte-xyz` generated classes, which gives the rule more specificity, and just adding a `body` is not enough to override it. you can double or triple the class selector you're targeting, which gives it enough specificity for css to read it as more important.
	- You could also achieve more specificity by adding more elements before the targeted class, like `body .workspace-leaf-content .timer-start-button`, but an advantage of `body .timer-start-button.timer-start-button` is that it's not dependent on any other classes - if `.workspace-leaf-content` changed at some point, or the timer start button was used outside it, the custom style would still work if you just doubled its class.
