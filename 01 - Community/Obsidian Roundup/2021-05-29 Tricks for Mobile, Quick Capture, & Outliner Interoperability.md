---
link: https://www.obsidianroundup.org/2021-05-29/
author: Eleanor Konik
published: 2021-05-29
publish: true
---

# 2021-05-29: Tricks for Mobile, Quick Capture, & Outliner Interoperability
Featuring more Zotero to Obsidian workflows (including mine!), a bunch of QoL improvements, & some neat tips & tricks for developers.

## In The Community

- `@nickmilo` hosted me for a chat about how I adapted Cat's amazing [workflow writeup](https://forum.obsidian.md/t/zotero-zotfile-mdnotes-obsidian-dataview-workflow/15536) and Argetina's comprehensive [Zotero tutorial](https://www.youtube.com/watch?v=9SzGxZbqyqc) to use [Zotero as a non-academic](https://www.youtube.com/watch?v=XbGJH08ZfCs).
- The [Metadata Group Discussion](https://forum.obsidian.md/t/metadata-group-discussion-community-talk/17070) will be moderated by `@Cat`. It is scheduled for [May 30th 20:00 CET](https://share.clickup.com/c/h/4gdf2-36/5b21a6f8588e5c6). [Submit discussion points or questions](https://forms.gle/W42Vjwdozde1YUeS8) by Friday.

## Obsidian Updates

[0.12.4](https://forum.obsidian.md/t/obsidian-release-v0-12-4-insider-build/18764) is now available to insiders. Featuring:

- Quick switcher now has an option to show links to files that haven’t been created yet.
- A new core plugin “Outgoing links” is now available, which is basically the opposite of the backlinks panel but works very similarly. [Example here](https://discord.com/channels/686053708261228577/744933215063638183/847660973745373275).
- Graph view’s right click menu now has an option to open the note in a new pane.
- Obsidian Sync’s status icon will now show red when not connected to the server.
- Status bar elements now have a css class of the plugin ID added to it, for example, plugin-word-count.

## Plugin News

### New

- The [[obsidian-collapse-all-plugin|Collapse All]] plugin for the file explorer is one of those nice little quality of life updates that can fly under the radar but really improve things.
- [[obsidian-dictionary-plugin|Obsidian Dictionary]] adds a View to the Sidebar in which you can search for Words in many different languages (including: English, German, Hindi, Spanish, French, & more) and now comes bundled with the "Synonym Popover Feature" from [[mgmeyers]].

### Updates

- [[supercharged-links-obsidian|Supercharged Links]] 0.2.4 lets you add a missing field by right-clicking the link. You can also show/hide the field options in the context menu, so that you can choose which plugin suits you for modifying fields. Example [here](https://discord.com/channels/@me/815308052323500033/845967637112291358). 2.5 lets you give your note a category to specify which [[dataview|Dataview]]/frontmatter field should appear in your note links' context menu. Demo [here](https://youtu.be/Av7DeYZILUk).
- It is now possible to hide note files automatically in [[alx-folder-note|AidenLx's Folder Note]].
- [[obsidian-excalidraw-plugin|Excalidraw]] [1.1.6](https://www.youtube.com/watch?v=FDsMH-aLw_I) adds functionality for links with the generated images.
- [[obsidian-kanban|Kanban]] [0.3.9](https://github.com/mgmeyers/obsidian-kanban/releases/tag/0.3.9) lets users search (demonstration [here](https://discord.com/channels/686053708261228577/707816848615407697/846082394033225759)). 0.3.10 and 0.3.11 were smaller fixes.
- [[metaedit]] [added toggle for UI elements](https://discord.com/channels/686053708261228577/771575014382108672/846094926987001896). You can now hide menu options, etc. There's also now an API with auto property handling.
- [[obsidian-outliner|Outliner]] an update to support line breaks.
- [[notetweet|NoteTweet🐦]] (which lets you tweet threads straight from Obsidian) now supports images.

### [[templater-obsidian|Templater]] [[🗂️ Templater templates|Scripts]]

- `@Murf` created a new [[templater-obsidian|Templater]] script that lets you [quick capture](https://github.com/SilentVoid13/Templater/discussions/231) — a modal popups up so you can input a new note (title and content) quickly, without having to change your workspace. Note: This was the thing that pushed me over the edge into downloading Templater, and it's amazing.
- `@Chhrriissyy` has an even more powerful version called [QuickAdd](https://github.com/chhoumann/Templater_Templates#quickadd-v2) that lets you quickly add new pages or content to your vault. It allows you to quickly add new pages from templates, as well as quick capture anything. You can customize practically everything about it. There's even custom templates, just for formatting titles and values. It even lets you put stuff below a particular heading in your daily note.
- `@death_au` uses this [Templater script](https://discord.com/channels/686053708261228577/840286238928797736/846205611167580207) to have a line in their daily note template to create a different day planner schedule depending on the day of the week.
- This [[templater-obsidian|Templater]] script lets from `@Murf` lets you open a `[[Link]]` under your cursor in Search pane with regex to show its Backlinks. Here's the [Github Discussion](https://github.com/SilentVoid13/Templater/discussions/245)
- `@Bejasc` put together a [Templater Script](https://discord.com/channels/686053708261228577/707816848615407697/847452061003284490) that lets you highlight text, run the template, and then choose an admonition type and give it a title. It makes it easier to use some of the less-common admonition tags without having to look them up, and I hope this functionality gets added into the admonition plugin soon!

### Under The Radar

- Obsidian-flowcharts supports [linking to subgraphs](http://discordapp.com/channels/686053708261228577/709580487550828614/843821744623058985) in Mermaid.
- [Obsidian Sortable](https://github.com/alexandru-dinu/obsidian-sortable) allows users to make tables (including those created by [[dataview|Dataview]]) sortable with clickable arrows, like on Wikipedia.
- [Obsidian Tasks] is getting a lot of love.
- The [markdown formatting assistant plugin](https://github.com/Reocin/obsidian-markdown-formatting-assistant-plugin) has some latex helpers, and I want to share it again because there have been a couple of discussions lately about taking math notes in Obsidian.

### For Developers

- `@liam` shared that you can set the [app badge count with javascript](https://discord.com/channels/@me/815308052323500033/846132119280549930), which might be useful for task management plugin devs (but if you choose to go this route, be sure to make it an optional setting!).
- `@shabegom` put together a helpful writeup on [how to write templater scripts with plain javascript](https://publish.obsidian.md/shabegom/Publish/How+To+Use+Templater++JS+Scripts), which is advised where possible since it's much cleaner to read.
- `@pjeby` released [Hot Reload 0.1.8](https://github.com/pjeby/hot-reload) to support symlinked plugins on Windows and OS X.
- Reminder: if you want to track usage statistics or something for a plugin, it should be _off by default,_ have a toggle in the settings panel, and explicitly explain what the purpose of the trackers are.

## Workflow Stuff

- Francisco Bricio's [presentation](https://www.youtube.com/watch?v=Ehw3hUZNF1M), hosted by `@nickmilo` of Linking Your Thinking, got resurfaced this week as being particularly useful for entrepreneurs.
- This [Discord](https://discord.com/channels/686053708261228577/840286238928797736/845277734477627412) example of how to assign multiple values to a piece of inline metadata (which can be used by [[dataview|Dataview]] and [Obsidian Tracker](https://github.com/pyrochlore/obsidian-tracker)) was really helpful.
- Relatedly, here is a [video demonstrating how to create a graph from table data interacively](https://www.youtube.com/watch?v=EVgz7UV6fbU) using Tracker v1.5
- Logseq and Obsidian can work together. `@shuyunzhang99` put together a [demonstration](https://www.youtube.com/watch?v=W4Art2DI9SA) of their interoperability on the same .md file.
- When looking at the backlinks/outlinks panel, you can open a note in a new pane using middle click from the scroll wheel.
- `@foreveryone` put together this handy [pro-con chart](https://discord.com/channels/686053708261228577/805952223124520961/845073044573782026) to help decide whether to split vaults, particularly for creative vs. knowledge vaults.
- This [iframe trick](https://discord.com/channels/686053708261228577/805952223124520961/809484088540266528) via `SlRvb` got resurfaced: it lets you use a dropbox link to embed a generated fantasy map into your vault, which is super useful for worldbuilders.
- `@StPag` added some admonition bits on top of the Zotero-Zotfile-MdNotes workflow and assigned a colour to highlight keywords and used some regex to build an index of the topics covered. There are [details on the forum](https://forum.obsidian.md/t/zotero-zotfile-mdnotes-obsidian-dataview-workflow/15536/29?u=eleanorkonik) but the actual [hacky rscript code is in the discord](https://discord.com/channels/686053708261228577/722584061087842365/847573039411757067).

### Mobile

- You can use a [shortcut to get .css snippets](https://forum.obsidian.md/t/ios-shortcuts-share-your-ideas/15149/33) into your mobile vault if you're using iOS with Obsidian Sync. Toolbox Pro required.
- For Android users, you can use [Markor](https://play.google.com/store/apps/details?id=net.gsantner.markor&hl=en_US&gl=US)'s quick note widget to let you take notes directly into your inbox folder in your Obsidian vault; the two programs synergize well. (thanks, `@brimwats` for the tip).

## Feature Requests

- Getting the [ability to create Filelinks/Tags for the Graph inside Codeblocks](https://forum.obsidian.md/t/ability-to-create-filelinks-tags-for-the-graph-inside-codeblocks/17419) was discussed in the Discord again, since it's a big limitation on the admonition plugin in particular. I proposed an [Optional Alternate Syntax for Codeblock Plugins](https://forum.obsidian.md/t/alternate-syntax-for-codeblock-plugins/18905) — please chime in with your preferences if this is something that matters to you.
- The request for [file explorer customer sort](https://forum.obsidian.md/t/file-explorer-custom-sort/1602/69) got resurfaced.
- A couple of people have lamented the lack of ocr allowing for the [searching of text in images](https://forum.obsidian.md/t/ocr-images-screenshots-to-make-them-searchable/6854).

## Appearance

- If you don't like the way that Obsidian's default font uses ligatures, you can [disable them with CSS](https://stackoverflow.com/a/39504776).
- This [css](https://discord.com/channels/686053708261228577/702656734631821413/842390693312725052) from `@SlRvb` lets you format inline keys with a `dv` cssclass.
- This [css](https://discord.com/channels/@me/815308052323500033/846089220430102628) from `@foreveryone` will let you hide a particular folder, i.e. your Attachments folder, from the file navigator.
- This [css](https://discord.com/channels/@me/815308052323500033/846752506054443069) (also from `@foreveryone`) will let you rotate an image, which can be really handy if you're on mobile and your phone takes stupid pictures.
- `@Chetachi` released the [Yin and Yang](https://github.com/chetachiezikeuzor/Yin-and-Yang-Theme/) theme.

## Knowledge Management

- `@Artefice` shared some [really nice advice about](https://discord.com/channels/686053708261228577/709712341066842113/847237568458522656) how to use Obsidian and personal knowledge management principles that are poplar in the community as a student.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- `@MrChad` [recommended](https://discord.com/channels/686053708261228577/710585052769157141/845503538490507334) [Refind](https://refind.com/EleanorKonik?invite=209801a8ad) as a read-later/bookmarking/link-curation app. It's got a browser add on that you can click on any article and save for later - and categorize if you want to. It reminds me of [Mix.com](https://mix.com/ekonik) except it seems to try to curate a more strict "top five" daily reading list with deep dives on different subjects.
- `@nvanderhoeven` [shared](https://nicolevanderhoeven.com/blog/20210302-presentation-slides-as-code/) how they use Obsidian + [[revealjs]] + [[Hugo]] + [[GitHub Pages]] to create presentations and publish them online.

## Housekeeping

- I updated the [Resources: For Beginners](https://obsidianroundup.org/resources/#for-beginners) to include a couple of new beginner videos.
- I updated the [Task Management Plugins](https://obsidianroundup.org/plugins/#task-management) list to include [[obsidian-kanban|Kanban]].

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-05-29%20Tricks%20for%20Mobile%2C%20Quick%20Capture%2C%20%26%20Outliner%20Interoperability.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-05-29%20Tricks%20for%20Mobile%2C%20Quick%20Capture%2C%20%26%20Outliner%20Interoperability.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
