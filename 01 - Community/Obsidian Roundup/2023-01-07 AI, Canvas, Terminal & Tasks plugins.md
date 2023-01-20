---
link: https://www.eleanorkonik.com/2023-01-07/
author: Eleanor Konik
published: 2023-01-07T15:17:17
publish: true
---

# 2023-01-07: AI, Canvas, Terminal & Tasks plugins
Improvements to academic workflows, an upcoming successor to Dataview, and the return of AnuPpuccin.

## Housekeeping

Happy New Year! This edition is going to by necessity be a bit "abbreviated" because it would otherwise overwhelm everyone (including me!) with like three weeks of content, including a ton of things made by wonderful people on holiday vacations who spent it at their desks 😅, but thanks to everyone for being understanding about _my_ holiday break. 

If there's something that happened or came out since December 17 that is not in this edition, but you feel should be shared with the community, please do me a favor and __send me an note letting me know__. 

PS: There are more subheadings than usual, so it might be more pleasant to view this on the web version so you can jump around more easily. 

## Obsidian Updates

The Installer has been updated to use Electron v21, which requires downloading [the latest Installer](https://obsidian.md/). Everyone should do this, but also, [Insider](https://forum.obsidian.md/t/obsidian-release-v1-1-7-insider-build/50052) [updates](https://forum.obsidian.md/t/obsidian-release-v1-1-8-insider-build/50111) made it into [1.1](https://forum.obsidian.md/t/obsidian-release-v1-1/50112) and [1.1.9](https://forum.obsidian.md/t/obsidian-release-v1-1-9/50426), so here are some highlights of what's new:

[Canvas plugin](https://forum.obsidian.md/t/obsidian-release-v1-1/50112#canvas) — A brand new core plugin for Obsidian. Arrange your notes in an infinite canvas.

* Canvas: Added new alignment options to justify content horizontally or vertically.
* Canvas: YouTube embeds are now shown at 16:9 instead of square.
* Canvas: Added a “privacy” toggle to the export modal. This will allow you to share the canvas while masking all the text on the cards.
* Canvas: Added a command to export your canvas as an image.

[Customizable ribbon](https://forum.obsidian.md/t/obsidian-release-v1-1/50112#customizable-ribbon) — Control what items appear in your ribbon and the order they appear in.

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list._ For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new).

* [Paste Mode](https://github.com/jglev/obsidian-paste-mode) by `@jglev`  makes it easier to paste content and mark block quotes at any level of indentation.
* [File Forgetting Curve](https://github.com/ptrsvltns/file-forgetting-curve-obsidian) by `@ptrsvltns`  is a spaced repetition plugin.
* [Paste As Html](https://github.com/maotong06/obsidian-paste-as-html-plugin) by `@maotong06`  lets users paste from web browsers as HTML and keep the original CSS styling.
* [Canvas Presentation](https://github.com/Quorafind/Obsidian-Canvas-Presentation) by `@Quorafind`  helps display cards based on sequences.
* [Open Gate](https://github.com/nguyenvanduocit/obisdian-open-gate) by `@nguyenvanduocit`  lets users embed any website to Obsidian, including ones that were previously difficult to iframe.
* [Toggle Case](https://github.com/MatthewAlner/obsidian-toggle-case) by `@MatthewAlner`  makes it easier to toggle between `lowercase` `UPPERCASE` and `Title Case`, a la the [Text Format](https://github.com/Benature/obsidian-text-format) plugin.
* [Read Later](https://github.com/Canna71/obsidian-readlater) by `@Canna71`  makes it easier to sync web pages to markdown and integrate with read-it-later apps (Pocket, Instapaper)
* [Workona To Obsidian](https://github.com/Holmes555/workona-to-obsidian) by `@Holmes555`  lets users import Workona resources through generated JSON file.
* [Project Garden](https://github.com/bgoosman/obsidian-project-garden) by `@bgoosman`  makes it easier to see all your projects in one place, although the implementation seems more folder based than the [Projects](https://github.com/marcusolsson/obsidian-projects/) plugin.
* [FuzzyTag](https://github.com/adriandersen/obsidian-fuzzytag) by `@adriandersen`  lets users fuzzy match autocomplete tags in Frontmatter
* [DMN Plugin](https://github.com/joleaf/obsidian-dmn-plugin) by `@joleaf`  enables viewing DMNs using dmn-js.
* [Translate](https://github.com/Fevol/obsidian-translate) by `@Fevol`  makes it easier to translate text and notes with Google Translate, DeepL, Azure, and more.
* [Text Extractor](https://github.com/scambier/obsidian-text-extractor) by `@scambier`  helps facilitate the extraction of text from images (OCR) and PDFs. It's meant to be paired with [Omnisearch](https://github.com/scambier/obsidian-omnisearch/releases/tag/1.10.0-beta.1) and other plugins.
* [Google Photos](https://github.com/alangrainger/obsidian-google-photos) by `@alangrainger`  is a Google Photos integration for Obsidian
* [Wordy](https://github.com/nqthqn/obsidian-wordy) by `@nqthqn`  offers a thesaurus, dictionary and more using the Datamuse API
* [Keyshots](https://github.com/KrazyManJ/obsidian-keyshots) by `@KrazyManJ`  adds classic hotkey/shortcuts commands from popular IDEs like Visual Studio Code or JetBrains Family.
* [WakaTime](https://github.com/wakatime/obsidian-wakatime) by `@alanhamlett`  offers automatic time tracking and metrics generated from your Obsidian usage activity.
* [Checklist Reset](https://github.com/lhansford/obsidian-checklist-reset) by `@lhansford`  adds a command to reset the state of any checklists in a document in Obsidian.
* [Base Tag Renderer](https://github.com/darrenkuro/obsidian-basetag) by `@darrenkuro`  renders the basename of tags in preview mode.
* [GPT-3 Notes](https://github.com/micahke/obsidian-gpt3-notes) by `@micahke`  is another way to create a note using OpenAI's GPT-3 language model.

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

#### AI

* [Automatic File Namer](https://github.com/0xble/obsidian-auto-file-namer) by `@0xble`  lets users automatically name files using GPT-3
* [Smart Connections](https://github.com/brianpetro/obsidian-smart-connections) by `@brianpetro`  makes it easier to find links to similar notes using artificial intelligence from OpenAI.
* [Silicon AI](https://github.com/deepfates/silicon) by `@deepfates`  integrates with Silicon AI.
* [Obsidian GPT](https://github.com/jmilldotdev/obsidian-gpt) by `@jmilldotdev`  enables GPT & Large Language Model completions in Obsidian editor via API
* [Canvas Conversation](https://github.com/AndreBaltazar8/obsidian-canvas-conversation) by `@AndreBaltazar8`  allows you to create a ChatGPT conversation using Canvas Cards.

#### Canvas

* [Canvas Random Note](https://github.com/jmilldotdev/obsidian-canvas-randomnote) by `@jmilldotdev`  add random notes from your vault to the Obsidian canvas
* [Canvas CSS class](https://github.com/Lisandra-dev/obsidian-canvas-css-class) by `@Lisandra-dev`  adds a CSS class to the canvas, as well as also other attributes.
* [Canvas Mindmap](https://github.com/Quorafind/Obsidian-Canvas-MindMap) by `@Quorafind`  helps make your canvas work like a mindmap.
* [Link Exploder](https://github.com/benhughes/obsidian-link-exploder) by `@benhughes`  creates a canvas from a note, embedding it's incoming (i.e. backlinks) and outgoing links onto the canvas (as well as the their linked notes).
* [Link Nodes In Canvas](https://github.com/Quorafind/Obsidian-Link-Nodes-In-Canvas) by `@Quorafind`  makes it possible to add edges between notes in Canvas based on their links.

#### Terminalish

* [Terminal Plugin](https://github.com/clevcode/obsidian-terminal-plugin) by `@clevcode`  supports editing files with Neovim and other terminal based editors.
* [Terminal](https://github.com/polyipseity/obsidian-terminal) by `@polyipseity` lets users open terminals in Obsidian directly.
* [Vim Toggle Plugin](https://github.com/conneroisu/vim-toggle-obsidian) by `@conneroisu`  enables togging vim mode on and off inside of the editor.

#### Academia

* [Reference Map](https://github.com/anoopkcn/obsidian-reference-map) by `@anoopkcn`  provides a reference and citation map for literature review and discovery
* [Zotero Annotations](https://github.com/anoopkcn/obsidian-zotero-annotations) by `@anoopkcn`  is a method to import metadata and annotations from Zotero
* [Custom LaTeX Style](https://github.com/KanavMadhura/Custom-LaTeX-Style) by `@KanavMadhura`  lets the user define a custom global LaTeX style, using only Obsidian.

#### Tasks

* [Task Marker](https://github.com/wenlzhang/obsidian-task-marker) by `@wenlzhang`  makes it easier to change task statuses with hotkeys and context menu. Complete, cancel and mark tasks, as well as cycle among selected task statuses.
* [Habit Calendar](https://github.com/hedonihilist/obsidian-habit-calendar) by `@hedonihilist` is helps you render a calendar inside DataviewJS code block, showing your habit status within a month.
* [Asana Sync](https://github.com/Maxymillion/asana-sync-plugin) by `@Maxymillion`  lets users import Asana tasks into Obsidian.

#### Other

* [OpenWeather](https://github.com/willasm/obsidian-open-weather) by `@willasm`  returns the current weather from OpenWeather in a configurable string format.
* [ArchiveBox Plugin](https://github.com/invariant/obsidian-archivebox-plugin) by `@invariant`  archives links to ArchiveBox, a self-hosted archiver, upon file modification.
* [Hints Flow](https://github.com/slpbx/obsidian-plugin) by `@neoantox`  save data directly to Obsidian with a specified template. Capture from Telegram, WhatsApp, Slack, Email, SMS, Raycast and more.
* [Hyphenation](https://github.com/7596ff/obsidian-hyphenation) by `@7596ff`  enables justified text and hyphenation
* [Boost Link Suggestions](https://github.com/jglev/obsidian-boost-link-suggestions) by `@jglev`  alters the order of inline link suggestions by link count and manual boosts.
* [File Chucker](https://github.com/kenlim/obsidian-file-chucker) by `@kenlim`  makes it faster to move a file to a new or existing folder, then open the next file.
* [widgets Plugin](https://github.com/bingryan/obsidian-widgets-plugin) by `@bingryan`  provides very beautiful widgets.
* [Kaffelogic Manager](https://github.com/flaper87/obsidian-kaffelogic-plugin) by `@flaper87`  makes it easier to manage roasts (klog files), notes, logs, amd schedules.
* [Pending notes](https://github.com/ulisesantana/obsidian-pending-notes) by `@ulisesantana`  makes it easier to search for links without notes in your vault (you can also do this with Dataview I think, but the plugin is probably easier for folks who find dataview overwhelming).
* [Email code block](https://github.com/joleaf/obsidian-email-block-plugin) by `@joleaf`  renders an email code block.
* [Larger Display Area](https://github.com/KelvinQiu802/larger-display-area) by `@KelvinQiu802`  helps users set a larger display area for content.
* [Short Internal Links to Headings](https://github.com/scottwillmoore/obsidian-short-internal-links-to-headings) by `@scottwillmoore`  enables displaying internal links to headings as just the heading name.
* [Obsidian Vega](https://github.com/Some-Regular-Person/obsidian-vega) by `@Some-Regular-Person`  makes it easier to create highly-customizable data visualizations like line charts and scatter plots using Vega or Vega-Lite.
* [Order List](https://github.com/lizard-heart/obsidian-order-list-plugin) by `@lizard-heart`  lets users order lists by number at end of line
* [Simply spaced](https://github.com/andrewromanenco/obsidian-simply-spaced) by `@andrewromanenco` provides spaced repetition based on SM-2 with extra randomization in intervals, with Git friendly progress tracking.
* [Meld Build](https://github.com/meld-cp/obsidian-build) by `@meld-cp` makes it easier to write and execute (sandboxed) JavaScript to render templates, query DataView and create dynamic notes.
* [Antidote](https://github.com/Heziode/obsidian-antidote) by `@Heziode`  and [Antidote Plugin](https://github.com/Samuel-Martineau/obsidian-antidote-plugin) by `@Samuel-Martineau` both  integrate Antidote with Obsidian; it's a powerful (and apparently popular) grammar checker.
* [Khoj](https://github.com/debanjum/khoj) by `@debanjum`  provides a more natural, incremental search.
* [The One Ring 2E Statblocks](https://github.com/modality/obsidian-the-one-ring-2e-statblocks) by `@modality`  lets users render TOR 2e statblocks in Obsidian.
* [Image Captions](https://github.com/alangrainger/obsidian-image-captions) by `@alangrainger`  adds captions to images when there is alt-text specified
* [Cycle In Sidebar Plugin](https://github.com/houcheng/obsidian-cycle-in-sidebar-plugin) by `@houcheng`  provides hotkeys to cycle through tabs in the left or right sidebars.
* [Plugin Groups](https://github.com/Mocca101/obsidian-plugin-groups) by `@Mocca101`  lets users manage plugins through groups and enable and disable multiple plugins through a single command, or delay the startup of plugins to speed up your Obsidian start up time.
* [IVRE](https://github.com/ivre/obsidian-ivre-plugin) by `@p-l-`  grabs data from IVRE and brings it into Obsidian notes.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

* [Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/8.0.0) supports not only markdown files but also other files.
* [Surfing 0.8.8](https://github.com/Quorafind/Obsidian-Surfing) lets users send current web page in surfing to [Readwise](https://readwise.io/i/ac9) when you are surfing the net from within Obsidian.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

* I do not normally feature works in progress that haven't yet been released for official beta testing, but this was too exciting to not share: `@blacksmithgu` has begun work on [Datacore](https://github.com/blacksmithgu/datacore), a successor to Dataview with a focus on UX and speed. Looks like planned features include a new Javascript API, WYSIWYG views, functioning embeds, and live editing.
* [Inbox](https://github.com/Zachatoo/obsidian-inbox) shows a notification when launching Obsidian if you have data to process in your "inbox" note.

### For Developers

* As a reminder, Obsidian 1.1 came with [some quality of life improvements for plugin developers](https://forum.obsidian.md/t/obsidian-release-v1-1/50112#developer-improvements) like a new metadata API, a way to configure a donation URL, and a changelog for the Obsidian API.
* Here's a nifty [design system file](https://www.figma.com/community/file/1172227539881210762) for Figma; it's basically a library of user interface components, styles and guidelines that are used while designing software

## Appearance

* [AnuPpuccin](https://github.com/AnubisNekhet/AnuPpuccin) by `@AnubisNekhet` is back.
* [Wikipedia Theme](https://github.com/Bluemoondragon07/Wikipedia-Theme) by `@Bluemoondragon07`  makes  your Obsidian vault feel like Wikipedia.
* [Shiba Uni](https://github.com/faroukx/Obsidian-shiba-uni-theme) by `@faroukx`  offers a soft, comfortable workspace with a Japanese touch.
* [Light & Bright](https://github.com/Bluemoondragon07/obsidian-light-and-bright-theme) by `@Bluemoondragon07` has a rounded, cozy feel.
* [Material Gruvbox](https://github.com/AllJavi/material_gruvbox_obsidian) by `@AllJavi` is based on the current [obsidian gruvbox](https://github.com/insanum/obsidian_gruvbox) theme, but with the [material gruvbox](https://gist.github.com/Cardoso1994/5fbbf98603b44bc986ec18e607b7dbf1) palete.
* [Atomus](https://github.com/PedroHenrique17/Atomus) by `@PedroHenrique17`  is a fork of the Atom theme, with codeblocks based on Dracula.
* [Wombat](https://github.com/hush-hush/obsidian_wombat) by `@hush-hush` is based on the [Wombat256](https://www.vim.org/scripts/script.php?script_id=2465) theme for Vim and offers a dark gray background with easy-on-the-eyes desert-like colors.
* [Abecedarium](https://github.com/zalenza/Abecedarium-theme) by `@zalenza` has hints of blue and yellow.

## Ancillary Code

* Here's [a Ruby script to download content of Reddit posts](https://www.reddit.com/r/ObsidianMD/comments/104k0om/script_save_reddit_posts_to_obsidian/) as a Markdown file usable in Obsidian.

## Guides

* The folks at Keep Productive have updated their [Obsidian Made Simple](https://francescod-alessio441.lpages.co/obsidian-made-simple-roundup/) Course for 2023.
* Here's how to [create your own Obsidian web clipper](https://medium.com/@gareth.stretton/obsidian-create-your-own-web-clipper-add83c7662d0) using a combination of the [Obsidian URI protocol](https://help.obsidian.md/Advanced+topics/Using+obsidian+URI) and [UserScripts](https://openuserjs.org/about/Userscript-Beginners-HOWTO), via Gareth Stretton.

## Showcases

* Check out how [Sarah Arminita Bentley made a chatbot that will answer questions using her Obsidian vault of 20k notes](https://twitter.com/Sarah_A_Bentley/status/1611069576099336207).
* Here's a fascinating use-case: [Obsidian for tracking interconnections in complex workplace email chains](https://www.reddit.com/r/ObsidianMD/comments/101yl9n/email_i_am_getting_deeply_into_connecting_dozens/).
* Here's a nifty [D&D Character Sheet using Canvas](https://www.reddit.com/r/ObsidianMD/comments/zvk7f0/a_dnd_character_sheet_i_made_with_canvas_complete/).
* Here's a [dashboard with lots of graphs](https://www.reddit.com/r/ObsidianMD/comments/104qxpd/created_a_dashboard_based_on_the_tfthacker_version/).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2023-01-07%20AI%2C%20Canvas%2C%20Terminal%20%26%20Tasks%20plugins.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2023-01-07%20AI%2C%20Canvas%2C%20Terminal%20%26%20Tasks%20plugins.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
