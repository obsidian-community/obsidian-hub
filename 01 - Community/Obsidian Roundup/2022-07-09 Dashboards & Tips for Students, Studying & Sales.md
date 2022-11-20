---
link: https://www.obsidianroundup.org/2022-07-09/
author: Eleanor Konik
published: 2022-07-09T12:30:00
publish: true
---

# 2022-07-09: Dashboards & Tips for Students, Studying & Sales
Discussions about quick capture methods, including inboxes, daily notes, and logs. Methods for copying shell commands, and metadata manipulation plugins.

## Obsidian Updates

-   Insider [v0.15.4](https://forum.obsidian.md/t/obsidian-release-v0-15-4-insider-build/39897) added a "toggle always on top" command to pin popout windows above the other windows on your desktop, improved scrollbar styling and view dragging experiences, and fixed some other quirks that cropped up with the new popout windows. Insider [v0.15.5](https://forum.obsidian.md/t/obsidian-release-v0-15-5-insider-build/40031) had some other assorted fixes.

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list. For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new)._

-   [Obsidian GoLinks](https://github.com/xavdid/obsidian-golinks) by `@xavdid`  renders [go/links](https://www.golinks.io/) — which are like fancy shortcuts for things like go/github — as clickable links.
-   [Zotero Link](https://github.com/vanakat/zotero-link) by `@MunGell`  lets users insert links to Zotero items from Obsidian interface using Zotero Bridge.
-   [Obsidian better Internal Link Inserter](https://github.com/salmund/obsidian-better-link-inserter) by `@salmund`  allows allows the use of selected words as an alias in link suggestion.
-   [PostgreSQL Obsidian](https://github.com/clouedoc/postgresql-obsidian) by `@clouedoc`  uploads note metadata to a database.
-   [Weread Plugin](https://github.com/zhaohongxuan/obsidian-weread-plugin) by `@zhaohongxuan`  integrates with a Chinese ebook store, similar to how the Kindle Highlights plugin interfaces with Amazon ebooks.

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Sidebar Toggler](https://github.com/chrisgrieser/obsidian-sidebar-toggler) by `@chrisgrieser`  offers finer control of the Obsidian sidebars and is meant to be used with an external window manager.
-   [FileExplorer Customizer](https://github.com/azaol-aegnor/obsidian-fec) by `@azaol-aegnor`  supports neat features like icons, folder hiding, outlines, directory highlighting, and more.
-   [TimeDiff plugin](https://github.com/dominiczaq/obsidian-plugin-time-diff) by `@dominiczaq`  calculates and displays diff in hours and minutes between two dates in `timediff` markdown block.
-   [Map for Note](https://github.com/Quorafind/Obsidian-Map-For-Note) lets users see all the paths between nodes, mindmap style, similar to the Journey plugin.
-   [Metadata Menu](https://github.com/mdelobelle/metadatamenu) by `@mdelobelle`  adds options to file and link context menu to change the metadata of the target note.
-   [Date in metadata](https://github.com/salmund/obsidian-date-in-metadata) by `@salmund`  will automatically insert the date in the YAML frontmatter when you create a file.
-   [Typing Transformer](https://github.com/aptend/typing-transformer-obsidian) by `@aptend`  is sort of like a text expander, so you can type `dpx` and it'll turn into `don't panic`.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

-   [Customizable Page Header Buttons](https://github.com/kometenstaub/customizable-page-header-buttons/releases/tag/4.4.0) got an auto-refresh update to make it more compatible with Pane Relief, which itself was updated to fix a bug related to the new popout windows in Insider. It also supports title bar buttons in pop-out windows, and works in graph view style panes.
-   [SQL powered tasks](https://github.com/sytone/obsidian-tasks-x/releases/tag/2.6.1) has been updated to keep it in step with the Tasks updates.
-   [Hover Editor 0.10.5](https://github.com/nothingislost/obsidian-hover-editor/releases/tag/0.10.5) is now available as a public release, suitable for use with Obsidian 0.14.5 through 0.15.3.
-   [Another Quick Switcher v5.2.0](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/5.2.0) now has commands to open in new pane vertically or horizontally.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   Here's a [fork of the longform plugin](https://github.com/GamerGirlandCo/longform/) that supports a new project structure.
-   [Query Control v0.5.0](https://github.com/nothingislost/obsidian-query-control/releases/tag/0.5.0) supports backlinks; you can now render backlinks as HTML as well as setting the defaults for backlink display such as "collapse results" or "show more context".
-   The new [compile notes plugin](https://github.com/michKneisel/obsidian-compile-notes-plugin) lets you compile a longer document by adding links or transclude links to your obsidian note and then pulls all the content from the notes and child notes into a new document.

### For Developers

-   There were some [workspace API improvements](https://forum.obsidian.md/t/obsidian-release-v0-15-4-insider-build/39897), changes to the `Suggest` component's DOM structure, and updates to the `workspace.getActiveFile` behavior. Theme developers can also choose not to override mac native scrollbars with the new Insider build.  Insider [v0.15.5](https://forum.obsidian.md/t/obsidian-release-v0-15-5-insider-build/40031) had some other assorted improvements for leaf views.

## Feature Requests

-   Some folks would like to see [html-backed tables that are editable in live preview](https://forum.obsidian.md/t/live-preview-edit-table-cell-by-cell/34110/4) mode.

## Appearance

-   [Golden Coffee](https://github.com/kinmury/obsidian-ukiyo) by `@kinmury`  is the new home of the `Golden Book` and `Alchemy` themes; they're alternates accessible via Style Settings.
-   [Prism v2.3.0](https://forum.obsidian.md/t/theme-prism/36493) got a bunch of small fixes and has better support for a couple more community plugins.
-   [ITS Theme](https://forum.obsidian.md/t/theme-its-dark-light-theme/12838/163) improved support for right to left bullet lists, changed the icons for horizontal and vertical split to be more accurate, and got new [documentation for callouts](https://github.com/SlRvb/Obsidian--ITS-Theme/blob/main/Guide/Callouts.md).

## Ancillary Code

-   Folks who like doing things with shell commands should check out [this github issue](https://github.com/Taitava/obsidian-shellcommands/discussions/151#discussioncomment-3071934=) where a way to share commands easily between vaults was discussed.

## Guides

-   Here's a really epic [video about using Obsidian for students](https://www.youtube.com/watch?v=LyOIvoHtRCM) that is epic enough that `@Silver` (one of the Obsidian developers) asked everyone to at least watch the first minute.
-   Here's a nice writeup on Twitter about [a red team pen testing practice](https://twitter.com/_rybaz/status/1544661984666427394) using Obsidian (among some other tools) to manage knowledge, methods, reports, findings, templates, etc.
-   Here's how to use the kanban and excalibrain plugins to [visualize notes in Obsidian](https://go-paperless.net/2022/07/08/how-i-use-visualization-to-make-sense-of-my-notes-in-obsidian/).
-   Here's a [dashboard workflow for using Obsidian to support work in sales](https://forum.obsidian.md/t/dashboard-and-workflow-for-obsidian-at-work-sales/34794).
-   Here's how to [use dataview and database folders](https://youtu.be/ZKOYtrVXSbk) for roleplaying games.
-   Here's a great how-to for [using Dataview to get the most out of daily notes](https://discord.com/channels/686053708261228577/744933215063638183/993741149380550758) used for logging things like meetings and emails, via Leah in Discord.
-   Here's a 30-minute video outlining [a notetaking framework for different subjects](https://www.youtube.com/watch?v=LyOIvoHtRCM), using Obsidian.

## Discussions

-   Here's a discussion Reddit about [why people use daily notes instead of inbox logs](https://www.reddit.com/r/ObsidianMD/comments/vpwvwe/why_do_some_people_stick_to_daily_note_what_am_i/).
-   And another discussing different [quick capture](https://www.reddit.com/r/ObsidianMD/comments/vt0w9s/i_want_to_understand_your_way_of_taking_quick/) methods.
-   Here's a brief one with tips and comments about [using Obsidian for studying](https://www.reddit.com/r/ObsidianMD/comments/vu3w03/this_is_the_study_way/).

## Ancillary Tools

-   [Fleeting Notes](https://fleetingnotes.app/posts/imagine-google-keep-with-obsidian-sync/) now has [bidirectional sync](https://github.com/fleetingnotes/fleeting-notes-obsidian/releases/tag/0.2.0) with Obsidian; they're billing it as [like Google Keep interfaced with Obsidian](https://www.reddit.com/r/ObsidianMD/comments/vrav7b/imagine_google_keep_with_bidirectional_sync_to/) over on Reddit.
-   The [Raycast Obsidian extension](https://www.raycast.com/marcjulian/obsidian) now has clipboard templates and an action to edit notes.
-   Here's an [RSS reader](https://theoldreader.com/) I had never heard of (The Old Reader) that got discussed on [Hacker News](https://news.ycombinator.com/item?id=31971892) this week.
-   Here's another iOS/macOS markdown app that has strong accessibility features: [mweb](https://www.mweb.im/onemarkdown-help.html).
-   The [Alfred workflow Shimmering Obsidian](https://github.com/chrisgrieser/shimmering-obsidian) got a bunch of little updates, including the ability to set tag-based icons and searches respecting excluded files.

## Housekeeping

-   The web version of the Roundup got updated to the new Ghost version, and you can now get an outline of each post on the left-hand side or top depending on how big your screen is. This should make it easier to jump to sections you care more about. If you're getting this as an email, you can always click the "view online" button at the top of the email to get the outline view. Here's a link to [last week's edition](https://www.obsidianroundup.org/2022-07-02/) so you don't have to scroll up if you want to test it out.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-07-09%20Dashboards%20%26%20Tips%20for%20Students%2C%20Studying%20%26%20Sales.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-07-09%20Dashboards%20%26%20Tips%20for%20Students%2C%20Studying%20%26%20Sales.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
