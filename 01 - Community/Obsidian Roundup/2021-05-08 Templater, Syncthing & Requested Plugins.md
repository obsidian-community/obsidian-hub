---
link: https://www.obsidianroundup.org/2021-05-08/
author: Eleanor Konik
published: 2021-05-08
publish: true
---

# 2021-05-08: Templater, Syncthing & Requested Plugins
Featuring the Excalidraw, Templater, Kindle, Dataview, Kanban, Tasks, Buttons, Leaflet & Comments plugins. Also tips for mobile, feature requests, & more!

## In The Community

- Federico Viticci (of [MacStories](https://www.macstories.net/) fame) discussed Obsidian (and some in-development plugins) at the [Connected podcast](https://www.airr.io/episode/60932a83ac7f415c5126b648).
- Theoretical physicist Francisco Bricio spoke about [how to manage projects, tasks, people, and yourself using Obsidian](https://www.youtube.com/watch?v=Ehw3hUZNF1M) with `@nickmilo` over at [[Linking Your Thinking]].
- This teacher reflects on how [using Obsidian in the classroom to create a class vault](https://www.youtube.com/watch?v=TgG14DkxoOg) went.

### [[Obsidian Community Talks|Community Talks]]

- The Zotero 101 community talk is available on YouTube. Here's [Part 1: Basics](https://www.youtube.com/watch?v=9SzGxZbqyqc) & [Part 2: Plugins](https://www.youtube.com/watch?v=LaEt9cqkj3I).
- The [CSS 101 intro and Q&A talk](https://forum.obsidian.md/t/css-101-community-talk-by-lithou/) by `@Lithou` scheduled for today at 4pm Eastern Time.
- `@TallGuyJenks` is doing the [Metadata talk](https://forum.obsidian.md/t/leveraging-metadata-and-bending-markdown-community-talk-by-tallguyjenks/) on May 30th 11:00 GMT-7.

## Obsidian Releases

- [Obsidian Release v0.12.2 (Insider build)](https://forum.obsidian.md/t/obsidian-release-v0-12-2-insider-build/17602) will let people pin commands at the top of the command palette, and mobile developers have some nifty functions for allowing things to be added to the editor toolbar. [[Obsidian Sync]] improvements also shipped out.

## Plugin News

### New

- `@iller` made a plugin for [[obsidian-react-components|making components with reactjs inside Obsidian]].
- For folks looking for a pomodoro timer, there's a [[obsidian-stopwatch-plugin|Stopwatch Plugin]] in the works.

### Updates

- [Excalidraw 1.0.8](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.0.8) now features [[templater-obsidian|Templater]] support, along with some quality of life improvements centered around saving.
- The [[obsidian-kindle-plugin|Obsidian Kindle plugin]] handles myclippings.txt now. It also has support for `{{date}}`
- [[dataview|Dataview]] has a [new API for javascript](https://blacksmithgu.github.io/obsidian-dataview/docs/api/intro) and [fancy new documentation](https://blacksmithgu.github.io/obsidian-dataview/). [[SkepticMystic]] [shared](http://discordapp.com/channels/686053708261228577/709712341066842113/840185601150943273) a dataview**js** codeblock that will return a single-level list of all tags in your vault, without duplicates.
- [[obsidian-kanban|Kanban]] [0.2.0](https://github.com/mgmeyers/obsidian-kanban/discussions/56) has been released with basic date support.
- [[templater-obsidian|Templater]] [ v1.6.0](https://silentvoid13.github.io/Templater/docs/) includes dynamic templates triggered in preview mode with `<%+`, user scripts, support for js files from a folder inside your vault and more.
- There was an update for [[obsidian-tasks-plugin|Obsidian Tasks]] that has some fancypants editing ability. It's not available in the community plugins list and requires Obsidian 0.12 to work, but it's a nifty new task management plugin that got [a lot of love on Reddit](https://www.reddit.com/r/ObsidianMD/comments/n32k6v/obsidian_tasks_is_now_at_version_070_with_a_new/).

### Under The Radar

- This [discussion](https://www.reddit.com/r/ObsidianMD/comments/n6p1zy/adding_file_extensions/) covers some different ways to interact with non-markdown files in Obsidian.
- The [[obsidian-leaflet-plugin|Obsidian Leaflet]] plugin [lets you have maps with markers/pins in your vault](https://forum.obsidian.md/t/new-plugin-obsidian-leaflet-interactive-maps-in-notes/14752). This is handy for lots of people, but particularly authors. Here's [an example of why](http://discordapp.com/channels/686053708261228577/744933215063638183/839224109450657874) via [[SlRvb]]. Apparently you can also use [[obsidian-spaced-repetition|Spaced Repetition]] with Leaflet plugin to make [image occlusion review](http://discordapp.com/channels/686053708261228577/694233507500916796/838073296057794591) (via `@boninall`)
- The [[obsidian-comments|obsidian comments]] plugin, which lets you annotate your notes, got re-surfaced.

### For Developers

- via [[liamcain]]: if you are gating UI or interface behavior, use `isMobile/isDesktop` but if you are checking for the availability of node.js libs or desktop-only features, use `isMobileApp/isDesktopApp`.

## Workflows

- This [github repository](https://github.com/masonlr/obsidian-starter-templates) contains a bunch of [[🗂️ Templates|starter templates]] for different use-cases (for example tracking tools, researching, etc).

### Tutorials

- `@Murf` created a [demo video](https://github.com/SilentVoid13/Templater/discussions/187) for "how to set up your first [[templater-obsidian|Templater]] script." They also put together a nifty [roundup of resources](https://discord.com/channels/686053708261228577/694233507500916796/838859649192296509) centered around how Obsidian block references differ from those in other tools.
- `@shabegom` had a helpful [summary](https://discord.com/channels/686053708261228577/707816848615407697/839853909103345735) of how the readwise community plugin works.

### Academic

- There was a nice [discussion on reddit](https://www.reddit.com/r/ObsidianMD/comments/n5hg2v/obsidian_for_academic_work_and_sundry_other/) about "getting started" with Obsidian as an Academic.
- There was a really nice discussion about what different people's [literature notes look like](http://discordapp.com/channels/686053708261228577/722584061087842365/839302335078727710).

### Mobile

- There was a discussion in the `#mobile` channel about Syncthing maybe being viable syncing between iOS, android, PC and Mac (and Linux). If you have any knowledge about this, please put together a guide and let us know about it. [Möbius Sync](https://www.mobiussync.com/faq/) seems to be a way to get [[Syncthing]] on iOS.
- A nifty trick for keeping desktop and mobile setups differently is going into `the settings > about > override config folder` section and changing which folder mobile (or desktop) uses to store its settings.

## Feature Requests

- `@dcoales` [asked](http://discordapp.com/channels/686053708261228577/707816848615407697/840195539617316866) about the viability of a plugin for spacially-organized notes on a "canvas."
- There's been some discussion about a proper [genealogy plugin](https://discord.com/channels/686053708261228577/744933215063638183/838859972094853160) for better management of family trees. [[Mermaid]] can't quite handle them correctly, but for story vaults and ancestry research, it would be super handy.
- The ability to [save node positions in graph view](https://forum.obsidian.md/t/save-node-positions-in-graph-view-edit-and-preview-toggle/1423) got discussed again.
- `@omarkhafagy` requested [better plugin management](https://forum.obsidian.md/t/better-plugin-management-with-folders-and-links/17568) with the ability to group plugins into folders.
- There was a request for the ability to ["pin" the header of a document](https://forum.obsidian.md/t/keep-title-visible-when-scrolling-down-note/17508), which might be particularly useful for people who use the sliding panes plugin.

## CSS Stuff

- `@nickmilo` pushed an update to the [[Cybertron]] theme
- A YouTube tutorial about [how to create a custom theme with snippets](https://www.youtube.com/watch?v=lyaEnxgow4E) by `@Reggie` got resurfaced.
- There was a snippet shared for [styling dates & completed cards](http://discordapp.com/channels/686053708261228577/702656734631821413/840059525298126868) for the kanban plugin.
- `@foreveryone` shared [a handy trick](http://discordapp.com/channels/686053708261228577/694233507500916796/839563732262453338) with styling `<i>` that allows for the [creation of columns](http://discordapp.com/channels/686053708261228577/805952223124520961/839696324365385750).
- There was a discussion of [how to highlight sections of text without having to rely on spans](https://www.reddit.com/r/ObsidianMD/comments/n3nkld/highlighting_sections_of_text_without_having_to/?utm_medium=android_app&utm_source=share) over at Reddit, with a couple of different possible solutions if that's something you're interested in.
- Here's a [snippet](https://forum.obsidian.md/t/arithmetic-gradient-heading-h1-h6/17551) that will let your headings automatically have a gradient based on a particular color, via `@Connor96`.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- [Espanso](https://espanso.org/) is a popular text replacement tool that lets you get create templates that will autocomplete text, for example turning `::now` into a timestamp, or `----` into `—` or whatnot. It even also allows for a system-wide autocorrect, which is nice since Obsidian doesn't really have that feature. Here's a handy [list of resources](http://discordapp.com/channels/686053708261228577/694233507500916796/839559608862507019).
- [Screenotate](https://screenotate.com/) is apparently an easy way to grab text from a screenshot (via `@smithtjosh`)
- `@tallguyjenks` did a review of [GingkoApp](https://youtu.be/dxCJHHWyNzY), which is a nifty mix of outliner, kanban board, writing organizer, and longform writing tool.
- `@Joschua` created a script to [import stuff from Goodreads into Obsidian](https://forum.obsidian.md/t/goodsidian-a-goodreads-to-obsidian-script/17523).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-05-08%20Templater%2C%20Syncthing%20%26%20Requested%20Plugins.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-05-08%20Templater%2C%20Syncthing%20%26%20Requested%20Plugins.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
