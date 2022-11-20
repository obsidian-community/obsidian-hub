---
link: https://www.obsidianroundup.org/2022-07-02/
author: Eleanor Konik
published: 2022-07-02T12:30:00
publish: true
---

# 2022-07-02: "Bionic Reading," Improved Popout Windows, & Better Databases
Showcases from game developers, roleplaying game players, and daily note takers. Plus a guide for when to use tags, folders and links.

## In The Community

-   This is your periodic reminder that Obsidian Community Talks are community organized, not "officially sponsored events" or anything, and basically anyone is welcome to propose or host one. If you're interested, reach out and I'll help you get in touch with the relevant people.

## Obsidian Updates

-   [Insider v0.15.3](https://forum.obsidian.md/t/obsidian-release-v0-15-3-insider-build/39566) brings a bunch of great new features for dragging panes between pop-out windows as well as some awesome improvements to Obsidian Sync, namely that the little button at the bottom of the screen lets you bring up a menu, so you don't need to go into settings to check on the sync log or pause things. They also fixed a bunch of hotkey stuff.

## Plugin News

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Trim Whitespace](https://github.com/zlovatt/obsidian-trim-whitespace) by `@zlovatt` trims unnecessary whitespace from your Obsidian documents, which I think is a more focused version of the [Text Format](https://github.com/Benature/obsidian-text-format) plugin.
-   [Custom Modals](https://github.com/helloitsian/custom-modals-obsidian) by `@helloitsian` lets users create powerful Custom Modals with HTML and JavaScript from the comfort of your notes.
-   [Habit Tracker](https://github.com/Narsail/habit-tracker-obsidian) by `@Narsail` adds pretty rendering to dataviewJS habit trackers.
-   [Bionic Reading](https://github.com/Quorafind/Obsidian-Bionic-Reading) by `@Quorafind` is a plugin to enable bionic reading mode in Live preview mode of Obsidian, although it only works on v0.15.3+ . Incidentally, [Readwise did a small test of whether bionic reading actually works](https://blog.readwise.io/does-bionic-reading-actually-work/) and there was an interesting [thread on HackerNews](https://news.ycombinator.com/item?id=31826204) discussing the results. Apparently it's one of their most requested features ever.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

-   ExcaliBrain, Supercharged Links, Sliding Panes, and Kanban now have improved support for Obsidian 0.15.2 Popout Windows. [Pane Relief](https://github.com/pjeby/pane-relief/releases/tag/0.1.0) added multi-window history support.
-   The [Jump to Link plugin](https://github.com/mrjackphil/obsidian-jump-to-link#how-to-use-lightspeed) now also has a lightspeed command, [which is originally a neovim plugin](https://github.com/ggandor/lightspeed.nvim). It works with Obsidian 0.15.x versions and above.
-   The [Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/5.1.1) plugin now lets users search by links and has a search delay, as well as recommended recent search command and modals to open and create in a new window (for those on the new Insider)
-   [Local Quotes 1.6.0](https://github.com/ka1tzyu/local-quotes) now has a button to refresh quote blocks immediately, a new search strategy for weighted random, and the ability to use plain text without formatting.
-   [Omnisearch](https://github.com/scambier/obsidian-omnisearch/releases/tag/1.4.0) got some search index improvements, improved tag search, added an API, and more.
-   [Notion-Like Tables v4](https://github.com/trey-wallis/obsidian-notion-like-tables/releases/tag/4.0.0) got a big update; it renders all tables as notion-like by default (tho you can opt out), there were a bunch of bug fixes, and now there's internal id management which should make things cleaner.
-   [Obsidian Tasks SQL Powered 2.5.0](https://sytone.github.io/obsidian-tasks-x/6-advanced/custom-functions/) is now updated with all the new Tasks features, along with some options for creation dates. There was also an update to the documentation.
-   [Database Folder](https://github.com/RafaelGB/obsidian-db-folder/releases/tag/1.8.0) now lets users use dataview queries as sources, there's templates for new rows, you can hide columns with configs, render images, use tags as sources, and more.

### For Developers

-   The release notes for [0.15.3](https://forum.obsidian.md/t/obsidian-release-v0-15-3-insider-build/39566) have a bunch of new enhancements for DOM elements and UI elements, as well as some new workspace events, changes, and deprecated some menu stuff.
-   The functionality that allows for editing metadata fields using Supercharged Links is looking for a new home. There are more [details in Discord](https://discord.com/channels/686053708261228577/855181471643861002/991682100707205150) if you're interested in helping out with this.
-   If anyone knows how to update the [Obsidian Vale](https://github.com/marcusolsson/obsidian-vale) client for Live Preview, it would be appreciated.

## Feature Requests

-   Being able to see [outlines in documents instead of the sidebar pane](https://forum.obsidian.md/t/outline-in-document/32714) would be useful.
-   Would it be useful for you if [workspace notes updated automatically](https://forum.obsidian.md/t/automatically-updating-workspace-notes/8300)? If so, provide your support to this feature request that got resurfaced this week.

## Appearance

-   [Theme Design Utilities](https://obsidian.md/plugins?id=obsidian-theme-design-utilities) now lets users toggle red outlines; this functions sort of like console.log() for CSS. [Here's an explanatory video](https://www.youtube.com/shorts/ii-lSK2_Nu4).
-   [Viridian](https://github.com/mulfok/obsidian-viridian) by `@mulfok` is designed to be a new joyful and focused theme. Here's a link to the [announcement in Discord](https://discord.com/channels/686053708261228577/855181471643861002/992191899437912074) if you'd like to give feedback to the developer.
-   Here's a CSS snippet for a [tidier sidebar calendar](https://discord.com/channels/686053708261228577/744933215063638183/989461706440851477) that was shared to Discord.

## Showcases

-   This video is focused on using Obsidian for roleplaying tabletop style games, but is also a nice showcase of [how dataview and database folder can be utilized](https://www.youtube.com/watch?v=ZKOYtrVXSbk).
-   Here's a great reflection about a bunch of stuff related to Obsidian, including [sync vs backup, themed logs vs daily notes, and recipes](https://medium.com/produclivity/plain-text-paper-less-productivity-digest-5-d2084b80bf98).
-   Here's why the [periodic notes plugin is awesome](https://www.youtube.com/watch?v=5Uxj0XgMp0k).

## Guides

-   Here's a video about [using Obsidian as a game developer](https://www.youtube.com/watch?v=1xuELZbkO9A).
-   Here's how to [style backlinks](https://obsidian-tasks-group.github.io/obsidian-tasks/how-to/style-backlinks/) using the Obsidian Tasks plugin.
-   Here's one way to [use Obsidian for studying](https://www.youtube.com/watch?v=TIcZt_41-DA).

## Discussions

-   Here is a periodic reminder to [back up your notes](https://www.reddit.com/r/ObsidianMD/comments/vm02le/10_minutes_of_terror_phd_student_lost_3_weeks_of/) and that while sync services can often be used as a backup in a pinch, that is not their primary purpose and you really should make actual backups.
-   Here's one method of differentiating between [when to use folders, tags, or links](https://www.reddit.com/r/ObsidianMD/comments/vofakc/folders_vs_links_vs_tags/), with an accompanying discussion.
-   Here's a nice discussion from the forum about [pulling ideas out of your notes as part of a writing workflow](https://forum.obsidian.md/t/whats-your-writing-workflow-for-pulling-ideas-out-of-your-zettelkasten/).
-   Here's a really great Reddit discussion about [how to take research notes in Obsidian](https://www.reddit.com/r/ObsidianMD/comments/vne0k5/question_on_research_notes_in_obsidianfeel_like/) that I wish I'd had more time to contribute to.
-   Here are some thoughts about [using Obsidian for mental health related journaling and notes](https://www.reddit.com/r/ObsidianMD/comments/vkf0ao/does_anyone_use_obsidian_for_mental_health/).

## Ancillary Tools

-   Here's a [fast, free quick capture app](https://apps.apple.com/us/app/quick-capture-fast-notes/id1609202525) for iOS.
-   It looks like [gitjournal got some updates](https://news.ycombinator.com/item?id=31914003), which is good to hear. It's a git-backed markdown editor for mobiles. This is the app a lot of folks used before Obsidian got a mobile version.
-   [Glasp](https://glasp.co/) (a social highlighting app) released a new feature to display a reading list of articles on Obsidian, using iframes. Here's [a tutorial](https://medium.com/glasp/how-to-show-your-reading-list-on-notion-obsidian-and-websites-with-glasp-c6e07571588e) and [a video](https://twitter.com/_Glasp/status/1539742066808623104).
-   Apparently some folks who use analog zettelkastens call them [antinets](https://www.reddit.com/r/antinet/). The subreddit community seems a bit dogmatic but I found skimming it to be interesting.

## Housekeeping

It's a holiday weekend in the States and I'm going to be on vacation until Monday night. I'll have minimal access to internet, and uncharacteristically I have a stack of emails from this week I haven't had a chance to reply to. I'll try to catch up by the end of next week, but if you try to reach out and I don't reply with my usual speed, that's why 😅

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-07-02%20Bionic%20Reading%2C%20Improved%20Popout%20Windows%2C%20%26%20Better%20Databases.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-07-02%20Bionic%20Reading%2C%20Improved%20Popout%20Windows%2C%20%26%20Better%20Databases.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
