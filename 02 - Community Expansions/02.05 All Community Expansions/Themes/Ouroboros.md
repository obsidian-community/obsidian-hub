---
aliases:
- 
tags: 
- 
publish: true
---

%% ----- Badges ----- %%

![Downloads](https://img.shields.io/badge/downloads-265-573E7A?style=for-the-badge&logo=)
![GitHub last commit](https://img.shields.io/github/last-commit/lemon695/obsidian-theme-ouroboros?color=573E7A&label=last%20update&logo=github&style=for-the-badge)
![GitHub issues by-label](https://img.shields.io/github/issues/lemon695/obsidian-theme-ouroboros/help%20wanted?color=573E7A&logo=github&style=for-the-badge) 
![GitHub Repo stars](https://img.shields.io/github/stars/lemon695/obsidian-theme-ouroboros?color=573E7A&logo=github&style=for-the-badge)

%% ----- Badges ----- %%

%% ----- Do not edit this section ----- %%

# Ouroboros

Repository: [GitHub](https://github.com/lemon695/obsidian-theme-ouroboros)
Designed by: [[lemon695]]
Modes: [[Dark-mode themes|dark]], [[Light-mode themes|light]]



![screenshot](https://github.com/lemon695/obsidian-theme-ouroboros/raw/HEAD/screenshot.png)

%% ----- Do not edit anything above this line ----- %% 

%% Does the repository or author have any sponsoring links? Uncomment the next line and add them to the author's note. If they don't, please delete the placeholder tag: #placeholder/author %%
%% ![[lemon695#Sponsor this author]] %%


## Features

- [[Themes with Friendly Settings|Friendly settings]]: Supports the [[obsidian-style-settings|Style Settings]] plugin

## Customization Options (Style Settings Plugin) 

**Features**: 
- Black mobile background: Change mobile editor background to default theme black
- Disable mobile floating-action button: Revert placement of edit/preview button to default in header (mobile)
- Highlight active line: Change background color of current working line
- Fancy code blocks: Enable fancy numbered code blocks
- Code block language labels: Show a small language badge on fenced code blocks in Reading View (fades on hover so the copy button stays reachable)
- Fancy highlighting: Enable fancy highlight styles with highlight underlines
- Disable Kanban board styles: Remove minimalist styling to the Kanban plugin

**Design Tweaks**: 
- **Style packs**: Whole-theme atmosphere presets. Pick ONE pack only — these are not mutually exclusive in the UI, so if you enable several, the pack lowest in this list wins (deterministic, but not what you usually want). Accent presets below can still override only the accent color on top of your chosen pack.
    - Classic Paper style pack: Quiet paper, ink contrast, restrained blue/cyan accents for everyday vault use.
    - Things Warm style pack: Warmer task-planning surface with amber accent and soft cream UI.
    - Research Desk style pack: Wider, cooler, evidence-friendly palette for citations, tables, and source-heavy notes.
    - Longform Book style pack: Book-like serif reading surface for essays, chapters, and manuscript work.
    - Night Ink style pack: Cool ink dark-room palette with clearer dark-mode chroma and a restrained light fallback.
    - Low Contrast Calm style pack: Softer contrast and sage accent for long low-fatigue sessions.
- **Accent presets**: Accent-only overrides. Pick ONE accent — if you enable several (moss / amber / sage / ink-blue / clay / slate), the one lowest in this list wins. Can be combined with one style pack.
    - Moss accent preset: Switch accents to a quieter green palette
    - Amber accent preset: Switch accents to a warmer amber palette
    - Sage accent preset: Switch accents to a calm sage green palette
    - Ink Blue accent preset: Switch accents to a deep, restrained ink-blue palette
    - Clay accent preset: Switch accents to a warm terracotta clay palette
    - Slate accent preset: Switch accents to a cool grey-blue slate palette
- **Paper temperature**: Shift the paper surfaces warmer or cooler. Pick ONE — if both are enabled, Cool wins.
    - Warm paper: Warmer, creamier paper surfaces (light and dark)
    - Cool paper: Cooler, more neutral paper surfaces (light and dark)
    - Compact UI density: Tighten tab, sidebar, and control spacing
    - Airy reading density: Increase reading width and line height
- **Reading width**: Width of the readable line column. Requires Obsidian's "Readable line length" enabled. Reading modes and style packs override these.
    - Reading column width: Pick a comfortable line width for body text.
    - Reading column width (advanced): Override the tier with any CSS length, e.g. 40rem or 760px. Leave blank to use the tier above.
    - Underline internal links: Show underlines on internal links
    - Underline external links: Show underlines on external links

**Typography**: 
- Reading font: Body and editor reading font. The interface chrome stays system sans. CJK mode and style packs override this.
- Default font colors: Use the default font color styling for bold, italics, and quotes
- Highlight color (light)
- Highlight color (dark)
- Bold font color
- Italics font color
- Blockquotes font color
- Inline code blocks font color (Light mode)
- Inline code blocks font color (Dark mode)
- Tag background color (Light mode)
- Tag font color (Light mode)
- Tag background color (Dark mode)
- Tag font color (Dark mode)
- Progress colorful mode switcher: Toggle progress color scheme
- progress 2-39% color
- progress 40-59% color
- progress 60-79% color
- progress 80-99% color
- progress 1,100% color

**Headings**: 
- Numbered headings: Add automatic outline numbers (1, 1.1, 1.1.1) to H1–H4 for a chapter-like feel. Works in Reading View and Live Preview.
- **Level 1 Headings**: 
    - H1 font size: Accepts any CSS font-size value
    - H1 font weight: Accepts numbers representing the CSS font-weight
    - H1 color
- **Level 2 Headings**: 
    - H2 font size: Accepts any CSS font-size value
    - H2 font weight: Accepts numbers representing the CSS font-weight
    - H2 color
    - H2 underline: Toggle H2 underline (border-bottom)
- **Level 3 Headings**: 
    - H3 font size: Accepts any CSS font-size value
    - H3 font weight: Accepts numbers representing the CSS font-weight
    - H3 color
- **Level 4 Headings**: 
    - H4 font size: Accepts any CSS font-size value
    - H4 font weight: Accepts numbers representing the CSS font-weight
    - H4 color
    - H4 transform: Transform the H4 heading text
- **Level 5 Headings**: 
    - H5 font size: Accepts any CSS font-size value
    - H5 font weight: Accepts numbers representing the CSS font-weight
    - H5 color
- **Level 6 Headings**: 
    - H6 font size: Accepts any CSS font-size value
    - H6 font weight: Accepts numbers representing the CSS font-weight
    - H6 color

**New Features**: 
- Bullet threading: Draw a rounded accent thread from ancestor bullets down to the active list line (Logseq-style outline cue). Editor only — Reading View has no cursor. Covers 6 indent levels; assumes Obsidian's default tab size.
- Clean embeds: Strip the card chrome from embedded notes so transclusions read as part of the host note, with a quiet accent rail on hover. Also available per note via cssclasses 'embed-clean'. Opt-in.
- Active path emphasis: Give the current note a warm low-noise cue — active tab title and top rail, the active pane's view-header title, and a quieter breadcrumb path. Only the current item is emphasized.
- Task priority palette: Map Tasks-plugin priorities (highest…lowest) to the warm progress 5-color ramp as a quiet left rail, with a warm due chip. Urgency reads warm-to-cool; date proximity needs a JS plugin. Opt-in.
- Paper panes: Give each editor tab group a thin border, soft shadow, and rounded corners so panes read as raised paper sheets. The active pane lifts a little more with a quiet accent edge. Editor area only; sidebars stay flat. Opt-in.
- Typewriter focus: A Focus mode sub-toggle. While editing, inactive lines dim and the active line stays sharp, with generous vertical room so you can keep the current line near the screen center. Live Preview / source only. Requires Focus mode on; a true scroll-locked typewriter needs a plugin.
- Focus mode: Dim sidebars, ribbon, and status bar while keeping hover/tab recovery rails visible
- Keyboard mode: Strengthen keyboard focus rings and add command/switcher navigation hints for keyboard-first vault work
- Research reading mode: Add citation, footnote, quote, table, and annotation polish for research-heavy notes
- Longform reading mode: Add chapter-like spacing, centered headings, scene breaks, and calmer prose rhythm for long essays and drafts
- CJK typography mode: Use CJK-optimized sans-serif font stack for Chinese/Japanese/Korean text
- CJK serif font: Switch CJK mode to use a serif (Song/Ming) font stack. Requires CJK mode on.
- Reduce motion: Disable all animations and transitions (overrides prefers-reduced-motion)

**Credits**: Created by Lemon695. Visual direction inspired by the Things app and the original Things theme by @colineckert.

## Plugin Compatibility[^1]

**Core plugins**:
- [[Obsidian Core Plugins#Backlinks|Backlinks]]
- [[Obsidian Core Plugins#None|None]]
- [[Obsidian Core Plugins#None|None]]
- [[Obsidian Core Plugins#None|None]]
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
- [[Obsidian Core Plugins#Daily notes|Daily notes]]
- [[Obsidian Core Plugins#Random note|Random note]]
- [[Obsidian Core Plugins#Publish|Publish]]
- [[Obsidian Core Plugins#Sync|Sync]]
- [[Obsidian Core Plugins#Word count|Word count]]

**Community plugins**:
- [[dataview|Dataview]]
- [[calendar|Calendar]]
- [[obsidian-full-calendar|Full Calendar]]
- [[obsidian-tasks-plugin|Tasks]]
- [[todoist-sync-plugin|Todoist Sync]]
- [[obsidian-excalidraw-plugin|Excalidraw]]
- [[obsidian-hover-editor|Hover Editor]]
- [[obsidian-banners|Banners]]
- [[obsidian-checklist-plugin|Checklist]]
- [[obsidian-kanban|Kanban]]
- [[obsidian-outliner|Outliner]]
- [[obsidian-timeline|Timeline]]
- [[obsidian-git|Git]]
- [[obsidian-style-settings|Style Settings]]

[^1]: Generally, Obsidian themes work with any plugins. That a plugin is not listed here does not mean that it won't work together with the theme. Plugins listed here only received special attention and/or styling by the theme designer.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Themes/Ouroboros.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Themes/Ouroboros.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
