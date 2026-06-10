---
aliases:
- 
tags: 
- 
publish: true
---

%% ----- Badges ----- %%

![Downloads](https://img.shields.io/badge/downloads-639-573E7A?style=for-the-badge&logo=)
![GitHub last commit](https://img.shields.io/github/last-commit/sonophage/Bureau?color=573E7A&label=last%20update&logo=github&style=for-the-badge)
![GitHub issues by-label](https://img.shields.io/github/issues/sonophage/Bureau/help%20wanted?color=573E7A&logo=github&style=for-the-badge) 
![GitHub Repo stars](https://img.shields.io/github/stars/sonophage/Bureau?color=573E7A&logo=github&style=for-the-badge)

%% ----- Badges ----- %%

%% ----- Do not edit this section ----- %%

# Bureau

Repository: [GitHub](https://github.com/sonophage/Bureau)
Designed by: [[sonophage]]
Modes: [[Dark-mode themes|dark]]



![screenshot](https://github.com/sonophage/Bureau/raw/HEAD/screenshot.png)

%% ----- Do not edit anything above this line ----- %% 

%% Does the repository or author have any sponsoring links? Uncomment the next line and add them to the author's note. If they don't, please delete the placeholder tag: #placeholder/author %%
%% ![[sonophage#Sponsor this author]] %%


## Features

- [[Themes with Friendly Settings|Friendly settings]]: Supports the [[obsidian-style-settings|Style Settings]] plugin

## Customization Options (Style Settings Plugin) 
- What's new — v2.9.3: **Bureau v2.9.3**

- **New README hero** — the README now leads with the Bureau wallpaper artwork (full 1536×1024, served as a 264 KB webp) in place of the small store screenshot. Docs/asset only — no theme changes.

Full release history is at the foot of this panel. **Updates:** install via the community-themes browser or [BRAT](https://github.com/TfTHacker/obsidian42-brat) to be notified automatically; otherwise re-download `theme.css` from the [releases page](https://github.com/Sonophage/Bureau).
- Reset all options: To restore every Bureau setting to its default: open this Style Settings pane's header row and click the reset (↻ "Reset all settings") button. Every option below has a defined default, so the reset is clean.

**Mode**: Quick effect presets and the inverted-editor toggle — start here.
- Effects mode: Quick preset. Low = base styling only · Medium = + textures & glow · High = everything on · Custom = use the toggles below. Your toggles are always preserved — Custom restores them. While Low or Medium is active it overrides those toggles; switch to Custom to use them.

**Color & accent**: Accent preset and custom colour, per-mode text, and black / white levels.
- Inverted editor (opposite palette to the chrome): Render the editor pane in the OPPOSITE palette to the rest of the UI — paper page on dark chrome in dark mode, dark page on light chrome in light mode. Flip Obsidian's light/dark appearance to switch which is which (a theme can't change that mode itself).
- Accent preset: Accent colour used across the whole UI and the glow.
- Custom accent: Used when Accent preset is set to Custom.
- Phosphor terminal (tint text to accent): Monochrome vintage-terminal look. Tints the dark-mode body text to the accent colour, so the type itself glows in one hue. Pair it with the Amber or Green (P1) accent preset above (any accent works). Use a bright accent — it recolours all body text, so a dark custom accent will hurt readability. Dark-mode effect.
- Text colour — dark mode: Body text colour while the dark theme is active.
- Text colour — light mode: Body text (typewriter ink) while the paper/light theme is active.
- Black level — dark background: How dark the base background is in dark mode (lower = blacker).
- White level — light background: How light the paper is in light mode (higher = whiter).

**Atmosphere**: Glow, film grain, vignette, shadow, and the accent halo — the ambient layer.
- Glow intensity: Strength of the ambient accent glow at the bottom of the window (0 = off).
- Glow reach: How far up the window the glow rises.
- Film grain: Fine noise over the whole window (0 = off).
- Shadow strength: Depth of shadows on callouts, properties, cards, the editor and side panels (0 = off).
- Sidebar texture: Concrete grain on the side panels.
- Sidebar texture strength: How visible the sidebar paper-grain texture is.
- Vignette: Darkened window edges — full ellipse in dark, top inverted-V (∧) in light (0 = off).
- Accent halo: A soft accent ring that breathes outward from the centre behind the UI. Set the strength below.
- ↳ Halo strength: Peak intensity of the halo ring (0 = invisible).

**CRT**: Scanlines, phosphor text-glow, fullscreen tube mode, and the focus line.
- CRT scanlines: Darkness of the horizontal scanlines over the editor (0 = off).
- Scanline spacing: Pixels between scanlines (smaller = more lines).
- CRT text glow: Phosphor-style glow on body text (0 = off).
- Fullscreen CRT mode: In fullscreen, add a curved CRT-glass vignette, amp scanlines/glow, and recede the chrome.
- Focus line (dim the rest): Dim every line but the one you're editing and mark it with an accent edge.
- ↳ Focus dim amount: How dark the off-focus lines get (lower = dimmer).

**Cards & layout**: Float panes as cards, plus reading width, line-height and spacing dials.
- Cards layout: Float every pane as a bordered card on a dark desk — the base the floating looks below build on.
- Horizontal settings nav: Reflow the settings window's left tab list into a scrolling strip across the top (desktop only).
- Print — show link URLs: When printing or exporting to PDF, append each external link's address after it.
- Card gap: Space between cards, in pixels.
- Card rounding: Corner radius, in pixels.
- Card shadow darkness: How dark the drop-shadow under each card is.
- Card shadow blur (px): How soft the drop-shadow under each card is.
- Card shadow spread (px): Grows or tightens the drop-shadow; negative pulls it in.
- Reading line width: Max line width with "Readable line length" on, in pixels.
- Line height: Body text line spacing.
- Paragraph spacing: Gap between paragraphs, in pixels.

**Floating & glass**: Optional soft/floating looks layered over the brutalist base. All off by default — the standard theme is untouched.
- Heavier card float: Deeper, larger drop shadow so panes float higher off the desk (needs Cards layout on).
- Frosted glass panes: Translucent, blurred editor and sidebar panes — the stage or your wallpaper shows through. Best paired with a custom background.
- Flat card edges (no bevel): Drop the inset glass bevel on cards and panes but keep the drop shadow — flat edges instead of the lit lip.
- Pill terminal (floating editor): Lift the header into floating pills and float the editor as its own rounded card on the desk (the Ultra-Lobster look). Best with Cards layout on. Desktop only — auto-suppressed on phones/tablets, where the floating card breaks layout.
- ↳ Pill terminal — hover to reveal: With Pill terminal on, collapse the header pills until you hover or focus the row, reclaiming that space (needs Pill terminal).
- Editor-only cards (flush sidebars): Only the editor floats as a card — strip the card border, rounding and shadow from the sidebars so they sit flush.

**Pill editor card**: The floating editor card in Pill terminal mode — its border and corner rounding. Needs Pill terminal on.
- ↳ Remove editor card border: Drop the outline around the floating editor card so only its shadow defines the edge.
- ↳ Custom editor card border colour: Recolour the editor card outline with the colour below instead of the theme default.
- ↳ Editor card border colour: Used when "Custom editor card border colour" is on (and ignored when the border is removed).
- ↳ Editor card rounding: Corner radius of the floating editor card, in pixels.
- ↳ Stacked-tabs spine inset: With stacked tabs on, how far the tab spine's top is pushed down to clear the floating pill header band, in pixels.

**Background**: A wallpaper behind the workspace, and an image on the New Tab pane. The wallpaper shows through Frosted glass panes (Floating & glass), so turn that on too.
- Custom background image: Show a wallpaper behind the workspace (best with Frosted glass). Set the image in the field below (a web URL, or a local image embedded as a base64 data URI). For a point-and-click local image, install the companion Redacted Background plugin via BRAT.
- ↳ Background image — web URL: Paste a full url(...) value. Web image: url('https://example.com/bg.jpg'). LOCAL image: embed it as a data URI, url('data:image/jpeg;base64,…') (convert with any image-to-base64 tool). Pure CSS can't point at a vault file by path. Leave as none to fall back to the Redacted Background plugin's image, if installed. A remote web URL is re-fetched on every launch (that server sees your IP); a data URI keeps it fully local.
- ↳ Background dim: Scrim over the wallpaper for legibility (higher = darker/more paper, lower = more image).
- New-tab image: What to show on the New Tab / empty pane, above the stamp + actions. Bureau image is the packaged artwork; Custom URL uses the field below.
- ↳ New-tab image — custom URL: Used when New-tab image is set to Custom URL. Paste a full url(...) value — a web URL, or a base64 data URI for a local file (same approach as the wallpaper field).
- New-tab image size (px): Width and height of the new-tab image.

**Tabs**: Tab shape, what each dock's tabs show, and pinned-tab behaviour.
- Tab shape: Folder = connected file-folder tabs. Pill = fully-rounded floating tabs.
- Main tab content: What the main editor tabs show — icon, title, or both.
- Left sidebar tab content: What the left sidebar tabs show — icon, label, or both.
- Right sidebar tab content: What the right sidebar tabs show — icon, label, or both.
- Pinned tabs — icon only: Pinned tabs collapse to just their icon to save room.

**Hide / Focus**: Focus Mode plus à-la-carte switches for hiding bits of chrome.
- Focus Mode: Hides the tab bar, window buttons & status bar. Bind a hotkey to "Style Settings → Toggle Focus Mode".
- Hide status bar
- Hide breadcrumbs
- Hide tab close button
- Hide left sidebar toggle
- Hide right sidebar toggle
- Hide folder collapse arrow
- Hide command-palette instructions

**Animation**: CRT power-on, scanning line, the Rolodex lift and other eased motions (the master toggle gates all).
- Animations: Restrained, CRT-flavoured transitions. Turn off to disable all motion.
- Animation speed (ms): Entrance speed. Hover/state transitions run at ~0.3× this for responsiveness.
- Animation easing: The motion curve for entrances and transitions.
- CRT power-on (on note/pane open): A quick scan-in flicker when a note or pane first opens.
- Boot sequence (CRT switch-on, on app launch): A bright slit fires across the screen and blooms into a soft wash of light as the app launches — the beam striking the glass before the workspace warms in.
- Ease the phosphor glow: Ramp the CRT text-glow in smoothly instead of snapping it on.
- Fade menus & modals: Menus, modals and popovers fade and scale in instead of appearing instantly.
- Typewriter tooltips: Tooltips type in left-to-right like a typewriter (single-line; turn off if long tooltips clip).
- Scanning line: A faint white line scans down the editor; stays steady, then glitches now and then (the static scanlines stay still).
- Scanning line — brightness: How bright the moving scan line is.
- Scanning line — glitch every (sec): How often the loose-wire blink-burst happens.
- Scanning line — glitch depth: How far the line blinks out during a glitch (0 = fully out / most violent).
- Breathe the ambient glow: Slowly pulse the accent glow at the window edge.
- Terminal block caret: Use a solid block cursor instead of the thin caret.
- Active-line scan sweep: Sweep a faint accent gradient across the line you're editing.
- CRT flicker (subtle): A barely-there brightness flicker over the whole window.
- Channel-change crossfade (note switch): Briefly crossfade the editor when you switch notes.
- Eased checkbox tick: Pop checkboxes with a small eased animation when ticked.
- Limelight (spotlight active pane): Dim every pane but the one you're working in — notes and sidebars. Hover a dimmed pane to peek.
- Respect "reduce motion": Honor the OS reduced-motion setting — disables animation when the system asks. (Phones/tablets are auto-lightened regardless — heavy effects are dropped on mobile by default.)

**Resize handles**: The divider lines between the sidebars and the editor — strip them, or recolour them.
- Remove resize handles: Drop the sidebar split divider lines for a seamless edge.
- Custom resize-handle colour: Recolour the divider lines with the colour below instead of the theme default.
- ↳ Resize-handle colour: Used when "Custom resize-handle colour" is on (and ignored when handles are removed).

**Scrollbars**: Hide the scrollbars, or set their width and thumb colour.
- Hide scrollbars: Hide every scrollbar while the content stays scrollable (wheel, trackpad, keys).
- Fade scrollbars (show on hover): Keep the scrollbar thumb invisible until the pointer is over the scroll area, then show it (covers wheel, trackpad and dragging the grip). A true idle-timeout fade on touch needs a plugin.
- ↳ Fade-out delay (ms): With Fade on, how long the thumb lingers after the pointer leaves the scroll area before it fades out. (Needs your build to animate scrollbar transitions; if it snaps, only a plugin can time it.)
- Accent the thumb while scrolling: Flush the thumb to the accent colour while it's gripped or hovered, easing back to its resting colour. Grip-drag is caught reliably; pure wheel scroll with the pointer off the bar can't be.
- Scrollbar width: Thickness of the scrollbars, in pixels.
- Custom scrollbar colour: Recolour the scrollbar thumb with the colour below instead of the theme default.
- ↳ Scrollbar colour: Used when "Custom scrollbar colour" is on (the active/dragged thumb keeps the accent unless you set a grip colour below).
- Custom scrollbar grip colour: Recolour the active (dragged) thumb with the colour below instead of following the accent.
- ↳ Scrollbar grip colour: Used when "Custom scrollbar grip colour" is on — the thumb colour while you drag it.

**Daily notes**: One accent per weekday — text and background derive from it automatically (works in light and dark). Add a weekday class (monday, tuesday, …) to a note. Disable the old Daily Note Themes snippet — Bureau owns this now.
- Sunday accent
- Monday accent
- Tuesday accent
- Wednesday accent
- Thursday accent
- Friday accent
- Saturday accent

**Changelog**: Every release, newest first.
- Release history: **v2.9.3**
- **New README hero** — the README now leads with the Bureau wallpaper artwork (full 1536×1024, served as a 264 KB webp) in place of the small store screenshot. Docs/asset only — no theme changes.

**v2.9.2**
- **Pill terminal no longer breaks on mobile** — the floating-editor / pill-chrome layout (its `clip-path` traps pane scroll and re-homes `position:fixed` children onto the editor card) doesn't survive a phone or tablet, so every `bu-pill-chrome` rule is now gated `:not(.is-mobile)`. The feature auto-suppresses on small screens even when it's left on for desktop; the editor falls back to the normal card/flat layout the mobile baseline already handles, and desktop is untouched.
- **README rewritten** — a top-to-bottom pass: the noir up front, then a technical walkthrough that follows the Style Settings panel in its real order, reconciled against the current toggles.

**v2.9.1**
- **File Properties pane scrolls under Pill chrome** — the pill card's `clip-path`/`overflow:hidden` on `.view-content` trapped the one sidebar view that scrolls at the view-content level (Properties); it now gets `overflow-y:auto` and no clip, so long property lists scroll again. (File/list/search/outline panes were always fine — they own an inner scroller.)
- **Ctrl+F field stays legible** — the in-editor Find bar's input had a transparent fill, so on the paper palette the document text behind it bled through the typed query. The field now takes a solid fill + explicit ink across rest/hover/focus, and the active match gets a solid accent chip (was a faint translucent default that washed out on light backgrounds).
- **Ctrl+F bar no longer drifts off-screen under Pill chrome** — Obsidian anchors the Find bar to `.markdown-source-view`, which scrolls with the document; the pill card's `clip-path` lets us re-home it to the stationary `.view-content` via `position:fixed`, so it stays pinned to the top of the editor while matches scroll.
- **Active tab name readable under Phosphor** — Phosphor collapses the ink to the accent, which dragged the inverted tab fills (and the active tab's label) into blue-on-blue. The active tab is now a recessed, accent-ringed chip with an accent label, so it reads as the one "lit" tab.

**v2.9.0**
- **Fonts embedded** — Courier Prime and Urbanist now ride inside `theme.css` as base64 woff2 (latin + latin-ext) instead of a Google Fonts `@import`. The theme no longer blocks first paint on a network fetch, renders correctly on a fresh offline install, and never pings Google. (`theme.css` is larger as a result — the price of carrying its own type.)
- **Style Settings reordered** — the card/float family is contiguous now (Cards & layout → Floating & glass → Pill editor card → Background), so the toggle that *enables* the pill editor comes before the section that tunes it. Resize handles and Scrollbars dropped to the bottom; Inverted editor moved into Color & accent where it belongs.
- **Dependency cues** — controls that do nothing until a parent toggle is on (Halo strength, Focus dim, the Pill-editor dials, the custom-colour fields…) now carry a `↳` prefix, so the hierarchy reads at a glance.
- **Clearer descriptions** — Effects mode notes that Low/Medium override the individual toggles; Phosphor terminal warns a dark accent recolours all body text; the background web-URL field notes a remote URL is re-fetched every launch.
- **Housekeeping** — two dead `.status-bar` rules removed, and the two largest CSS sections re-signposted (honest section banners plus sub-dividers for tabs, side docks, graph, Notebook Navigator, search, CRT and fullscreen) so the stylesheet is easier to navigate.

**v2.8.0**
- **Stacked-tabs spine inset** — a new Style Settings slider (under **Pill editor**) tunes how far the tab spine drops to clear the floating pill header when tabs are stacked — replacing a hard-coded value.
- **Wallpaper snippet retired** — the bundled `bureau-wallpaper.css` snippet is gone. Set a local background by pasting a `url('data:image/…')` into the **Background image — web URL** field, or install the [Redacted Background](https://github.com/Sonophage/Redacted-Background) plugin for a point-and-click image. The web-URL field and the plugin both work exactly as before.
- **Housekeeping** — refreshed store/README screenshots, trimmed dead CSS (contradictory transition fallbacks, a vestigial variable, redundant `-webkit-clip-path`), and dropped ~2 MB of unused images from the repo.

**v2.7.0**
- **New-tab dossier** — the empty pane opens on packaged Bureau artwork now, shown by default (switch it Off or to your own image under Style Settings → **New-tab image**), and the old "NO ACTIVE FILE" stamp is retired. The art ships embedded as a base64 webp inside `theme.css` — a theme can only carry `theme.css` + `manifest.json`, so the image rides along in the stylesheet — at double the previous size.
- **Redacted action bar** — the new-tab actions (new note, go to file, …) are a horizontal row of themed icons instead of text, floating on no card. Hover one and the *others* get a hand-skewed censor stripe swept across them — blacked out, like someone decided you didn't need them — while the hovered icon lifts and glows accent. (The icon treatment + data-URI new-tab image are adapted from the [Border theme by Akifyss](https://github.com/Akifyss/Border); the artwork is original.)
- **Lighter listing** — the gallery screenshot dropped from 2.7 MB to a trim 768px PNG, and the README now leads on a 1280px webp hero.

**v2.6.0**
- **Accessibility pass** — secondary "faint" text now clears WCAG AA in both palettes (was ~2.8:1); accent-coloured text (links, *italic* emphasis) darkens on paper via a new `--bu-accent-ink` so it clears AA there too, while borders, fills and glow keep the vivid accent; and a `:focus-visible` keyboard ring marks focus for keyboard / assistive-tech users without showing on mouse clicks.
- **Phosphor terminal** — two new accent presets, **Amber** and **Green (P1)**, plus a **Phosphor terminal** toggle that tints the dark-mode body text to the accent for a monochrome vintage-CRT look.
- **Boot sequence** — the CRT power-on is a real tube switch-on now (collapse to a scan-slit, vertical bloom, phosphor settle), and a new **Boot sequence** toggle adds a beam-striking-the-glass flash on app launch, front-loaded so it lands as the window appears.
- **Accent caret** — the caret rides the accent in every mode (dark, paper, inverted) so it stops getting lost against the ink, and the Block caret pulses like a terminal cursor (stops under reduced-motion, the solid block stays).
- **Checkboxes** — a checked task box is a printed box: white field on dark, black on paper, with an accent mark; fixed the mark vanishing in the editor under Paper / Inverted-editor mode.
- **Coverage** — **notices / toasts**, **Canvas** (node cards + bevel, accent focus, themed edges and backdrop), **footnotes**, and **MathJax** are now styled instead of falling back to stock grey.
- **New Style Settings levers** — **Flat card edges** (bevel off, shadow kept), **Card shadow blur** + **spread** sliders, a **custom scrollbar grip colour** (decoupled from the accent), and an **Animation easing** select (Ease-out / Smooth / Linear).
- **Light-mode fixes** — the accent no longer reverts to red inside the inverted-editor pane (the accent palette moved to a zero-specificity `:where(body)` rule so the Style Settings choice always wins); focused property fields lift onto a visible surface instead of vanishing into the page, and resting property fields carry an accent border.
- **Under the hood** — removed all `:has()` selectors (selector-invalidation cost), consolidated the metadata-input rules from five overlapping blocks into one, tokenised the card drop-shadow, gave the graph-controls panel the theme's card material, and added a `CONTRIBUTING.md` plus a `test/kitchen-sink.md` regression note.

**v2.5.3**
- Resize handles — remove / recolour the sidebar split dividers.
- Pill editor card — border (remove / recolour) + corner-rounding slider.
- Scrollbars — hide, width, thumb colour, hover-fade (+ delay), accent-while-gripped.
- Tabs — centred labels, larger uppercase title, native-divider line removed.
- Inline text — accent italic, bold-italic stamp, white bold on light, www chips on bare URLs.
- Typewriter tooltips restored; nested-modal blur; native/startup accent follows Obsidian's Appearance accent.
- Mobile — file explorer / Notebook Navigator no longer render blank until tapped.

**v2.5.2**
- Editor scroll fix, centred status bar, property-stamp hover.

**v2.5.1**
- Every Style Settings heading carries a one-line description.

**v2.5.0 — Pill terminal & the reading surface**
- Full Ultra-Lobster floating layout; editor floats as its own rounded card; hover-to-reveal reclaims space; tabs rebuilt (active = solid accent, inactive = inverted, editor-aware); per-mode text colour + black/white levels; bare-URL wallpaper; reading-surface polish.

**v2.4.0**
- Floating-header pill chrome + hover peek, glass-bevel cards, accent halo, horizontal settings nav, first print/PDF block.

**v2.3.0**
- Floating & glass mode (frosted panes, wallpaper, pill chrome), rolodex tabs/list.

**v2.2.0 / v2.1.0 / v2.0.0**
- Limelight spotlight; council cleanup pass; daylight (light) variant + inverted-editor chiaroscuro.


%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Themes/Bureau.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Themes/Bureau.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
