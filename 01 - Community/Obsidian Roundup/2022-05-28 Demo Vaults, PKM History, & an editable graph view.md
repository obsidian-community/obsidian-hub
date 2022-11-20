---
link: https://www.obsidianroundup.org/2022-05-28/
author: Eleanor Konik
published: 2022-05-28T12:30:00
publish: true
---

# 2022-05-28: Demo Vaults, PKM History, & an editable graph view
Archive everything you link to, check out a new tab-style interface, & join the discussion about using Obsidian for long term planning.

## In The Community

-   Here are [all fifteen sessions](https://www.linkingyourthinking.com/lytcon/nick-milo-keynote) from the Linking Your Thinking Conference. I was able to attend a few in addition to giving my own talk about migrating to a vault in safe mode (which was valuable for a number of reasons but yes, I'm back to using some plugins).
-   Nick's also hosting a live event this Sunday, May 29 at 9AM PDT (1600 UTC). It’ll include an overview of the upcoming LYT workshop and a Q&A.

## Obsidian Updates

-   [Insider v0.14.13](https://forum.obsidian.md/t/obsidian-release-v0-14-13-insider-build/37942) allows users to rename block IDs just like headers, has error messages that indicate the plugin’s name instead of showing `eval at anonymous`, and fixed note composer's merge functionality not updating links after merging (among other things).
-   [Insider v0.14.14](https://forum.obsidian.md/t/obsidian-release-v0-14-14-insider-build/38046) has daily notes with templates created as a single step instead of filling in an empty file, among other small fixes.
-   [Mobile Insider v1.2.2 (build 54)](https://discord.com/channels/686053708261228577/817515900349448202/978695830267633734) fixed the extra scrollbar on the toolbar on Android and the black bar at the bottom on iPad when using external keyboard.

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list._ For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new).

-   [Nuke Orphans](https://github.com/sandorex/nuke-orphans-plugin) by `@sandorex`  trashes orphaned files and attachments
-   [Upcoming](https://github.com/charliecm/obsidian-upcoming) by `@charliecm`  can open upcoming daily notes in their own panes.
-   [BBCode Convertor](https://github.com/salockhart/obsidian-bbcode) by `@salockhart`  can convert Markdown files to BBCode
-   [Folder Focus Mode](https://github.com/grochowski/obsidian-folder-focus-mode) by `@grochowski`  will focus file explorer on chosen folder and its files and subdirectories, while hiding all the other elements.
-   [Front Matter Title](https://github.com/Snezhig/obsidian-front-matter-title) by `@Snezhig` lets you define a title in frontmatter to be displayed as the filename
-   [Release Timeline](https://github.com/cakechaser/obsidian-release-timeline) by `@cakechaser`  renders based on notes metadata with a dataview-like syntax.

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [ExcaliBrain](https://github.com/zsviczian/excalibrain) by `@zsviczian`  is a clean, intuitive and editable graph view for Obsidian. I haven't messed with it much yet, but I'm considering using it to map out an anthology...
-   [File Hider](https://github.com/Oliver-Akins/file-hider) by `@Oliver-Akins`  allows hiding files and folders in the built-in file explorer.
-   [Trans Them](https://github.com/Quorafind/Obsidian-Trans-Them) by `@Quorafind`  is like note composer's "split file" functionality except for bullets lists instead of headings.
-   [Markbase for Obsidian](https://github.com/markbaseteam/obsidian-markbase) by `@markbaseteam`  is another Obsidian Publish alternative.
-   [Obsidian Selected Search Highlight](https://github.com/osadasami/obsidian-selected-search-highlight) by `@osadasami`  highlights the selected search result.
-   [Obsidian shared to Notion](https://github.com/EasyChris/obsidian-to-notion) by `@EasyChris`  will share obsidian files to Notion using the Notion API.
-   [Thumbnails](https://github.com/Meikul/obsidian-thumbnails) by `@Meikul`  lets users insert youtube thumbnails into notes.
-   [Note Content Pusher](https://github.com/lizard-heart/obsidian-note-content-pusher) by `@lizard-heart`  can automatically create notes with some specified content when you link to a note that doesn't yet exist.
-   [Zotero](https://github.com/MunGell/obsidian-zotero) by `@MunGell` allows users to search and insert links to Zotero items from Obsidian interface. Not to be confused with [Zotero Integration](https://github.com/mgmeyers/obsidian-zotero-integration) by `@mgmeyers` which used to be called "Zotero Desktop Connector" and can insert and import citations, bibliographies, notes, and PDF annotations from Zotero into Obsidian.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

-   The [extract url plugin](https://github.com/trashhalo/obsidian-extract-url) to now extract and converts to markdown every `[foo](https://bar.xyz)` it finds in the document. This is called "Archive" mode. Here's [a demo](https://www.youtube.com/watch?v=6W2Kul_uuPo).
-   [Obsidian List Modified](https://github.com/franciskafieh/obsidian-list-modified/releases/tag/1.2) now lets users exclude certain folders, which will not be added to daily notes when they are modified.
-   [Database Folder](https://github.com/RafaelGB/obsidian-db-folder/releases/tag/1.3.0) now allows every type of column to have its own configuration.
-   Obsidian Mkdocs Publisher is now [Obsidian GitHub Publisher](https://github.com/Mara-Li/obsidian-github-publisher) and works for sending to any repository based on a frontmatter key.
-   The [Map View plugin](https://github.com/esm7/obsidian-map-view) got a big update with new queries and search operators, view saving, easier navigation, real note previews on hover, and more.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   Here's a plugin for learning English that works like [LingQ](https://github.com/guopenghui/obsidian-language-learner).
-   [Snippetor 3.0](https://github.com/ebullient/obsidian-snippetor) is available via BRAT and allows users to set the font for checkboxes and task text.

## Feature Requests

-   [Iterating through the files in the file sidebar with the keyboard](https://forum.obsidian.md/t/iterate-through-files-in-the-file-sidebar-with-keyboard/629/43) would be nice.
-   There's been a lot of chatter about [bionic reading and whether it's legally and technically feasible to implement in various tools like Obsidian](https://www.reddit.com/r/ObsidianMD/comments/uv995v/bionic_reading_seems_great_but_patent_is_a_bummer/).

## Appearance

-   [WiseLight](https://github.com/learnerfvs/WiseLight) by `@learnerfvs`  is new.
-   Here's some neat code to turn [lists into pseudo callouts](https://discord.com/channels/686053708261228577/744933215063638183/978793024492560464) using the dynamic highlights plugin.
-   [Minimal 5.2.8](https://github.com/kepano/obsidian-minimal/releases/tag/5.2.8) added the Everforest color scheme and support for block widths in DataviewJS.
-   The [ITS-based Callouts Snippet](https://github.com/SlRvb/Obsidian--ITS-Theme/blob/main/Guide/Callouts.md) got updated with new callout types aside, column, and timeline.
-   Here's an in-leaf implementation of [a tab-style interface](https://gist.github.com/sailKiteV/e1124244161e2ab5ac3045562beee4ae) using nothing but CSS and callouts.

## Ancillary Code

-   If you've ever fallen afoul of the way that Logseq only recognizes `- bullets` but not `* bullets` when trying to use it and Obsidian on the same vault... here's [a regular expression](https://discord.com/channels/686053708261228577/700466324840775831/979512966435192832) for you to use with VS Code (via Discord).
-   Here's a [NCBI taxonomy script for the QuickAdd plugin](https://github.com/DLBPointon/QuickAdd-ncbi) that automatically generates taxonomy lists using a biology engineer.

## Guides

-   Here's [the hotkey list Obsidian inherits from the CodeMirror](https://codemirror.net/doc/manual.html#commands), which is Obsidian's text editor "under the hood."
-   Bryan Jenks put out a video about [how media extended is useful for taking notes on videos](https://www.bryanjenks.dev/blog/obsidian-media-extended-the-best-way-to-take-notes-on-videos-).

## Exemplars

-   The [Linking Your Thinking kit#6 is now available](https://www.linkingyourthinking.com/lyt-kit-6).
-   [Rainbell's example vault](https://www.reddit.com/r/ObsidianMD/comments/utwdgd/rainbell_example_vault_is_released_today/) is available and has been translated into English.
-   I did a big refactor of [my public vault](https://publish.obsidian.md/eleanorkonik/00+Meta/03+Guidance/Welcome) and pushed it live this week. Changes include an updated folder structure, a very quick and dirty guide on how to use Obsidian aimed at folks downloading my notes without any prior knowledge of Obsidian (i.e. most of the subscribers to [my fiction & history newsletter](https://newsletter.eleanorkonik.com/)), about 800 examples of claim statements and evidence, etc.
-   Here's [Paul Bauer's Obsidian notes](https://bauer.codes/notes/Obsidian), which are super useful especially for vimrc users but contain a wealth of information about programming & how Obsidian works.

## Meta

-   I wrote once about how [I don't particularly care for the "second brain" metaphor](https://www.obsidianroundup.org/ite-not-second-brain/) for Obsidian. Here's an interesting (brief) article article addressing how [Obsidian isn't a notetaking app](https://austingovella.medium.com/why-its-hard-to-get-started-obsidian-s-not-really-a-note-taking-app-75bafbebf6f3), it's an "integrated thinking environment" that doesn't push a particular method. Here's [@azzabazazz with an even better tagline](https://twitter.com/azzabazazz/status/1528894994781642754): "it's like being able to play your mind like a video game"
-   Here's a nice [comparison of Linking Your Thinking and zettelkasten methods](https://writing.bobdoto.computer/zettelkasten-linking-your-thinking-and-nick-milos-search-for-ground/) from Bob Doto.
-   This [5-part video series on the history of workflow](https://youtube.com/playlist?list=PLScTm9PMx5cjvm_OhWA9NRUMNI4o5iiJs) compares knowledge management stuff like BASB, LYT, & Obsidian to steelmaking & the Industrial Revolution.

## Discussions

-   Here's an useful discussion in Discord about  how different people [use obsidian to plan for long term projects or schedule events](https://discord.com/channels/686053708261228577/710585052769157141/977348234563436595).
-   Here's a sneak peek into the raw brain dump of an article I'm writing as my monthly "thank you" to financial supporters, about [my epiphany about why daily notes don't work well for me, and what I do instead](https://twitter.com/EleanorKonik/status/1529806813394239489); it's on Twitter, and the replies I got from folks were pretty thoughtful.

## Ancillary Tools

-   [Intrigue](https://github.com/shaunabanana/intrigue) is a nifty free and open source tool similar to apps like Gingkowriter or a mindmap, designed to help with taking notes on academic papers, books, or videos in a visual way. It seems worth checking out for academics in particular.

## Housekeeping

-   I'm going to be attending and helping out with the [8th Linking Your Thinking workshop](https://www.linkingyourthinking.com/#pricing). I'll be leading 4 sessions about synthesizing research & writing. I'm very excited to spend six weeks applying Nick's methodologies in doing intense knowledge work after my son starts full day daycare... and before I go back to work teaching.
-   I was hoping to avoid going back, but it turns out that there are some new tax rules about student loan forgiveness that would make it _unbelievably_ irresponsible of me to do anything other than work for a government or nonprofit as many months as possible between now and 2026; I'm not only going to have to put off pivoting to full time writing, I'm going to have to put off having my second kid. My newsletters will continue, but I'm going to have to close down my consulting work and probably punt a bit on some of the exciting extra projects I've been working on, i.e. reading and publishing books. Believe me I am bummed, but I hope to try again to switch careers after I take advantage of the public student loan forgiveness act... and vest my pension 👀
-   Ghost (my newsletter host) updated to 5.0 this week. I'm probably going to hold off updating until they make it to 5.1, but if you see anything weird this month please let me know.
-   Speaking of Ghost updates, we just hit 5,000 members even after list cleanup and removing inactive folks, which means another pricing increase for Ghost Pro. If you ever wondered why I ask for financial support to run this newsletter, go move [the slider on the Ghost Pro pricing page](https://ghost.org/pricing/) to "8,000" for the "Creator" tier and remember [what happened the last time I tried to self-host the newsletter to save money](https://www.obsidianroundup.org/billing-error-aka-the-saga-of-eleanors-corrupted-ghost-databases/).
-   In that vein, I'll be hosting another "5x8 Event" for financial supporters on June 9. Save the date, but next week I'll send out a formal invite and more information. Generally folks bring an article we liked enough to take notes on, and discuss it. It's an index card reference, but mostly refers to 5 people sharing their thing for 8 minutes each. The last one was really fun!

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-05-28%20Demo%20Vaults%2C%20PKM%20History%2C%20%26%20an%20editable%20graph%20view.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-05-28%20Demo%20Vaults%2C%20PKM%20History%2C%20%26%20an%20editable%20graph%20view.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
