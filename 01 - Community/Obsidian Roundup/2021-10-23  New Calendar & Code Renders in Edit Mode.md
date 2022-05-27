---
link: https://www.obsidianroundup.org/2021-10-23/
author: Eleanor Konik
published: 2021-10-23T11:30:00
publish: true
---

# 2021-10-23: New Calendar & Code Renders in Edit Mode
iOS guides, more WYSIWYG improvements, & some neat text tabbing & cursor tricks.

## In The Community

-   The community talk by `@phibr0` for [creating your own obsidian plugin](https://www.youtube.com/watch?v=XaES2G3PVpg) is now available.
-   The [TTRPG panel community talk](https://www.youtube.com/watch?v=Ovqu_1aW3Sw) is now available.
-   The [[LYT House]] talk with `@ryanjamurphy` about making [Obsidian an Integrated Thinking Environment](https://www.youtube.com/watch?v=fhkwEgGFOg8) is now available.
-   A bunch of Discord accounts got hacked and are spamming scam links. It'd be great if you enabled 2-factor authentication on your accounts.
-   `u/tonystar29` made a [keypad with a macro to automatically](https://www.reddit.com/r/ObsidianMD/comments/qcw5ck/i_made_a_macro_pad_to_track_my_mood_in_my/) put mood ratings into Obsidian daily notes. It's really cool.

## Obsidian Updates

## Plugin News

_Remember: You can manually install plugins that aren't in the community list by copying the main.js, manifest.json and (optionally) the styles.css files into {vault}/.obsidian/plugins/{plugin-folder}. It can then be enabled like any other plugin (you may need to refresh the list first). Usually these files can be found at the GitHub repo under Releases. Conversely, you can install the new [BRAT](https://github.com/TfTHacker/obsidian42-brat) plugin and just input the repository's URL. Note, though, that this is **not as safe** as waiting for them to go through code review. I personally usually wait a week or so to see what the status of a new plugin is unless I really trust the dev._

### New

-   [Fantasy Calendar](https://github.com/valentine195/obsidian-fantasy-calendar) is already one of my favorite plugins — I literally downloaded [BRAT](https://github.com/TfTHacker/obsidian42-brat) so I could automatically get updates for it even before it's gone through code review, it's that good. It was technically made to manage events in fantasy worlds with non-standard calendars, but the Gregorian calendar works great for real life stuff too. It's dynamic, it's beautiful, it's flexible, it's literally better than any fantasy calendar app I've ever used in my life. I've been looking for something like for _years_ and as a bonus it solves _two_ huge problems for me.
-   The new [Pikt plugin](https://github.com/arnau/obsidian-pikt) adds support for the Pikchr markup language for diagrams in technical documentations. It looks like a more flexible version of [[Mermaid]].
-   You can now [tab out](https://github.com/phibr0/obsidian-tabout) of markup.
-   [Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher) has a bunch of nice functionality for searching, including backlinks search, emoji support, and more.
-   Here's a nice [daily quote](https://github.com/twentytwokhz/quote-of-the-day) plugin.
-   You can [practice speed reading](https://github.com/AlexAndHisScripts/obsidian-flashread) in Obsidian now.
-   Vim users will want to check out [Vim cursor](https://github.com/hhhapz/improved-obsidian-vimcursor).
-   You can now [autocomplete HTML tags](https://github.com/bicarlsen/obsidian_html_tags_autocomplete).
-   There's a new [prompt plugin](https://github.com/hungsu/obsidian-prompt) for giving yourself writing prompts.
-   You can now [directly download Tweets into your vault](https://github.com/kbravh/obsidian-tweet-to-markdown).
-   Obsidian now supports [chess notes](https://github.com/pmorim/obsidian-chess).
-   [Stenography](https://github.com/bramses/stenography-obsidian) will translate code into plain language.
-   Here's [autocomplete for LaTeX](https://github.com/echaos/BetterLatexForObsidian).
-   You can now [archive links](https://github.com/tomzorz/obsidian-link-archive) in a note to archive.org. This means they'll be available even if the original site goes down or gets removed.

### Updates

-   [BRAT](https://github.com/TfTHacker/obsidian42-brat) got some quality of life improvements.
-   [CodeMirror Options 0.4.2](https://github.com/nothingislost/obsidian-codemirror-options/releases/tag/0.4.2) adds support for rendering HTML and certain code blocks (i.e. dataview) in edit mode.
-   [Advanced Cursors](https://github.com/SkepticMystic/advanced-cursors) now has support for VS Code style `ctrl + d` which lets users move to the next instance of the current selection and add another cursor at the next instance of the current selection. This is useful for making a bunch of changes at once to thing that are similar.
-   [Code Editor Shortcuts v1.2.0](https://github.com/timhor/obsidian-editor-shortcuts/releases/tag/1.2.0) now supports expanding a selection to brackets and quotes.
-   The [Linter](https://github.com/platers/obsidian-linter) plugin has a bunch of new settings added.
-   [Advanced-URI v1.13.0](https://github.com/Vinzent03/obsidian-advanced-uri/releases/tag/1.13.0) supports search and replace for daily notes.
-   [The Map View plugin](https://github.com/esm7/obsidian-map-view) added marker clusters, inline tag support, and collapsible map controls to aid mobile usage.
-   In [QuickAdd v0.4.17](https://github.com/chhoumann/quickadd), input prompt file name search is now based on file names, rather than file paths. There's also a new WYSIWYG LaTeX formula prompt.
-   [File Tree Alternative v1.5.7](https://github.com/ozntel/file-tree-alternative/releases/tag/1.5.7) allows users to change the default expand and close icons with the alternatives in the plugin settings. You can also focus in & out with certain folders within Folder Pane (as of [v1.5.4](https://github.com/ozntel/file-tree-alternative/releases/tag/1.5.4))
-   [Excalidraw 1.3.20](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.3.20) got an important performance update but represents a breaking change; once you use the new version, old versions won't be able to open the relevant image.

### Betas

-   [Obsidian RSS](https://github.com/joethei/obsidian-rss) is in early beta. It's already neat, though. To open up the pane, run `RSS Reader: Open Feed` from the command palette. Here's what the [Roundup looks like in an Obsidian RSS reader](https://www.youtube.com/watch?v=_MjJ2TM6ylU). The video uses the awesome new Sanctum theme, which includes icons, so you know if the link goes to Github or Discord or whatever — see the Appearance section for more.
-   Here's an easier way to [find the URL to a published note from within Obsidian](https://github.com/kometenstaub/copy-publish-url)

### For Developers

-   Here's a nice Discord discussion about [how to make your theme and plugin screenshots look nice](https://discord.com/channels/686053708261228577/702656734631821413/898721139977760788).
-   If you've defined a style settings config in your plugin's CSS file, you can now notify Style Settings that your plugin has a config that needs to be parsed like so: `this.app.workspace.trigger("parse-style-settings")`
-   Here's notes for [releasing plugins with github actions and using standard-version](https://marcus.se.net/obsidian-plugin-docs/publishing/release-your-plugin-with-github-actions#use-standard-version-to-automatically-tag-your-release).
-   [obsidian-repos-downloader.py](https://github.com/claremacrae/obsidian-repos-downloader) is a python script to download all the published community Plugins and/or Themes to use as a reference.

## Feature Requests

-   [Delay loading of plugins until after Sync finishes](https://forum.obsidian.md/t/feature-request-sync-service-api-events-delayed-plugin-loading/26004)
-   [Search operator for creation and modified dates to filter results by time](https://forum.obsidian.md/t/search-operator-for-creation-and-modified-dates-to-filter-by-time/25802)
-   [Search operator for searching within a list](https://forum.obsidian.md/t/search-operator-similar-to-section-but-for-lists-search-within-a-single-list-or-parent-list-item-and-its-children-list-items/25803)
-   [generative syntactic trees for linguists](https://forum.obsidian.md/t/is-there-a-plugin-to-help-create-generative-syntactic-trees-is-obsidian-if-not-it-would-be-cool/26014)
-   [Better hotkey support for the settings menu](https://forum.obsidian.md/t/keyboard-navigation-in-settings-menu-plugin-menu/25787)
-   [Assets in plugins support](https://forum.obsidian.md/t/support-for-assets-in-plugins/25837)

## Appearance

-   You can get [WYSIWYG mode](https://github.com/Mara-Li/Obsidian-Snippet-collection) on mobile with the Style Settings plugin.
-   [Sanctum](https://github.com/jdanielmourao/obsidian-sanctum/releases/tag/v0.2.3) got an update. It adds a little icon before a link, for example to Discord, so you know where the link goes in preview mode. It also has nice support for asides, graph colors, etc. I'm loving it so far.
-   [ITS](https://forum.obsidian.md/t/theme-its-dark-light-theme/12838/135) got some updates, especially with the icons.
-   Here's the [CSS snippet for adding icons to external links](https://github.com/SlRvb/Obsidian--ITS-Theme/blob/main/S%20-%20External%20Link%20Icons.css).
-   The new [Slytherin](https://github.com/MatheusZarkov/Obsidian-Slytherin) theme styles Minimal into Slytherin colors and adds folder icons, darker icons, bigger headers, and visually distinct headers.
-   [Rose Pine Moon](https://github.com/mimishahzad/rose-pine-moon-obsidian) is new and has a nice floral color scheme.
-   Here's how to add [pretty backgrounds to kanban boards](https://discord.com/channels/686053708261228577/889616783458304001/898966313957998632).

## Ancillary Code

-   Here's a [shortcut](https://www.icloud.com/shortcuts/440f5d89e6664992a88506649da2e199) for quick capturing notes from an Apple watch using Drafts.

## Guides

-   Here's a playlist of 9 video tutorials covering the basics of [Obsidian Mobile for IOS/IPad OS](https://youtube.com/playlist?list=PLDxMSDwXuwBO0SYztJe3QiexH0tDxEEUU).
-   Here are some [tips on how to adapt to Obsidian if you're used to outliners](https://twitter.com/syncretizm/status/1447903121049460743?t=tsmOWZjaTcUNxLDLEXg2sQ).
-   The [Life-Disciplines-Projects](https://github.com/uwidev/life-disciplines-projects) life-management framework vault had a major overhaul and was updated to v0.2.
-   Here's how to [access hidden .obsidian and plugin folders / directories in your vault on iPhone and iPad using iSH Shell app](https://discord.com/channels/686053708261228577/864046194195431425/899362264962957352)
-   Here's a [collection of resources](http://discordapp.com/channels/686053708261228577/722584061087842365/900793115517009921) for using hypothes.is and Obsidian for annotations.

## Discussions

-   Here's a [discussion thread for Obsidian with NaNoWriMo](https://forum.obsidian.md/t/nanowrimo-obsidian/25076/10) that covers a lot of things relevant to authors.
-   Here's a reminder that [[Zettelkasten]] style notes are [not optimized for doing well on exams](https://www.reddit.com/r/ObsidianMD/comments/qbigpl/help_needed_when_it_comes_to_integrating_obsidian/).
-   [How are you using Obsidian to organize your podcast notes?](https://forum.obsidian.md/t/how-are-you-organizing-your-knowledge-from-podcasts/26013)

## Knowledge Management

-   Jonathan Miller shared [10 takeaways from the Linking Your Thinking workshop](https://www.jmill.dev/lyt-takeaways-f21) that just wrapped up. It reminded me of how much Nick's philosophy of notetaking has always resonated with me.

## Ancillary Tools

-   Here's a tool meant to [create and reorder a Johnny Decimal system](https://johnny-decimal-generator.netlify.app/)
-   Here's a discussion of [Windows file explorer tools](https://www.reddit.com/r/ObsidianMD/comments/qcetgb/using_obsidian_as_a_file_explorer/) that "feel" like Obsidian for navigating files.

## Housekeeping

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-10-23%20%20New%20Calendar%20%26%20Code%20Renders%20in%20Edit%20Mode.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-10-23%20%20New%20Calendar%20%26%20Code%20Renders%20in%20Edit%20Mode.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
