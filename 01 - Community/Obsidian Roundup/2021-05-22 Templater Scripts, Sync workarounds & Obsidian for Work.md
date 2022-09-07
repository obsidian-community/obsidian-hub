---
link: https://www.obsidianroundup.org/2021-05-22/
author: Eleanor Konik
published: 2021-05-22
publish: true
---

# 2021-05-22: Templater Scripts, Sync workarounds & Obsidian for Work
Discussions about what motivates writing & how not to take notes. Showcases using Obsidian for CRM & technical jobs.

## In The Community

- There was a [lovely discussion](http://discordapp.com/channels/686053708261228577/744933215063638183/844726309410308177) prompted by `@AB1908` about what motivates people to write.
- The Leveraging Metadata and Bending Markdown talk has been cancelled, but we'll be hosting instead a Metadata Group Discussion on the same date and time (May 30th 8PM CET). Details [here](https://forum.obsidian.md/t/metadata-group-discussion-community-talk/)

## Obsidian Updates

## Plugin News

### New

- the [[metaedit|MetaEdit]] plugin by `@Chhrriissyy` allows users to easily update YAML properties and [[dataview|Dataview]] fields, mark a task as completed (from anywhere), and the file will be updated with the new count. It also auto updates properties in files linked to from Kanban boards on lane change. Requires manual install.
- [[obsidian-dictionary-plugin|Obsidian Dictionary]] requires manual install but creates a nifty "dictionary view" pane.
- [[supercharged-links-obsidian|Supercharged Links]] allows for some neat features for styling internal links. It also allows users to change any [[dataview|Dataview]] inline field or frontmatter by right clicking on an internal link.

### Updates

- The [[obsidian-excalidraw-plugin|Excalidraw]] [1.1.0](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases) by `@zsviczian` update discontinued code block embedding and implemented native `![[drawing.excalidraw]]` embedding. The MIGRATE command in the command palette should let you convert your old Excalidraw code blocks.
- The [[oz-image-plugin|Image in Editor Plugin]] plugin now displays Excalidraw drawings in markdown mode.
- [[media-extended|Media Extended]] [2.6.0](https://github.com/alx-plugins/media-extended/releases/tag/2.6.0) by `@AidenLx` has new features to get timestamp from player and open timestamp link on external video.
- [[buttons]] [0.4.7](https://discord.com/channels/686053708261228577/771575014382108672/845040678840827975) by `@shabegom` now has text buttons.
- [[obsidian-tracker|Tracker]] [v1.5](https://github.com/pyrochlore/obsidian-tracker) by `@pyrochlore` added two new search types. `searchType 'table'` lets you extract data from a table and then make a plot for it while `searchType 'dvField'` allows retrieving data in "[[dataview|Dataview]] plugin's inline field" format. `@bettyzhang` has an example [here](https://discord.com/channels/686053708261228577/771575014382108672/845223773178691594).
- [Pane Relief](https://github.com/pjeby/pane-relief#readme) by `@pjeby` now allows you to right-click on Obsidian's history arrows.

### Under The Radar

- [[obsidian-focus-mode|Focus Mode]] by `@ryanpcmcquen`

### Magic

- `@zsviczian` created a [workaround to Sync plugin settings with Obsidian Sync via Templater on GitHub](https://github.com/SilentVoid13/Templater/discussions/211). This should be helpful for iOS users. There are more details [here](https://discord.com/channels/686053708261228577/840286238928797736/843217947488157716).
- `@zsviczian` also shared how to [add syntax highlighting to templater scripts](http://discordapp.com/channels/686053708261228577/840286238928797736/843409737562325022).
- `@RoamHacker` put together [a Dataview script](https://gist.github.com/roamhacker/4e019abd25c58de57376add6e3aa4173) designed to give a more useful view of tasks by date, separated out by overdue, soon, due, and undated.
- `@Yas` created a [dataviewjs query](https://discord.com/channels/686053708261228577/771575014382108672/843841380773658664) to replicate the "on this day" timehop-style feature that some apps have.
- `@shabegom` created [a Templater script](https://discord.com/channels/686053708261228577/771575014382108672/844016103109165076) that prompts for a query and then shows notes and lines that include the query.
- `@Christian` shared a bunch of [Templater scripts](https://github.com/chhoumann/Templater_Templates), including a [[Readwise]] importer, and a [[quickadd]] that lets you append quick notes to a specified file.

### For Developers

- There was a really interesting [discussion about Promises and Javascript](http://discordapp.com/channels/686053708261228577/840286238928797736/844549148904128512) that could be really valuable for anyone interested in learning to create plugins for Obsidian who isn't already good at Javascript.

## Workflow Stuff

- There was a discussion about workarounds that might replicate the "reading ruler" effect that some people with learning disorders like dyslexia use to help with reading

## Feature Requests

- a writeup on "the absolute state of syncing things between devices as relevant for obsidian" would be valuable. If someone knowledgeable on the topic can put that together (even just a meta post linking to stuff like the git options / the summaries about why iOS is hinky, the issues with google drive etc) many people would be grateful (and I will add it to the big meta resources post on the roundup).
- The desire to see the results of [[dataview|Dataview]] queries (among other things) render in the graph was [discussed](https://discord.com/channels/686053708261228577/694233507500916796/843116572167372820).
- A couple of different people asked about a plugin to allow for the custom rearranging of notes and folders on the sidebar, which has come up a lot. After I [asked](https://discord.com/channels/686053708261228577/707816848615407697/844722593025490944) about how viable it would be to do that, `@danieltomasz` proposed [a solution that might be easier to implement](https://discord.com/channels/686053708261228577/707816848615407697/844858290536972289): creating a new navigation pane (a la the starred notes plugin) that is more flexible.

## Appearance

- This nifty css hack will make [the wordcount report screen flicker less](https://forum.obsidian.md/t/word-count-adds-distracting-motion-to-status-bar/18253).
- `SlRvb` has a version of "aside" CSS that leverages how `<i>, <s>,` & `<b>` allow for markdown code to work inside of them. The [theme repo for ITS](https://github.com/SlRvb/Obsidian--ITS-Theme) has a bunch of handy snippets.
- `@Mara` offered up [a snippet to hide files](http://discordapp.com/channels/686053708261228577/702656734631821413/844823253554036766) in the Obsidian explorer.
- `@yungbananapeel` figured out how to make [dataview tables look like gallery cards](https://discord.com/channels/686053708261228577/771575014382108672/844453734724796467).

## Knowledge Management

- `@itsTimConnors` put together a nice "getting started" [guide for knowledge management](https://itstimconnors.com/a-builders-guide-to-note-taking/) that also covers relationship management & recording information about entities like people and companies.
- This [reddit discussion](https://www.reddit.com/r/ObsidianMD/comments/ng9pqg/how_not_to_take_smart_notes/) started by `@joshduffney` had a really great discussion of "what not to do" when it comes to taking notes, and `@tyhe` added on with a bunch of background about Luhmann and the origins of the [[Zettelkasten]] method that I think were very informative.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- a list of [GUI programs](https://tesseract-ocr.github.io/tessdoc/User-Projects-%E2%80%93-3rdParty.html) that use [[Tesseract]], an open source OCR engine, to use a mobile device with a camera to translate images into text, via `@brimwats`
- `@argentum` had a really nice explanation of [[Vim]], for those who have always sort of wondered [what it is and why people like it](http://discordapp.com/channels/686053708261228577/722584061087842365/844522162862030859).

## Housekeeping

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-05-22%20Templater%20Scripts%2C%20Sync%20workarounds%20%26%20Obsidian%20for%20Work.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-05-22%20Templater%20Scripts%2C%20Sync%20workarounds%20%26%20Obsidian%20for%20Work.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
