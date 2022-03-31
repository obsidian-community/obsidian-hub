---
link: https://www.obsidianroundup.org/2022-02-19/
author: Eleanor Konik
published: 2022-02-19T13:30:00
publish: true
---

# 2022-02-19: Improved Calendars & Embedded Searches
There's a new proof of concept plugin for collaborative live editing, and other plugins looking for new maintainers & assistant. Plus other updates for devs. 

## In The Community

-   The developer of [Buttons](https://github.com/shabegom/buttons) is hoping for [user feedback](https://forms.gle/TCaU2qfsnadVHsUB8) about feature prioritization for the plugin.

## Obsidian Updates

[Insider build v0.13.25](https://forum.obsidian.md/t/obsidian-release-v0-13-25-insider-build/32701) included a bunch of fixes and also:

-   Clicking on links in Live Preview will now open them directly.
-   Embedding list items will now show any sub list items when rendering.
-   Embeds to files that don't yet exist will automatically load the file once it's created. This avoids issues with images that syncs in after opening the note it was embedded in.
-   Word count now properly counts apostrophes.
-   Renamed "Swap line up/down" commands to "Move line up/down".

For Obsidian Publish:

-   Now has an option to hide page title headings.
-   Fixed double scrollbar in hover page preview
-   Viewers using macOS and iOS will now get native scrollbars
-   Frontmatter aliases can now be used to redirect broken links to new content.

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list._

-   [Word Splitting for Japanese in Edit Mode](https://github.com/sonarAIT/cm-japanese-patch) by `@sonarAIT`  helps Obsidian support Japanese word splitting.
-   [Settings Search](https://github.com/valentine195/obsidian-settings-search) by `@valentine195`  lets users globally search settings.  You can even open plugin settings (both core and community) directly from the search results.
-   [Insert Heading Link](https://github.com/signynt/insert-heading-link) by `@Signynt`  lets users add a link to a heading.
-   [Auto Note Mover](https://github.com/farux/obsidian-auto-note-mover) by `@farux`  will automatically move the active notes to their respective folders according to the rules.
-   [Persistent Graph](https://github.com/Sanqui/obsidian-persistent-graph) by `@Sanqui`  adds commands to save and restore the positions of nodes on the global graph view.

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Advanced Selection](https://github.com/anselmwang/obsidian-advanced-selection) by `@anselmwang`  offers more flexible ways to select text in the editor.
-   [Things Link](https://github.com/gavinmn/obsidian-things-link) by `@gavinmn`  makes it easier to  link an Obsidian Note to a Things Project.
-   [Command Palette--](https://github.com/qawatake/obsidian-command-palette-minus-plugin) by `@qawatake`  is the command palette _without_ unwanted commands
-   [Path Title](https://github.com/jdeal/obsidian-path-title-plugin) by `@jdeal`  adds the path (or optional replacement) to the filename title of each pane.

### Updates

-   [Obsidian Fantasy Calendar](https://github.com/valentine195/obsidian-fantasy-calendar) now supports repeating events, leap days, and support for importing events created with the Timelines plugin. It also got a huge performance update.
-   `@AidenLx` created a version of [Alx Folder Note](https://github.com/aidenlx/alx-folder-note/issues/57#issuecomment-1043869102) without `folderv`, which should help it load faster on mobile.
-   [Various Complements  v5.3.0](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/5.3.0) added a `Open source file key` option and an option to include only files under current directory option on current vault complement.
-   Excalidraw 1.6.8 has tray-mode & customizable color palettes. Here's [a demo](https://www.youtube.com/watch?v=2v9TZmQNO8c).
-   [Block Reference Count](https://github.com/shabegom/obsidian-reference-count) now has a bunch of toggles, and fixed a bug with tables in Live Preview.
-   [Codeblock Completer](https://github.com/SkepticMystic/codeblock-completer) now has templates
-   Breadcrumbs now has [a dedicated documentation site](https://skepticmystic.github.io/breadcrumbs/index.html) and an API.
-   [Hider  v1.1.1](https://github.com/kepano/obsidian-hider/releases/tag/1.1.1) added setting to hide vault name in file navigator.
-   [Snippetor](https://github.com/ebullient/obsidian-snippetor) added a slider to control checkbox roundness and has a fix for Blue Topaz theme.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   [Embedded Query Control](https://github.com/nothingislost/obsidian-embedded-query-control) adds controls to all inline queries (in live preview and reading modes) that let you collapse, sort, enable context, copy, hide the title, and hide the results.
-   [Full Calendar](https://github.com/davish/obsidian-full-calendar) replicates the core functionality and appearance of Google Calendar. GCal sync support and task management are on the roadmap, but for now it already handles click-and-drag to create and edit events. Here's a blog post [from the developer](https://davi.sh/blog/2022/01/obsidian-zero/) explaining why they like to use Obsidian, which kicks off a whole series about their workflow.
-   [Zotero plugin](https://github.com/aidenlx/obsidian-zotero-plugin) and [Zotero Obsidian Note](https://github.com/aidenlx/zotero-obsidian-note) are still in alpha phase and won't be available to public soon, but the developer is looking for help and _did_ post it, so I'm sharing it with y'all.
-   There's a new  [proof of concept plugin](https://github.com/shabegom/obsidian-liveblocks) for using [https://liveblocks.io/](https://liveblocks.io/) in obsidian. It would allow for a collaborative editing experience similar to google docs. If anyone is interested in working on this, or taking the poc further **please reach out to the dev** — they could use help on the codemirror parts 🙂
-   [Markdown Commands](https://github.com/JulesGuesnon/obsidian-markdown-commands) (not to be confused with "[extra markdown commands](https://github.com/chrisgrieser/obsidian-extra-md-commands)") acts like a text expander so that you can enter commands like `>todo` to get the markdown `- [ ]` if you forget, which is handy for things like markdown tables, which suck to remember the formatting for.

### For Developers

-   `@esm90` is looking for someone to take over maintenance of the [Vimrc plugin](https://github.com/esm7/obsidian-vimrc-support).
-   `@ifthenelsa` is a technical writer volunteering to help write "getting started" documentation for plugins to help lower the barrier to entry for use by non-technical users. Here's [more information in Discord](https://discord.com/channels/686053708261228577/707816848615407697/942882658252382218).
-   Note that the new Codemirror editor has received an upgrade where previous `&ZeroWidthSpace;` characters, used as placeholders for computing cursor positions, have been switched to 0-width elements. Licat & Silver recommend double-checking that your theme does not contain global `img { ... }` CSS rules to avoid breaking the editor.
-   `TFile.unsafeCachedData` has been removed and is now stored in a private inaccessible `WeakMap` to avoid accidental use of this unsafe data.
-   There is now a new `requestUrl` API function that returns an object with the http response status, headers, as well as getters for `arrayBuffer`, json, and text. This is a more advanced version of the request API. (Requires API version 0.13.25)
-   The request and the new `requestUrl` functions can now accept a body of type `ArrayBuffer`.
-   Also, here's a discussion about [how and why to reduce plugin load time](https://forum.obsidian.md/t/call-for-plugin-performance-optimization-especially-for-plugin-startup/32321).

## Feature Requests

-   It would be cool if we could [create a graph view based on folder structure](https://forum.obsidian.md/t/create-a-graph-based-on-the-folder-structure/32411), with link connections being _superimposed_ on top of it without impacting node positions.

## Appearance

-   [Ebullientworks 0.3.16](https://github.com/ebullient/obsidian-theme-ebullientworks) has cssclass support for tables to force-wrap and word-wrap, and more color support.
-   [Primary v1.2.0](https://github.com/ceciliamay/obsidianmd-theme-primary/releases/tag/v.1.2.0) now has Style Settings support.
-   [Willemstad](https://github.com/tingmelvin/willemstad-x) by `@tingmelvin`   added support for the [footnote indicator](https://github.com/chrisgrieser/obsidian-footnote-indicator) plugin and got some style settings options. It also has a bunch of improvements to tables and other features.
-   [Royal Velvet](https://github.com/caro401/royal-velvet) by `@caro401` exists now.
-   [Minimal](https://github.com/kepano/obsidian-minimal/releases/tag/5.1.3) 5.1.3 got some fixes and new style settings options: can now change the highlighted text background color and bold text weight. 5.1.4 adds the Atom color scheme. 5.1.5 added some fixes for footnotes and narrow panes.
-   The very colorful [Sparkling Wisdom](https://github.com/learnerfvs/Sparkling-Wisdom-obsidian-theme-) theme got some more gradients and improved visibility.
-   [ITS Theme](https://forum.obsidian.md/t/theme-its-dark-light-theme/12838/153) restyles Dataview & Kanban plugins to mimic Notions Board and Gallery views and got a `dvl-c` cssclass inspired by Minimal to style _only_ dataview lists and tables as Notion Cards.

## Small Tips

-   You can use the [MetaEdit plugin](https://github.com/chhoumann/MetaEdit) to quickly add tags to all files within a folder.

## Ancillary Code

-   Here's a [quick entry GUI](https://github.com/parallelinnovation/Quick-note-entry-for-Obsidian) to add entries to your Obsidian daily note even if Obsidian isn't open. It's written in python.
-   Here's a new way to [generate a static site from your Obsidian files](https://github.com/A/obsidian-blog).
-   Here's [a Templater script](https://gist.github.com/GitMurf/ec35c81003b172ce01044993d9849505) that will "clean" selected text from within Obsidian into a friendlier format; it removes square brackets from page links, leave only alias from links, extracts URLs from markdown links, structures bulleted lists to match Microsoft formatting and removes Obsidian tags from the text.
-   Here's a [dynamically created filter menu for dataview tables](https://github.com/kuroshirouma/obsidian-dataview-table-filter-menu).

## Guides

-   Here's a new write-up about [how to convert OneNote notes to markdown suitable for Obsidian](https://github.com/theohbrothers/ConvertOneNote2MarkDown/issues/123).
-   Here's a [tutorial for folder notes](https://docs.kenjibailly.xyz/obsidian-folder-notes) (the original version, not Aiden's).
-   [HYPERUNIVERSITY](https://www.hyperuniversity.org/) has curated resources for contemporary digital tools and training in computer skills aimed at students and scholars in the humanities. It's basically an index of useful guides.
-   Here's a comprehensive guide to [using markdown, R, git, and other software](https://plain-text.co/) relevant for the social sciences.
-   Here's a 20-minute video guide on [how to use Obsidian for open-source intelligence work](https://www.myosint.training/courses/osint-documentation-with-obsidian) (OSINT) along with some [templates](https://github.com/WebBreacher/obsidian-osint-templates). The creator also has a [course](https://www.myosint.training/courses/osint-documentation-with-obsidian) available for pre-order.
-   Here's a guide for how to [manage projects and goals](https://bagerbach.com/blog/projects-and-goals-obsidian) from the developer of QuickAdd. It uses Minimal, Contextual Typography, Dataview, QuickAdd, Kanban, and MetaEdit. Christian also included [a demo vault](https://github.com/chhoumann/DemoVault).
-   Here's another guide on how to use [git for syncing with Android](https://werzum.github.io/tech/2022/02/13/Obsidian-Mobile-Sync.html).

## Discussions

-   Here's a discussion about various ways people use [Obsidian for work](https://www.reddit.com/r/ObsidianMD/comments/susevz/does_anyone_use_obsidian_for_work/).
-   Here's one about using [Obsidian for school](https://www.reddit.com/r/ObsidianMD/comments/sv7hf9/obsidian_for_college/) (mostly computer science & med school, but lots of great advice that's broadly applicable).

## Knowledge Management

-   My article about [the value of consistent naming conventions](https://www.obsidianroundup.org/consistent-naming/) went live on Thursday to financial supporters, one of whom shared this excellent article about [the importance of being smart about naming your files](https://mcgeesmusings.net/2016/03/25/whats-in-a-name-unexpected-demands-on-21st-century-knowledge-workers/) — especially when you have nearly 50,000 files to sort through after a fruitful career as a knowledge worker.

## Ancillary Tools

-   [Glasp](https://glasp.co/) is a social highlighting & annotating tool that lets you extract highlights (& annotations) from web articles and send them Obsidian. Here's [a guide](https://medium.com/glasp/tutorial-how-to-export-web-articles-highlighted-sentences-into-obsidian-25d63285bcb9), but as far as I can tell, it's not automatic like the [Readwise](https://readwise.io/i/ac9) plugin, but does export to markdown and is designed with Obsidian users in mind. It's free but as far as I know there's no way to keep your highlights/annotations private, so that's the trade-off.
-   Ernie at Tedium decided to try self-hosting his own cloud setup and then wound up going with Syncthing, but I enjoyed his [explanation of why](https://tedium.co/2022/02/16/self-hosting-dropbox-alternatives/) and what Syncthing is good at. Syncthing is pretty popular in the Obsidian community but this is a pretty good explanation of _why_ people like it.

## Housekeeping

-   I've been doing [one-on-one](https://www.obsidianroundup.org/consult/) meetings on Zoom to help people with Obsidian-related questions for a little over two weeks now. I'm extremely pleased to say that it's been going well: I genuinely do believe that I've helped everyone I've spoken with, and the "pay what you can afford / what you think my time & help help was worth" model is going pretty well, I think.
-   As mentioned last week, I increased the price of the Roundup's "exclusive offerings" (I hate that phrase; I prefer to think of them as a "thank you" to financial supporters). I settled on $4/mo or $44/year. This will _not_ impact current supporters; if you're able to see [The Value of Consistent Naming Conventions](https://www.obsidianroundup.org/consistent-naming/) when you log in (or got it as an email on Thursday), you're good to go (unless you _want_ to switch plans, in which case push the "membership" button floating in the bottom right, you'll need to enable javascript if you have that turned off).
-   Next month's exclusive article will be about creating mental shifts to lower stress and improve productivity. I promise it's not as hokey as it sounds.
-   Some folks asked, so: as things stand, the Roundup has to have about twice as many subscribers as it currently does to support me enough for me to quit teaching when my leave ends. It would have to grow by about 5x to replace my teaching income. Or I guess I could try to figure some kind of ad thing but, ugh, I'd rather not.
-   But! If my consulting work continues at its current rate (I have no idea if this is likely), I'll be able to afford to stay home and continue doing Obsidian community work at my current level even at the current numbers. I'm really hoping that this will all be sustainable for me, and I appreciate everyone's support 💚

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-02-19%20Improved%20Calendars%20%26%20Embedded%20Searches.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-02-19%20Improved%20Calendars%20%26%20Embedded%20Searches.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
