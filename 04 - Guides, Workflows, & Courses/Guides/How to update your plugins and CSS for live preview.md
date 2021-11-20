---
aliases: 
- 
tags:
- seedling
publish: true
---

# How to update your Plugins and CSS for Live Preview

**Target audience**: Authors of Plugins, Themes and CSS snippets

This is a collection of information and notes being gathered, to collate information, hints and tips for authors of Plugins, Themes and CSS snippets, to update them so that they work with [Live Preview Mode](https://twitter.com/obsdmd/status/1458523572448727051), as well as with the earlier Edit and Preview modes.

Additions to this page are very much welcomed, as developers and users learn more about any changes needed to support Obisidian Extensions as the software evolves.

The eventual goal is to end up with a table with two columns, where each row lists a piece of old code, and then what to replace it with, to modernise code - and another table for CSS.

## Abbreviations

- CM: [CodeMirror](https://codemirror.net)
- CM5: CodeMirror 5
- CM6: CodeMirror 6

## For Plugin Developers

### The Editor Interface

From `@licat`:

> The Editor interface is purposefully designed to be a drop in replacement of CodeMirror 5's object for anything that we support. The migration should be as straightforward as changing the object reference to the editor instead of `sourceMode.cm`. If a plugin is using more advanced API on CodeMirror 5 then we don't support it anyway, and it just won't work on CodeMirror 6 regardless.

### Obsidian DOMs

From [[nothingislost]]

#### Environments

Here's my take on the modes, DOM wise. Licat can correct me if I'm wrong on any of this 🙂

Different Obsidian Desktop environments:

- **Desktop CM5: Editor** <- Original
- **Desktop CM6: Editor (Source)** <- New
- **Desktop CM6: Editor (Live Preview)** <- New
- **Desktop: Preview** <- Original

Different Obsidian Mobile environments:

- **Mobile CM6: Editor (Source)** <- Around since the inception of mobile
- **Mobile: Preview** <- Around since the inception of mobile

Equivalences:

- **Desktop CM6: Editor (Source)** == **Mobile CM6: Editor (Source)**
- **Desktop: Preview** == **Mobile: Preview**

#### The DOMs

- **Desktop CM6: Editor (Live Preview)** should be very similar, DOM wise, to **Desktop CM6: Editor (Source)** with the exception that inactive markdown tokens are replaced with a zero width space.
- **Desktop CM6: Editor (Live Preview)** also has the added distinction that it can now have embedded content rendered in it which adds new DOM elements into the CM6 Editor DOM. These elements should look pretty similar to their preview mode counterparts but we'll probably want to wait until things stabilize before their structure is documented.

### Code Snippets

#### Detect if Live Preview is supported

If you need to write code whose behaviour depends on whether Live Preview is supported (such as during the porting process):

```typescript
// Version 1: Not recommended, as it needs @ts-ignore
//@ts-ignore
if (this.app.vault.config?.livePreview) {
    // Running new Obsidian, that supports Live Preview
} else {
    // Running pre-Live Preview version of Obsidian
}
```

```typescript
// Version 2: Bit better, as no need for @ts-ignore
if ((this.app.vault as any).config?.livePreview) {
    // Running new Obsidian, that supports Live Preview
} else {
    // Running pre-Live Preview version of Obsidian
}
```

Even better would be to wrap the check in to a helper function such as `isLivePreviewSupported()`, so that the logic is in only one place, and can be updated easily if needed.

### Example Code for Updating Plugins

- Porting the [[nldates-obsidian|Natural Language Dates]] plugin - by [[argenos|Argentina Ortega Sainz]]
	- A selection of useful steps:
		- [Use Editor interface for CM6 and CM5](https://github.com/argenos/nldates-obsidian/pull/57/commits/642bac6977597dc48ec994ecc1bcf957097647dd)
		- [Refactor getWordBoundaries to support CM6](https://github.com/argenos/nldates-obsidian/pull/57/commits/16e103335409df6f259a9ef0fc65cb3f4fe55f40)
		- [Fix hotkeys for CM5](https://github.com/argenos/nldates-obsidian/pull/57/commits/6094aa7c056954b9f3caf5376a66f10faccf6d82)
	- The complete PR (which contains other fixes/refactoring too): [argenos/nldates-obsidian/#57](https://github.com/argenos/nldates-obsidian/pull/57 "https://github.com/argenos/nldates-obsidian/pull/57")

## For Theme Developers

From `@licat`:

> With respect to themes, we try our best to maintain the same css classes and DOM structure as we possibly can when migrating to CM6. Some changes are inevitable due to how the new underlying editor works, but since CM6 has been in effect for mobile since day 1, most actively updated themes that works well on mobile should work similarly well for Live Preview

### Example Code for Updating Themes

- [CSS for inline block references that works for both NEW CM6 Live Preview and also Preview Mode for both CM5 (Legacy) and CM6 (New)](https://gist.github.com/GitMurf/46c9ae78d6c3ce53d42d7832c7601271) - by `@Murf`
