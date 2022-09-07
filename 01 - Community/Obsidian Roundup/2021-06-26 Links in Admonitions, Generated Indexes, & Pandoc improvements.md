---
link: https://www.obsidianroundup.org/2021-06-26/
author: Eleanor Konik
published: 2021-06-26
publish: true
---

# 2021-06-26: Links in Admonitions, Generated Indexes, & Pandoc improvements
There's some new note refactoring options. We also discussed various methods for sharing notes, some nifty & best practices for YAML.

## Obsidian Updates

- [Obsidian Release v0.12.6 (Insider build)](https://forum.obsidian.md/t/obsidian-release-v0-12-6-insider-build/19914) added the new [Note Composer](https://help.obsidian.md/Plugins/Note+composer) core plugin.
- [Obsidian Release v0.12.7 (Insider build)](https://forum.obsidian.md/t/obsidian-release-v0-12-7-insider-build/20004) was mostly focused on bugfixes and Sync; third party sync tools should have a harder time corrupting the sync database now.

## Plugin News

### New

- [[file-explorer-note-count|File Explorer Note Count]] lets you see how many files you have in a folder without having to hover.
- You can now get a [[obsidian-statusbar-pomo|pomodoro timer in your status bar]].
- the [[breadcrumbs|Breadcrumbs]] plugin allows you to assign parent, child, and sibling links to other notes using YAML and then get a visual navigation sidebar thing.
- There’s a new [[tq-obsidian|task management]] plugin. Each task is represented as a Markdown note with a single task line and some metadata in the frontmatter.

### Updates

- The new updates to [[obsidian-admonition|Admonition]] allow for non-codeblock admonitions so that links can work! This is _incredible_. Here’s an [example](https://www.loom.com/share/730f77bbeeef453f94f22576df7178f4).
- [[table-extended|Table Extended]] also moved away from codeblocks in order to better support backlinks and forward links.
- [[note-refactor-obsidian|Note Refactor]] [1.7.0](https://github.com/lynchjames/note-refactor-obsidian/releases/tag/1.7.0) is now available. It supports `[markdown](links)` and adds a new command for extracting selections.
- [[obsidian-tracker|Tracker]] [1.7.0](https://github.com/pyrochlore/obsidian-tracker) adds a new output type 'month', rendering a month view for a given dataset, as in [this example](https://discord.com/channels/686053708261228577/855181471643861002/856529983031607316).
- [[quickadd|QuickAdd]] [0.2.2](https://github.com/chhoumann/quickadd) has a bunch of behind the scenes improvements, and updated documentation. 0.2.12 adds an example for fetching tasks from Todoist into your vault, in a format that the Tasks plugin will collect. A lot happened here this week. If you like [[templater-obsidian|Templater]], you will probably also like QuickAdd. For example, this incredible [QuickAdd script](https://discord.com/channels/686053708261228577/840286238928797736/855883637367242752) `Christian` put together lets you split _named_ (instead of just numbered) headings off into atomic notes in a particular folder, embedding the section in the new note instead of moving the text out of the literature note. This solves a bunch of the problems outlined in the discussion of my [increasingly atomic folders] workflow writeup about why I do it “my way” instead of using the “proper” atomic note method. Now you can have the best of both worlds!
- [[obsidian-tasks-plugin|Obsidian Tasks]] [1.1.2](https://github.com/obsidian-tasks-group/obsidian-tasks/releases/tag/1.1.2) had some bugfixes and a documentation update. It should be easier to use now.
- v0.1.0 of the [[obsidian-languagetool-plugin|LanguageTool plugin]] has been released. It adds automatic checking, a new suggestions popup, and a handy status bar menu.
- [[obsidian-smart-typography|Smart Typography]] [1.0.3](https://github.com/mgmeyers/obsidian-smart-typography/releases/tag/1.0.3) adds better dash rules so that YAML and arrows don’t get screwed up anymore.

### Under the Radar

- [[mrj-text-expand|Text expand]] can generate indexes across notes if you specify a `\folder, #tag or [[Link]]` to generate an output of links that are readable by obsidian.

### For Developers

- When putting together [[quickadd]], `@Christian` figured out how to enable the Obsidian autocomplete for page names in the modal window. Check out the repo (or ping him, he’s very nice) if this would be useful for something you’re working on.
- There is now a `editor-menu` event on Workspace, which can be used to add more options to the context menu inside the editor.

## Workflow Stuff

- `@tallguyjenks` shared [best some practices for YAML](http://discordapp.com/channels/686053708261228577/694233507500916796/856218976946618399)
- `@cotemaxime` shared that you can type `app.garbleText()` into the console to blur text before sharing a screenshot.
- Another neat [template for Zotero](http://discordapp.com/channels/686053708261228577/710585052769157141/856977587976011787) was shared. This time with buttons!
- `@thecookiemomma` shared [a plugin list](http://discordapp.com/channels/686053708261228577/694233507500916796/858023992743821373) they think would be useful for writers.
- `@death_au` shared a tip: Playing videos in Obsidian supports Picture-in-Picture!
- `@Patrick` shared a [showcase video](https://youtu.be/vfGDnIa34ag) showing how he uses Obsidian for creating tabletop adventures.
- Federico at the AppStories podcast [shared](https://appstories.net/episodes/228/) his research and note-taking setup.

## Appearance

- This [css snippet](https://forum.obsidian.md/t/css-snippet-for-multiple-blockquote-styles-with-syntax-formatting/19839/8) lets you have multiple blockquote styles depending on what you tag the quote.
- This small css snippet allows for information to be [displayed in multiple columns](http://discordapp.com/channels/686053708261228577/707816848615407697/856860634884341830) without the interactivity of kanban, if you prefer to avoid plugins but are fine with custom css.
- `@gammons` created a [base16 theme](https://github.com/gammons/base16-obsidian) that enables basically 131 new "themes" for Obsidian.
- This css snippet will let you [hide certain folders](https://discord.com/channels/686053708261228577/694233507500916796/845664939292229642), i.e. attachments.
- This css trick is useful for when you’re trying to set rules for [printing a note to pdf](https://discord.com/channels/686053708261228577/722584061087842365/855105812463616040).

## Knowledge Management

- There was a [discussion](http://discordapp.com/channels/686053708261228577/722584061087842365/857982337814888508) about what good habits, methods, etc exist for learning, processing, and applying information. A really nice list came from the discussion; I recommend checking it out.
- There was a discussion about [how to take notes as a high school student](http://discordapp.com/channels/686053708261228577/694233507500916796/855792400278224907).
- We discussed [how Twitter threads are similar to zettelkasten card series](http://discordapp.com/channels/686053708261228577/710585052769157141/857716879393423371) and how to adapt that to Obsidian.
- There was a [discussion about how to combine different pkm/life-os systems](https://discord.com/channels/686053708261228577/710585052769157141/856366772130807829).
- There was an insightful discussion over on reddit about [zettelkasten vs evergreen systems](https://www.reddit.com/r/ObsidianMD/comments/o589cd/is_it_me_or_is_the_zettelkasten_being/).
- `@sivwuk` shared a [showcase video](https://www.youtube.com/watch?v=_81oIoHMQrQ) showing how they use Obsidian to study.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- I put together a bit of a stream-of-consciousness review / list of recommended guides for [setting up Ghost](https://eleanorkonik.com/ghost-my-experiences-running-a-self-hosted-newsletter/). It’s what I use to run this Roundup. A couple of people asked how I liked it because they were thinking about maybe checking it out, so I thought I’d share.
- This [guide for using Dropbox with Obsidian](https://theproductiveengineer.net/ultimate-guide-to-using-dropbox-for-obsidian-notes/) was shared. It seems very comprehensive.
- [Rentry](https://rentry.org/) is a minimalistic tool that is basically “pastebin for markdown” if you want to just share an Obsidian note with someone really quick without losing the formatting.
- [Nebo](https://www.nebo.app/features/) is a paid app for handwriting on tablets, apparently the OCR is really good and it can handle mixing handwriting and typed statements within a single document. A bunch of people really like it.
- `@hstagner` shared a [Twitter thread](https://twitter.com/hstagner/status/1408388869549137921?s=21) discussing the differences between a [[Digital garden|digital garden]] and a blog. It’s another nudge for me personally; I’ve been considering opening up my notes as a [[Digital garden|digital garden]] to supplement my blog in a way similar to what’s described in the thread.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-06-26%20Links%20in%20Admonitions%2C%20Generated%20Indexes%2C%20%26%20Pandoc%20improvements.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-06-26%20Links%20in%20Admonitions%2C%20Generated%20Indexes%2C%20%26%20Pandoc%20improvements.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
