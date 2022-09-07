---
link: https://www.obsidianroundup.org/2021-06-12/
author: Eleanor Konik
published: 2021-06-12
publish: true
---

# 2021-06-12: Folder Indexer, Smarter Typography, & OCR
Featuring a bunch of new plugin features, including iCal imports, adjacency matrix, better file trees, new file placement, & oath handshakes for mobile Dropbox backups.

## In The Community

- The Knowledge Organization in Obsidian community talk by `@brimwats` is live on [Youtube](https://www.youtube.com/watch?v=jMJbVUUi34I). It offers a history of library organization, a detour into cataloging vs classification, and the lowdown on foldering/tags in PKMs. This [discord post](https://discord.com/channels/686053708261228577/694233507500916796/852555393741750272) contains links to unfilmed discussion points about geographical terms and classification systems, niche vocabularies, and "semantic obsidian."
- `@SkepticMystic` will be giving the [Using Pandoc to write PDFs, Word documents, and slideshows in Markdown](https://forum.obsidian.md/t/using-pandoc-to-keep-your-workflow-inside-obsidian-community-talk-by-skepticmystic/) talk this [Sunday at 18:00 (CET)](https://share.clickup.com/c/h/4gdf2-36/5b21a6f8588e5c6).
- `@Payload` had an excellent explanation of [what plugins are, some examples, and how they work](https://discord.com/channels/686053708261228577/707816848615407697/851695771178762240) that I recommend for anyone who finds them confusing.
- I feel a little weird including this, but it made it to the starboard and I posted it directly by request of multiple community members, so here's a condensed paper I wrote for my master's course about best practices in [teaching critical thinking skills](https://eleanorkonik.com/difficulties-teaching-critical-thinking/). There's probably a fair amount of applicability for _learning_ critical thinking skills, which help a lot with figuring out best practices for personal knowledge management and metacognition and life in general.

## Obsidian Updates

[Public v0.12.4](https://forum.obsidian.md/t/obsidian-release-v0-12-4/18764)

- Quick switcher now has an option to show links to files that aren't created yet.
- New core plugin "Outgoing links" which can be enabled through the settings page, which shows a list of destinations your note links to and gives a list of unlinked mentions from the current note that can be linked.

[Insider 0.12.5](https://forum.obsidian.md/t/obsidian-release-v0-12-5-insider-build/19374)

- The template core plugin now has commands to insert the current time or the current date.
- There’s now a new dedicated command to focus on the editor.
- Pasting images copied from Chrome’s “Copy image” menu action will now properly import the image to the vault, instead of creating a link to the image’s original URL.
- Fixed some [[Mermaid]] diagrams not rendering properly (journey missing text, gantt unreadable active task, class diagrams have very faint text).
- There is now a function available for converting HTML to Markdown called htmlToMarkdown, which is using a pre-configured Turndown Service.

## Plugin News

### New

- the [[zoottelkeeper-obsidian-plugin|Zoottelkeeper Plugin]] is an automated folder-level index file generator and maintainer that let me delete a bunch of tags and I'm really thrilled about it.
- [[obsidian-smart-typography|Obsidian Smart Typography]] automatically converts straight quotes to smart quotes. It also has support for em dashes, and ellipsis, and I'm really grateful for its existence. [[mgmeyers]] wants to expand support to other languages, so if there's something you'd like added, file an issue on the github repo.
- [[obsidian-advanced-new-file|Advanced new file]] lets you assign folder for a new file when you trigger the hotkey.
- The [Obisidan OCR plugin](https://github.com/schlundd/obsidian-ocr-plugin) extracts the text of image attachments.
- The [Obsidian iCal plugin](https://github.com/mdelobelle/obsidian-ical/tree/master) (Mac only) includes the events of your Calendar at the end of your daily notes with templating capabilities.
- the [[adjacency-matrix-maker|Adjacency Matrix Maker]] [0.4.0](https://github.com/SkepticMystic/adjacency-matrix-maker/releases/tag/0.4.0) by `@SkepticMystic` (of "helps people with [[dataview|Dataview]]" fame) is a nifty alternative to the graph view.
- [[obsidian-text-format|Text Format]] will "clean up" formatting, getting rid of excessive spaces and newlines if you, for example, paste in text from a pdf.
- [[obsidian-grandfather|Grandfather]] puts the time (and date if you want) in the status bar, which might be useful for people who like to work in fullscreen mode.
- The [[file-tree-alternative|File Tree Alternative Plugin]] plugin creates a file explorer similar to Evernote where folders and files are in separate leafs. I think [this feature request](https://forum.obsidian.md/t/split-view-of-the-file-pane/19555) gives a pretty useful overview of why someone might want this.
- The [Bible Reference Plugin](https://forum.obsidian.md/t/new-plugin-bible-reference-plugin-alpha/19532) will let you "fetch" a particular passage of the Bible from the [ESV.org](https://www.esv.org/).

### Updates

- [[obsidian-dropbox-backups|Aut-O-Backups]] [0.12.4](https://github.com/ryanpcmcquen/obsidian-dropbox-backups) supports mobile. Developers looking for an example of oath browser handshakes might want to give it a look, as well.
- The [[obsidian-collapse-all-plugin|Collapse All]] (folders) plugin how has functionality for expanding all folders.
- v1.5.0 of the [[obsidian-spaced-repetition|Spaced Repetition]] allows for nested decks, better load balancing, and some other QoL improvements.
- [[obsidian-kanban|Kanban]] [v0.5.6](https://github.com/mgmeyers/obsidian-kanban/discussions/177)'s metadata fields now support rendering markdown.

### Under The Radar

- the [[obsidian-argdown-plugin|Argdown]] plugin can be useful for [taking notes on things that require a train of thought](https://forum.obsidian.md/t/taking-notes-on-information-that-requires-a-chain-of-thought/19531).

## Workflow Stuff

- A [tip](http://discordapp.com/channels/686053708261228577/707816848615407697/852793134479835146) via `@Payload` is that the order of plugins being loaded decides the order of content that they populate in the status bar (if they are loaded first, they would be on the left of the status bar). You can change this ordering in .obsidian/config. Look for enabledPlugins, the array contains all your enabled plugins, in the order at which they are loaded. Change the order to one that you like.
- There was an interesting discussion on the forum about [how to build a recipe database using Obsidian](https://forum.obsidian.md/t/help-howto-build-recipe-database-in-obsidian-complex/19548/4).
- There was a discussion on Reddit about how [university teachers](https://www.reddit.com/r/ObsidianMD/comments/nx9ayz/any_teachers_out_there_using_obsidian/) use Obsidian to manage their notes and lecture plans.

## Appearance

- This [CSS code](http://discordapp.com/channels/686053708261228577/702656734631821413/850509685110210580) will let you style specific headings (e.g. `## Reading Log` but not `## Tasking`)
- This [CSS code](http://discordapp.com/channels/686053708261228577/702656734631821413/851588418487975966) will visually shorten url links so they take up less space in the editor.
- This [CSS code](https://forum.obsidian.md/t/soft-wrap-file-name-in-sidebar/2369) will cause sidebar titles to wrap.
- `@SlRvb` [figured out](https://discord.com/channels/686053708261228577/771575014382108672/850791937371537458) how to put svg icons into css for use with folders.
- `@Payload` shared a really beautiful bit of [code](https://discord.com/channels/686053708261228577/702656734631821413/851474397238788146) that adds a visual background of stars and nebulae to an Obsidian instance.
- `@Chetachi` shared a tutorial for [multicolored highlights](https://www.reddit.com/r/ObsidianMD/comments/nu0olr/multicolored_highlighting_in_obsidian/) in Obsidian.

## Knowledge Management

- This [discussion about source v. literature v. permanent v. atomic v. evergreen notes](https://forum.zettelkasten.de/discussion/1582/what-are-source-notes-literature-notes-permanent-notes-atomic-and-evergreen-notes) over at the zettlekasten.de is a useful summary of some of the common "vocabulary terms" that crop up in the Obsidian community.
- There was a related [discord discussion](https://discord.com/channels/686053708261228577/710585052769157141/852673138843189258) about different notetaking methodologies with a focus on multifacted systems and the value of the oft-maligned "bookkeeping" systems.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- [ShareX](https://getsharex.com/)is a popular gif creating & sharing tool. [Loom](https://www.loom.com/) is popular for sharing screen captures with voiceover.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-06-12%20Folder%20Indexer%2C%20Smarter%20Typography%2C%20%26%20OCR.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-06-12%20Folder%20Indexer%2C%20Smarter%20Typography%2C%20%26%20OCR.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
