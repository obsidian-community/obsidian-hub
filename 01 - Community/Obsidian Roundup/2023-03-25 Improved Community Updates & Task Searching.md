---
link: https://www.eleanorkonik.com/2023-03-25/
author: Eleanor Konik
published: 2023-03-25T12:30:21
publish: true
---

# 2023-03-25: Improved Community Updates & Task Searching
New folder plugins, LLM powered plugins, plugin APIs, improved audio notes support,  and some neat new public vaults.

## In The Community

* The `#updates` channel in the [community Discord server](https://discord.com/invite/obsidianmd?ref=eleanorkonik.com) has a new bot to update folks about new plugins and themes, with support for threaded discussions. It's a lot more pleasant to use now :)

### Pending (as of Friday morning)

__Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat?ref=eleanorkonik.com). Note, though, that this is not as safe as waiting for them to go through code review.__

* [Folder notes](https://github.com/LostPaul/obsidian-folder-notes?ref=eleanorkonik.com) by `@LostPaul` lets users create notes within folders that can be accessed without collapsing the folder, similar to the functionality offered in Notion and the other [Folder Note](https://github.com/aidenlx/alx-folder-note?ref=eleanorkonik.com) plugins.
* [Link Current Folder](https://github.com/ccosnean/link-current-folder?ref=eleanorkonik.com) by `@ccosnean` inserts the current folder path.
* [TagMeOut](https://github.com/tizianococcio/tagmeout?ref=eleanorkonik.com) by `@tizianococcio` extracts the header following each specified tag. It can be useful to create a summary of a note.
* [Askify Sync](https://github.com/helloworldkr/Askify-Obsidian-Sync?ref=eleanorkonik.com) by `@helloworldkr` help to sync notes from [Askify](https://askify.video/?ref=eleanorkonik.com), which lets users take screenshots and notes from YouTube.
* [Flashcard Learning](https://github.com/gaetanmuck/obsidian-flashcard-learning?ref=eleanorkonik.com) by `@gaetanmuck` is an alternate way flashcards can be used inside Obsidian in order to learn and remember things.
* [Page Properties](https://github.com/necauqua/obsidian-page-properties?ref=eleanorkonik.com) by `@necauqua` renders page properties similar to Logseq.
* [External Favicon](https://github.com/ordidxzero/obsidian-external-favicon?ref=eleanorkonik.com) by `@ordidxzero` adds favicon to anchors.
* [Tab Rotator](https://github.com/autohub7/obsidian-tab-rotator?ref=eleanorkonik.com) by `@autohub7` rotates opened tabs to the left or right with a specified interval.
* [Smart Rename](https://github.com/mnaoumov/obsidian-smart-rename?ref=eleanorkonik.com) by `@mnaoumov` renames notes while keeping previous title in existing links.
* [Dynamic Timetable](https://github.com/L7Cy/obsidian-dynamic-timetable?ref=eleanorkonik.com) by `@L7Cy` calculate the estimated time of completion from the estimated time of the task and dynamically creates a timetable.
* [Avatar](https://github.com/froehlichA/obsidian-avatar?ref=eleanorkonik.com) by `@froehlichA` displays an avatar image in your notes.
* [Latex Matrices](https://github.com/Deltekk/Obsidian-Latex-Matrices?ref=eleanorkonik.com) by `@Deltekk` speeds up latex matrices writing.

#### LLM-powered pending plugins

__Reminder: most plugins of this type need to make calls to the internet to function; many need to send your data to external servers to be indexed. Here's a [proposal for possible consent mechanisms for plugins that do so](https://forum.obsidian.md/t/add-consent-mechanism-to-plugins-that-send-your-notes-to-the-cloud/56324?ref=eleanorkonik.com).__

* [Auto Classifier](https://github.com/HyeonseoNam/auto-classifier?ref=eleanorkonik.com) by `@HyeonseoNam` automatically classifies your notes using the ChatGPT API.
* [Markdown GPT Chat](https://github.com/Tagada216/markdown-chat-gpt?ref=eleanorkonik.com) by `@Tagada216` lets users use ChatGPT with a command in Obsidian
* [Companion](https://github.com/rizerphe/obsidian-companion?ref=eleanorkonik.com) by `@rizerphe` is a github copilot-like interface for obsidian that can use ChatGPT under the hood.

### Updates

__If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates?ref=eleanorkonik.com) by Ganessh Kumar.__

* [QuickAdd v0.14](https://github.com/chhoumann/quickadd?ref=eleanorkonik.com) has improved macro handling, better customizations, and new options exposed via the API.
* [Another Quick Switcher 8.7.0](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/8.7.0?ref=eleanorkonik.com) added support for [2 hop links](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher?ref=eleanorkonik.com#what-is-the-2-hop-link).
* [Various Complements 8.1.0](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/8.1.0?ref=eleanorkonik.com) is now easier to disable on mobile.
* [Audio Notes](https://github.com/jjmaldonis/obsidian-audio-notes?ref=eleanorkonik.com) includes additional support for [Deepgram AI](https://deepgram.com/?ref=eleanorkonik.com) that allows you to transcribe your online audio files faster, as well as record voice messages, see a live transcript of your podcast/lecture/audio as you are listening, and access the full transcript of your audio.
* [Obsidian Git 2.19.0](https://github.com/denolehov/obsidian-git?ref=eleanorkonik.com) contains a new History view to see your logs and the changed files per commit.
* [Tasks 2.0.0](https://github.com/obsidian-tasks-group/obsidian-tasks/releases/tag/2.0.0/?ref=eleanorkonik.com) added searching of date ranges, tag filters, and a public API to retrieve markdown strings for new tasks.

## Appearance

* [sQdth One](https://github.com/KeithLerner/ObsidianMDsQdthOne?ref=eleanorkonik.com) by `@KeithLerner` is a new theme that reminds me a bit of old school terminals, albeit prettier.
* [Sanguine](https://github.com/Satchelmouth/Obsidian-Theme-Sanguine?ref=eleanorkonik.com) by `@Satchelmouth` is inspired by classic slasher horror films.
* [Everforest Enchanted](https://github.com/FireIsGood/obsidian-everforest-enchanted?ref=eleanorkonik.com) by `@FireIsGood` follows the Everforest theme family guidelines.

## Guides

* Here's a review of [many AI powered plugins](https://uttercodex.com/The+Codex+of+Utterances/Aspirants/Evaluating+the+Obsidian+AI+plugin+landscape?ref=eleanorkonik.com), with first impressions for most and further information for a few.
* Here's a discussion of [the value of folding sections of long notes](https://ricraftis.au/obsidian/how-to-use-folding-and-callouts-in-obsidian-maps-of-content-mocs-for-compact-appearance/?ref=eleanorkonik.com) by Ric Raftis.
* Here's a blog post detailing [Daily and Weekly Note templates and workflows](https://judisohn.com/2023/03/19/my-2023-digital-life-in-practice-obsidian-daily-and-weekly-notes/?ref=eleanorkonik.com) by Judi Sohn.

## Showcases

* Here's a really neat Obsidian Publish site created by volunteers from the Carbon Almanac network. It's called [Carbon Dots](https://publish.obsidian.md/carbon-dots/%E2%97%8F+Welcome?ref=eleanorkonik.com), and focuses on helping people take action about climate change.
* Here's an Obsidian-backed Digital Garden touching on [productivity, psychology, and philosophy](https://chaselittlepaws.com/?ref=eleanorkonik.com).

## Housekeeping

* I'm so sorry for any broken links you may have experienced last weekend; I am still banging my head against trying to fix the DNS problems for [https://newsletter.eleanorkonik](https://newsletter.eleanorkonik/?ref=eleanorkonik.com) and unfortunately following the directions I'd been given led to a lot more getting busted. I reverted the changes until I get a chance to dive in deeper and round up someone with more expertise than the other people I've already asked for help 😅

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2023-03-25%20Improved%20Community%20Updates%20%26%20Task%20Searching.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2023-03-25%20Improved%20Community%20Updates%20%26%20Task%20Searching.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
