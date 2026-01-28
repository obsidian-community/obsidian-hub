---
aliases:
- 
tags: 
- 
publish: true
---

%% ----- Badges ----- %%

![Downloads](https://img.shields.io/badge/downloads-298060-573E7A?style=for-the-badge&logo=)
![GitHub last commit](https://img.shields.io/github/last-commit/chrisgrieser/shimmering-focus?color=573E7A&label=last%20update&logo=github&style=for-the-badge)
![GitHub issues by-label](https://img.shields.io/github/issues/chrisgrieser/shimmering-focus/help%20wanted?color=573E7A&logo=github&style=for-the-badge) 
![GitHub Repo stars](https://img.shields.io/github/stars/chrisgrieser/shimmering-focus?color=573E7A&logo=github&style=for-the-badge)

%% ----- Badges ----- %%

%% ----- Do not edit this section ----- %%

# Shimmering Focus

Repository: [GitHub](https://github.com/chrisgrieser/shimmering-focus)
Designed by: [[chrisgrieser]]
Modes: [[Dark-mode themes|dark]], [[Light-mode themes|light]]



![screenshot](https://github.com/chrisgrieser/shimmering-focus/raw/HEAD/assets/promo-screenshot.png)

%% ----- Do not edit anything above this line ----- %% 

%% Does the repository or author have any sponsoring links? Uncomment the next line and add them to the author's note. If they don't, please delete the placeholder tag: #placeholder/author %%
%% ![[chrisgrieser#Sponsor this author]] %%


## Features

- [[Themes with Friendly Settings|Friendly settings]]: Supports the [[obsidian-style-settings|Style Settings]] plugin

## Customization Options (Style Settings Plugin) 
- ℹ️ Theme Information: - [Documentation of Features](https://github.com/chrisgrieser/shimmering-focus#shimmering-focus-)


**🙈 Show/Hide UI Elements**: Re-enable UI Elements hidden by this theme.
- Hide Settings Button: Hide the floating Settings button in the bottom left. You can still access the settings by using the hotkey `⌘+,` or `ctrl+,`.
- Permanently show the Sidebar Header Buttons: By default, the buttons at the top of the sidebar panels are only visible when hovering.
- Re-enable the Ribbon: The ribbon is the thin vertical bar to the very left. Without the ribbon, you can still trigger any action via the Command Palette.
- Show URLs of Markdown Links: By default, the URLs of markdown links are hidden in Source Mode, except for the currently active line.
ℹ️ This can also be toggled via command palette or hotkey.

- Re-enable New Tab Button: You can still open a new tab via `⌘+T` / `ctrl+T`.
- Re-enable Tab List Button: You can still switch to tabs via Quick Switcher, and you can toggle stacked tabs via command palette.
- Re-enable Sidebar Toggle Buttons: Note that sidebar buttons of hidden sidebars are going to be inaccessible when also enable the setting to hide the tab bar. You can still toggle the sidebars via command palette.
- Re-enable Close Buttons: You can still close settings with `Esc`, and tabs/panes by with `ctrl/cmd+W`.
- Search Pane: Re-enable Suggestions: By default, this theme hides the Suggestions in Search Core Plugin Pane.
- **File Explorer**: 
    - Hide attachments folders: Affects folders exactly named "attachments" (case-insensitive).
    - Show Vault Name: Enable this to drag and drop items to the vault root.
    - Re-enable Navigation Buttons: The navigation buttons are the buttons for new file, new folder, and sorting. You can do the former two without the buttons via the context menu.
- **Status Bar Items**: 
    - Hide the Status bar completely, when both sidebars are hidden: ⚠️ Requires Obsidian installer version 1.1.9 or later.
    - Hide Properties Count
    - Hide Backlinks Count
    - Hide Pane Relief Focus Lock
    - Hide Language Tools
    - Hide Electron Window Tweaker `Always on top` Icon
    - Hide Icons from the Text Generator Plugin except when Autosuggest is active
    - Hide Pandoc Reference List Icon
    - Hide the Shimmering Focus icon (⟡)

**🔲 Workspace**: Sidebar, Tab Bar & Header Bar
- Tab Bar when only one tab (experimental): By default, this theme turns the Tab Bar into a Header Bar. It turns back into a Tab Bar on hover or when another tab is opened. Alternatively you can also hide the tab bar altogether, when there is only one tab (⚠️ requires Obsidian installer version 1.1.9 or later).
- Re-enable the Header Bar (Tab Title Bar): By default, this theme removes the header bar, except for the "More Options" Button and the Breadcrumbs moved to the right. You can still toggle reading/editing mode, navigate back/forward, and rename your current file with the respective command in the command palette or a hotkey. (This setting has no effect if "Show tab title bar" in the Appearance settings is disabled.)
- Tab Width: This setting only affects tab width when there is enough space in the tab bar. (Obsidian automatically reduces tab width when there are more open tabs when there is space for them.)
- Sidebar: Trim File Names: When enabled, long file and folder names will be trimmed. When disabled, long names will be wrapped to the next line.
- Sidebar: Overlaying Right Sidebar: The right sidebar is placed on top of the editor instead of making the editor more narrow (i.e. the behavior on mobile).
- Sidebar: No Animations: Disable all sidebar-related animations.

**🔠 Font**: Headings, MathJax, Code
- Headings: Font Family
- Headings: Font Size Scaling: The font size of all headings is multiplied by this factor.
- Headings: No Alternating Colors: Do not colorize odd heading levels (h1, h3, h5).
- Headings: No Level Indicators in Live Preview
- Headings: Compactness: Makes Headings more compact by decreasing their letter spacing.
- Code Blocks: Font Size Scaling: The font size of all code blocks is multiplied by this factor. Also affects templater code and YAML frontmatter in source mode.
- MathJax: Font Family (Source Mode): By default, uses the monospace font you have set in the Obsidian core settings or if you have not set one, this theme's monospace font (Input Mono S).
- MathJax: Font Size
- None: You can change the font used elsewhere by the theme in the Obsidian settings: `Appearance → Font`

**🎨 Colors**: Native macOS Look, Background Color, Colored Bold/Italics, Highlight Color
- Native macOS Look: Background colors like in a native macOS app.
- Background Color Tone (Light Mode)
- Background Color Tone (Dark Mode)
- Uncolored Bold: **Bold text** will use the standard text color instead of being colored.
- Uncolored Italic: *Italic text* will use the standard text color instead of being colored.
- Color Tone of Highlights: Hue of ==highlighted text==
- More Color Customization: You can further customize theme colors or even create your own color scheme – without knowledge of CSS! – by using a CSS snippet. [See the theme docs for further information](https://github.com/chrisgrieser/shimmering-focus#create-and-share-your-own-color-scheme).

**📑 Editor Content**: Active Lines, Active Table Cells, Dimmed Panes, Clean Embeds, Line Length, Inline Backlinks, Folded Lines
- Dimmed Inactive Panes: Opacity of inactive panes. Set to 100% to disable dimming.
- Active Line Indicator
- Emphasize the active Table Cell (Live Preview): ⚠️ Requires Obsidian installer version 1.1.9 or later and Obsidian 1.5 or later.
- Turn Off Line Numbers in Code Blocks (Edit Mode): By default, this theme adds line numbers to code blocks in Edit Mode.
- Reading Mode: Clean Embeds: Embedded Notes integrate seamlessly with the rest of the note content.
- Line Length: The length of the editor content (when the `Readable Line Length` Setting is enabled). You can use the cssclass `full-width` to lift line length restrictions for individual notes.
- Folded Line Emphasis: ⚠️ Requires Obsidian installer version 1.1.9 or later. Slightly darkens the background of folded lines, similar to folds in vim.

**🖼️ Media**: Images, Tables, Canvas
- Automatically disable `Readable Line Length` on notes with tables: ⚠️ Requires Obsidian installer version 1.1.9 or later.
- Images: No alt-text as caption: By default, the alt-text of images is used as image caption in Reading Mode.
- Images: Size (Percent): The theme also adds a command `Toggle Max Image Size` which toggles between 100% image size and the reduced image size below. In addition, clicking & holding images will also enlarge an image.
- between Reduced and Max Image Size: INFO This is a dummy setting, since this is hidden and only added for the toggle-command
- Canvas: Heading Font in Cards and Notes: Only affects headings in canvas cards/notes. (Some heading fonts look good in notes, but not that good in cards.)
- Canvas: Center Text in all Cards and Notes: The theme also adds a command to toggle this setting

**✏️ Markup & Special Syntax**: Blockquote Alignment, Trailing Spaces, Pandoc Emphasis, Annotation Tags
- Left-aligned Blockquote Text: Use left-aligned text in blockquotes instead of justified text.
- Hide Trailing Spaces: By default, this theme indicates the presence of trailing spaces when there are more than one with "··↵". This can be useful for the "Two Space Rule" in Markdown, where exactly two spaces at the end of a line force a line break.
- No Emphasis of Pandoc Citations: Turn off the coloring of Pandoc Citations [@citekey] in Editing Mode. (Also affects the styling for the Pandoc Reference List Plugin.)
- Disable Annotation Tags: "Annotation Tags" are tags that are visually emphasized when used inline (i.e., not the YAML frontmatter). They include: #definition, #question, #goal, #todo, #summary, #important, #main, #critique, #gap, #litreview, #quote, #agree, #disagree, #example, #data, #method, #idea, #epistemic-break, and #sidenote.
- Width of Sidenote Callouts: Percentage of the readable line length. Affects callouts with `> [!sidenote]`. 

**🏃 Vim Mode**: Cursor, Relative Line Numbers
- Disable Blinking for the Vim Cursor
- Relative Line Numbers: ⚠️ Requires Obsidian installer version 1.1.9 or later. `Line Numbers` must also be enabled in the Obsidian settings.

**✍️ Longform & Writing**: Settings for notes in longform projects and notes with the writing cssclass.
- Main Font: Font used in longform/writing notes (Except code, which still use the monospace font.)
- Font Size in longform/writing notes
- Line Height in longform/writing notes
- Letter Spacing in longform/writing notes
- Background Color Tone (Hue): Use this setting to visually distinguish your longform and writing notes from the rest of your vault.
- Status Bar: Show Word Count *only* when longform/writing note is open: ⚠️ Requires Obsidian installer version 1.1.9 or later. Works for the Word Count Core Plugin and the Better Word Count Community Plugin.
- Status Bar: Hide Longform Wordcount: This affects the word count from the Longform plugin, not the other word count plugins.
- Tasks: Use Gray instead of Normal Text Color: This can help with differentiating tasks from "finished" text.
- Left-aligned text: Use left-aligned text instead of justified text.
- First-Line Indent & No Spacing between Paragraphs (Reading Mode): ⚠️ Requires Obsidian installer version 1.1.9 or later. Indent the first Line of a paragraph and remove the spacing between paragraphs.
- Disable active line highlights in longform/writing notes

**⚙️ Plugin-specific Settings**: Backlinks, Outgoing Links, Supercharged Links, Git Gutter
- Normal Outgoing Links and Backlinks: By default, the sidebar for outgoing links and backlinks are reduced to linked mentions only. Enable this setting to restore their original display.
- Use Normal Inline Backlinks: By default, the inline-backlinks are displayed in a more minimalistic manner. Enable this setting to restore original display of backlinks. This also affects the Influx Plugin.
- Supercharged Links: Disable built-in Icons: By default, the theme adds various icons if you have the Supercharged Links plugin installed: https://github.com/chrisgrieser/shimmering-focus#recommended-plugins.
- Obsidian Git: Turn Author Line Information into Gitsigns: Repurposes the Author Line Information feature to work like Gitsigns/Git Gutter. Required Plugin Settings: Enable "Show commit authoring information next to each line", hide author name, and hide authoring date.

**🧊 Miscellaneous**: Private Mode
- Private Mode: When enabled, all notes with the cssclass `private` will be garbled. This setting is meant to be enabled temporarily during screen sharing. Install Supercharged Links and add 'cssclass' as a target attribute to also garble any links and occurrences in the File Explorer and Quick Switcher. Note that note contents can still show up in views and sidebars created from plugins.
ℹ️ This can also be toggled via command palette or hotkey.


**ℹ️ Info**: 
- 👤 Credits: - Created by [pseudometa aka Chris Grieser](https://chris-grieser.de/).
- If you like the theme, [you can buy me a coffee](https://ko-fi.com/pseudometa). ☕


## Plugin Compatibility[^1]

**Core plugins**:
- [[Obsidian Core Plugins#Backlinks|Backlinks]]
- [[Obsidian Core Plugins#Command palette|Command palette]]
- [[Obsidian Core Plugins#File explorer|File explorer]]
- [[Obsidian Core Plugins#Outline|Outline]]
- [[Obsidian Core Plugins#Starred notes|Starred notes]]
- [[Obsidian Core Plugins#None|None]]
- [[Obsidian Core Plugins#Quick switcher|Quick switcher]]

**Community plugins**:
- [[recent-files-obsidian|Recent Files]]
- [[link-favicon|Link Favicons]]
- [[obsidian-floating-toc-plugin|obsidian-floating-toc-plugin]]
- [[various-complements|Various Complements]]
- [[obsidian-electron-window-tweaker|Electron Window Tweaker]]
- [[obsidian-another-quick-switcher|Another Quick Switcher]]
- [[obsidian-dynamic-highlights|Dynamic Highlights]]
- [[obsidian-kanban|Kanban]]
- [[longform|Longform]]
- [[oz-image-plugin|Ozan's Image in Editor Plugin]]
- [[obsidian-style-settings|Style Settings]]
- [[breadcrumbs|Breadcrumbs]]
- [[obsidian-languagetool-plugin|LanguageTool Integration]]
- [[dataview|Dataview]]
- [[supercharged-links-obsidian|Supercharged Links]]
- [[obsidian-pandoc-reference-list|Pandoc Reference List]]
- [[obsidian-hider|Hider]]
- [[obsidian-git|Obsidian Git]]

[^1]: Generally, Obsidian themes work with any plugins. That a plugin is not listed here does not mean that it won't work together with the theme. Plugins listed here only received special attention and/or styling by the theme designer.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Themes/Shimmering%20Focus.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Themes/Shimmering%20Focus.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
