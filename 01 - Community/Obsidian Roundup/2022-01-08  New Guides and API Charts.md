---
link: https://www.obsidianroundup.org/2021-01-08/
author: Eleanor Konik
published: 2022-01-08T13:30:00
publish: true
---

# 2022-01-08: New Guides & API Charts
The Gems of the Year voting has ended, and there's a new YouTube channel for people to contribute videos to a community playlist.

## In The Community

-   There's a really important discussion about [the current state of the meta](https://forum.obsidian.md/t/css-magicians-theme-creators-standardisation-of-theming-practices/29937/17) in regard to Obsidian's appearance, namely themes and CSS snippets.
-   The [Gems of the Year](https://forum.obsidian.md/t/obsidian-gems-of-the-year-2021-voting/28759) voting ended. You can see the winners by poking through the forum, but I imagine there will be a formal announcement soon. Usually, the developers like to contact the winners first.
-   The [Obsidian Community Talks YouTube channel](https://www.youtube.com/channel/UCxNSTq2kmupdR6LD400FpvA) now has a separate playlist for Contributed Videos, for folks who want to contribute a video to the Obsidian knowledge base but not necessarily deal with hosting their own YouTube channel and figure out discoverability, etc.

## Obsidian Updates

-   [Insider v.0.13.18](https://forum.obsidian.md/t/obsidian-release-v0-13-18-insider-build/29790) has new hotkeys for in-document search and, copyable code blocks, and vim mode improvements.
-   [v0.13.19](https://forum.obsidian.md/t/obsidian-release-v0-13-19/29998) has a couple of fixes that mostly won't be noticeable except as potential problems that might not happen anymore... as well as everything from Insiders 15-18.

## Plugin News

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

### Community Plugins

These plugins went through code review and are now available in Obsidian's plugin list.

-   [Smarter Markdown Hotkeys](https://github.com/chrisgrieser/obsidian-smarter-md-hotkeys) by `@chrisgrieser` lets users select words and lines more effectively before applying markup. Multiple cursors are supported as well.
-   [Tomorrow's Daily Note](https://github.com/frankolson/obsidian-tomorrows-daily-note) by `@frankolson` creates tomorrow's daily note for pre-emptive planning.
-   [Indentation Guides](https://github.com/mgmeyers/obsidian-indentation-guides) by `@mgmeyers` adds vertical lines to the editor denoting indentation level of lists and other content. This moves the functionality out of themes and into a plugin, for easier support.
-   [Wrap with shortcuts](https://github.com/manic/obsidian-wrap-with-shortcuts) by `@manic` Wrap selected text in custom tags with shortcuts.
-   [Native Scrollbars](https://github.com/mgmeyers/obsidian-native-scrollbars) by `@mgmeyers` enables native OS scrollbars throughout obsidian.
-   [Plaintext](https://github.com/dbarenholz/obsidian-plaintext) by `@dbarenholz` allows opening specified files as plaintext (RAW mode).
-   [Metronome](https://github.com/curtgrimes/obsidian-metronome-plugin) by `@curtgrimes` adds interactive metronomes to your notes.
-   [Emotion Picker](https://github.com/dartungar/obsidian-emotion-picker) by `@dartungar` lets users choose an emotion from a list to insert into a note.
-   [Vim IM Select](https://github.com/ALONELUR/vim-im-select-obsidian) by `@ALONELUR` supports auto selection the opposite input method in different vim mode.
-   [Global Hotkeys](https://github.com/mjessome/obsidian-global-hotkeys) by `@mjessome` adds support for global hotkeys.

### Pending (as of Friday morning)

_Note: Most of these plugins are not yet available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool (BRAT)](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Phrasebank](https://github.com/viktorbezdek/obsidian-phrasebank) by `@viktorbezdek`  adds shortcodes with various prewritten phrases to improve quality and productivity of your writing.
-   [Local File Interface](https://github.com/qawatake/obsidian-local-file-interface-plugin) by `@qawatake` provides commands for moving files in and out of the vault
-   [Topic Linking](https://github.com/liammagee/obsidian-topic-linking) by `@liammagee` can convert PDF files and web links to Markdown.
-   [Binary File Manager](https://github.com/qawatake/obsidian-binary-file-manager-plugin) by `@qawatake` detects new binary files in the vault and create markdown files with metadata.
-   [Rule folder template](https://github.com/daoif/obsidian-Rule-folder-template-daoif) by `@daoif` lets users create a new document from the template and place it in the folder of the specified rule.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   [Remotely Save](https://github.com/fyears/remotely-save) is an unofficial sync plugin allowing you sync your notes between local devices and third-party services. It works with S3, Dropbox, webdav, and OneDrive. It also supports mobile (including iOS) and e2e encryption, and I think it's designed to get around some annoying iCloud stuff.
-   Here's a new plugin called [BibNotes Formatter](https://github.com/stefanopagliari/bibnotes). It is designed for academics and the Zotero workflow, and should let users keep the literature notes on Obsidian updated when the data is changed in Zotero without the risk of losing the manual edits. It works with notes extracted both from the Zotero native pdf reader and via Zotfile.
-   [Obsidian Typograph v.0.0.6](https://github.com/MalignantCarp/obsidian-typography-plugin/releases/tag/0.0.6) has a new HTML parser and new ways to customize quotation marks.
-   [Obsidian Memos](https://github.com/Quorafind/Obsidian-Memos) will recognize `- HH:mm text` or `- [ ] HH:mm text` in daily notes and pull them out into stuff like Big Calendar. It supports mobile and hotkeys.

### Updates

-   As of [0.3.2](https://github.com/lanice/obsidian-rant), inline rant-lang blocks now also markdown-parse the output.
-   Version 1.7.0 of the [[obsidian-spaced-repetition|Spaced Repetition Plugin]] supports note transclusion, audio & video in flashcards. It also got some bug fixes, and allows users to zoom into an image when clicking it. It's even been translated into German and Dutch!
-   [Metacopy](https://github.com/Mara-Li/obsidian-metacopy/releases/tag/0.0.20) now allows users to create a link based on a frontmatter key and a base value. Users can also disable the file and context menus using a frontmatter key.
-   React Components 0.1.3 now supports Live Preview.
-   [Advanced Slides 1.3.0](https://github.com/MSzturc/obsidian-advanced-slides) allows users to export slides to html and got a bunch of bugfixes. 1.5.0 added a chalkboard, a menu plugin, and a bunch of settings.
-   [Various Complements v4.0.0](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/4.0.0) removed the Toggle Auto-complete command, added new ignore key options, allows users to load custom dictionaries, and more!
-   [Code Editor Shortcuts v1.4.1](https://github.com/timhor/obsidian-editor-shortcuts/releases/tag/1.4.1) got some bugfixes.
-   [Toggl Track Integration for Obsidian v 0.4.0](https://github.com/mcndt/obsidian-toggl-integration/wiki/Creating-Toggl-reports-inside-notes)  was focused on visualizing the Toggl track data inside of Obsidian.
-   [Quoth 0.2.0](https://github.com/erykwalder/quoth/releases/tag/0.2.0), which offers more flexible embedding. It lets users embed precise selections, inline embeds, and include author and title. There are some new buttons and better contextualization since the initial version, too.

### For Developers

-   There's a new github repository [template for creating an Obsidian theme](https://github.com/obsidian-community/obsidian-theme-template). It's designed to help people get started with theme development, similar to the Obsidian sample plugin. Feel free to submit more examples!
-   Here's a [graphical representation of the Obsidian API](https://i.joethei.space/obsidian-api.png). Here it is as [an svg](https://i.joethei.space/obsidian-api.svg). Here's the [.puml file used to generate it](https://i.joethei.space/obsidian-api.puml).
-   [Theme Design Utilities 0.14](https://github.com/chrisgrieser/obsidian-theme-design-utilities) allows users to cycle between dark and light mode, as well as source, live preview, and reading mode, with a single hotkey.

## Feature Requests

Last week, we discussed "shoot for the moon" ideas for exciting things the community would love to see in 2022. Here are some highlights from Discord.

-   [Revolutionize the landscape for markdown tables](https://discord.com/channels/686053708261228577/694233507500916796/926480875783340112).
-   [Figure out real-time, multiplayer Obsidian](https://discord.com/channels/686053708261228577/694233507500916796/926490659509112872).
-   [Improved database functionality, to make some of the key functionality of Dataview & Templater more accessible](https://discord.com/channels/686053708261228577/694233507500916796/926513276140027975).
-   [Facilitate a bigger variety of view types for the graph, i.e. hyperbolic view](https://discord.com/channels/686053708261228577/694233507500916796/926826434838810624).

## Appearance

-   [ITS](https://forum.obsidian.md/t/theme-its-dark-light-theme/12838/148) restyled some of the plugins, particularly breadcrumbs, Fantasy Calendar, Initiative Tracker and Indent Group.
-   [Wyrd 0.3.2](https://github.com/curio-heart/obsidian-wyrd/releases/tag/v0.3.2) got some updates for Live Preview and styling for embeds.
-   [Prism v1.2.0](https://github.com/damiankorcz/Prism-Theme/releases/tag/1.2.0) has a new system for customizing headers, along with a new wiki showcasing all the Style Settings options for the plugin.
-   [Sanctum v0.5.5](https://github.com/jdanielmourao/obsidian-sanctum/releases/tag/v0.5.6) added indents to Style Settings sections, reworked headings to have pre-set color options, which makes it easier to pick a color scheme that fits with the theme's aesthetic, and made it so heading indicators are only visible on the active line.
-   [Shimmering Focus v1.550](https://github.com/chrisgrieser/shimmering-focus) got a bunch of improvements to support the longform plugin, as well as a much smaller file size and a bunch of fixes.
-   [Ebullientworks 0.2.6](https://github.com/ebullient/obsidian-theme-ebullientworks) got some improvements for using light theme to print, and a toggle for brightness & contrast of tags.
-   [Bubble Space Theme v1.4](https://github.com/Emrie-Candera/Bubble-Space-Theme/releases/tag/v1.4) has been updated for Live Preview and mobile. There's also some new plugin styling.
-   [Dracula Slim](https://github.com/bLaCkwEw/Dracula-Slim) by `@bLaCkwEw` is new.

## Guides

-   Here's a neat forum post about [relational databases in Obsidian](https://forum.obsidian.md/t/toying-with-relational-databases-using-dataview/17433?u=riddyrayes).
-   Here's a new video about [Breadcrumbs and all the new features](https://www.youtube.com/watch?v=N4QmszBRu9I&ab_channel=ObsidianCommunityTalks), as well as a showcase of the [new Threading Mode from Breadcrumbs](http://youtube.com/watch?v=AS5Mv6YNmsQ).
-   Here's how you can [manage tags in Obsidian like Bear](https://www.reddit.com/r/ObsidianMD/comments/rxm23s/manage_tags_like_bear_in_obsidian/).
-   Here's a [guide for daily notes plugin](https://www.reddit.com/r/ObsidianMD/comments/rwmh64/i_made_a_guide_on_how_i_use_the_daily_notes/) that comes with a downloadable vault for experimentation.
-   Here's a video about [using Obsidian as a high school student](https://www.youtube.com/watch?v=fsA6YhOWi5w).
-   Here's a nice guide about [Obsidian and Pandoc](https://notes.nicfab.it/en/en/posts/obsidian/obsidian03/).

## Discussions

-   Here's a great discussion about what worked for different people to help them [get started with Obsidian](https://www.reddit.com/r/ObsidianMD/comments/rxt4ef/i_have_no_clue_how_to_leverage_this_app_where_can/). This video by Artem Kirsanov hadn't crossed my radar yet but comes [highly recommended](https://youtu.be/E6ySG7xYgjY).

## Ancillary Tools

-   Here's a sample [Airtable Database for Personal Knowledge Management](https://airtable.com/shrIw43VorHcjsJWn)
-   [The Raycast Obsidian extension](https://www.raycast.com/marcjulian/obsidian) now supports opening vaults, easy vault switching, and multiple vaults.
-   Here's a writeup about the "future of search" as it relates to [Semantic Search & Obsidian](https://bram.substack.com/p/the-future-of-search-is-not-what).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-01-08%20%20New%20Guides%20and%20API%20Charts.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-01-08%20%20New%20Guides%20and%20API%20Charts.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
