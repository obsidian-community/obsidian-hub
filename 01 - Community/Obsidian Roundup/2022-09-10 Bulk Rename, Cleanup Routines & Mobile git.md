---
link: https://www.obsidianroundup.org/2022-09-10/
author: Eleanor Konik
published: 2022-09-10T12:30:54
publish: true
---

# 2022-09-10: Bulk Rename, Cleanup Routines & Mobile git
There's an upcoming discussion of daily logs, a new jira integration, and a job opportunity from the folks at Readwise right as Obsidian's team expanded too :)

## In The Community

* Bianca and Leah are going to chat about the advantages of daily logs [Sunday, September 11](https://lu.ma/5gqo20vg) on Twitter Spaces.
* [This Reddit post](https://www.reddit.com/r/PKMS/comments/wq3u6g/im_researching_how_neurodivergent_people_use_pkm/) involves a PhD student with ADHD is asking people who identify as neurodivergent in some way (including but not limited to ADHD, autism, and dyslexia) to take a survey for dissertation research about how folks use personal knowledge management.

## Obsidian Updates

* The team size has officially doubled, which means the team's [About page](https://obsidian.md/about) has been updated; click through for super cute photos of the babies and cats!
* Folks who were worried about losing Sliding Panes, rejoice! [Tab Stacks](https://forum.obsidian.md/t/obsidian-release-v0-16-2-insider-build/42829) replicate the functionality of Sliding Panes / Andy's Mode in core, as of Insider 0.16.2. [0.16.1](https://forum.obsidian.md/t/obsidian-release-v0-16-1-insider-build/42701) brought a bunch of improvements, including the nifty feature where we'll get in-app release notes after updates!

## Plugin News

### New in Community Plugins

__These plugins went through code review and are now available in Obsidian's plugin list.__ For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new).

* [Bulk Rename](https://github.com/OlegLustenko/obsidian-bulk-rename) by `@OlegLustenko` renames files based on patterns. As of 1.0.0, it allows users to search by tags across the vault and later move or update the names of those notes. It also lets users search for tags and move all files with a particular tag to a particular folder. There's also improved regex support.
* [Note Linker](https://github.com/AlexW00/obsidian-note-linker) by `@AlexW00` will automatically find and link notes.
* [Raindrop Highlights](https://github.com/kaiiiz/obsidian-raindrop-highlights-plugin) by `@kaiiiz` lets you sync your Raindrop.io highlights.
* [Default New Tab Page](https://github.com/chrisgrieser/new-tab-default-page) by `@chrisgrieser` opens a note of your choice when creating a new tab, like in the browser.
* [Open in other editor](https://github.com/yekingyan/obsidian-open-in-other-editor) by `@yekingyan` will open the currently active file in gVim or VScode.
* [Agile Task Notes](https://github.com/BoxThatBeat/obsidian-agile-task-notes) by `@BoxThatBeat` lets users import tasks from your Azure or Jira to take notes on them and make todo-lists!
* [Embed Code File](https://github.com/almariah/embed-code-file) by `@almariah` allows for embedding code files.
* [Embedded Note Paths](https://github.com/b0o/obsidian-embedded-note-paths) by `@b0o` inserts the note file path above each note.
* [Literate Haskell](https://github.com/jajaperson/obsidian-literate-haskell) by `@jajaperson` makes integrating .lhs files into your PKM easier.
* [QuickShare](https://github.com/mcndt/obsidian-quickshare) by `@mcndt` lets users securely share Obsidian notes with one click. Notes are end-to-end encrypted. No API keys or configuration required.
* [Dashing cursor](https://github.com/9r0x/obsidian-dashing-cursor) by `@9r0x` enables a dashing cursor that follows the page scroll.
* [Obsidian Git Mobile](https://github.com/Vinzent03/obsidian-git-mobile) by `@Vinzent03` lets users back up with Git on all devices
* [Kobo Highlights Importer](https://github.com/OGKevin/obsidian-kobo-highlights-import) by `@OGKevin` imports highlights from Kobo devices.
* [RPG Manager](https://github.com/carlonicora/obsidian-rpg-manager) by `@carlonicora` makes it easier to manage your Tabletop Role Playing Game campaigns for Obsidian.

### Pending (as of Friday morning)

__Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the __recently updated__ [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review.__

* [Todoist completed tasks](https://github.com/Ledaryy/obsidian-todoist-completed-tasks) by `@Ledaryy` fetches completed tasks from todoist API and adds them to the Obsidian note.
* [Day and Night](https://github.com/CyberT17/obsidian-day-and-night) by `@CyberT17` automatically toggles themes between day theme and night theme on a set time schedule.
* [TikZJax](https://github.com/artisticat1/obsidian-tikzjax) by `@artisticat1` renders LaTeX and TikZ diagrams in Obsidian notes.
* [Copy Search URL](https://github.com/czottmann/obsidian-copy-search-url) by `@czottmann` adds a button to the search view for copying the Obsidian search URL.
* [HTML Reader](https://github.com/nuthrash/obsidian-html-plugin) by `@nuthrash` is a HTML file reader plugin that can open documents with ".html" and ".htm" file extensions.
* [Obsidian Editing Toolbar](https://github.com/cumany/obsidian-editing-toolbar) by `@cumany` is modified from cmenu, and provides more powerful customization settings and has many built-in editing commands to be a MS Word-like toolbar editing experience.
* [Janitor](https://github.com/Canna71/obsidian-janitor) by `@Canna71` performs cleanup tasks on a Obsidian vault.
* [Squiggle](https://github.com/jqhoogland/obsidian-squiggle) by `@jqhoogland` enables running squiggle code snippets within a note.

### Updates

__If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar.__

* [Obsidian Git](https://ko-fi.com/post/Obsidian-Git-on-Mobile-S6S1EESYJ) __officially__ works on Mobile now!
* [Templater v0.13.0](https://github.com/SilentVoid13/Templater) added an option to show or hide the Templater ribbon icon.
* Using Obsidian Linter v1.4.4, the "move footnote to bottom" option no longer ignores tags, regular markdown links, or wiki links, [among other things](https://github.com/platers/obsidian-linter/releases/tag/1.4.4).
* [Database folder](https://github.com/RafaelGB/obsidian-db-folder) got new documentation as well as new ways to create database from command & sidebar menu with a wizard helper.
* A bunch of plugins like [Commander](https://github.com/phibr0/obsidian-commander) have been updated to work with the Insider build.

### Betas

__Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes.__

* [Literate Styles](https://github.com/johanfriis/obsidian-literate-styles) uses CSS codeblocks to enable styling.

### For Developers

* Readwise is [hiring a frontend engineer](https://readwise.notion.site/Frontend-Engineer-403ee91089204d3f81d354528ff6172d), so if you're good with Javascript & React, or have experience with iOS/Android, reach out -- from what I can tell they're pretty great to work with.
* Here's a great [guide for how to use the new CSS variables effectively](https://www.youtube.com/watch?v=yl0pvIRTWWo&t=7s) for theme development.

## Feature Requests

* Here's a nice [roundup of feature requests to make Obsidian be a bit more in line with some nice features of Scrintal](https://forum.obsidian.md/t/workspace-plugin-update-2-0-discussion/43108).
* [Vertical tabs](https://forum.obsidian.md/t/vertical-tabs-for-more-efficient-use-of-space-and-easier-faster-navigation/42987), a la the Vivaldi browser, would be handy.
* It would be nice if we could [easily filter plugins and themes](https://forum.obsidian.md/t/filter-0-16-ready-themes/42910) for compatability.

## Appearance

* [Minimal](https://github.com/kepano/obsidian-minimal/releases/tag/6.0.1) is now updated to be compatible with the new default theme in 0.16+ and one of the neatest features is that you can color-code the frame by vault, to help differentiate between multiple vaults. There's a great [FAQ](https://github.com/kepano/obsidian-minimal/releases/tag/6.0.1) explaining the difference between Minimal and the new Default theme, and what the development of Default means for Minimal. v6.0.4 adds syntax highlighting options to Style Settings.
* [Silence](https://github.com/luke-rmaki/silence-obsidian) by `@luke-rmaki` is a dark theme that looks updated for v0.16+

## Guides

* Here's a twitter thread detailing an entire [series on how to get the most out of Templater](https://twitter.com/kicki22/status/1565363960240656385).
* Here's an [introduction to folders, links, and tags](https://www.youtube.com/watch?v=IaSl21e19ck).
* Here's a nice guide on [outlining in Obsidian](https://thesweetsetup.com/outlining-in-obsidian/), written and with an accompanying video.
* Here's a really neat breakdown of [how the Graph Analysis plugin works](https://medium.com/@ensleytan/obsidians-graph-analysis-plugin-c9c107da3331).
* Here's a nice [setup guide and sample vault](https://twelvetables.blog/taking-notes-with-obsidian/).

## Showcases

* Here's a nice .gif of someone using [Obsidian like a bullet journal](https://media.discordapp.net/attachments/744933215063638183/1016847016938180749/bulletobsidian.gif).

## Ancillary Tools

* Readwise now has a twitter account just for the [Reader app](https://twitter.com/ReadwiseReader). If you're an existing [Readwise subscriber](https://readwise.io/i/ac9), they've got a self-serve onboarding set up, so the waitlist should move a lot more quickly than it used to.
* Here's a fun photograph of an [analog zettelkasten card](https://discord.com/channels/686053708261228577/935988957034991628/1014875461039435776) from Discord's analog tools thread under the `#off-topic` channel. It's got page, source, zotero bibtex, tags, reference, importance rate, certainty rate, and support for vertical titling!
* Glasp now allows users to import all highlights & notes in Kindle, and export them as a markdown file you can move into your Obsidian vault. Here's a [demonstration](https://twitter.com/_Glasp/status/1564108203368910848) and a [written tutorial](https://medium.com/glasp/tutorial-how-to-import-kindle-highlights-notes-into-glasp-export-them-as-a-file-92301bb539da).

## Housekeeping

* I think I'm caught up after my weekend without Discord or a mouse. If I missed something cool from the last 2-3 weeks (especially notable plugin or theme updates), please reach out and let me know! I'm still digesting some of the info in Discord, but from what I can tell, most of the focus is on the v0.16.x updates with tabs and all the new appearance stuff. I expect that'll take a few more weeks to shake out.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-09-10%20Bulk%20Rename%2C%20Cleanup%20Routines%20%26%20Mobile%20git.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-09-10%20Bulk%20Rename%2C%20Cleanup%20Routines%20%26%20Mobile%20git.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
