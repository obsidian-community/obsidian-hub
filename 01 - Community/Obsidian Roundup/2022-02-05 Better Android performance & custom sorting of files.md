---
link: https://www.obsidianroundup.org/2022-02-05/
author: Eleanor Konik
published: 2022-02-05T13:30:00
publish: true
---

# 2022-02-05: Better Android performance & custom sorting of files
Themes with built-in color schemes! Plus, it's now easier to debug mobile plugins, QuickAdd has mobile support, and clouds of frequently-used words. 

## Obsidian Updates

Insider Mobile v1.1.0 (Build 37) is up to parity with Desktop and also:

-   iOS: Fixed drag and drop and long-hold context menu not working.
-   Android: **Improve cold startup performance for large vaults.**
-   Android: Fix sync sometimes react to files when nothing has changed due to mis-reported modified times.
-   Android: Fixed images from http sources not loaded due to insecure context.

It should now be much easier to open Obsidian quickly — and if your load times are still long, you can get a report on which plugins are slowing down your load times, if you have plugins enabled. For me personally, Obsidian now opens roughly as fast as Google Keep 🥳

## Plugin News

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Divide & Conquer](https://github.com/chrisgrieser/obsidian-divide-and-conquer) by `@chrisgrieser`  provides commands for bulk enabling/disabling of plugins. It's useful for debugging when you have many plugins.
-   [Excel to Markdown Table](https://github.com/ganesshkumar/obsidian-excel-to-markdown-table) by `@ganesshkumar`  lets users paste Excel tables as Markdown tables in Obsidian editor; this is a nice complement to [Advanced Tables](https://github.com/tgrosinger/advanced-tables-obsidian/) so people don't have to iframe converter websites anymore.
-   [Relative Line Numbers in Live Preview](https://github.com/EndlessReform/obsidian-relative-line-numbers) by `@EndlessReform`  looks like a fork of [relative line numbers](https://github.com/nadavspi/obsidian-relative-line-numbers) updated for the new editor.
-   [Power Search](https://github.com/aviral-batra/obsidian-power-search) by `@aviral-batra`   searches Anki Notes based on the current line.
-   [Live2D Widget](https://github.com/moelody/live2d-widget-obsidian) by `@moelody`  will add live2d model widget to obsidian; it's an anime-esque visual frill.

### Updates

-   [QuickAdd 0.5.0](https://github.com/chhoumann/quickadd) has mobile support 🥳 just in time to run the [zettelizer macrp](https://github.com/chhoumann/quickadd/tree/master/docs/Examples) on my new iPad.
-   [Quick Explorer 0.1.10](https://github.com/pjeby/quick-explorer/releases/tag/0.1.10) got some bugfixes and should work better in Live Preview now.
-   [Emoji Toolbar v0.3.1](https://github.com/oliveryh/obsidian-emoji-toolbar/releases/tag/0.3.1) has improved compatibility with Primary theme, & Live Preview users can now press 'Enter' to insert the first emoji in the list.

-   [KOReader Sync 0.3.0](https://github.com/Edo78/obsidian-koreader-sync#dataview-embedded) has a setting to create a note with a dataviewjs query so that all the notes of a book can be shown in a single big list. [0.4.0](https://github.com/Edo78/obsidian-koreader-sync#commands) added commands to sync, mark note as edited (or not), or to enable/disable sync.

-   [Map View](https://github.com/esm7/obsidian-map-view) now supports a proper "new geolocation note" dialog with geosearch _and_ configurable URL parsing (from Google Maps etc).
-   [Task Collector 0.7.6](https://github.com/ebullient/obsidian-task-collector) has support for [Snippetor](https://github.com/ebullient/obsidian-snippetor), which is actively iterating to work with more themes and load faster — the idea is that it will support custom styling for `- [?]` style checkboxes across themes.
-   [Code Editor Shortcut 1.5.0](https://github.com/timhor/obsidian-editor-shortcuts/releases/tag/1.5.0) lets users copy selected lines up/down in a way that emulates VS Code.
-   you can now turn off drop shadows in [Admonition](https://github.com/valentine195/obsidian-admonition) settings. Nested admonitions will receive a light border to make them visually distinct.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   [Bartender](https://github.com/nothingislost/obsidian-bartender) adds support for rearranging the view action icons and Minimal's  floating ribbon bar. The order will be saved whenever you rearrange the icons. Bartender also now supports **custom sorting of files and folders**. Here's a [demonstration on Discord](https://discord.com/channels/686053708261228577/931552763467411487/938535617195814972).
-   You can make a word or [tag cloud](https://github.com/joethei/obsidian-tagcloud) for your vault; it's a nice visual representation of what you write about most often. [It turns out I have a lot of notes about domestication](https://twitter.com/EleanorKonik/status/1488251003619188740).
-   [Remotely-save 0.2.14](https://github.com/fyears/remotely-save) has improvements for OneDrive syncing
-   The new Goodreads plugin [Booksidian](https://github.com/MichaBrugger/booksidian_plugin) lets users choose from the list of all parameters available over the Goodreads RSS feed  (+ some extra that can be deduced from them like subtitle or series). It has templating features to let users lay out the body and  frontmatter according to their preferences.

### For Developers

-   Here's some tips about [how to write good documentation](https://www.swyx.io/documentation-levels).

## Appearance

-   Here's how to [use Minimal & Dataview to create a gorgeous card view of your library](https://twitter.com/chrisbbh/status/1489327905511555073?s=21).
-   [Shimmering Focus](https://chrisgrieser.github.io/shimmering-focus/) has a new `writing` cssClass: Applying it to a note will switch the theme to a serif font, justified text, slightly tinted background, and more (configurable with the Style Settings Plugin). There's also a new _alternate_ [Shimmering Focus](https://github.com/tingmelvin/willemstad), created by `@Melvin`, which includes a style setting for colored heading backgrounds (one of my personal favorite theme features).
-   [Sanctum v.0.6.2](https://github.com/jdanielmourao/obsidian-sanctum/releases/tag/v0.6.2) added new color schemes; cold grey, hearth, moss (my favorite!), and tide. There were also a bunch of tweaks and bugfixes.
-   [Minimal 5.0](https://github.com/kepano/obsidian-minimal/releases/tag/5.0.0) also added new color schemes for Dracula, Gruvbox, Nord, Notion, Things & Solarized.
-   [Ebullientworks 1.3.12](https://github.com/ebullient/obsidian-theme-ebullientworks) got a bunch of fixes and improvements, including blockquotes in live preview and support for Snippetor.
-   [Primary](https://github.com/ceciliamay/obsidianmd-theme-primary/releases/tag/v.1.1.0) got some bugfixes.
-   Here's a snippet to [style kanban dates & completed cards](https://discord.com/channels/686053708261228577/702656734631821413/84005952529812686) from `@mgmeyers` in Discord.

## Ancillary Code

-   Here's a [templater script to copy the current Obsidian note as a markdown link](https://gist.github.com/selfire1/9b69a35840d02405942a3f9739276b3e) (`[Title](ObsidianURI)`) to easily open your Obsidian notes from anywhere.

## Guides

-   Here's how to use [Voiceliner as a quick capture tool for Obsidian](https://www.youtube.com/watch?v=VO9AD438czU). It's got good support for creating outlines with voice-to-text, it seems like.
-   Here's a guide from an ex-Evernote user about [how to find notes quickly in Obsidian](https://jamierubin.net/2022/02/01/practically-paperless-with-obsidian-episode-16-finding-notes-quickly/).
-   Here's how to [get nested daily note folders natively in Obsidian](https://www.reddit.com/r/ObsidianMD/comments/sjm5gp/nested_daily_note_folders_natively_in_obsidian/).
-   This [Dataview tutorial](https://www.youtube.com/watch?v=7kFEl7Ovsr8) got resurfaced as a particularly accessible guide.

## Discussions

-   Here's a nice discussion about [using Obsidian for task management](https://www.reddit.com/r/ObsidianMD/comments/sfq78s/unpopular_opinion_obsidian_is_an_excellent_task/). Their system is a lot more complicated than mine, which I discussed [over on Twitter](https://twitter.com/EleanorKonik/status/1487472577085800452). The beautiful thing about Obsidian is how flexible it is 💚
-   Here's a nice discussion about [methods for managing information about a library of books](https://www.reddit.com/r/ObsidianMD/comments/shb8s6/library_in_obsidian/).
-   This [unpopular opinion: Obsidian is an excellent Task Manager](https://www.reddit.com/r/ObsidianMD/comments/sfq78s/unpopular_opinion_obsidian_is_an_excellent_task/) thread on Reddit got a lot of love.
-   I wrote a piece about why [I think it's okay if Obsidian isn't your 'second brain,' it's 'just' an awesome notetaking app](https://www.obsidianroundup.org/ite-not-second-brain/). It got discussed [on Twitter](https://twitter.com/TfTHacker/status/1488482500850638853) and [Reddit](https://www.reddit.com/r/ObsidianMD/comments/shuy0d/obsidian_is_my_thinking_environment_not_my_second/).
-   Here's a [discussion on Discord about the value of the Graph Analysis plugin](https://discord.com/channels/686053708261228577/710585052769157141/938171786724536340), which was later summarized [on the forum](https://forum.obsidian.md/t/supercharging-a-messy-library-with-the-graph-analysis-plugin/31724).

## Ancillary Tools

-   Someone asked for [my Readwise export template](https://gist.github.com/eleanorkonik/1f0586fe13d98f1dbf18ec72b00bf37d), so I made a gist for it.
-   Here's a Windows utility which allows you to [search & launch vault files](https://github.com/fglass/obsidx) without having Obsidian open.

## Housekeeping

My supporters-only 5x8 event had some great discussion, and I wanted to share a really awesome ["digital brain" project that dates from 1997](https://www.jerrysbrain.com/welcome) "Jerry's brain" got brought up during the discussion of "second brains" and it was fascinating to see how old the metaphor — and process — is.

We also discussed this great article about [the difference between planning to start and planning to finish](https://studio.ribbonfarm.com/p/planning-to-start-planning-to-finish).

I also officially finalized moving my articles off Wordpress & onto Ghost thanks to the incredible concierge service. My [new landing page](https://eleanorkonik.com/) is a static site (hand-edited, no generator, & I used SCSS) hosted on GitHub & Netlify. All the old links should still work; if you happen to find a broken one, let me know.

I still have some auditing to do, and I haven't decided if/how to transfer comments over to the Roundup, but in the meantime, the Roundup is now the official home of my Obsidian-adjacent essays & thoughts, while the Iceberg hosts all of my worldbuilding/history/book review stuff.

If you haven't already read my piece on [why it's hard to teach critical thinking skills](https://www.obsidianroundup.org/difficulties-teaching-critical-thinking/), maybe check it out at its new home?

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-02-05%20Better%20Android%20performance%20%26%20custom%20sorting%20of%20files.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-02-05%20Better%20Android%20performance%20%26%20custom%20sorting%20of%20files.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
