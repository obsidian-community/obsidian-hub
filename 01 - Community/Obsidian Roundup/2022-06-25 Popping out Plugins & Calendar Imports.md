---
link: https://www.obsidianroundup.org/2022-06-25/
author: Eleanor Konik
published: 2022-06-25T12:30:00
publish: true
---

# 2022-06-25: Popping out Plugins & Calendar Imports
Obsidian reached the 600 plugin mark, there are some new references for vim users, and improved integration with Notion.

## In The Community

-   As of this week, there are over 600 plugins officially in the community plugins list!

## Obsidian Updates

-   [Insider v0.15.2](https://forum.obsidian.md/t/obsidian-release-v0-15-2-insider-build/39114) has some fixes and improvements. Working out the kinks of the major 0.15.0 update and helping plugins get adapted to the new Codemirror changes was a pretty major focus this week.

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list._ _For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new)._

-   [Redirect](https://github.com/jglev/obsidian-redirect) by `@jglev`  is for redirecting links based on YAML frontmatter.
-   [Google Calendar and Contacts Lookup](https://github.com/ntawileh/obsidian-google-lookup) by `@ntawileh`  will import contact and calendar event information from your Google account.
-   [Code Block](https://github.com/paddan/code-block-plugin) by `@paddan`  converts text into code blocks with automatic language detection.
-   [Task Progress Bar](https://github.com/Quorafind/Obsidian-Task-Progress-Bar) by `@Quorafind`  adds a progress bar for tasks.
-   [Share as Gist](https://github.com/timrogers/obsidian-share-as-gist) by `@timrogers`  shares an Obsidian note as a GitHub gist, which is handy for sharing an individual note.
-   [obsidian echarts](https://github.com/cumany/obsidian-echarts) by `@cumany`  renders Apache ECharts, an open source JavaScript visualization library, in Obsidian.
-   [Stack Overflow Answers](https://github.com/bramses/obsidian-stack-overflow) by `@bramses`  lets users import Stack Overflow answers directly into Obsidian.
-   [Linkify](https://github.com/matthewhchan/linkify) by `@matthewhchan`  will convert matching text into links, for example anything prepended with `@` into a twitter link.
-   [Table to CSV Exporter](https://github.com/metawops/obsidian-table-to-csv-export) by `@metawops`  allows for exporting tables from a pane in reading mode into CSV files.
-   [Obsidian shared to Notion](https://github.com/EasyChris/obsidian-to-notion) by `@EasyChris`  lets users share files in their Obsidian vault to Notion with using Notion's API.
-   [Thumbnails](https://github.com/Meikul/obsidian-thumbnails) by `@Meikul`  will insert video thumbnails into your notes.
-   [Image Gallery](https://github.com/lucaorio/obsidian-image-gallery) by `@lucaorio`  is an easy way to set up a masonry-style image gallery in Obsidian.
-   [Wielder](https://github.com/victorb/obsidian-wielder) by `@victorb`  lets you run Clojure scripts inside your Obsidian documents, similar to how Templater lets you do JavaScript. Here's the [introduction tutorial](https://wielder.victor.earth/Tutorials/01-Introduction).
-   [Timestamp Notes](https://github.com/juliang22/ObsidianTimestampNotes) by `@juliang22`  improves side-by-side notetaking with videos. It makes it easier to annotate your notes with timestamps to directly control the video and remember where each note comes from.
-   [Translator](https://github.com/luhaifeng666/obsidian-translator) by `@luhaifeng666`  translates selected text.
-   [braincache](https://github.com/XSPGMike/braincache_obsidian) by `@XSPGMike`  is a new way to create flashcards from obsidian notes.

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Zotero Link](https://github.com/vanakat/zotero-link) by `@MunGell`  will insert links to Zotero items from Obsidian interface using Zotero Bridge.
-   [Obsidian GnuPlot](https://github.com/theFr1nge/obsidian-gnuplot) by `@theFr1nge`  turns gnuplot code blocks into plots

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

-   [v0.1.2 Fleeting Notes Sync](https://github.com/fleetingnotes/fleeting-notes-obsidian/releases/tag/0.1.2) added mobile support.
-   [Database Plugin](https://github.com/tomaszkiewicz/obsidian-database-plugin) now lets users add and delete files directly from the table.
-   The new [Control Characters](https://github.com/joethei/obsidian-control-characters) update requires Obsidian 0.15.0 or higher, but lets users define what characters will be visible for note, and show other invisible characters, optionally within a selection.
-   [Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher) plugin v5.0.0 allows users to disable "search from headers," use alt instead of ctrl/cmd as part of the hotkeys, and got some other fixes — but _only_ works on Obsidian 0.15.1+
-   [Excalidraw 1.7.0](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.7.0) allows Excalidraw to support the insider 0.15.0 popout windows. This method is not expected to be the permanent solution, but it _does_ work for Obsidian 0.15.2+. ExcaliBrain was also updated to support the insider build.
-   [Quick Explorer](https://github.com/pjeby/quick-explorer/releases/tag/0.1.26) was also updated to work with 0.15.2 multi-window support.
-   [Sliding Panes](https://github.com/deathau/sliding-panes-obsidian/releases/tag/3.2.4) was updated to fix some focus issues, and got separate desktop and mobile leaf width options.
-   [Pane Relief](https://github.com/pjeby/pane-relief/releases/tag/0.0.25) got updated to resolve a minor rendering issue introduced in the insider 0.15.0 build.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   [Meta Bind beta 0.1.4](https://github.com/mProjectsCode/obsidian-meta-bind-plugin) allows users to link to other files, got two-way-sync coded in, and allows for styling with custom CSS.
-   [Hover Editor 0.10.0](https://github.com/nothingislost/obsidian-hover-editor/releases/tag/0.10.0) supports multiple windows in Obsidian 0.15.2 (the current insider build)

### For Developers

-   Here's a discussion about [solutions for supporting popout windows for plugins dealing with complex view things like kanban and excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin/discussions/667).

## Feature Requests

-   Here's a feature request for [better search support for nested tags](https://forum.obsidian.md/t/include-nested-tags-in-auto-completion/39322) you can add your support to if you like.

## Appearance

-   [Minimal 5.3.0](https://github.com/kepano/obsidian-minimal/releases/tag/5.3.0) is a breaking change; if you set your fonts using Minimal Theme Settings you'll need to move them into the Obsidian Appearance section.
-   [Willemstad v0.5.3 Jordaan](https://github.com/tingmelvin/willemstad-x/releases/tag/v0.5.3) was updated to support Obsidian 0.15.x, updated the Publish file, and got some other visual visues.

## Guides

-   There's a new index of useful information [for vim users](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/for+Vim+users) on the Obsidian Hub.
-   Here's a tutorial for [how to make a book tracker in Obsidian](https://thebuccaneersbounty.wordpress.com/2022/06/19/tutorial-how-to-make-a-book-tracker-in-obsidian/).
-   Here's a guide about how to [automatically trigger a template](https://youtu.be/5zcdG6ZWja4) based on the filename of a link.

## Discussions

-   Here's a discussion about [different ways to organize book and course notes](https://www.reddit.com/r/ObsidianMD/comments/vji3kx/how_do_you_guys_organise_your_notes_say_for_a/) via Reddit.

## Ancillary Tools

-   The [Raycast extension](https://www.raycast.com/marcjulian/obsidian) lets users do full content search, use more temples, automatically finds vaults, and more.
-   Here's a way to see the ["backlinks" for HackerNews and Reddit](https://www.reddit.com/r/ObsidianMD/comments/vgnxp1/i_wanted_to_recreate_the_backlink_experience_on/) discussions.
-   [Taio](https://taio.app/) is an iOS/macOS markdown app with excellent accessibility features. It's especially useful for searching nested tags.
-   Here's a markdown-based method for [creating timelines](https://news.ycombinator.com/item?id=31810876) that is similar to mermaid.

## Housekeeping

Welcome to all the 200 or so new folks who signed up for the Obsidian Roundup in the last week! I'm excited to know that my piece about [how I find themed logs more useful than daily notes](https://www.obsidianroundup.org/themed-logs-not-daily-notes/) resonated with so many of you.

I'll send another longform piece of insights about my Obsidian usage to financial supporters on the third Thursday of every month, but in the meantime, this is the "regularly scheduled" content. As soon as I get my newsletter host (Ghost) upgraded to the new version 5.0, you'll be able to opt out of the Obsidian updates and just get the longform essays, if that's your preference.

Enjoy the rest of your weekend!

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-06-25%20Popping%20out%20Plugins%20%26%20Calendar%20Imports.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-06-25%20Popping%20out%20Plugins%20%26%20Calendar%20Imports.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
