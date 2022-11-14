---
link: https://www.obsidianroundup.org/mobile-pdf-indexing/
author: Eleanor Konik
published: 2022-10-22T12:30:48
publish: true
---

# 2022-10-22: Improved note relationship sensing & Catppuccinos!
Kepano shared some thoughts about the AI-assisted text generation plugins, there's a new plugin for RTL/LTR language detection, plus: improved OCR

## In The Community

_Note: a bunch of great things happen in Discord every week, but the links require you to be logged in to [the community server](https://obsidian.md/community) and generally launch in the browser version of Discord unless you paste them into your app directly. Sorry!_ 

The videos of the 3rd week of Obsidian October live sessions are up:

* [Setting up plugin settings](https://www.youtube.com/watch?v=gG4HJ3RbzD4) with Marcus Olsson.
* [Creating a theme for Obsidian 1.0](https://www.youtube.com/watch?v=tARSN_dSaaI) with Stephan Ango (aka `@kepano`).

## Obsidian Updates

* Obsidian Mobile 1.4.0 updated Mobile to Obsidian 1.0, got a big user interface overhaul, new navigation bars, tabs, haptic feedback, and more. Definitely read [the release notes](https://forum.obsidian.md/t/obsidian-mobile-1-4-0/45618); a lot of things moved around.
* Insider Desktop builds [v1.0.1](https://forum.obsidian.md/t/obsidian-release-v1-0-1-insider-build/45735/2) and [v1.0.2](https://forum.obsidian.md/t/obsidian-release-v1-0-2-insider-build/45769/2) were both mostly bugfixes.
* I really enjoyed this [reflection on the update to Obsidian 1.0](https://miscellaneplans.medium.com/obsidian-1-0-frustration-fixes-fidelity-69178347cdea) and how it disrupted things for one user (Ellane W), but she adapted.

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list._ _For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new)._

* [Influx](https://github.com/jensmtg/influx) by `@jensmtg` is a very exciting alternative backlinks plugin, which displays relevant and formatted excerpts from notes with linked mentions, based on the position of mentions in the notes' hierarchical structure (bullet level indentation).
* [Doubleshift](https://github.com/Qwyntex/doubleshift) by `@Qwyntex` makes it possible to open the command palette by pressing Shift (or any other key) twice like in IntelliJ and create your own shortcuts
* [Novel word count](https://github.com/isaaclyman/novel-word-count-obsidian) by `@isaaclyman` displays a word count (and more!) for each file, folder and vault in the File Explorer pane.
* [Dynamic RTL](https://github.com/mwxgaf/obsidian-dynamic-rtl) by `@mwxgaf` will change the RTL/LTR direction per line / paragraph, depending on the language.
* [Theme Toggler](https://github.com/larsmagnus/obsidian-theme-toggler) by `@larsmagnus` adds a theme toggle button to each pane in your workspace, allowing users to set the theme on a _per-panel_ basis, along with adding commands to toggle themes between states.
* [HTML Reader](https://github.com/nuthrash/obsidian-html-plugin) by `@nuthrash` lets users open documents with ".html" and ".htm" file extensions.
* [Week Planner](https://github.com/rwirdemann/obsidian-week-planner) by `@rwirdemann`defines commands for creating planning documents and moving tasks between them.
* [Squiggle](https://github.com/jqhoogland/obsidian-squiggle) by `@jqhoogland` enables running squiggle code snippets within a note.

### Pending (as of Friday morning)

_Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

* [Relation Pane](https://github.com/mottox2/obsidian-relation-pane) by `@mottox2`displays a panel that summarize relations between notes.
* [Mathpad](https://github.com/Canna71/obsidian-mathpad) by `@Canna71` is a fancy calculator that works inline and in the sidebar.
* [Obsidian Things3 Sync](https://github.com/royxue/obsidian-things3-sync) by `@royxue`  syncs between Obsidian and Things3, create Todo and sync Todo status.
* [qmd as md](https://github.com/danieltomasz/qmd-as-md-obsidian) by `@danieltomasz` provides an initial support for viewing files with .qmd extension. QMD files contain a combination of markdown and executable code cells and are a format supported by Quarto open source publishing system.
* [Obsidian Github Uploader](https://github.com/yaleiyale/obsidian-github-uploader) by `@yaleiyale` uploads the files in your clipboard to Github.
* [Status Bar Quote](https://github.com/yesjinu/StatusBarQuote) by `@yesjinu` will display a favored quote in the status bar.
* [Old Note Admonitor](https://github.com/tadashi-aikawa/obsidian-old-note-admonitor) by `@tadashi-aikawa`shows warnings if the note has not been updated in a period of time you set.
* [Double Click Tab](https://github.com/Quorafind/Obsidian-Double-Click-Tab) by `@Quorafind`modifies the default behavior when you double click on the tab title, like close tab.
* [Checkbox 3 states](https://github.com/hrenaud/obsidian-checkbox3states-plugin) by `@hrenaud`adds a third state to checkbox list.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

* [Obsidian OCR v1.3.0](https://github.com/MohrJonas/obsidian-ocr/releases/tag/1.3.0) got a bunch of stability and speed improvements, improved installation instructions, previews when searching, and more.
* [Digital Garden 2.17.0](https://notes.ole.dev/set-up-your-digital-garden/) introduced the option to show backlinks and a local graph in your published notes.
* [Latex Suite 1.6.0](https://github.com/artisticat1/obsidian-latex-suite/) now allows  you to load snippets from another file, which means you can use an external text editor to edit, backup and share snippets with others.
* [database folder 2.7.4](https://github.com/RafaelGB/obsidian-db-folder/releases/tag/2.7.4) now has support for nested YAML fields and the ability to edit the name of tags which updates all the rows and files.
* [Excalidraw 1.7.23](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.7.23) added support for webp, bmp, and ico images, which extends the already supported formats (jpg, gif, png, svg). v1.7.24 also got a bunch of bug fixes and a new hook for changing the styling when the canvas color changes. The automations possible with Excalidraw are incredible.
* Obsidian Bulk Rename, Media DB Plugin, Buttons, Obsidian Git, Advanced Slides (and probably more!) updated to have improved compatibility with the Obsidian 1.0 update. Please update often as developers adjust to the new stable (!) API.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

* The [Omnisearch Beta](https://github.com/scambier/obsidian-omnisearch/releases/tag/1.6.5-beta.5) (which allows for PDF indexing) now works on mobile.
* [Strange New Worlds](https://forum.obsidian.md/t/obsidian-october-2022-daily-progress-and-learnings/43767/13?u=tfthacker), from `@TfTHacker` is meant to help show the interconnections between notes and is sort of a spiritual successor to the Block Ref Counter plugin.

## Appearance

* ITS Theme, Wyrd, CyberGlow, Shimmering Focus (and probably more!) have been updated to work with Obsidian 1.0 – please update your themes if you experience problems.
* [Fusion](https://github.com/zamsyt/obsidian-fusion) by `@zamsyt` aims at minimalism and has a nice blue tint.
* The Catppuccino color scheme (a "soothing pastel theme for the high-spirited") is now available in [Catppuccin](https://github.com/catppuccin/obsidian) by `@mbeckrich`, [AnuPpuccin](https://github.com/AnubisNekhet/anuppuccin) by `@AnubisNekhet`, and [Minimal](https://minimal.guide/) by `@kepano`. The latter two support several other popular color schemes as well.
* [Dayspring](https://github.com/erykwalder/dayspring-theme) by `@erykwalder` looks particularly nice for religious texts: it allows for putting things like verse numbers besides paragraphs in an unobtrusive way, outside of the flow of the main text.
* Here's a snippet in Discord to [turn the highlightr plugin into a plugin that changes text color](https://discord.com/channels/686053708261228577/855181471643861002/1030379180430462987) just with a custom config & a css snippet.

## Ancillary Code

* Here's a MacOS shortcut that is useful for [intersitial journal entries](https://twitter.com/hstagner/status/1579804046306656258?s=20&t=oC2QljfioVCKe3ozMEa7Eg) explained in both video and written form.

## Guides

* This is a pretty good explanation of how to use Obsidian as a content management system for a website without using the official Publish plugin, with [the Obsidian vault and website directory as sibling directories](https://www.gatlin.io/content/how-i-use-obsidian-as-a-cms-for-my-website) so that it's easier to distinguish between public/private notes. It's a pretty novel approach as far as I know.
* Here's an excellent [introduction to markdown for beginners](https://twitter.com/n_vanderhoeven/status/1583488865234345984) video.
* This thread explains a method for [database style queries](https://twitter.com/ThoughtfulAtlas/status/1580251417993805825) with lots of screenshots.
* Martine Ellis shared a [system for idea generation, journaling, and article outputs](https://twitter.com/MartineGuernsey/status/1581540522594045953).
* This video describes an approach to [planning music classes & ensembles](https://www.youtube.com/watch?v=YhMVOtzcgX0) using Obsidian.

## Discussions

* There was an interesting folders vs. tags discussion in Discord where some nice thoughts were shared about [the value of neat tags and messy subtags](https://discord.com/channels/686053708261228577/710585052769157141/1033191865228472351).
* Lots of folks on Twitter shared [meeting notes templates](https://twitter.com/Federico_Presta/status/1582383574224760832?s=20&t=oC2QljfioVCKe3ozMEa7Eg).

## Showcases

* Here's a neat [subscription tracker template](https://www.reddit.com/r/ObsidianMD/comments/y699wi/a_basic_subscription_tracker_template_for/) that uses the Advanced Tables plugin.
* Here's how Zsolt (developer of the Excalidraw plugin) [integrates time into notes](https://www.youtube.com/watch?v=qIKg_1FNUgk).

## Food For Thought

* `@kepano` shared some [thoughts about AI-assisted writing](https://stephanango.com/photoshop-for-text) in the context of some of the relevant Obsidian plugins: [Text Generator](https://github.com/nhaouari/obsidian-textgenerator-plugin) and [Obsidian Ava](https://github.com/louis030195/obsidian-ava).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-10-22%20Improved%20note%20relationship%20sensing%20%26%20Catppuccinos%21.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-10-22%20Improved%20note%20relationship%20sensing%20%26%20Catppuccinos%21.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
