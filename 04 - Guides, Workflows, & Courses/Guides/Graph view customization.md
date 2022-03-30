# Graph view customization

Since the graph is rendered using `<canvas>` and WebGL, [[Customizing CSS|CSS]] is unable to affect things like nodes and links. To customize graph view, we have provided a way to convert CSS colors into WebGL commands.

## The following CSS classes are supported:

```
.graph-view.color-fill
.graph-view.color-fill-focused (use transparent to disable)
.graph-view.color-fill-tag (theme-dependent)
.graph-view.color-fill-attachment (theme-dependent)
.graph-view.color-arrow
.graph-view.color-circle
.graph-view.color-line
.graph-view.color-text
.graph-view.color-fill-highlight
.graph-view.color-line-highlight
.graph-view.color-fill-unresolved
```

\* theme-dependent means you may have to add `.theme-dark` or `.theme-light` to style it for different themes. See [[#Defaults]] for explanation.

## The following CSS rules are supported:

```css
 .graph-view.color-class {
	/* Supports all CSS color directives, like #HEX, rgb and rgba */
	color:   #FFF;
	color:   #FFFFFF;
	color:   rgb(0, 0, 0);
	color:   rgba(0, 0, 0, 1);
	/* Opacity (similar to rgba) will make the color transparent */
	opacity: 0.5;
}
```

## Defaults

These CSS rules are the ones Obsidian uses by default. You may override any of them using an identical or [more specific](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity) CSS rule. This applies especially to `.color-fill-tag` and `.color-fill-attachment` As a last resort, add `!important` to the end of your rule.

```css
.graph-view.color-fill,
.theme-dark .graph-view.color-fill-tag,
.theme-light .graph-view.color-fill-tag,
.theme-dark .graph-view.color-fill-attachment,
.theme-light .graph-view.color-fill-attachment,
.graph-view.color-arrow,
.graph-view.color-circle,
.graph-view.color-line,
.graph-view.color-text,
.graph-view.color-fill-highlight,
.graph-view.color-line-highlight,
.graph-view.color-fill-unresolved {}
```