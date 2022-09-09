---
link: https://www.obsidianroundup.org/2021-07-03/
author: Eleanor Konik
published: 2021-07-03
publish: true
---

# 2021-07-03: Sync Updates, URI improvements, & workflows
Lots of new ways to access the APIs of other tools, like Amazing Marvin, Pocket, & Twitter. Also: a neat trick to get the same vault working on two monitors.

## In The Community

- The recording of the last Community Talk, [What your Vault Knows](https://youtu.be/58-Ue2mDy0k), which involves three short presentations and a discussion about using computational methods to extract knowledge from our vaults, is now online on YouTube.

## Obsidian Updates

- The Insider Build ([12.9](https://forum.obsidian.md/t/obsidian-release-v0-12-8-insider-build/20214)) lets [[Obsidian Sync]] be used to synchronize your settings, appearance tweaks, custom CSS, and installed plugins. It can now sync any file type using the “Sync all other types” option.

## Plugin News

### New

Note: Some of these are pending code review and are not yet available in the community store. They may require manual install.

- the [Obsidian & reMarkable plugin](https://github.com/cobalamin/obsidian-remarkable) is looking for Windows testers.
- the [[initiative-tracker|Initiative Tracker]] plugin should make things easier for people who are using Obsidian to run tabletop RPGs.
- `@death_au` created a new [command URI plugin](https://github.com/deathau/command-uri-obsidian) that should allow for the creation of a system-wide hotkey to create new notes from anywhere. It opens up uri schemes to plugins that haven't necessarily defined them. I think it’s intended for things like this method to use [ULauncher](https://ulauncher.io/), an alternative to Alfred for Linux, to help with [quick capture of thoughts into a daily note](https://forum.obsidian.md/t/linux-alfred-alternative-for-quick-caputure/20203).
- [[obsidian-pocket|Pocket integration]] allows you to sync your Pocket reading list into Obsidian, so that you can easily create Obsidian notes directly from your Pocket reading list.
- [[obsidian-map-view|Map View]] looks incredible for trip planning & taking notes about places you’ve been.
- You can now query the [[obsidian-amazingmarvin-plugin|Amazing Marvin]] API for a list of tasks.

### Updates

- You can now [schedule tweets](https://github.com/chhoumann/notetweet_obsidian/blob/master/GuideToSettingUpScheduler.md) with [[notetweet]]. For what it’s worth, NoteTweet is the absolute best (& cheapest) way to write Twitter threads that I’ve found anywhere. We also recently discussed how [tweets can be used as a type of atomic note conversation](https://discord.com/channels/686053708261228577/710585052769157141/857716879393423371).
- [[quickadd]] can now detect the end of sections, and the format syntax suggester will now help you write formats easier. There were also some updates to the documentation and some bugfixes. Date offset functionality was added, and there’s a new API feature for variables. It’s up to 3.0 now.
- obsidian [[obsidian-smart-typography|Smart Typography]] has been updated to support [customizing the open/closing quote characters](https://github.com/mgmeyers/obsidian-smart-typography/issues/5).
- The [[obsidian-dictionary-plugin|Obsidian Dictionary plugin]] (which has been way more useful for me personally than I thought it would be) now supports caching, which helps with offline / slow internet usage.

### Under The Radar

- The [[obsidian-dice-roller|Dice Roller]] plugin lets you randomly select entries from a table, as in [this example](https://discord.com/channels/686053708261228577/805952223124520961/860471875678896159). This can be used for, say, [generating writing prompts](https://discord.com/channels/686053708261228577/805952223124520961/860534603521196062).
- [[better-fn|Better footnotes]] is really nice. If you use footnotes and aren’t using it, it might help: it lets you preview on hover with footnote links.
- There’s a plugin that assigns [[obsidian-shortcuts-for-starred-files|hotkeys to starred files]]. It will, for example, let you jump quickly to an index note.

### For Developers

- This [shell script](https://github.com/kometenstaub/shell) via `@koala` will make it easier to beta test plugins; it facilitates updating plugins which are not in the Obsidian community plugin store. This [discord post](http://discordapp.com/channels/686053708261228577/840286238928797736/858448800737001522) has more details.
- Obsidian’s config file has been split up into 4 different files.
- `registerMarkdownPostProcessor` and `registerMarkdownCodeBlockProcessor` will now return the `MarkdownPostProcessor` callback function to facilitate manual un-registration.

## Workflow Stuff

- Moderator `@cotemaxime` shared the full breakdown of their [productivity system]([Maxime Cote | Personal Site](https://www.maximecote.me/blog/my-productivity-system-planning/)) over on their blog. It pulls from David Allen’s “Getting Things Done,” [Tiago Forte](https://twitter.com/fortelabs/status/1397572271548502020), Cal Newport and more. It’s a great example of mashing together best practices from various sources to land on what works for you, which Maxime also wrote [a guide for](https://www.maximecote.me/blog/how-to-architect-your-productivity-system-yourself/).
- `@joshduffney` [recorded & shared their smart notes workflow in Obsidian](https://www.youtube.com/watch?v=o_pq43WzeEo&t).
- `@mutton44` shared a somewhat hacky way to get [obsidian to work on two monitors with the same vault on Windows 10](http://discordapp.com/channels/686053708261228577/694233507500916796/860128416724025364). I don’t know if I’d be brave enough to try it, but I’d be remiss to not share.

## Feature Requests

- `@edith` posted a feature request for [keeping the focus in the current panel/tab](https://forum.obsidian.md/t/keep-focus-in-current-pane-tab/20317).
- There’s a [feature request](https://forum.obsidian.md/t/selected-note-shown-highlighted-on-the-local-graph/9643/18) to highlight the active note on graph view that got resurfaced.

## Appearance

- `@bobheadxi` created a script to [sync global graph settings to the local graphs](https://gist.github.com/bobheadxi/ad4bc77a7b8c80d26f7668dac8a47576).
- There’s a new dark theme in town; check out [Rmaki](https://github.com/luke-rmaki/rmaki-obsidian).

## Knowledge Management

- `@anthonyamar` shared this [curated list of public Zettelkastens / Second Brains / Digital Gardens](https://github.com/KasperZutterman/Second-Brain).
- `@Animalistic` shared a very popular [method for choosing when to skim, when to focus, and when to highlight](https://discord.com/channels/686053708261228577/694233507500916796/858514569978445854) when processing a text.
- There was a nice reddit thread about how to use [[dataview|Dataview]] to [track books](https://www.reddit.com/r/ObsidianMD/comments/oa8q80/how_would_you_use_dataview_to_make_a_book_tracker/).

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- [Scholarcy](https://www.scholarcy.com/), an online summarizing tool & flashcard generator, added Markdown export to our Chrome Extension, so it's easier to get full text research papers, including key findings and references, into Obsidian.
- After some discussion of tab organizers, [Session Buddy](https://chrome.google.com/webstore/detail/session-buddy/edacconmaakjimmfgnblocblbcdcpbko) was shared as a nice way to keep browser tabs organized by source in an outline format.
- [ActivityWatch](https://activitywatch.net/) is a free and open source device tracker that can be used to keep track of your productivity, time spent on different projects, bad screen habits, or just to understand how you spend your time.

## Housekeeping

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-07-03%20Sync%20Updates%2C%20URI%20improvements%2C%20%26%20workflows.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-07-03%20Sync%20Updates%2C%20URI%20improvements%2C%20%26%20workflows.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
