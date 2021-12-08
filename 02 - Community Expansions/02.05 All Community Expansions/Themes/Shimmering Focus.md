---
aliases:
- 
tags: 
- 
publish: true
---

%% ----- Badges ----- %%

![Downloads](https://img.shields.io/badge/downloads-6085-573E7A?style=for-the-badge&logo=)
![GitHub last commit](https://img.shields.io/github/last-commit/chrisgrieser/shimmering-focus?color=573E7A&label=last%20update&logo=github&style=for-the-badge)
![GitHub issues by-label](https://img.shields.io/github/issues/chrisgrieser/shimmering-focus/help%20wanted?color=573E7A&logo=github&style=for-the-badge) 
![GitHub Repo stars](https://img.shields.io/github/stars/chrisgrieser/shimmering-focus?color=573E7A&logo=github&style=for-the-badge)

%% ----- Badges ----- %%

%% ----- Do not edit this section ----- %%

# Shimmering Focus

Repository: [GitHub](https://github.com/chrisgrieser/shimmering-focus)
Designed by: [[chrisgrieser]]
Modes: [[Dark-mode themes|dark]], [[Light-mode themes|light]]



![screenshot](https://github.com/chrisgrieser/shimmering-focus/raw/main/dual-theme-screenshot.png)

%% ----- Do not edit anything above this line ----- %% 

%% Does the repository or author have any sponsoring links? Uncomment the next line and add them to the author's note. If they don't, please delete the placeholder tag: #placeholder/author %%
%% ![[chrisgrieser#Sponsor this author]] %%


## Features

- [[Themes with Friendly Settings|Friendly settings]]: Supports the [[obsidian-style-settings|Style Settings]] plugin

## Customization Options (Style Settings Plugin) 

**Show/Hide UI Elements**: Re-enable Elements hidden by this theme
- Re-enable Title Bar: Re-enable this to have a title bar, e.g. for moving the Obsidian window
- Re-enable Ribbons: Ribbons are the thin vertical bars to the very left & right
- Permanently show the Header Bar: When false, the Header bar is still visible upon focus and hover
- Permanently show the Status Bar: When false, the Status bar is still visible when hovering. (This setting will be overriden when you use the default status bar.)
- Default Theme Status Bar: Use the Status Bar from the default theme, which will also be permanently visible.
- Re-enable Close Buttons: When false, you can close the menu with `Esc` or by clicking outside the menu area.
- Re-enable Scrollbars: When false, only the scroll bars in the Editor are shown.
- Permanently show the Edit Mode Collapse Arrows: When false, you collapse buttons still become visible upon hovering.
- Re-enable the Fold Markers: Fold markers are the ellipses ("...") next to a folded/collapsed item.
- Permanently show the Graph Controls: When false, Graph controls are still visible when open, or upon hovering the top-left area.
- Re-enable the Starred Pane Buttons: The two buttons to star the current file and the current search.

**Aesthetics**: Shapes, Color Schemes (coming soon), Cursor, & Decoration
- Angular Shapes: Enable to use angular shapes (🔲). Disable to use rounded shapes (🔘).
- Block Cursor: Use a block cursor instead of a line cursor. For best results, also switch the main font to a monospace font.
- Mono-colored Cursor: Use a mono-colored, purple cursor like in previous versions of "Shimmering Focus".
- Normal Checkboxes: Use the checkboxes from the default theme.
- Colored YAML: Use colored YAML frontmatter (in Edit Mode).

**Fonts**: Sizes, Font-Face, Letter-Spacing
- Main Font
- Monospace Font: Used in Code blocks, YAML in Edit Mode, tables in Edit Mode, etc.
- Monospace Font Size
- Side Bar Font: Applies to all text in the left and right side bar
- Side Bar Font Size
- Menu Font: Font used in menus (i.e., Settings, Plugin Browser, Theme Browser).
- Menu Font Size
- Normal-sized Blockquotes: Blockquotes have the same size and line-height as the rest of the text.
- Status Bar Font Size
- Heading Font: Applies to h1 to h5 Headings. (h6 headings are used for Pseudo-Admonitions.)
- No Alternating Italic of Headings: In this theme, the Heading Levels alternate between italic/regular to make them more distinguishable. You can turn that feature off if you prefer non-italic for all heading levels.
- Level 1 Headings
- Level 2 Headings
- Level 3 Headings
- Level 4 Headings
- Level 5 Headings

**Views & Content**: Max View, Focus View, Images, PDFs, & Line Length
- Disable "Max View": "Max View" makes panes full length and images/PDFs full width when the left sidebar is hidden and readable line length when the left sidebar is shown.
- Enable "Focus View": Hiding the left side bar will also hide the right one. Note that with this feature, the right side bar stays hidden until the left one is shown again. Synergizes with "Max View", but also works with "Max View" disabled. 
- Size of Images: Size of Images in % (when Max View is disabled or not active)
- Size of embedded PDFs: Size of embedded PDFs in % (when Max View is disabled or not active)
- Remove image borders: Disables the frame put around images.
- Align Images & PDFs to the left: When disabled, they will be aligned to the center instead.
- No Dark Mode for PDFs: Disable Dark Mode for PDFs when Obsidian is set to dark mode.

**Spellcheck**: Style & Fine-tuning
- Use Classic Spellcheck Styling: Turns off the spellcheck styling of this theme and use the classic spellcheck styling.
- No Spellcheck in YAML Header: Turn off Spellcheck in YAML Header.
- No Spellcheck in Blockquotes: Turn off Spellcheck in Blockquotes.
- No Spellcheck for HTML Tags: Turn off Spellcheck in HTML Tags (e.g. <br/> not marked)
- No Spellcheck in Headers: Turn off Spellcheck in all headings.
- No Spellcheck in strikethroughs: Turn off Spellcheck in any text enclosed by the strikethrough syntax (~~foobar~~).
- No Spellcheck in comments: Turn off Spellcheck in comments (%%comments%% as well as <!--comments-->).
- No Spellcheck in Pandoc Citations: Turn off Spellcheck in Pandoc Citations (Bare Links).

**Longform Plugin**: Font, Alignment, Background
- Main Font for Longform Notes: Font used in folders marked as Longform Project
- Longform Font Size
- Left-aligned text in Longform notes: Use left-aligned instead of justified text.
- No Background Color for Longform Notes: Turn off the slight coloring of longform notes.
- Hide files named "Index.md" from File Explorer: Files named that way are created by some plugins like the Longform Plugin and in many cases should not be touched.

**Mobile**: Settings specifically for mobile
- Mobile Font Size

**Miscellaneous**: Popovers, Pandoc Citations, Annotation Tags, Active Line Highlighting, Command Palette, Alternating Row Colors, Relationship Lines
- Size of Popovers (Page Previews): Width & Height of Popovers in px
- No Emphasis of Pandoc Citations: Turn off the coloring of Pandoc Citations [@citekey] done by this theme.
- Turn off "Annotation Tags": "Annotation Tags" will visually emphasize some tags that are commonly used for academic reading.
- Turn off Active Line Highlighting
- Turn off Alternating Row Coloring: Affects tables, Command Palette & Suggesters.
- Command Palette: Move the plugin name back to the left: Enable this in case some commands are aren't displayed properly in the Command Palette.
- Disable Relationship Lines for lists: If you want to use a custom relationship line snippet or the relationship lines from the Outliner plugin, you can disable this theme's relationship lines to prevent interference.

## Plugin Compatibility[^1]

**Core plugins**:
- [[Obsidian Core Plugins#Backlinks|Backlinks]]
- [[Obsidian Core Plugins#Command palette|Command palette]]
- [[Obsidian Core Plugins#File explorer|File explorer]]
- [[Obsidian Core Plugins#Search|Search]]
- [[Obsidian Core Plugins#Graph view|Graph view]]
- [[Obsidian Core Plugins#Outgoing Links|Outgoing Links]]
- [[Obsidian Core Plugins#Outline|Outline]]
- [[Obsidian Core Plugins#Page preview|Page preview]]
- [[Obsidian Core Plugins#Starred notes|Starred notes]]
- [[Obsidian Core Plugins#Quick switcher|Quick switcher]]
- [[Obsidian Core Plugins#Tag pane|Tag pane]]
- [[Obsidian Core Plugins#File recovery|File recovery]]

**Community plugins**:
- [[recent-files-obsidian|Recent Files]]
- [[advanced-cursors|Advanced Cursors]]
- [[obsidian-another-quick-switcher|Another Quick Switcher]]
- [[obsidian-codemirror-options|CodeMirror Options]]
- [[obsidian-kanban|Kanban]]
- [[oz-image-plugin|Ozan's Image in Editor Plugin]]
- [[calendar|Calendar]]
- [[obsidian-dangling-links|Dangling links panel]]
- [[mysnippets-plugin|MySnippets]]
- [[obsidian-drag-and-drop-blocks|obsidian-drag-and-drop-blocks]]
- [[map-of-content|Map of Content]]
- [[quick-explorer|Quick Explorer]]
- [[templater-obsidian|Templater]]
- [[obsidian-system-dark-mode|System Dark Mode]]
- [[obsidian-extra-md-commands|Extra Markdown Commands]]
- [[obsidian-style-settings|Style Settings]]
- [[obsidian-activity-history|Activity History]]
- [[breadcrumbs|Breadcrumbs]]

[^1]: Generally, Obsidian themes work with any plugins. That a plugin is not listed here does not mean that it won't work together with the theme. Plugins listed here only received special attention and/or styling by the theme designer.
