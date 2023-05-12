---
link: https://www.eleanorkonik.com/2023-05-06/
author: Eleanor Konik
published: 2023-05-06T12:30:55
publish: true
---

# 2023-05-06: GPT Tips & Tools, Atomic Notes Advice, & Graph Filter Saving
New dev docs & a hub for medium articles, rapid logging tips, & a guide for ensuring productivity goals don't stress you out.

## In The Community

* The new [developer documentation](https://docs.obsidian.md/?ref=eleanorkonik.com) has tutorials for how to get started with plugin and theme development, reference docs for the plugin API and CSS variables, and guidelines for how to publish your project to the Obsidian catalog.
* Last week was the third annual [Linking Your Thinking Conference](https://www.linkingyourthinking.com/lytcon-3?ref=eleanorkonik.com), featuring a fireside chat with Obsidian's CEO, the Bullet Journal founder, an award-winning author who uses Obsidian to write novels in markdown, the Co-Founder of Readwise, the guy who runs the Obsidian book club, a bunch of LYT Alumni, and other names you would probably recognize. I was hideously busy this week getting caught up from my trip so I missed most of it, but I'm really looking forward to the replays!

## Obsidian Updates

* Mobile [v.1.4.4(99)](https://forum.obsidian.md/t/obsidian-mobile-v1-4-4-build-99/59005?ref=eleanorkonik.com) made Bookmarks available on mobile, fixed some bugs for Android users, and brought the desktop and mobile apps to parity.
* Desktop [1.2.7](https://forum.obsidian.md/t/obsidian-release-v1-2-7/59004?ref=eleanorkonik.com) marked the removal of the Starred core plugin, now that the Bookmarks plugin is available on mobile. There were also ribbon icon improvements, search UI improvements, and several bugfixes.
* Desktop Insider [v.1.2.8](https://forum.obsidian.md/t/obsidian-release-v1-2-8-insider-build/59086?ref=eleanorkonik.com) made some improvements to Bookmarks and some changes impacting developers.

## Plugin News

### New in Community Plugins

__These plugins went through code review and are now available in Obsidian's plugin list.__ For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new?ref=eleanorkonik.com).

* [Quickly](https://github.com/tmfelwu/obsidian-inbox?ref=eleanorkonik.com) by `@tmfelwu` adds a shortcut that brings up a quick capture modal.
* [Companion](https://github.com/rizerphe/obsidian-companion?ref=eleanorkonik.com) by `@rizerphe` facilitates autocomplete with AI, including ChatGPT, through a copilot-like interface.
* [AI Mentor](https://github.com/clementpoiret/ai-mentor?ref=eleanorkonik.com) by `@clementpoiret` is an open source AI mentor.
* [Copilot](https://github.com/logancyang/obsidian-copilot?ref=eleanorkonik.com) by `@logancyang` is a ChatGPT Copilot in Obsidian.
* [Folder Index](https://github.com/turulix/obsidian-folder-index?ref=eleanorkonik.com) by `@turulix` will automatically generate a table of contents for the current Folder.
* [Markdoc](https://github.com/kamoshi/obsidian-markdoc?ref=eleanorkonik.com) by `@kamoshi` adds basic support for Markdoc files
* [Show Diff](https://github.com/ivan-lednev/obsidian-automatic-changelog?ref=eleanorkonik.com) by `@ivan-lednev` will render Git diffs in Obsidian files
* [Linked Data Helper](https://github.com/kometenstaub/linked-data-helper?ref=eleanorkonik.com) & [Linked Data Vocabularies](https://github.com/kometenstaub/linked-data-vocabularies?ref=eleanorkonik.com) by `@kometenstaub` add linked data (LCSH) as metadata to your notes, like a library might use.
* [Game Search](https://github.com/CMorooney/obsidian-game-search-plugin?ref=eleanorkonik.com) by `@CMorooney` helps you find games and create notes.
* [April's Automatic Timelines](https://github.com/April-Gras/obsidian-auto-timelines?ref=eleanorkonik.com) by `@April-Gras` is a simple timeline generator for story tellers
* [Persistent Links](https://github.com/ivan-lednev/obsidian-persistent-links?ref=eleanorkonik.com) by `@ivan-lednev` will automatically repair internal links to blocks and headings
* [GitHub Issue Augmentation](https://github.com/samprintz/obsidian-issue-augmentation-plugin?ref=eleanorkonik.com) by `@samprintz` provides additional information to issue titles.
* [Confluence Integration](https://github.com/obsidian-confluence/obsidian-confluence?ref=eleanorkonik.com) by `@andymac4182` makes it easier to publish notes to Confluence.
* [Links](https://github.com/mii-key/obsidian-links?ref=eleanorkonik.com) by `@mii-key` makes it easier to link, unlink, convert, and edit links.
* [Personal Assistant](https://github.com/edonyzpc/personal-assistant?ref=eleanorkonik.com) by `@edonyzpc` streamlines workflows, helping users manage memos and plugins with a single command.
* [Loom](https://github.com/cosmicoptima/loom?ref=eleanorkonik.com) by `@cosmicoptima` adds a Loom integration for creating videos.

### Pending (as of Friday morning)

__Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat?ref=eleanorkonik.com). Note, though, that this is not as safe as waiting for them to go through code review.__

* [Open Plugin Settings](https://github.com/Lisandra-dev/open-plugin-settings-commands?ref=eleanorkonik.com) by `@Lisandra-dev` creates a command to open a specified plugin settings.
* [Countdown Timer](https://github.com/KaizelZero/obsidian-countdown?ref=eleanorkonik.com) by `@KaizelZero` adds a countdown to an event.
* [Colored Text](https://github.com/erincayaz/obsidian-colored-text?ref=eleanorkonik.com) by `@erincayaz` makes it esaier to color selected texts.
* [Auto Template Trigger](https://github.com/numeroflip/obsidian-auto-template-prompt?ref=eleanorkonik.com) by `@numeroflip` will automatically trigger the 'Insert Template' command when creating a note.
* [Canvas View](https://github.com/aqav/obsidian-canvas-view?ref=eleanorkonik.com) by `@aqav` shows which canvases the current active file embedded in.
* [Html Server](https://github.com/Pr0dt0s/obsidian-html-server?ref=eleanorkonik.com) by `@Pr0dt0s` makes it easier to spin up a local http server to access your vault via a web browser from any device in your network.
* [Sync Calendar](https://github.com/dustinksi/obsidian-sync-calendar?ref=eleanorkonik.com) by `@dustinksi` synchronizes events from the calendar and manages them like tasks.
* [Quail](https://github.com/lyricat/obsidian-quail?ref=eleanorkonik.com) by `@lyricat` integrates with an open-source newsletter service that looks interesting but I couldn't figure out how to sign up for.
* [TodoTxt](https://github.com/mvgrimes/obsidian-todotxt-plugin?ref=eleanorkonik.com) by `@mvgrimes` helps manage todotxt files.
* [APIRequest](https://github.com/Rooyca/obsidian-api-request?ref=eleanorkonik.com) by `@Rooyca` makes it easier to request and retrieve data from APIs. The responses are delivered in a JSON format for easy integration with your notes.
* [Better MathJax](https://github.com/greasycat/BetterMathjax?ref=eleanorkonik.com) by `@greasycat` provides math autocompletion and customizable snippets.
* [Link Head Icon](https://github.com/apankov/obsidian-link-head-icon-plugin?ref=eleanorkonik.com) by `@apankov` shows little image icon ahead of external URL
* [Mood Tracker](https://github.com/dartungar/obsidian-mood-tracker?ref=eleanorkonik.com) by `@dartungar` makes it easier to track your moods & emotions, then visualize tracked history and browse the past entries.
* [Auto Hide Cursor](https://github.com/moismat/obsidian-auto-hide-cursor?ref=eleanorkonik.com) by `@moismat` hides the cursor when scrolling and shows it again when moving the mouse.
* [Shukuchi](https://github.com/tadashi-aikawa/shukuchi?ref=eleanorkonik.com) by `@tadashi-aikawa` lets users to teleport to links (URL or internal link) and jump to their destinations.
* [Slide Note](https://github.com/Phantom1003/obsidian-slide-note?ref=eleanorkonik.com) by `@Phantom1003` makes it easier to take notes on PDF course slides.
* [Chem](https://github.com/Acylation/obsidian-chem?ref=eleanorkonik.com) by `@Acylation` renders SMILES strings into chemistry structures.
* [Custom State for Task List](https://github.com/OkamiWong/obsidian-custom-state-for-task-list?ref=eleanorkonik.com) by `@OkamiWong` makes it easier to add custom states to task list items.

### Updates

__If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates?ref=eleanorkonik.com) by Ganessh Kumar.__

* Tasks 3.4.0+ supports root & folder filters, [global queries](https://publish.obsidian.md/tasks/Queries/Global+Query?ref=eleanorkonik.com), and more.
* [Footnote Shortcut v0.1.0](https://github.com/MichaBrugger/obsidian-footnotes?ref=eleanorkonik.com) now supports non-numeric (named) footnotes with a new hotkey.
* [Outliner 4.5.0](https://github.com/vslinko/obsidian-outliner/discussions/190?ref=eleanorkonik.com) adds experimental support for drag & drop.
* [Webpage HTML Export](https://github.com/KosmosisDire/obsidian-webpage-export/?ref=eleanorkonik.com) now has an interactive graph view simulation, a background exporter, instant link navigation, progress indicators, and an HTML beautifier, among other improvements.
* [Excalidraw 1.8.25](https://www.youtube.com/watch?v=BvYkOaly-QM&ref=eleanorkonik.com) came with some quality improvements, like a scribble helper and multi-link support.
* [Rapid Notes 1.2](https://www.reddit.com/r/ObsidianMD/comments/13665lo/rapid_notes_12_create_notes_into_specific_folders/?ref=eleanorkonik.com) makes it easier to prefix filenames so they get created in a specified folder, among other things. This plugin is basically a simpler version of QuickAdd.
* [Terminal 3.8.0](https://github.com/polyipseity/obsidian-terminal/releases/tag/3.8.0?ref=eleanorkonik.com) supports themes now.
* [Webpage HTML Export 1.5.0](https://github.com/KosmosisDire/obsidian-webpage-export/?ref=eleanorkonik.com) has an interactive graph view simulation, progress indicators, and instant link navigation.
* [Hotkey Helper 0.3.17](https://github.com/pjeby/hotkey-helper/releases/tag/0.3.17?ref=eleanorkonik.com) now works with the 1.x plugin browser, restoring several features.
* [Linter v1.13.0](https://github.com/platers/obsidian-linter/releases/tag/1.13.0?ref=eleanorkonik.com) added Chinese, Spanish, and German language support in the UI.

NOTE: If your plugin had a particularly important update in the last 14 days, I might have missed it due to travel. Feel free to reach out (email is best) if you'd like me to include it in the next edition.

### Betas

__Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes.__

* [Obsidian Zotero](https://obzt.aidenlx.top/getting-started/install/obsidian?ref=eleanorkonik.com) got [discussed in Discord](https://discord.com/channels/686053708261228577/710585052769157141/1103308207306321921?ref=eleanorkonik.com) as an alternative to the Zotero Integration plugin.

### For Developers

* An upcoming version of Obsidian (Insider 1.2.8+) will be removing support for app://local links due to a potential vulnerability when using `<iframe>`. Moving forward, you should use `vault.getResourcePath(file: TFile)` and `vault.adapter.getResourcePath(vaultPath: string)` as a replacement. These also work on mobile. There's a [discussion in Discord](https://discord.com/channels/686053708261228577/1103015564055691324/1103015623480578138?ref=eleanorkonik.com).
* Insider 1.2.8 also fixed an issue with `navigator.clipboard` API not working in popout windows. - If you were relying on `app://local` for functionality within your plugin, you should use `vault.getResourcePath(file: TFile)` and `vault.adapter.getResourcePath(vaultPath: string)` as a replacement. These also work on mobile.

## Appearance

* [iB Writer](https://github.com/whereiswhere/iB-Writer?ref=eleanorkonik.com) by `@whereiswhere` was inspired by the iA Writer focused writing environment. It reminds me a bit of the Serenity theme, although the design choices are definitely distinct.

## Guides

* The [Obsidian Observer](https://medium.com/obsidian-observer?ref=eleanorkonik.com) is a new catalog of interesting & useful articles on Medium to help new to advanced users explore & leverage Obsidian's potential.
* Here's a great Twitter thread with [advice for turning text snippets into outlines](https://twitter.com/herdom/status/1654127919369957394?s=20&ref=eleanorkonik.com) from a German professor.
* Here's the best guide for [how to prompt a large language model](https://www.oneusefulthing.org/p/a-guide-to-prompting-ai-for-what?ref=eleanorkonik.com) that I've come across thus far, and a discussion of [the best ways to integrate ChatGPT into Obsidian](https://www.reddit.com/r/ObsidianMD/comments/12v6ccl/the_best_way_to_integrate_chatgpt_inside_obsidian/?ref=eleanorkonik.com).
* This is intended for bullet journals, not Obsidian specifically, but I thought I'd share this really well-regarded quick guide to [easily starting a journaling practice](https://www.youtube.com/watch?v=xHGtMw-JFRU&ref=eleanorkonik.com) using rapid logging methods, which seem to work well for people who like daily notes.
* I enjoyed this book review of [How to Calm Your Mind](https://bookthoughts.substack.com/p/how-to-calm-your-mind?ref=eleanorkonik.com) about how to make sure that productivity goals don't interfere with your happiness; don't wind up [in an abusive relationship with your notetaking apps](https://medium.com/@NotEntirelyBoring/i-am-in-an-abusive-relationship-with-note-taking-apps-3bbdc384b7e6?ref=eleanorkonik.com), people!
* This method for [how to spot emerging clusters of notes and use them](https://youtu.be/-XZwcZHKnMg?ref=eleanorkonik.com) got shared around recently.
* The Obsidian developers shared some [great tips for utilizing Bookmarks](https://discord.com/channels/686053708261228577/694233507500916796/1102993920666898512?ref=eleanorkonik.com), which lets you save graph settings.
* Here is a good explanation of [the differences between folder notes plugins](https://discord.com/channels/686053708261228577/855181471643861002/1103298367641104445?ref=eleanorkonik.com).

## Discussions

* Discord hosted an interesting discussion on [note atomicity](https://discord.com/channels/686053708261228577/710585052769157141/927690984844853358?ref=eleanorkonik.com) as it applies to different fields, particularly focused on when it's useful and when it isn't.
* There was a fairly detailed discussion of [daily notes for task management](https://www.reddit.com/r/ObsidianMD/comments/131pvv6/daily_notes_template_for_obsidian_task_edition/?ref=eleanorkonik.com) on Reddit, with lots of sample codes using the Tasks and Dataview plugins.
* This discussion covered a couple of different [methods for fiction writing](https://www.reddit.com/r/ObsidianMD/comments/12xwhcm/obsidian_for_fiction_writing/?ref=eleanorkonik.com).
* Here's a discussion of [how to integrate Obsidian notes with other tools students use](https://www.reddit.com/r/ObsidianMD/comments/135jnaa/students_how_do_you_combine_obsidian_with_other/?ref=eleanorkonik.com).
* I liked this discussion about the value of [using a read-it-later service as a middleman](https://www.reddit.com/r/ObsidianMD/comments/1342t29/advantages_using_a_readitlater_service_rather/?ref=eleanorkonik.com) instead of clipping directly to your vault.

## Showcases

* Here's how one user went from being an [overwhelmed newbie to a happy dashboard user](https://www.flavienbonvin.com/how-obsidian-improved-my-organization-at-work-and-home-first-month-review/?ref=eleanorkonik.com) thanks to Danny Hatcher and Canvas.
* Here's how a [Civil Engineering student uses Obsidian](https://www.reddit.com/r/ObsidianMD/comments/134ayz9/civil_engineer_student_enjoying_my_career_more/?ref=eleanorkonik.com).

## Ancillary Tools

* iOS users can now generate pretty PDFs using a python package called [obsidian-pdf-gen](https://github.com/mhbl3/obsidian-pdf-gen?ref=eleanorkonik.com).
* Here's a [basic Dataview query builder](https://s-blu.github.io/basic-dataview-query-builder/?ref=eleanorkonik.com) intended for folks without a technical background.
* Here are some [subreddits frequented by folks who comment on r/ObsidianMD](https://anvaka.github.io/map-of-reddit/?x=17601.213980789787&y=23047.158751334082&z=75.44417382415922&v=2&q=ObsidianMD&ref=eleanorkonik.com).

## Housekeeping

* Whew! Ireland was great, and I can confirm that it would have been flatly impossible to write the Roundup last week, so thanks for bearing with me and I hope you enjoyed this doubled-up edition.
* Also, good news: physical therapy has really been helping manage my [pregnancy-induced pelvic dysfunction](https://www.eleanorkonik.com/state-of-the-eleanor-02/), and I've been able to start writing articles again although I'm still sleeping a stupendous amount. For those of you [subscribed to my research overviews](https://www.eleanorkonik.com/#/portal), keep an eye out on Monday for a deep dive into the intricacies of ivory.
* Hopefully soon I'll be able to finalize my article on how to leverage Obsidian after a long time of inactivity, and why it's been super useful to me even when I'm not actively able to __take__ many notes 🙃

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2023-05-06%20GPT%20Tips%20%26%20Tools%2C%20Atomic%20Notes%20Advice%2C%20%26%20Graph%20Filter%20Saving.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2023-05-06%20GPT%20Tips%20%26%20Tools%2C%20Atomic%20Notes%20Advice%2C%20%26%20Graph%20Filter%20Saving.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
