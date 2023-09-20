---
link: https://www.eleanorkonik.com/pretty-callouts-developer-oriented-plugins/
author: Eleanor Konik
published: 2023-06-10T15:43:05
publish: true
---

# 2023-06-10: Pretty Callouts & Developer-oriented plugins
Featuring guides for verifying encryption, using Obsidian for TTRPGs, link to tab, and Zotero Citation Picker.

## Plugin News

### New in Community Plugins

__These plugins went through code review and are now available in Obsidian's plugin list.__ For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new?ref=eleanorkonik.com).

* [Interlinear Glossing](https://github.com/Mijyuoon/obsidian-ling-gloss?ref=eleanorkonik.com) by `@Mijyuoon` helps users format interlinear glosses used in linguistics texts.
* [Better MathJax](https://github.com/greasycat/BetterMathjax?ref=eleanorkonik.com) by `@greasycat` provides math autocompletion and customizable snippets.
* [Mood Tracker](https://github.com/dartungar/obsidian-mood-tracker?ref=eleanorkonik.com) by `@dartungar` makes it easier to track moods and emotions, visualize them, and browse past entries.

### Pending (as of Friday morning)

__Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat?ref=eleanorkonik.com). Note, though, that this is not as safe as waiting for them to go through code review.__

* [SyncFTP](https://github.com/alex-donnan/SyncFTP?ref=eleanorkonik.com) by `@alex-donnan` syncs files to SFTP, with credentials in settings.
* [Pieces for Developers](https://github.com/pieces-app/obsidian-pieces?ref=eleanorkonik.com) by `@mark-at-pieces` offers powerful features for capturing, managing, translating, and enhancing code snippets. (Closed Source)
* [Markdown Blogger](https://github.com/afazio1/obsidian-markdown-blogger?ref=eleanorkonik.com) by `@afazio1` allows developers to push markdown notes to their local blog, portfolio, or static site. Works with Astro.js, Next.js, and any other framework configured to render markdown pages.
* [Logstravaganza](https://github.com/czottmann/obsidian-logstravaganza?ref=eleanorkonik.com) by `@czottmann` is a simple proxy for `console.*()` calls which copies log messages and uncaught exceptions to a note.
* [Time Ruler](https://github.com/joshuatazrein/obsidian-time-ruler?ref=eleanorkonik.com) by `@joshuatazrein` is drag-and-drop time ruler combining the best of a task list and a calendar view (integrates with Tasks, Full Calendar, and Dataview).
* [Chemical Structure Renderer](https://github.com/xaya1001/obsidian-Chemical-Structure-Renderer?ref=eleanorkonik.com) by `@xaya1001` renders chemical structures from SMILES strings into PNG or SVG format using Ketcher and Indigo Service.
* [Lilypond](https://github.com/dot-asterisk-nl/obsidian-lilypond?ref=eleanorkonik.com) by `@Vaults` adds Lilypond support.
* [Query all the things](https://github.com/sytone/obsidian-queryallthethings?ref=eleanorkonik.com) by `@sytone` allows you to make SQL queries against the internal data of obsidian and render it how you want.
* [AI Notes Summary](https://github.com/irbull/obsidian-ai-summary?ref=eleanorkonik.com) by `@irbull` can summarize referenced notes using OpenAI.

### Updates

__If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates?ref=eleanorkonik.com) by Ganessh Kumar.__

* [Notion Like Tables v6.15.0](https://github.com/trey-wallis/obsidian-notion-like-tables/releases/tag/6.15.0?ref=eleanorkonik.com) introduced support for embedding tables into markdown files.
* [Another Quick Switcher 8.11.0](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/8.11.0?ref=eleanorkonik.com) added a "show in system explorer" command in the custom search dialog, along with utilizing selection words as default query input.
* [JSON/CSV Importer v0.30.0](https://github.com/farling42/obsidian-import-json/releases/tag/0.30.0?ref=eleanorkonik.com) now allows downloading a JSON file directly from a URL.
* [Folder notes 1.2.4](https://github.com/LostPaul/obsidian-folder-notes/releases/tag/1.2.4?ref=eleanorkonik.com) provides options to store folder notes outside of folders and to move folder notes from the old storage location with a button. [1.2.5](https://github.com/LostPaul/obsidian-folder-notes/releases/tag/1.2.5?ref=eleanorkonik.com) allows users to exclude folders with regex or wildcards and provides multiple ways to use a pattern for folder exclusion.
* [No Dupe Leaves v0.0.10](https://github.com/scambier/obsidian-no-dupe-leaves/releases/tag/0.0.10?ref=eleanorkonik.com) got an update to fix a bunch of issues, so try it out again if you ran into trouble in previous months.
* [Omnivore plugin 1.4.1](https://github.com/omnivore-app/obsidian-omnivore/releases/tag/1.4.1?ref=eleanorkonik.com) fixed an issue where some notes with special characters in the name could not be saved on Windows. [1.4.2](https://github.com/omnivore-app/obsidian-omnivore/releases/tag/1.4.2?ref=eleanorkonik.com) exposed the highlight ID as a variable for use in templates and fixed issues with syncing articles to an existing file without front matter.
* [Another Quick Switcher 8.12.0](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/8.12.0?ref=eleanorkonik.com) introduced a new setting to use selection words as a default input query.
* [Task Collector 1.0.11](https://github.com/ebullient/obsidian-task-collector?ref=eleanorkonik.com) supports numbered tasks and stabilizes click handling in Live Preview mode.

## Appearance

* [Bolt](https://github.com/Bluemoondragon07/Obsidian-Bolt?ref=eleanorkonik.com) by `@Bluemoondragon07` is a new theme inspired by Android apps and Material Design by Google.
* [Ebullientworks Theme 0.7.10](https://github.com/ebullient/obsidian-theme-ebullientworks?ref=eleanorkonik.com) got tweaked to better support Calendar.
* [Easy multi-column notes v0.5.4](https://github.com/zamsyt/obsidian-snippets/wiki/Easy-multi-column-notes?ref=eleanorkonik.com) now prevents the display of columns in source mode and fixed excess height of multi-column embeds in v0.5.3.
* Here are some beautiful [custom callouts with gradient colors](https://kneecaps.org/wires/workspace/callouts?ref=eleanorkonik.com).
* Here are some nice new codes for pretty [blockquotes](https://forum.obsidian.md/t/how-to-achieve-css-code-snippets/8474/244?ref=eleanorkonik.com).

## Food for Thought

* Here's [a video guide for how to use ChatGPT](https://www.youtube.com/watch?v=xHY3OHUNOrQ&ab_channel=JohnMavrick&ref=eleanorkonik.com) from inside Obsidian for free, have a chatbot to search anything from your notes, and get suggested smart connections to related ideas in your notes.
* Here's the Obsidian team on [how to verify Obsidian Sync's e2e encryption](https://obsidian.md/blog/verify-obsidian-sync-encryption/?ref=eleanorkonik.com).
* Here's a new [Obsidian TTRPG Tutorials](https://obsidianttrpgtutorials.com/?ref=eleanorkonik.com) site designed to help folks with tabletop roleplaying games and worldbuilding.
* Here are some tips for [getting the Zotero Citation Picker to stop opening in the background](https://github.com/mgmeyers/obsidian-zotero-integration/issues/4?ref=eleanorkonik.com#issuecomment-1566690780).
* Here's how the [Link to Tab](https://medium.com/obsidian-observer/obsidian-quick-tip-enhance-markdown-editing-with-link-with-tab-55a8b5c99177?ref=eleanorkonik.com) feature works.
* This 2022 article about how [it's a good thing that notes apps are where ideas go to die](https://www.reproof.app/blog/notes-apps-help-us-forget?ref=eleanorkonik.com) made the rounds again thanks to [a HackerNews discussion](https://news.ycombinator.com/item?id=36136179&ref=eleanorkonik.com).

## Housekeeping

Sorry for the slight delay in getting this edition out to everyone; somewhat embarrassingly I forgot to take my laptop charger to the gym this morning 😅 three cheers for my husband volunteering to take our kid to play mini-golf so I'd have time to write this anyway. 


%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2023-06-10%20Pretty%20Callouts%20%26%20Developer-oriented%20plugins.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2023-06-10%20Pretty%20Callouts%20%26%20Developer-oriented%20plugins.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
