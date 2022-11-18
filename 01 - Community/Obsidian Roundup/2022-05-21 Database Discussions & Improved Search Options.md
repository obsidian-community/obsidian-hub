---
link: https://www.obsidianroundup.org/2022-05-21/
author: Eleanor Konik
published: 2022-05-21T12:30:00
publish: true
---

# 2022-05-21: Database Discussions & Improved Search Options
Leverage markdown's semantic line break features with help from a new plugin, or check out the new guide for using Zotero6 with Obsidian.

## Obsidian Updates

As of [Insider v.0.14.11](https://forum.obsidian.md/t/obsidian-release-v0-14-11-insider-build/37580).

-   You can now move or delete multiple selected items via the right-click context menu in the File Explorer. (which for me personally is a huge deal)
-   The backslash escape character will now be hidden when your cursor is not on the same line in Live Preview.
-   When exiting in-document search, the last searched result will be selected automatically.

And [Mobile Insider v1.2.2](https://discord.com/channels/686053708261228577/817515900349448202/975796883610009631)...

-   Includes all new functionality and bug fixes up to Obsidian Desktop v0.14.10.
-   Fixed rename vault functionality gets stuck.
-   You can now setup Obsidian Sync right from the starting screen.

## Plugin News

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Semantic Line Breaker](https://github.com/chrisgrieser/obsidian-sembr) by `@chrisgrieser`  lets users apply and remove Semantic Line Breaks (SemBr). Here's a [discussion about why they're useful](https://discord.com/channels/686053708261228577/805952223124520961/976590646150324304).
-   [RequireJS](https://github.com/cstrahan/obsidian-requirejs) by `@cstrahan`  makes it easy to write reusable JavaScript code using ReactJS.
-   [Media DB Plugin](https://github.com/mProjectsCode/obsidian-media-db-plugin) by `@mProjectsCode`  can query multiple APIs for movies, series, anime, games, music and wiki articles, and import them into your vault.
-   [Image Gallery](https://github.com/lucaorio/obsidian-image-gallery) by `@lucaorio`  makes it easier to get a masonry image gallery for Obsidian
-   [Sequence Hotkeys](https://github.com/moolmanruan/obsidian-sequence-hotkeys) by `@moolmanruan`  allows users to set hotkeys with key sequences instead of a single chord.
-   [Note Auto Creator](https://github.com/SimonTC/obsidian-note-autocreation) by `@SimonTC`  will automatically create notes when links are created to them.
-   [Packrat](https://github.com/therden/packrat) by `@therden`  adds functionality to Obsidian Tasks plugin to process recurring tasks to the bottom of the active note file, append the task to a designated archive file, or delete the task since it's done.
-   [State Switcher](https://github.com/lijyze/obsidian-state-switcher) by `@lijyze`  adds a modal / graphical dropdown menu for changing a value in your YAML to keep you from making mistakes.
-   [Better Audio Recorder](https://github.com/salmund/obsidian-better-audio-recorder) by `@salmund`  allows users to pause and resume recordings.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

-   [Notion Like Tables](https://github.com/trey-wallis/obsidian-notion-like-tables/releases) got Live Preview support. The `#` symbol is now optional for tags. The textarea box now changes size as you type, and there are a bunch of other small fixes along those lines.
-   [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases) got an improved collaborative experience.
-   [Linter](https://github.com/platers/obsidian-linter/releases) has a demo gif, some new options for folder linting, and more. This is a heartwarming update because there are a bunch of contributors to the plugin.
-   [Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases) lets users star recent search & see the full path of the directory.
-   [Advanced Slides 1.12.0](https://github.com/MSzturc/obsidian-advanced-slides) added support for the emoji shortcodes plugin, but also templates, embeds and layouts are now more stable in interaction with each other.
-   For [Database folder v1.1.0](https://github.com/RafaelGB/obsidian-db-folder/releases/tag/1.1.0), calendar columns exist now. They support time select. The text columns allow Obsidian links.
-   [Obsidian List Modified](https://github.com/franciskafieh/obsidian-list-modified/releases/tag/1.1.4) (a plugin that links modified files to your daily note) now creates your daily note automatically if it does not exist.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   [Omnisearch 1.3.0-beta](https://github.com/scambier/obsidian-omnisearch/releases/tag/1.3.0-beta) added support for Chinese, a Settings page for tweaking how results are weighted, and improved indexing.
-   [Codeblock Completer](https://github.com/SkepticMystic/codeblock-completer) works better with the Codeblock Labels plugin and allows you to ignore certain codeblock types, so that they don't appear in the suggester options.

## Feature Requests

-   It would be neat if we could [push content to newly created file](https://forum.obsidian.md/t/push-content-to-link-automatically-apply-tags-links-embeds-into-newly-created-links-through-link-insert-content/36844), i.e. `automatically apply #tags, [[links]], ![[embeds]] into newly-created [[links]] through “[[link]]>>{insert content}”`
-   It would be nice if we could [assign commands to bare function keys](https://forum.obsidian.md/t/be-able-of-using-the-function-keys-f1-f12-to-perform-functions/15748/9).
-   Oh hey I'm not the only one who wishes we could [search text in PDFs](https://forum.obsidian.md/t/search-text-in-pdfs/511) from inside Obsidian.

## Appearance

-   Here's a css snippet using the Minimal card view css. You can use it to [enable card view with any theme you like](https://discord.com/channels/686053708261228577/744933215063638183/972334987133202522), and make notes look like index cards. Just include cssclass: zettelkasten in the YAML section.

## Ancillary Code

-   Here's a dataview query that [pulls all notes created or modified on the same day](https://gist.github.com/therealfakemoot/5d40568631136c12fb63440ddde11677) as "current" note.
-   Here's a neat way to make sure template [frontmatter doesn't get picked up and indexed](https://twitter.com/TfTHacker/status/1521444266446311424), as long as you're using Templater plugin.

## Discussions

-   There's a useful discussion about [ways to integrate handwritten notes into your vault](https://www.reddit.com/r/ObsidianMD/comments/us0dbx/taking_handwritten_notes_and_importing_them_to/).
-   [Dataview made it to the front page of HackerNews](https://news.ycombinator.com/item?id=31407781), which led to a pretty robust discussion. I recognize some of the community members involved, and think the conversation about user-friendly query languages is worth checking out if you're into that kind of thing.
-   Here is [a template folder structure and file-naming convention](https://discord.com/channels/686053708261228577/805952223124520961/976197753728278529) for structuring fiction notes.
-   Here's a discussion of [what academics put in their YAML](https://discord.com/channels/686053708261228577/722584061087842365/975508104437465128).
-   Here's a lengthy collection of [example workflows in Obsidian](https://forum.obsidian.md/t/example-workflows-in-obsidian/1093).

## Knowledge Management

-   Here's a really nifty article about [annotation](http://patthomson.net/2022/05/16/everyday-acts-of-annotation/), not specific to Obsidian.
-   [The opposite collector's fallacy](https://technosoof.wordpress.com/2020/05/23/the-opposite-collectors-fallacy/) & [antilibrary](https://www.themarginalian.org/2015/03/24/umberto-eco-antilibrary/) articles came up in conversation in Discord, and make for interesting reads.

## Showcases & Guides

-   Here's how to [use Obsidian and iOS Shortcuts (+Drafts) to automate a daily podcast log](https://leahferguson.com/blog/obsidian-overcast-daily-podcast-log/).
-   Here's a neat showcase of how someone uses Dataview and Book Search to [track books](https://www.reddit.com/r/ObsidianMD/comments/usgl1m/tracking_books_in_obsidian_with_dataview_book/).
-   This adorable [parrot management system](https://www.reddit.com/r/ObsidianMD/comments/uqovz7/parrot_management_pm_system_using_obsidian/) is not to be missed.
-   This [snapshot of college radio stations](https://twitter.com/kramermj/status/1526990230095646720) was created using Obsidian and it's super interesting to see all the many ways the app can be used.
-   Here's how Katrina Moody [uses Obsidian for fiction writing](https://twitter.com/KatrinaMoody/status/1526980274219024384).
-   Here's all the ways Mike Schmitz [uses Obsidian](https://twitter.com/_MikeSchmitz/status/1526918986230816771) (33k plaintext notes!)
-   This list of [useful resources for TTRPG players](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/for+TTRPG) is really handy.

## Ancillary Tools

-   Here are directions for [a new Zotero-Obsidian workflow](https://publish.obsidian.md/history-notes/From+Zotero+Annotations+to+Obsidian+Research+Notes) (aimed at students). It uses Zotero Desktop Connector with Zotero 6 annotations instead of Zotfile. You lose a few options of the ZDC-Zotfile workflow but all the basic features work just fine and you need fewer plugins. (The niche parts are directions for historians in the workflow.)
-   There's a developer trying to gauge interest in a [search engine for your notes](https://www.reddit.com/r/ObsidianMD/comments/uqvsir/ive_built_a_search_engine_that_connects_to_your/) and the discussion had some interesting alternatives to their project mentioned.
-   Here's a [free and open source alternative to Obsidian Publish](https://mindstone.tuancao.me/).
-   Github is [considering adding support for note & warning callouts](https://github.com/github/feedback/discussions/16925). They're considering different syntax options; here's the [comment encouraging them to use the same syntax as Obsidian and Microsoft Docs](https://github.com/github/feedback/discussions/16925#discussioncomment-2794263=) if you'd like to upvote or add feedback.  

## Housekeeping

-   If anyone had questions I didn't get a chance to answer during my presentation about taking notes without plugins or themes during the LYT Conference, check out [this thread](https://twitter.com/EleanorKonik/status/1526653928485560321) on Twitter.
-   My article about [notes bound by time and location](https://www.obsidianroundup.org/on-notes-bound-by-time-and-location/) was sent to financial supporters this week. It's about the importance of being specific, aware of your biases, keeping track of your sources, and breaking down information into its component parts for easier remixing.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-05-21%20Database%20Discussions%20%26%20Improved%20Search%20Options.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-05-21%20Database%20Discussions%20%26%20Improved%20Search%20Options.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
