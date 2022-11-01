---
link: https://www.obsidianroundup.org/2022-08-20/
author: Eleanor Konik
published: 2022-08-20T12:30:46
publish: true
---

# 2022-08-20: Mobile Git Backups & a Hotkey Keyboard Map
A new tool for diffing PDFs, a new method for managing RPG campaigns, and guides for using Obsidian with Devonthink or Dendron.

## Housekeeping

* I'll be in Chicago for Worldcon the first couple of days of September. Here's my [official schedule](https://newsletter.eleanorkonik.com/chicon-2022-schedule/) if you're planning to attend or happen to live in the area and want to grab coffee or something.
* I was able to install Obsidian on my new work laptop! This is very exciting — I wasn't expecting to be allowed to. I'm glad I procrastinated on figuring out how Docker works 😂

## In the Community

* There's a new book club being organized [via discord](https://discord.com/channels/686053708261228577/700466324840775831/1009112156064718951). So far most of the interest seems to be around genre fiction books. Here's the [resource document](https://docs.google.com/document/d/1Tltglt-UGwsqo2PAlcJGK4LwgGocHiUhV3GrPo6BiZs/edit), here's [the list of proposed books](https://docs.google.com/spreadsheets/d/1JthB7H9yfa-w4ksTIQGz72IxPEZqDpjI_jsRtV2c74w/edit?usp=sharing). Consider joining in and signing up!
* There's a guy who is active in the Obsidian community who has low code integration experience but is looking to break into a software engineering role. He's primarily comfortable with Python but has recently picked up TS/JS. He's contributed to a few plugins you might have used like the SRS plugin and Dataview, but has no prior software dev experience and is looking for a junior role. He's open to remote contract work (lives abroad) but is willing to move back to the US as well. Please let me know if you'd like to get in touch.

## Plugins

* If you use the [File Hider plugin](https://github.com/Oliver-Akins/file-hider/discussions/19) please consider contributing to the discussion about the future direction of the plugin.

### New in Community Plugins

__These plugins went through code review and are now available in Obsidian's plugin list. For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new).__

* [Heading Shifter](https://github.com/k4a-dev/obsidian-heading-shifter) by `@k4a-dev` makes it easier to shift and change markdown headings.
* [Open File by Magic Date](https://github.com/SimplGy/obsidian-open-file-by-magic-date) by `@SimplGy` lets users define a Moment.js date pattern that specifies the file that is most important to you (eg: your daily/weekly/monthly note). It'll create the file if it doesn't exist.
* [No dupe leaves](https://github.com/scambier/obsidian-no-dupe-leaves) by `@scambier` makes sure you don't open the same note multiple times.
* [Better Inline Fields](https://github.com/dsarman/better-inline-fields) by `@dsarman` enhances Dataview style inline fields.
* [Hide Sidebars on Window Resize](https://github.com/NomarCub/obsidian-hide-sidebars-on-window-resize) by `@NomarCub` automatically hides the sidebars when your window is resized to be narrower.
* [Tagged Documents Viewer](https://github.com/mgeduld/obsidian-tagged-documents-viewer) by `@mgeduld` opens a modal with scrollable content of all documents that contain a specific tag or tags.
* [Meeting notes](https://github.com/TimHi/obsidian-meeting-notes) by `@TimHi` automatically creates a meeting note if a new file is created in a meeting folder.

### Pending (as of Friday morning)

__Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review.__

* [QuickShare](https://github.com/mcndt/obsidian-quickshare) by `@mcndt` lets users securely share notes with one click. Notes are end-to-end encrypted with no API keys or configuration required.
* [Auto Hide](https://github.com/skelato1/obsidian-auto-hide) by `@skelato1` collapses sidebars when clicking on the editor/viewer panel.
* [Dashing cursor](https://github.com/9r0x/obsidian-dashing-cursor) by `@9r0x` enables a dashing cursor that follows the page scroll.
* [Obsidian Git Isomorphic](https://github.com/Vinzent03/obsidian-git-isomorphic) by `@Vinzent03` is another way to backup your vault with git... that works on mobile.
* [Anki Synchronizer](https://github.com/tansongchen/obsidian-anki-synchronizer) by `@tansongchen` is another spaced repetition app for Anki.
* [URL Namer](https://github.com/zfei/obsidian-url-namer) by `@zfei` retrieves the HTML titles to name the raw URL links. I think it's manual instead of automatic the way [Auto Link Title](https://github.com/zolrath/obsidian-auto-link-title) is.
* [Obsidian Header Format](https://github.com/dbarenholz/obsidian-headerformat) by `@dbarenholz` makes it easier to format the current line as a header.

### Updates

__If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar.__

* Another Quick Switcher plugin had a major update with lots of new featurs, including "insert all to editor," grep support, custom searches, an option to hide hotkey guides. Some settings also got removed, so make sure you [check the release notes](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/6.0.0) before updating. [6.1.0](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/6.1.0) added vim-like navigation, too.
* [Obsidian Plaintext](https://github.com/dbarenholz/obsidian-plaintext) now supports Obsidian Mobile.
* [Obsidian Linter 1.4.0](https://github.com/platers/obsidian-linter/releases/tag/1.4.0.) lets users format YAML arrays, tags, and aliases. Incidentally, I recently (re?) learned that this plugin lets you enforce `*` or `_` for bold/italic throughout your whole vault, if you're  like me and sometimes vary between the two.
* [Metadata Menu 0.1.11](https://github.com/mdelobelle/metadatamenu) has a new field type: `file` which can be populated with a file in your vault. Here's [a demo](https://youtu.be/sYudigxPEnY).
* [Obsidian Database Folder 2.2.0](https://github.com/RafaelGB/obsidian-db-folder/releases/tag/2.2.0) makes it possible to hide columns, and made filters accessible from the navbar. You can also sort and search tags.

### Betas

__Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes.__

* [RPG Manager](https://github.com/carlonicora/obsidian-rpg-manager) requires dataview but is setting-agnostic and focuses on helping writing campaigns and linking various elements of a campaign together for ease of running sessions.
* [Virtual Hotkey Board](https://github.com/Quorafind/Obsidian-Virtual-Hotkey-Keyboard/releases/tag/1.1.2) lets you see what hotkeys you have set in a nice keyboard layout style.

## Ancillary Tools

* Here's a tool mentioned on HackerNews that's useful for [cross-referencing the difference between PDFs](https://news.ycombinator.com/item?id=32353479).

## Feature Requests

* A word count that [ignores stuff only visible in source mode and counts from reading mode](https://forum.obsidian.md/t/word-count-based-on-preview-text-not-editor-text/4758) would be nice. Bonus if it shows word count for the currently active view mode.
* The ability to [sync settings and options between different vaults on the same computer](https://forum.obsidian.md/t/option-to-sync-settings-themes-and-plugins-across-multiple-vaults/41789?u=synchronicity) would be nice.

## Appearance

* [ITS Theme](https://forum.obsidian.md/t/theme-its-dark-light-theme/12838/169) now has support for turning dataview lists into columns, and got some other callout updates.
* [Primary](https://github.com/ceciliamay/obsidianmd-theme-primary/releases/tag/v.1.4.8) added variations for callouts and alternate checkbxoes, improved accessibility, and more checkbox styles.
* [Wyrd](https://github.com/curio-heart/obsidian-wyrd/releases/tag/v0.3.4) got some bugfixes.
* [Mado Miniflow 0.2.0](https://github.com/hydescarf/Obsidian-Theme-Mado-Miniflow/releases/tag/v0.2.0) has an improved mobile experience.

## Guides

* Here's a video from Bob Doto explaining how to [write essays using a zettelkasten system in Obsidian](https://youtu.be/9OUn2-h6oVc).
* Here's a guide about how to use Obsidian to [track tasks, meetings, classes, and relationships](https://twelvetables.blog/taking-notes-with-obsidian/).
* Here's an explanation of how someone used [Obsidian to help prepare for public speaking](https://realhardman.medium.com/public-speaking-a-nightmare-unlock-excellence-with-the-awesome-obsidian-4246f3022d27).
* Here's an [argument for why DevonThink and Obsidian are great in tandem](https://simontheak.medium.com/why-i-use-both-devonthink-and-obsidian-to-manage-my-content-8f76490ee295), directed mostly at apple-ecosystem folks.
* Here's a nice thread about the value of using [Dendron and Obsidian together](https://twitter.com/aadimator/status/1558435103990218753) and how to set that up.
* Here's a migration guide for [making Obsidian work like Bear](https://www.reddit.com/r/ObsidianMD/comments/wrs5wi/bear_minimum_obsidian/).
* Here's an [infographic about how to make notes and write](https://www.reddit.com/r/ObsidianMD/comments/ws3vk8/my_visualization_of_the_making_notes_portion_of/).
* Here's a guide for [using Obsidian for team knowledge management](https://medium.com/@ensleytan/using-obsidian-for-group-km-145646068cd7).

## Showcases

* Here's an [example of a flexible working environment](https://echinopscis.github.io/) for folks in the biodiversity informatics area, along with a [twitter thread explaining its purpose](https://twitter.com/nickynicolson/status/1559524647175086081). It's basically an extensible notebook for open science on specimens — "a working environment that allows researchers to write, access data and create links between literature, specimens, names, institutions, people, traits etc."
* [OB Templates](https://github.com/llZektorll/OB_Template) got a new template for creating a word dictionary.
* Here's a [recording](https://www.youtube.com/watch?v=zCbXERZf8vM) of `@mapogatari` researching and processing the notes for those who find "working examples" and models more useful than lecture-style explanatory guides.

## Food For Thought

* Here's a lovely article about [the value of purposefully framing important habits as rituals](https://leisureguy.wordpress.com/2017/03/27/reprise-of-coveys-7-habits/) that focuses on things like weekly planning.
* Here's a thread about [how historians take notes](https://www.reddit.com/r/AskHistorians/comments/wlu8df/how_historians_take_notes_when_working_with/) — the major takeaway is that there's no set standard and everyone has personalized systems, but the discussion was still valuable, particularly since it was from the AskHistorians subreddit and not a subreddit dedicated to notetaking nerds.
* [The Rise and Fall of Getting Things Done](https://www.newyorker.com/tech/annals-of-technology/the-rise-and-fall-of-getting-things-done) was popular this week.
* This article [in defense of complicated programming languages](https://viralinstruction.com/posts/defense/) really reminded me of my article about [the difficulties of teaching notetaking](https://www.obsidianroundup.org/the-difficulties-of-teaching-notetaking/), particularly the bit about how hard it is to get people to learn something they don't need just because it might be useful later down the line. Although ostensibly about programming languages, the core argument was very applicable to notetaking systems. In fact, I liked it so much that it inspired this month's thoughts: [don't minimize difficulty](https://www.obsidianroundup.org/dont-minimize-difficulty/).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-08-20%20Mobile%20Git%20Backups%20%26%20a%20Hotkey%20Keyboard%20Map.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-08-20%20Mobile%20Git%20Backups%20%26%20a%20Hotkey%20Keyboard%20Map.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
