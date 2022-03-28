---
link: https://www.obsidianroundup.org/2022-01-22/
author: Eleanor Konik
published: 2022-01-22T13:30:00
publish: true
---

# 2022-01-22: API improvements for devs & Reference vs. Reflection usage
Workflow explanations, including a series about migrating from Evernote by the original "paperless ambassador." Plus: upcoming monthly essays from me

## In The Community

-   The next [4-week Book Club](https://www.youtube.com/watch?v=19_QNqBQ6LE) hosted by Dan Allosso will take place in February. It'll be focused on note-taking workflow and will cover _How to Take Smart Notes_ and a couple of Zettelkasten articles.

## Obsidian Updates

desktop Insiders v[0.13.20](https://forum.obsidian.md/t/obsidian-release-v0-13-20-insider-build/30790) & [.21](https://forum.obsidian.md/t/obsidian-release-v0-13-21-insider-build/30799) fixed a _bunch_ of bugs and got the following improvements:

-   The new editor now supports the `cssclass` frontmatter property.
-   Live Preview will now detect whether the editor is focused to apply syntax hiding.
-   Community plugin search filter will now also match by author.
-   Added shortcuts for plugin settings and hotkeys in the community plugins list

mobile Insider v1.1.0 (Build 35) was mostly a feature update to get mobile up to parity with desktop v0.13.21. Specifically, the mobile Insider now supports:

-   Drag and drop by long-holding (files and folders, starred, outline pane)
-   Long holding to view the image full-screen.

## Plugin News

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Core Search Assistant](https://github.com/qawatake/obsidian-core-search-assistant-plugin) by `@qawatake`   enhances the built-in search by offering a keyboard interface, card preview, & bigger preview.
-   [Dynamic Highlights](https://github.com/nothingislost/obsidian-dynamic-highlights) by `@nothingislost`   highlights text based on cursor selection or search query with full regex, mobile, and live preview support.
-   [Weather Fetcher](https://github.com/fyears/weather-fetcher) by `@fyears`   will fetch and insert current weather into the editor.

### Updates

-   [Auto Link Title](https://github.com/zolrath/obsidian-auto-link-title) got fixed! 1.2.5 integrates a bunch of community fixes so now it doesn't overwrite data anymore. I am _very_ excited for this one, it's like having an old friend back :)
-   [QuickAdd](https://github.com/chhoumann/quickadd) now supports multi-line inputs.
-   [Ledger](https://github.com/tgrosinger/ledger-obsidian/releases)  now supports editing existing transactions. You can also now add comments to a transaction and have multiple splits.
-   [Advanced Tables](https://github.com/tgrosinger/advanced-tables-obsidian/releases) will no longer try to format tables that are in code blocks or math blocks. It also now ignores tables that are preceded by -tx- so it plays nice with [Table Extended](https://github.com/aidenlx/table-extended)
-   [File Tree Alternative](https://github.com/ozntel/file-tree-alternative/releases/tag/1.7.5) now includes an additional button to `Reveal Active File` within the plugin's file tree. There's also a new custom event handler, which you can trigger programmatically in case you would like to customize.
-   [Supercharged Links](https://github.com/mdelobelle/obsidian_supercharged_links) version 0.4.2 now properly targets styled dataview inline fields. [0.4.4](https://github.com/mdelobelle/obsidian_supercharged_links) supports the recent files plugin, properly unloads styling in panes, and instantly applies styling to the file browser.
-   [Table Extended v1.6.0](https://github.com/aidenlx/table-extended/releases/tag/1.6.0) introduced experimental export to pdf support for `-tx-` tables.
-   [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.5.17) added a new font and fixed hover previews link.
-   [Remotely-Save](https://github.com/fyears/remotely-save) adds support for scheduled auto-sync and new sidebar ribbon icons.
-   [Memos 1.2.0](https://github.com/Quorafind/Obsidian-Memos/releases/tag/1.2.0) lets users use `@` to get a date picker and now has a translation module. [1.3.0](https://github.com/Quorafind/Obsidian-Memos/releases/tag/1.3.0) supports file suggest, task switching, date formats, and more. 1.4.3 added a button and bottom mode for mobile. It's up to [1.6.1](https://github.com/Quorafind/Obsidian-Memos/releases/tag/1.6.1) now and got a number of features.
-   As of 0.4.7, [Tag Wrangler](https://github.com/pjeby/tag-wrangler/releases/tag/0.4.7) will no longer reformat metadata fields or comments that don't contain changed tags.
-   [Obsidian Linter 1.2.9](https://github.com/platers/obsidian-linter/releases/tag/1.2.9) has improved performance on large notes, and a new rule: `remove-empty-list-markers`
-   The [Imgur plugin](https://github.com/gavvvr/obsidian-imgur-plugin/releases/tag/2.1.1) has been fixed to support the new editor.
-   The [Raycast](https://github.com/marcjulianschwarz/obsidian-raycast) extension has new shortcuts for searching and a new command for creating notes, with a tag picker and folder structure support.
-   [Chessboard 0.5.0](https://github.com/THeK3nger/obsidian-chessboard/releases/tag/0.5.0) allows users to rotate the chessboard.
-   [Linked Data Vocabularies](https://github.com/kometenstaub/obsidian-linked-data-vocabularies) now supports the opening of selected headings in the browser.
-   [AnkiBridge 0.6.0](https://jeppeklitgaard.github.io/ObsidianAnkiBridge) works with Live Preview now, and got a bunch of new documentation, but includes a breaking change that will require a migration (which is well-documented).

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   [Breadcrumbs 2.40.1](https://github.com/SkepticMystic/breadcrumbs/releases/tag/2.40.1) has support for implied relationships. You can learn more about [how it works](https://discord.com/channels/686053708261228577/929513881041248266/933451283464085527) in the `#breadcrumbs` thread on Discord.

### For Developers

-   There's a new discord channel for theme/CSS development, called `#appearance-dev`
-   If you haven't seen the [developer resources on the Hub](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/for+Plugin+Developers) you should definitely check them out. There's even a neat list of what tools and libraries are used by Obsidian.

Also, from the v0.13.20 Insider:

-   Fixed sometimes empty duplicate `<span>` elements show up before or after widgets, causing issues when using css padding or :before/:after.
-   The debug info command now includes the OS information.
-   There is now a new `editorLivePreviewField: StateField<boolean>` that can be used to check whether Live Preview is enabled in the editor.
-   Fixed out-of-bound `{line,ch}` pairs causes error with new editor
-   Introduced `apiVersion: string` and `requireApiVersion(version: string): boolean` to help with API version requirements. Plugin authors can use this function to limit functionality that depends on new Obsidian APIs to avoid crashing on older versions of Obsidian.

## Feature Requests

-   Some folks would like the [file deletion dialog to be a bit nicer](https://www.figma.com/file/nhRMHagfyuiLrhmnSPPk0j/Obsidian---Delete-file-dialog?node-id=0%3A1).
-   Wouldn't a [quick switcher for themes](https://forum.obsidian.md/t/quick-theme-switcher/30952) be nice?

## Appearance

-   [LYT Mode](https://github.com/nickmilo/LYT-Mode) is officially available now.
-   [Ebullientworks 0.3.0](https://github.com/ebullient/obsidian-theme-ebullientworks/blob/main/tasks-snippet.css) spun out bullet journal style alternative checkbox styles into a snippet that works with the default theme. Sanctum style [custom checkboxes](https://github.com/jdanielmourao/obsidian-sanctum/blob/main/snippets/Sanctum%20Custom%20Checkboxes.css) are also available as a snippet.
-   [Minimal 4.4.2](https://github.com/kepano/obsidian-minimal/releases/tag/4.4.2) has support for cards and table helpers in Live Preview. 4.4.3 improved stylings and got a bunch of fixes.

## Ancillary Code

-   Here's a script from Nicole van der Hoeven to [prioritize reading material](https://twitter.com/n_vanderhoeven/status/1482744465605505026).
-   Here's a [tutorial for how to use templater's javascript scripts](https://shbgm.ca/obsidian/docs/how-to-use-templater-js-scripts)
-   The [Alfred Workflow](https://github.com/chrisgrieser/shimmering-obsidian) for Obsidian now has a scratchpad, support for the BRAT plugin, features for developers, easier installation, and a bunch of other things. Here's a [reddit discussion](https://www.reddit.com/r/ObsidianMD/comments/s4dzul/obsidian_shimmering_obsidian_alfred_workflow/) of people talking about how helpful it is.
-   Here's a script to [fetch video game data](https://www.reddit.com/r/ObsidianMD/comments/s7fsfd/a_script_for_quickadd_plugin_to_fetch_video_game/) using QuickAdd.

## Discussions

-   Approximately eleven billion people bookmarked this Discord [discussion of how to decide between focusing on using Obsidian for references or reflection](https://discord.com/channels/686053708261228577/710585052769157141/932183110261567528) and methods for annotating and creating literature notes.
-   Here's an extensive discussion about [whether Obsidian Sync is worth it](https://www.reddit.com/r/ObsidianMD/comments/s7u7p5/people_who_use_obsidian_sync_whats_it_like_and_is/) from Reddit (a community that tends to be very anti-spending-money, for what it's worth).

## Showcases & Guides

-   I wrote a bit about my recent [refactor of how I organize my articles and tags](https://twitter.com/EleanorKonik/status/1483158511710318592).
-   Here's how Mark McElroy uses [Readwise](https://readwise.io/i/ac9) & Obsidian to [prompt a morning journaling process](https://twitter.com/markmcelroy/status/1482383447595364355)
-   Here's Curtis McHale on [9 plugins writers should check out](https://curtismchale.ca/2022/01/10/9-obsidian-writing-plugins/).
-   Here's Misha on how to [use Obsidian daily notes to support a creative workflow](https://www.mishacreatrix.com/obsidian-daily-note-2022).
-   Here's Nadja showcasing her [personal knowledge management system and daily driver maps of content](https://www.youtube.com/watch?v=rbYQdeNND5g) via Linking Your Thinking.
-   Here's a really great twitter thread about [how managers to can use Obsidian to have more confidence in their decision-making](https://twitter.com/jevy/status/1483767557228273669).
-   Here's a nice video about how to [use Obsidian for academic work](https://youtu.be/4T0q2kQwc2o), including a section on how Evan uses the graph view.
-   This [showcase of different graph clusters](https://lmy.medium.com/a-tour-to-my-zettelkasten-notes-dc26a75e5257) in someone's 2 year old vault did really well in Hacker News.
-   [Personal Knowledge Management: How to Choose the Right System for You](https://denisetodd.medium.com/personal-knowledge-management-how-to-choose-the-right-system-for-you-dfd84c254520) by Denise Todd is from the perspective of a former Roam user who now uses Obsidian.
-   There's a new [Zotero / bibnotes workflow explanation](https://discord.com/channels/686053708261228577/722584061087842365/933568877756030996) available that I think is intended for the Zotero beta.
-   [How to export web articles' highlighted sentences into Obsidian](https://medium.com/glasp/tutorial-how-to-export-web-articles-highlighted-sentences-into-obsidian-25d63285bcb9)
-   Here's how you can [use latex efficiently for even live lecture notes](https://castel.dev/post/lecture-notes-1/)
-   Here's a weekly blog series on Jamie Rubin's [migration to Obsidian from Evernote](https://jamierubin.net/blog-series/practically-paperless-with-obsidian/) He's known for being Evernote's "paperless ambassador" about ten years back. He also had some [great tips](https://www.reddit.com/r/ObsidianMD/comments/s98i0a/practically_paperless_with_obsidian/) over in the Reddit discussion.

## Small Tips

-   If you mark a codeblock as ```poetry (or prose) it'll use black instead of red text.

## Ancillary Tools

-   The PDF to markdown conversion over at [Scholarcy](https://mobile.twitter.com/scholarcy/status/1482044752073838593) supports tables, including tables that are split across pages. It's still in alpha, but if you're one of the many obsidian users who enjoys spaced repetition and flashcards to help parse academic research, they have an AI for that.
-   The static site generator [eleventy](https://www.11ty.dev/) (useful to host notes as an alternative to publish, Hugo, or Jekyll), just had their 1.0 release.  [Zola](https://www.getzola.org/) got mentioned as an alternative.

## Housekeeping

I'm working on moving my articles about Obsidian over from my personal blog to the Obsidian roundup. If you follow the Roundup vs RSS, your feeds might "push" these to you in bulk, depending on whether the reader respects publication-dates. If you get an email from me that is a longform article, it will be because I messed up the button in the Ghost interface. Sorry!

This is happening because I'm shuttering my blog at eleanorkonik.com over the next few weeks. For a variety of reasons, it's time for eleanorkonik.com to be more of a landing page and less of a blog. Old links should redirect to new homes for all the articles by the time I'm done. Essays related to Obsidian & knowledge management will be hosted here, stuff about worldbuilding & history is getting moved to [The Iceberg](https://newsletter.eleanorkonik.com/tag/article/) newsletter.

As part of this, **I will start sending out at least one essay edition a month to the wonderful people who have supported the Roundup financially**. It will probably ship on the third Thursday of the month, because I do really well with recurring deadlines like that. If you prefer not to get those in your inbox, I plan to pre-pend all the titles with an 🌲emoji, to help with filtering.

If you _do_ want a monthly essay from me about stuff like productivity, notetaking, my perspectives on tools other than Obsidian that are nonetheless relevant to our community, folders vs. namespacing, how to actually _use_ some of the new plugins I tell you about, when to use tags vs. metadata, etc...

💚

Grab a [membership](https://www.obsidianroundup.org/membership/) and hold onto your hats. If I can convince about 1/3rd of you that supporting my insights & efforts is worthwhile, I can afford not to go back to work in the fall when my maternity leave ends. 2/3rds would almost replace my lost income 😅 but that seems like aiming high.

You may have heard me talk before about how much I love teaching, and how I wasn't planning to quit teaching to write. It was true at the time — because I _do_ love teaching. But the fact of the matter is, I haven't heard a single reassuring thing from colleagues about the pandemic's impacts on my school district. Besides, as one of my fellow moderators pointed out: I love _teaching_ — not just teaching children.

As I approach a million words of notes in my vault, I realize that I have a _ton_ of things I want to say. Things I've been scared to commit to, because I knew I'd have to scale back when the new school year comes. I have thoughts about the discourse surrounding personal knowledge management that I've been holding off on sharing because I thought it would be better not to start something I wouldn't be able to continue.

Tens of thousands of words worth of thoughts are about productivity and notetaking and leveraging Obsidian. A lot of it never quite felt "right" as something as static as a book in the quick-changing world of Obsidian plugins (although I do plan to ship my nonfiction book once my kid starts daycare full time 👀).

After weeks of self-reflection, it turns out that want — very badly — to be able to produce more of the kind of work that led you all to vote me [Content Creator of the Year for the Obsidian community](https://forum.obsidian.md/t/obsidian-gems-of-the-year-2021-voting/28759) (!)

With your help, I can.

[SUPPORT MY WORK](https://www.obsidianroundup.org/membership/)

PS: Subscription prices gets locked at the moment you sign up. It's possible that I'll increase the price of new subscriptions if I start doing things like office hours, or weekly essays instead of monthly.

& don't worry — even if I do have to go back into the school building, this newsletter will continue to exist. The Roundup itself will always be free.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-01-22%20API%20improvements%20for%20devs%20%26%20Reference%20vs.%20Reflection%20usage.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-01-22%20API%20improvements%20for%20devs%20%26%20Reference%20vs.%20Reflection%20usage.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
