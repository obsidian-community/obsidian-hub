---
link: https://www.obsidianroundup.org/2021-06-19/
author: Eleanor Konik
published: 2021-06-19
publish: true
---

# 2021-06-19: QuickAdd, a plugin updates channel, & new guides
Featuring a lot of useful knowledge management showcases, some really helpful css snippets, and discussion of the new outbound links core plugin.

## Community 
* There was a very informative [discussion](http://discordapp.com/channels/686053708261228577/694233507500916796/853418012320071700) about pricing models and why Obsidian charges for certain features while some competitors choose not to charge for those specific features. 
* `@person` put together [a rough experimentation guide](https://forum.obsidian.md/t/an-obsidian-experimentation-starter-guide/19580) intended for for folks new to Obsidian. 
* `@anthonyg` over at [[Obsidian Office Hours]] shared this in-depth [Zotero-with-Obsidian  deep dive](https://www.youtube.com/watch?v=YaMH_d4dj1k) by `@argentum`.
## Plugin News

### New
* `@Christian` released a [[templater-obsidian|Templater]] script as a new plugin: [QuickAdd](https://github.com/chhoumann/quickadd). It’s incredible.  At it’s core it lets you add pages from templates, do quick capture, etc. But now there’s a new and improved GUI for choices, and a custom macro engine to let you execute JS scripts and Obsidian commands like macros. Also, choices can now be added as Obsidian commands so you can activate them with hotkeys etc. There’s even added automatic suggestion for tags and file names in the input prompt.
* There’s a new plugin called [pluck](https://github.com/kevboh/obsidian-pluck) that lets you insert the contents of a webpage into a note. If you’re not already familiar with it, [this thread](https://forum.obsidian.md/t/how-do-i-get-content-from-websites-into-my-notes/1738) from the forum is full of great recommendations for browser extensions to capture web pages as markdown. 

### Updates
* The [[file-tree-alternative]] plugin now has a feature for pinning files to the top.
* [Jump to link](https://github.com/mrjackphil/obsidian-jump-to-link) now can jump to words or any other Regexp based symbol. This is configurable.
* The [Adjacency Matrix Maker](https://github.com/SkepticMystic/adjacency-matrix-maker) can now show folders on the matrix up to any depth. 
*  [Templater](https://github.com/SilentVoid13/Templater) (1.8.0) has new internal functions in the tp.file module and syntax highlighting in edit mode. 
### Scripts
* `@Nick_At_Day` shared this [[templater-obsidian|Templater]] [script](http://discordapp.com/channels/686053708261228577/840286238928797736/853274331135606814) intended for folks who use "ABC" lists to try to come up with tags. It will allow you to select the table and return only the tags.
* `@Witt` shared a nice, simple, straightforward example of how to use inline [[dataview|Dataview]] queries that act as formulas manipulating a variable. 
* `@Christian` created a [[quickadd|QuickAdd]] [script to move all notes with a tag to any folder](https://github.com/chhoumann/quickadd#macro-move-notes-with-a-tag-to-a-folder). 
### Under The Radar
* [[oz-image-plugin|Image in Editor]] was resurfaced as a super useful plugin for folks who hate switching over to preview mode to see the images they’re embedding. 
* This plugin lets you [[obsidian-underline|assign a hotkey for underlining]] the HTML way: `<u>`.
### For Developers

## Workflow Stuff
* There was a really nice discussion about the difference between the backlinks panels and outgoing links in the new core plugin. It begins [here](http://discordapp.com/channels/686053708261228577/694233507500916796/853264650987634698) and even has some nifty infographics. 
* `@Aonto` shared [how to use metaedit, dataview and Kanban](https://forum.obsidian.md/t/project-tracking-metaedit-dataview-and-kanban/19343) to track projects with a progress-bar.

## Feature Requests
* `@Sam Baron` created a feature request for Obsidian to [create a changelog file](https://forum.obsidian.md/t/plugin-updates-changelogs-release-notes/19642). There’s a [pull request](https://github.com/obsidianmd/obsidian-releases/pull/334) if you’d rather look into that, and in the interim we’ve got a new channel in the Discord for “#plugin-updates” where the github bot will post new plugins and developers can post updates there. 
* The feature request to [create references for headers or blocks by drag-and-drop](https://forum.obsidian.md/t/create-references-for-headers-or-blocks-by-drag-and-drop/7313) got resurfaced. 

## Appearance
* `@Kepano`'s css snippet for [image zoom](http://discordapp.com/channels/686053708261228577/702656734631821413/853888596116373524) got resurfaced. 
* `@mano` shared this code to get the [navigation on a publish website in a specific order](https://discord.com/channels/686053708261228577/768134314864017429/855247315681935390) instead of alphabetical + files following folders. 
* `@mano` also shared this snippet for [larger popovers](http://discordapp.com/channels/686053708261228577/702656734631821413/855348236322865182), which has been requested a lot lately. 
* `@Mara` shared a [WYSIWYG snippet](https://github.com/Mara-Li/Obsidian-WYSIWYG) along with a [forum post with video](https://forum.obsidian.md/t/pseudo-wysiwyg-snippet-mobile-pc/19733) to explain.

## Knowledge Management
* There was a lot of great discussion in this Reddit thread asking [how do you write permanent notes?](https://www.reddit.com/r/ObsidianMD/comments/nzpd56/no_seriously_how_do_you_write_permanent_notes/)

## Ancillary Tools
* There was a nice review of [[mailbox.org]] vs. [[ProtonMail]] [shared](https://jeppe.science/thoughts/why-i-fled-mailbox-for-protonmail/) by a community member (`@Jeppe Klitgaard`) 
* `@Briwats` put together a [forum thread](https://forum.obsidian.md/t/onyx-boox-obsidian-appreciation-theme/19588) compiling images and videos of Obsidian on the [[Onyx Boox]] eink tablet. Full disclosure, these convinced me buy a Boox ;) 
* For folks who use a static site generator like [[Hugo]] to run websites (or self-host your [[Digital garden|digital gardens]]) there was a great discussion about [various comments options](https://discord.com/channels/686053708261228577/700466324840775831/855162654493245441) in the Discord. 
*  `@Silver` shared a cool game made by friends of the Obsidian developers: [Keyword](https://store.steampowered.com/app/1393320/Keyword/) is a narrative thriller where you’ll depend on skills of logical deduction, hacking, and social engineering to solve challenging puzzles as the only means of finding your missing daughter. Keyword demo will be available during Steam Next Fest till the end of this month.

## Housekeeping

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-06-19%20QuickAdd%2C%20a%20plugin%20updates%20channel%2C%20%26%20new%20guides.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-06-19%20QuickAdd%2C%20a%20plugin%20updates%20channel%2C%20%26%20new%20guides.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
