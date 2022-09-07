---
link: https://www.obsidianroundup.org/2021-09-04/
author: Eleanor Konik
published: 2021-09-04
publish: true
---

# 2021-09-04: View !\[\[transclusions\]\] in edit mode & an end to early bird pricing!
Lots of stuff for developers this week: requests, a way to download all plugin code, & discussions about inter-plugin API best practices.

## Obsidian Updates

- There are now over 300 plugins and 40k members of the community Discord!
- The early bird discount pricing for Sync and [[Obsidian Publish|Publish]] is ending at the end of this month (September 30, 2021). Please read the [FAQ](https://forum.obsidian.md/t/last-chance-to-get-early-bird-discount-for-sync-and-publish-before-september-30-2021/23541) and remember: Obsidian is created by a very small team of two and they only charge personal users for services that cost _them_ money (servers aren't cheap, especially if you don't have economy of scale advantages).

[v0.12.15](https://forum.obsidian.md/t/obsidian-release-v0-12-15/23348) is now available for public access, featuring:

- Improved [graph timelapse animation](https://forum.obsidian.md/t/obsidian-release-v0-12-13/21959) that's ordered by creation time.
- Right click on a [heading to rename](https://forum.obsidian.md/t/obsidian-release-v0-12-14/23046) and update all links to this heading.
- Right click on selected text to [search for it globally](https://forum.obsidian.md/t/obsidian-release-v0-12-15/23348).

## Appearance

- [[Shimmering Focus]] is a condensed minimalist theme aimed at working nicely with pandoc. It has a bunch of really nice features, like increased contrast.

## Plugins

### New

- [Obsidian plaintext](https://github.com/dbarenholz/obsidian-plaintext) will let you edit `.bib` and presumably `.css` files etc directly in Obsidian instead of needing a text editor like Visual Studio Code (although there isn't any syntax highlighting, it's not meant as a replacement for [[VSCode]] or whatnot).
- You can now get a direct feed from the [[obsidian-hackernews|HackerNews]] top stories into an Obsidian pane. Presumably it wouldn't be too hard to add other RSS feeds to this by forking it or creating a pull request?
- [[obsidian-copy-block-link|Copy Block Link]] lets you right click a block and copy the link to the block.
- A new plugin lets you execute [[obsidian-jupyter|Jupyter notebooks]], which I'm told are super useful for the data science / machine learning folks.
- There's a new riff off of focus mode: [[ghost-fade-focus|Ghost Fade Focus]].
- [[random-structural-diary-plugin|Random Structural Diary]] will give you a random list of questions to journal about.
- This plugin integrates [[drawio-obsidian|drawio]] diagramming. If anybody knows how this is different than [[obsidian-excalidraw-plugin|Excalidraw]] or [[Mermaid]] I'm interested.
- [[obsidian-file-link|Better File Link]] makes it easier for people to link to external files without having to drag and drop from the file explorer.

### Updates

- The [[oz-image-plugin|Image in Editor]] plugin has commands to convert Wikilinks to Markdown links and vice-versa in all files within the vault or only in the active file. This is amazing for switching _to_ wikilinks for **seeing transclusions in editor mode using this plugin**, or for people trying to convert to Markdown links for interoperability with other programs like static site generators.
- [[quick-explorer|Quick Explorer]] [0.0.7](https://github.com/pjeby/quick-explorer) has more hotkey support and a quick preview mode. It also has a really amazing Readme.
- The [[obsidian-spaced-repetition|Spaced Repetition]] plugin got some love; more stastics, you can review cards from a single note if you want, and some niftier post-review edit options.
- [[obsidian-tasks-plugin|Tasks]] v1.3.0 has new sorting options, better CSS support, and mobile toolbar icons.
- [[obsidian-excalidraw-plugin|Excalidraw]] 1.2.21 supports transclusion of sections in addition to blocks. 1.3.0 has an extended ExcalidrawAutomate API that lets users access elements of the active drawing and add elements on the fly.
- [[cmenu-plugin|cMenu]] now has a status bar menu and some QoL updates.

### For Developers

- Here's a nice [guide for new programmers](https://joschuasgarden.com/Five+lessons+from+a+new+programmer+for+a+new+programmer) who are starting out learning because of Obsidian, written by a programmer who started out programming because of Obsidian.
- Here's a discussion about [inter-plugin communication](https://forum.obsidian.md/t/inter-plugin-communication-expose-api-to-other-plugins/23618) that is probably important as a central discussion point for best practices for exposing plugin APIs from plugins.
- `@jgauthier` is working on a big update to the Citations plugin and is looking for CSS/design help and feedback (or contributions to development). Here's the [development branch](https://github.com/hans/obsidian-citation-plugin/tree/references-view).
- Theme developers should be on the lookout for breaking changes coming to the kanban plugin, which is currently [beta testing](https://github.com/mgmeyers/obsidian-kanban/releases/tag/1.0.0-beta.1) custom drag and drop and some other stuff like hotkeys and lists.
- This [script](https://github.com/luckman212/obsidian-plugin-downloader) will download all of the Obsidian plugin repositories to use as a reference for developing plugins
  .

## Requests

- There was [discussion](https://discord.com/channels/686053708261228577/694233507500916796/883218999628927066) about the possibility of creating a docker instance of a webtop window manager and running obsidian on it. If someone could put together a guide for "how to run Obsidian on a server so that you can access it from the web" I feel confident that a great many people would appreciate it.
- Rendering citations in preview mode was requested. There's was a good discussion about ways to [get started](https://discord.com/channels/686053708261228577/722584061087842365/881108789774942258) in Discord.

## Guides

- Did you know that you can use a `\` backslash to escape characters, so that they aren't treated as markdown commands and will therefore render in preview without needing to be commented using a backtick ( \`)?
- This is a really nice video guide for how to [process source notes into permanent notes](https://www.youtube.com/watch?v=qQM1pjxu3WE) and what Obsidian features help.
- The video from the Buttons community talk from Buttons developer `@shabegom` is now live [on YouTube](https://www.youtube.com/watch?v=3LhtmBYy6Jc).
- `@Christian` shared a QuickAdd script and process for importing notes that emulates other automatic importers but allows a bit more control.
- `@productivity guru` shared a [guide for using Templater](https://www.youtube.com/watch?v=LjdJbknTjm4) to insert variables and functions into your notes.
- `@zsviczian` shared a video of how to implement the [Clothesline Method for Sequencing Ideas](https://www.youtube.com/watch?v=q8KF3flIyKs&feature=youtu.be) using [[templater-obsidian|Templater]] and Excalidraw. Here's [part two](https://www.youtube.com/watch?v=yhljjFPzpzI).
- Here's a [Reddit discussion and video](https://www.reddit.com/r/FoundryVTT/comments/ozxpte/obsidian_md_module_or_markdown_integration/) about how to get things from the virtual tabletop Foundry into Obsidian.
- Here's a [script using netlify](https://forum.obsidian.md/t/yet-another-free-publish-yafp/23608) as an alternative to [[Obsidian Publish]].
- Here's how Mac/iOS users can use [keyboard maestro for quick capture and inbox processing](https://forum.obsidian.md/t/quick-capture-mac-ios-and-inbox-processing/21808).

## Different Usecases

- `@JeremyMcLellan` shared in Discord how he uses [Obsidian for standup comedy](https://discord.com/channels/686053708261228577/805952223124520961/883076332144168961).
- `@SlRvb` shared a [sample vault for journaling](https://forum.obsidian.md/t/slrvbs-journaling-setup/22346/14).
- On Discord, `@Vincer` shared a list of the plugins that help them have [a more visual experience](https://discord.com/channels/686053708261228577/707816848615407697/853289760578469948) with Obsidian.
- On Discord, `@pseudometa` had a [widely-bookmarked comment](https://discord.com/channels/686053708261228577/700466324840775831/881472955853459486) about why _and when_ highlighting and extracting notes can be more valuable than summarizing the main points of a text
- Here are some nice [starter templates](https://github.com/masonlr/obsidian-starter-templates).
- A user on Reddit shared their [workflow for task and project management in Obsidian](https://www.reddit.com/r/ObsidianMD/comments/pepced/hey_everyone_i_just_wanted_to_share_my_personal/).

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- `@pseudometa` shared detailed documentation for how they use the (mac-only) tool [Alfred with Obsidian](https://github.com/chrisgrieser/shimmering-obsidian/releases/latest). Lots of gems there for Alfred users, I suspect.
- `@argentum` created an [issue on Github](https://github.com/argenos/zotero-mdnotes/issues/133) to track the migration of Mdnotes to the new Zotero beta. You can subscribe if you're looking for updates.
- `@Santi Younger` shared a video about [the Readwise integration](https://youtu.be/g_5Pk7XwDFg) with Obsidian.
- [Duplicati](https://github.com/duplicati/duplicati) is a free & open source backup client that securely stores encrypted, incremental, compressed backups on cloud storage services and remote file servers. It works on OSX, Windows and Linux. `@peterOlson` says it was easy. Since [[Obsidian Sync]] is _not_ a backup service and as best practice you should separate backups from sync, it's been recommended as a nice companion.
- `@psuedometa` shared their note about [different PDF annotation extraction methods](http://discordapp.com/channels/686053708261228577/722584061087842365/882368061481570324), with some pros/cons of every tool, as `.md` file on Discord.

## Housekeeping

- If you're curious to see how my theory about [writing gestalt book reviews is helpful for processing knowledge](https://eleanorkonik.com/lit-review-value-gestalt-reflection/), I wrote a [twitter thread reflecting](https://twitter.com/EleanorKonik/status/1432855712934289408) on how the process of [reviewing Tamed by Alice Roberts](https://eleanorkonik.com/book-review-tamed/) helped me understand the book better.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-09-04%20View%20transclusions%20in%20edit%20mode%20%26%20an%20end%20to%20early%20bird%20pricing.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-09-04%20View%20transclusions%20in%20edit%20mode%20%26%20an%20end%20to%20early%20bird%20pricing.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
