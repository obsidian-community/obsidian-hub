---
link: https://www.obsidianroundup.org/2022-07-16/
author: Eleanor Konik
published: 2022-07-16T12:30:00
publish: true
---

# 2022-07-16: Roadmap updates, OCR & Podcast notes
There were so many new guides and showcases I had to group them by topic: daily notes, dashboards, academic uses, links vs. folders, etc.

## In The Community

-   The [Obsidian Book Club videos](https://vimeo.com/danallosso) are live now.

## Obsidian Updates

-   [Obsidian v0.15.6](https://forum.obsidian.md/t/obsidian-release-v0-15-6/40227) has some important internal changes in this version, which brings popout windows out of Insider-only access and to all users. It's also designed to make the app feel more "native" on your operating system, which may have impacted your font. If you hate it and want the old font back, change the font to `Inter` in settings. I strongly recommend reading [the release notes](https://forum.obsidian.md/t/obsidian-release-v0-15-6/40227) if you haven't already. Here's a great [video about the value of the new popout windows feature](https://www.youtube.com/watch?v=TiVVFBhkJU4).

Also, the [roadmap](https://trello.com/b/Psqfqp7I/obsidian-roadmap) was updated. Here's some of the major news and highlights.

-   `@kepano`, the developer of Minimal, is working on a new "default theme" for Obsidian. He said it "will follow many of the same design principles as Minimal, particularly in making Obsidian feel native across platforms. It will differ in that it will prioritize accessibility and affordances more than Minimal does. In addition the new default theme will make customization and theme development easier than before."
-   The developers are working on implementing "tabs" and plan to implement some kind of corkboard/whiteboard core plugin as the next big "push" after that.

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list._ For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new).

-   [TimeDiff plugin](https://github.com/dominiczaq/obsidian-plugin-time-diff) by `@dominiczaq`  will calculate and displays diff in hours and minutes between two dates in a `timediff` markdown block.
-   [Metadata Menu](https://github.com/mdelobelle/metadatamenu) by `@mdelobelle`  adds options to file and link context menu to change metadata of the target note. It also allows for autocomplete of frontmatter and dataview fields. Here's [a demo](https://youtu.be/mqua0rloDLE).
-   [Typing Transformer](https://github.com/aptend/typing-transformer-obsidian) by `@aptend` offers improved, configurable auto formatting as you type.
-   [Text Expander JS](https://github.com/jon-heard/obsidian-text-expander-js) by `@jon-heard`  lets users type text shortcuts that expand into javascript generated text.
-   [Habit Tracker](https://github.com/Narsail/habit-tracker-obsidian) by `@Narsail`  makes it easier to visually track completion of habituated actions.
-   [List Callouts](https://github.com/mgmeyers/obsidian-list-callouts) by `@mgmeyers`  allows users to create simple callouts in lists.

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [New Note Plus](https://github.com/ilucaslee/obsidian-new-note-plus) by `@ilucaslee`  offers a a new URL Scheme to create new notes using clipboard contents.
-   [MOV Support](https://github.com/connectdotz/obsidian-mov-support) by `@connectdotz`  lets users view/play embedded .mov videos inline.
-   [Commander](https://github.com/phibr0/obsidian-commander) by `@phibr0`  lets users customize a workspace by adding commands everywhere.
-   [Meeting notes](https://github.com/TimHi/obsidian-meeting-notes) by `@TimHi`  will automatically create a meeting note if a new file is created in a meeting folder.
-   [Table Generator](https://github.com/Quorafind/Obsidian-Table-Generator) by `@Quorafind`  allows users to generate markdown tables quickly and works like Typora.
-   [Focus and Highlight](https://github.com/nagi1999a/obsidian-focus-plugin) by `@nagi1999a`  will highlight and focus on the currently selected heading.
-   [Eagle Embeds](https://github.com/fengxxx/obsidian-eagle-embeds) by `@fengxxx`  replaces Eagle links (mostly images) with embeds when previewing a file.
-   [Path Finder](https://github.com/jerrywcy/obsidian-path-finder) by `@jerrywcy`  will find the shortest path between two notes.
-   [Ninja Cursor](https://github.com/vrtmrz/ninja-cursor) by `@vrtmrz`  enhances cursor visibility.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

-   [Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/5.3.0) now has a "create" button when no results are found in the switcher.
-   [Local Quotes 1.8.0](https://github.com/ka1tzyu/local-quotes) comes with [improved documentation](https://ka1tzyu.github.io/local-quotes/).
-   A bunch of [Hover Editor](https://github.com/nothingislost/obsidian-hover-editor/releases/tag/0.11.0) updates are now out of beta and available for everyone. It should play nicely with the new Popout Windows.
-   [Pane Relief](https://github.com/pjeby/pane-relief/releases/tag/0.2.1) has a new feature to allow users to "lock" the focus to non-sidebar-panes.
-   [Note Auto Creator v1.2.0](https://github.com/SimonTC/obsidian-note-autocreation/releases/tag/1.2.0) supports searching for existing notes by alias, lets users disable suggestions for non-existent notes, and supports linking to headers in existing notes.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   [Obsidian OCR](https://github.com/MohrJonas/obsidian-ocr) allows users to search for text in the images and PDFs in a vault. I haven't had a chance to test it yet but I'm _very_ excited; this is a feature I've been hoping for for a long time. Here's a [showcase of how it works](https://www.reddit.com/r/ObsidianMD/comments/vvqfqj/presenting_obsidian_ocr/).
-   [Podnotes](https://github.com/chhoumann/PodNotes) is a new plugin from the developer of QuickAdd that is designed to make it easier to take notes on podcasts; it turns Obsidian into a podcast player, and works on mobile and computer, saves progress on the episodes, and lets you use plugins like QuickAdd or Templater to create notes and capture insights with linked timestamps that can launch the podcast from the appropriate moment for a re-listen.

### For Developers

-   Here's a guide for [how to update your plugin to support pop-out windows](https://forum.obsidian.md/t/plugin-developers-how-to-update-your-plugin-to-support-pop-out-windows/40228).
-   Here's a Discord discussion about the [value of API usage examples](https://discord.com/channels/686053708261228577/840286264964022302/996107444331753473); if you have any thoughts about how this could be useful in the Obsidian development ecosystem, please share!
-   The developer of [Buttons](https://github.com/shabegom/buttons) has been slammed with real-life-work stuff and is looking for help triaging some of the bug reports.
-   If anyone is interested in [taking over the day planner plugin maintenance and updating it so it works on new Obsidian builds](https://github.com/lynchjames/obsidian-day-planner) it would [be appreciated](https://discord.com/channels/686053708261228577/707816848615407697/991622417590001684).

## Feature Requests

-   It would be nice if [fold state synced between devices](https://forum.obsidian.md/t/preserve-heading-indent-foldings-on-desktop-after-file-is-edited-on-mobile-and-vice-versa/34998/2) so if you, for example, folded half the headings on your daily note on your desktop device, when you opened the note later on your iPad they would remain folded.
-   I also wish we could have [improved block treatment when it comes to lists](https://forum.obsidian.md/t/treat-lists-as-blocks-for-better-querying/40219)...
-   Here's an idea for [note previews in the file explorer](https://forum.obsidian.md/t/plugin-for-3-pane-file-explorer-with-note-previews/40361) without needing to hover.

## Appearance

-   [Encore](https://github.com/Maldonacho/obsidian-encore-theme) by `@Maldonacho`  is new.
-   [Ebullientworks](https://github.com/ebullient/obsidian-theme-ebullientworks) 0.3.27 better supports sliding panes and popout windows, and got a bunch of small improvements to heading heights, callouts, etc.
-   [Sanctum](https://github.com/jdanielmourao/obsidian-sanctum) got a _bunch_ of bug fixes. Sanctum is going to be [changing how it handles releases](https://discord.com/channels/686053708261228577/855181471643861002/996848211513847809) going forward (Discord link) to align more closely with Obsidian updates — you can check out [the Roadmap here](https://github.com/users/jdanielmourao/projects/1/views/4) in the meantime.

## Showcases & Guides

-   Here's a new roundup of resources for using [Obsidian for religious uses](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/for+Religious+Uses) via the community hub, and here are some new methods for [Bible study in Obsidian](https://forum.obsidian.md/t/introducing-kingdom-study-tools-for-obsidian/40394/2) that I hope to get added to that list soon. If you'd like to help, join us in the `#hub` channel on [Discord](https://discord.gg/veuWUTm) :)
-   Here's a wonderful story about how [Obsidian helped an author facing chronic illness cope with brain fog](https://irarobinson.substack.com/p/this-program-has-cleared-my-brain), complete with screenshots of their methods and templates.
-   Here's an example from Discord about [how to make color swatch tables in Obsidian](https://discord.com/channels/686053708261228577/744933215063638183/996077949600153620).
-   Here's a [new list of public digital gardens](https://lukerambling.de/gardens/).
-   Here's a template from Discord that can be used for [weekly review](https://discord.com/channels/686053708261228577/965681451297304596/996962701970522232), and a nice example of [daily notes in Obsidian](https://agileadam.com/2022/07/obsidian-daily-note-implementation-v2/) with an accompanying [discussion from Reddit](https://www.reddit.com/r/ObsidianMD/comments/vz2mw5/my_latest_daily_notes_implementation_link_to_blog/). There was also an example of a [daily development log](https://publish.obsidian.md/manuel/Logs/Dev/Dev+Log+2022-07-09), which comes complete with a whole public vault to explore. I imagine this would be extremely useful for developers to check out, in particular. There's also this [comprehensive guide to daily notes](https://thebuccaneersbounty.wordpress.com/2022/01/05/how-i-use-the-daily-notes-plugin-a-comprehensive-guide/).
-   Here's a [practical tutorial for Academic writing](https://universvm.medium.com/obsidian-tutorial-for-academic-writing-87b038060522) including Zotero highlights and word citations, with an [accompanying discussion](https://www.reddit.com/r/ObsidianMD/comments/vy1e62/i_wrote_a_practical_obsidian_tutorial_for/). There was also a roundup of [Obsidian hacks and tips](https://www.reddit.com/r/ObsidianMD/comments/vz2wah/what_is_your_obsidian_hack_tip_or_feature_you/) via Reddit, along with one method for [using Obsidian as a university student to take lecture notes](https://forum.obsidian.md/t/university-setup-with-lecture-notes-progress-bar-and-more-using-templater-dataview-and-buttons/32094).
-   Here's a video about how to [build a personal project dashboard](https://www.youtube.com/watch?v=jL3q71EM42M), and another one about [creating a home note dashboard](https://thesweetsetup.com/creating-obsidian-dashboard/) in general, and another one for [how to create a movie database](https://www.youtube.com/watch?v=t-hKCgGhQuk).
-   Here's Nicole van der Hoeven answering a bunch of Obsidian-related and other questions over on YouTube, including about [Templater, daily notes, and email processing](https://www.youtube.com/watch?v=3HsZm5owieg).
-   Here's a guide to [using Obsidian's graph view effectively](https://www.youtube.com/watch?v=cW8F1HYe_cA), here's one for [using the kanban plugin](https://www.youtube.com/watch?v=sjJgKMxOZ5k), and here's one on how to [use inline Dataview fields to visualize connections with ExcaliBrain](https://www.youtube.com/watch?v=haGAfc9QUuA).
-   Here's a discussion about [how to get dataview to return multi-line quotes](https://discord.com/channels/686053708261228577/710585052769157141/995881770782306304).
-   Here's a method for [mapping arguments using mermaid](https://twitter.com/Cedric_Eyssette/status/1544599827035602944), which works in Obsidian.

## Discussions

-   Here's a discussion about [using fly.io for livesync](https://github.com/vrtmrz/obsidian-livesync/discussions/85) that is looking for more involvement.
-   Here's a nice Discord discussion of [why the query control plugin is useful](https://discord.com/channels/686053708261228577/744933215063638183/995155821371596931); it facilitates making the daily note experience closer to what you'd find in an outliner like Logseq, including "tag pages" that are fully rendered, etc.
-   Here's a discussion about [the value of linking](https://www.reddit.com/r/ObsidianMD/comments/vxzoln/after_a_year_of_trying_i_just_dont_see_the_value/) that had a lot of nice insights and examples. There was also some interesting discussion about [possible implementations of allowing links to folders, not just files](https://forum.obsidian.md/t/allow-links-to-folders/874/30). Incidentally, how [using folders in Obsidian doesn't bind you to the limitations of folders at the file-system level, but does add future-proofing](https://discord.com/channels/686053708261228577/710585052769157141/997269995446870056) was full of useful insights, and this was a nice reflection on the value of [using the Johnny Decimal system with Obsidian](https://medium.com/produclivity/using-johnny-decimal-with-obsidian-solved-all-my-organising-woes-68c8c5c3dcc9).

## Ancillary Tools

-   Here's a neat free and open-source tool for [managing research photos](https://tropy.org/) and their metadata.

## Housekeeping

-   It's official; I'm headed back to work in August. My first day is August 15, and students return on the 29th. I'll be teaching 11th grade World History, which is a pretty good fit for my interests and skills and better than I was afraid I'd get. It will be fun figuring out how to best use Obsidian to learn a new content area while working in a field where I have to collaborate using Office and Google products, for varying measures of fun. The Obsidian Roundup itself will continue as normal, but I will by necessity be somewhat less active on social media going forward.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-07-16%20Roadmap%20updates%2C%20OCR%20%26%20Podcast%20notes.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-07-16%20Roadmap%20updates%2C%20OCR%20%26%20Podcast%20notes.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
