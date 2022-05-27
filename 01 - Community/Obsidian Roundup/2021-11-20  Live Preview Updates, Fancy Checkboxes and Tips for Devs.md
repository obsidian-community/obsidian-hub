---
link: https://www.obsidianroundup.org/2021-11-20/
author: Eleanor Konik
published: 2021-11-20T13:11:00
publish: true
---

# 2021-11-20: Live Preview Updates, Fancy Checkboxes & Tips for Devs
Check out how Obsidian is used by software developers, content creators, & TTRPG fans. Plus, a roundup of how people use tags.

## Obsidian Updates

[v0.13.3](https://forum.obsidian.md/t/obsidian-release-v0-13-3-insider-build/27381) and [v0.13.4](https://forum.obsidian.md/t/obsidian-release-v0-13-4-insider-build/27387) are now available for Insiders, with many improvements for Live Preview, including backlinks in document, [[Mermaid]], query blocks & block quotes, better image handling, (some) custom code blocks from plugins & other code block improvements (see the developers section for more), more native cursor handling on MacOS, better IME handling (which should help Chinese and Japanese users) and auto-pairing of brackets for markdown formatting symbols such as `$`, `=`, `~` and `%`.

The devs also...:

-   Added show-plugin Obsidian URI action. Example: obsidian://show-plugin?id=admonition
-   Added notice for indexing large files taking too long to help debug indexing stuck issues.
-   Fixed a bunch of little things, like a bug in the `replace all` function and the way reference style markdown links and images render.

## Plugin News

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

### New

-   [Extra Markdown Commands](https://github.com/chrisgrieser/obsidian-extra-md-commands) has hotkeys for html commands, underscore bold & italics, and multicolor highlights.
-   [Note From Template](https://github.com/mo-seph/obsidian-note-from-template) is a new templating plugin that allows users to fill in the set fields without leaving the active note. I think of it as being like QuickAdd but with templates.
-   [Customizable Page Header buttons](https://github.com/kometenstaub/customizable-page-header-buttons) adds command buttons left to the standard buttons in Obsidian (which is particularly great for mobile).
-   [icon shortcodes](https://github.com/aidenlx/obsidian-icon-shortcodes) has Built-in Unicode 13.1 Emoji, Font Awesome, and Remixicon support and the ability to import svg icons.
-   You can now automatically upload images in your vault to [Cloudinary](https://github.com/jordanhandy/obsidian-cloudinary-uploader).

### Updates

-   [Auto Class v2.0.0](https://github.com/OfficerHalf/obsidian-auto-class/releases/tag/2.0.0) now supports adding CSS classes to the markdown view based on tags in the current file.
-   [Excalidraw 1.4.10](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.4.10) has support for the new Live Preview Insider build, but it'll need to run a quick patch 7 minutes after your update.
-   [Various Complements](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/1.2.0) v1.2.0 supports custom dictionaries, delays, and a toggle for auto complete. v1.0.0 added support for mobile & live preview mode.
-   [alx-folder-note v0.12.0](https://github.com/aidenlx/alx-folder-note/releases/tag/0.12.0) added support for custom folder icon in file explorer
-   [BRAT 0.6.0](https://github.com/TfTHacker/obsidian42-brat) works with themes!
-   [CodeMirror Options 0.9.0](https://github.com/nothingislost/obsidian-codemirror-options) can now render icon shortcodes in edit mode. There were some other small fixes, and a new Style Settings option to enable minimal page & header embeds in edit mode.
-   [Obsidian RSS](https://github.com/joethei/obsidian-rss) allows users to create custom filtered folders and tag articles.
-   [Natural Language Dates v0.6.0](https://github.com/argenos/nldates-obsidian/releases/tag/0.6.0) added `@time` to the auto-suggest and is compatible with the new Live Preview and fully-compatible with mobile.
-   [Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/2.0.0) displays tags and aliases matched by queries.

### Betas

-   [Expiring Notes](https://github.com/joerncodes/obsidian-expiring-notes) lets users mark notes in your vault as expiring via a frontmatter date. After that date, they either get deleted or moved to a configurable archive folder, so ephemeral notes don’t clutter up your vault.

### For Developers

-   Here's a guide for [how to update your plugins and CSS for Live Preview](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/How+to+update+your+plugins+and+CSS+for+live+preview).
-   If your plugin uses `registerCodeBlockPostProcessor` then the new custom code block handling will work. If your plugin uses registerPostProcessor and finds the code block yourself then it won't.
-   There is now a `.is-live-preview` class on `div.markdown-source-view` which will allow you to differentiate live preview from source mode for CSS styling purposes (Thanks `@NothingIsLost`)
-   the new Live Preview mode changes the `pre.HyperMD-codeblock` element to a `div.HyperMD-codeblock`. This has been the case on mobile for awhile now but if you're seeing syntax highlighting issues with your themes in live preview, look out for any styles you have that may still reference `pre.HyperMD-codeblock` (Thanks `@NothingIsLost`)
-   Here's where `@argentum` discusses how she handled the [migration to CodeMirror 6](http://discordapp.com/channels/686053708261228577/840286264964022302/910526814177329193).
-   GitHub would love it if you enabled 2FA on your account[to help prevent stuff like the recent issues with npm security](https://github.blog/2021-11-15-githubs-commitment-to-npm-ecosystem-security/).

## Feature Requests

-   Discussion of [how Obsidian should handle merges](https://forum.obsidian.md/t/add-a-toggle-to-disable-automatic-merging-of-changes/14874) was resurfaced again this week.
-   There was a popular proposal for [rendering block references inline](https://forum.obsidian.md/t/a-proposal-for-rendering-block-references-inline/27093).
-   Some folks would really appreciate it if the [ZoteroRoam plugin](https://alix-lahuec.gitbook.io/zotero-roam/) was [ported to Obsidian](https://discord.com/channels/686053708261228577/840286264964022302/909658819880177664). This is the [functionality they care about most](https://www.dropbox.com/s/a3ktpw8wbexhdpq/Screen%20Recording%202021-11-15%20at%202.58.20%20pm.mov?dl=0), and it's worth noting they're willing to pay.

## Appearance

-   The [alternate checkboxes](https://github.com/SlRvb/Obsidian--ITS-Theme/blob/main/S%20-%20Checkboxes.css) css snippet now supports Live Preview & has better resizing.
-   Sanctum has admonition-esque checkboxes built in. Here's a [screenshot of how I use them](https://discord.com/channels/686053708261228577/744933215063638183/909883363505098853). Here are [the codes](http://discordapp.com/channels/686053708261228577/702656734631821413/909186409087246406).
-   [Ebullientworks](https://github.com/ebullient/obsidian-theme-ebullientworks) had some visual tweaks.
-   [Obsidian You 0.1.5](https://github.com/selfire1/obsidian-you-theme/releases/tag/0.1.4) got some title bar button settings and support for iOS safe area insets.
-   Spectrum 1.0.1 allows users to resize graph controls and comes with a bunch of snippets on [the repository](https://github.com/Braweria/Spectrum/tree/main/snippets).
-   Minimal [4.1.3](https://github.com/kepano/obsidian-minimal/releases/tag/4.1.3) adds support for new "Backlinks in document" feature (Obsidian v0.13.3).

## Ancillary Code

-   Here is a collection of [Dice Roller Tables](https://github.com/WychWitch/Obsidian-Dice-Roller-Tables) used to run DND campaigns
-   The [Word Count Dashboard](https://gist.github.com/chrisgrieser/ac16a80cdd9e8e0e84606cc24e35ad99#file-word-count-dashboard-md) using dataview.js got some updates and I believe now works with tags in addition to folders.

## Guides

-   Here's [a diagram of element classes](https://discord.com/channels/686053708261228577/744933215063638183/910295327213506580) originally created to help `@jdanielmourao` reorganize Sanctum's css.
-   This [guide for how to blog using Obsidian and Nextcloud and Gatsby](https://andri.dk/blog/2021/blogging-with-obsidian-gatsby-and-nextcloud) got resurfaced.

## Showcases

-   Here's a nice example of how to [use dataview as a research dashboard](https://discord.com/channels/686053708261228577/744933215063638183/909203223011811348).
-   Here's a twitter thread about [how to use Obsidian in conjunction with physical journals](https://twitter.com/anthonybaker/status/1459547762517688327).

## Knowledge Management

-   `@Necromant` [compiled the stand-out responses from Discord's history](http://discordapp.com/channels/686053708261228577/710585052769157141/910921442059759656) on the topic of [how people use tags](https://cdn.discordapp.com/attachments/710585052769157141/910921439417364560/Howpeopleusetags.jpg).
-   Here was an interesting discussion about how often people [create notes vs. surf notes](https://www.reddit.com/r/ObsidianMD/comments/qwvhhx/seasoned_obsidian_users_how_much_of_your_time_is/).

## In The Wild

-   CGP Grey had some nice things to say about Obsidian during [the State of the Apps](https://overcast.fm/+E7b7c7ryM/2:10:06). He talks about his writing workflow, how he’s switched over from Ulysses to Obsidian full time now, and had some lovely things to say about community plugins.
-   I wrote about [how Obsidian replaced video games and helped me publish](https://eleanorkonik.com/obsidian-replaced-games-now-prolific/).
-   Here's a video by `@nvanderhoeven` about how she uses [Obsidian for her work as a software engineer](https://www.youtube.com/watch?v=D7e1ud_Dk24).
-   A popular TTRPG DM, Sly Flourish, [covered Obsidian in his weekly talk show](https://www.youtube.com/watch?v=Dh1nybxv_vQ&t=235s).
-   A member of the community just finished up their PhD and thanked the Obsidian developers in [their thesis acknowledgments](https://discord.com/channels/686053708261228577/694233507500916796/911096399603593226). Congrats, `@Verma`!

## Ancillary Tools

-   Version 2.3 of the Alfred Workflow [Shimmering Obsidian](https://github.com/chrisgrieser/shimmering-obsidian#installation--configuration) features updated documentation, better spellcheck tuning, settings search, vault switching, improved workspace switcher, and a simplified setup.
-   Here's [how to convert .md files to .docx documents from android](https://forum.obsidian.md/t/how-to-convert-md-files-to-docx-documents-directly-from-your-android-phone/27326).

## Housekeeping

-   For clarity's sake, [CardBoard](https://github.com/roovo/obsidian-card-board) is the plugin that works like an alternate kanban board. [CorkBoard](https://github.com/jmilldotdev/obsidian-corkboard) is a Scrivener-esque corkboard view that functions as a visual canvas for Obsidian notes.
-   Normally, a premium membership for my history & fantasy fiction newsletter is $20/year, but I'm currently running a [25% off sale](https://newsletter.eleanorkonik.com/100-500) for the annual membership. I don't mention it often, but membership comes with .zip files of my actual working Obsidian vault backups. I remove obvious stuff like my taxes & copyrighted PDFs, but otherwise it's my actual setup, complete with all my notes into weird history, niche science, and how my fantasy stories connect with everything.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-11-20%20%20Live%20Preview%20Updates%2C%20Fancy%20Checkboxes%20and%20Tips%20for%20Devs.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-11-20%20%20Live%20Preview%20Updates%2C%20Fancy%20Checkboxes%20and%20Tips%20for%20Devs.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
