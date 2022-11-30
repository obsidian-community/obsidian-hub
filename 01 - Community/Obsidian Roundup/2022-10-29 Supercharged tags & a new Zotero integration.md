---
link: https://www.obsidianroundup.org/2022-10-29/
author: Eleanor Konik
published: 2022-10-29T12:30:02
publish: true
---

# 2022-10-29: Supercharged tags & a new Zotero integration
Lots of new color schemes are proliferating. Plus, inspiring stories about quitting marijuana and putting visual studio code inside of an Obsidian window.

## Obsidian Updates

* [v1.0.3](https://forum.obsidian.md/t/obsidian-release-v1-0-3/46219) comes with a bunch of bug fixes, so if you ran into problems with v1.0.0, update and try again.
* Mobile got a similar update and is now on [v1.4.1](https://forum.obsidian.md/t/obsidian-mobile-v1-4-1/46216).

## Plugin News

### Pending (as of Friday morning)

_Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

* [Mentions in Status Bar](https://github.com/GRONADE457/obsidian-mentions-in-status-bar) by `@GRONADE457` displays all the mentions of the current file in the status bar.
* [Wordy](https://github.com/nqthqn/obsidian-wordy) by `@nqthqn` uses the Datamuse API to serve as a thesaurus, dictionary, and more.
* [New Bullet With Time](https://github.com/Quorafind/Obisidna-New-Bullet-With-Time) by `@Quorafind` allows you to automatically add the current time to new bullet lines.
* [Pretty BibTeX](https://github.com/sandrofigo/obsidian-pretty-bibtex) by `@sandrofigo` shows raw BibTeX bibliography entries in a prettier way.
* [Vika Sync](https://github.com/romantic-black/obsidain-vika-sync) by `@romantic-black` lets users sync notes to a cloud-based database software in China that works similarly to airtable.
* [Scroll to Top Plugin](https://github.com/cloudhao1999/obsidian-scroll-to-top-plugin) by `@cloudhao1999` adds a button to scroll to the top of the current note.
* [Custom File Extensions Plugin](https://github.com/MeepTech/obsidian-custom-file-extensions-plugin) by `@MeepTech` associates views with custom file extensions via settings.
* [Edit Gemini](https://github.com/Basil-Mori/obsidian-edit-gemini) by `@Basil-Mori` allows the user to edit and create .gmi files, which seem to be an alternative web protocol to HTTPS.
* [Colorful Tag](https://github.com/rien7/obsidian-colorful-tag) by `@rien7` makes it easier to add a prefix or suffix to a tag and change the tag’s background or text color.
* [Daily Note Outline](https://github.com/iiz00/obsidian-daily-note-outline) by `@iiz00` adds a custom view which shows outline of multiple daily notes with headings, links, tags and list items.
* [Awesome Flashcard](https://github.com/AwesomeDog/obsidian-awesome-flashcard) by `@AwesomeDog` is another Anki integration for Obsidian.
* [Improved Random Note](https://github.com/ShockThunder/improved-random-note) by `@ShockThunder` adds something a bit nicer for a wandering mode.
* [Trash Explorer](https://github.com/proog/obsidian-trash-explorer) by `@proog` lets users more easily restore and delete files from the Obsidian .trash folder
* [Ordered List Style](https://github.com/erykwalder/obsidian-list-style) by `@erykwalder` lets users set ordered list styles inline as alphabetic lists, roman numeral lists, etc.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

* There was, perhaps inevitably, a [discussion on the forum about the feasibility of something like Tana's "supertags"](https://forum.obsidian.md/t/supertags-in-obsidian/) in Obsidian. If you scroll down a bit, you'll see the author of Metadata menu describing how v0.3 implements something similar. Here's [a demo](https://www.youtube.com/watch?v=I73uW8fqOZ8) about how to build tags with file classes in Obsidian. Here's [the documentation](https://mdelobelle.github.io/metadatamenu/).
* [Omnisearch 1.7.6](https://github.com/scambier/obsidian-omnisearch/compare/1.6.4...1.7.6) added PDF indexing and got a major refactor to improve caching and make indexing and searching super smooth.
* [Obsidian Linter v1.7.0](https://github.com/platers/obsidian-linter/releases/tag/1.7.0) got a big update to make it easier to force your preferred defaults onto YAML and format other things like math.
* [Obsidian OCR v1.3.1](https://github.com/MohrJonas/obsidian-ocr/releases/tag/1.3.1) added a progress bar, a new file format for transcript files, and several search improvements. [v1.4.0](https://github.com/MohrJonas/obsidian-ocr/releases/tag/1.4.0) added a bunch of performance updates.
* Tasks plugin [v1.16.0](https://github.com/obsidian-tasks-group/obsidian-tasks/releases/tag/1.16.0) now has [ways to find tasks with invalid dates](https://obsidian-tasks-group.github.io/obsidian-tasks/queries/filters/#finding-tasks-with-invalid-dates), [easier selection of priority when editing tasks](https://obsidian-tasks-group.github.io/obsidian-tasks/getting-started/create-or-edit-task/#introduction),
* [CardBoard v0.6.0](https://github.com/roovo/obsidian-card-board) (which is sort of a tasks/kanban plugin) now understands due and completion dates in Tasks format out of the box.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

* There's a fancy new [Zotero integration](https://obzt.aidenlx.top/getting-started/install/) that can read data directly from the Zotero database, with no need to export data into a text-based format. It has templating, it has complete access to Zotero data, it has annotation views, as far as I can tell it has the kitchen sink.
* [Strange New Worlds](https://github.com/TfTHacker/obsidian42-strange-new-worlds) (which I finally installed and is genuinely amazing at showing me all of the places a particular reference gets referenced in a nice hover pane) got mobile, tablet, and preview improvements. Here's [a 2 minute overview](https://youtu.be/i08ksJ-nK9c) of how the plugin works.

## Appearance

* [Cyber Glow v7.2](https://github.com/ArtexJay/Obsidian-CyberGlow/releases/tag/v7.2) got a new line highlighter to make it more obvious which line you're on. [7.4](https://github.com/ArtexJay/Obsidian-CyberGlow/releases/tag/v7.4) improved mobile support, among other things.
* [AnuPpuccin](https://github.com/anubisnekhet/anuppuccin) v1.0.2 - 1.1.1 added a custom dark coffee theme and an alternative card layout option. v1.0.7 overhauled the style settings menu and added support for a bunch of new color schemes as well as custom callouts.
* [Ebullientworks](https://github.com/ebullient/obsidian-theme-ebullientworks) v0.6.0 got a ton of updates and should be all set to go for Obsidian 1.0.
* [GitHub theme](https://github.com/krios2146/obsidian-github) by `@krios2146` has a color scheme reminiscent of Github.
* [Ultra Lobster](https://github.com/7368697661/Ultra-Lobster) by `@7368697661` sounds very aggressive but is actually really nice looking with careful attention to fonts and typography.

## Guides

* Here's a fantastic guide on how to [automatically sync notes on iOS for free using git and a-shell](https://forum.obsidian.md/t/mobile-automatic-sync-with-github-on-ios-for-free-via-a-shell/46150).
* Here's how to [(self) publish your digital garden with Flowershow](https://flowershow.app/docs/publish-tutorial).
* Here's how to get [Visual Studio Code Server inside of Obsidian](https://www.reddit.com/r/ObsidianMD/comments/yfxdlb/vs_codeserver_in_obsidian/).
* [Display data in views and status bar](https://youtu.be/zR86pftlOsg) with Marcus Olsson: Marcus works you through how to display your plugin data in views and status bar.
* [Easy and fast UI development with Svelte](https://youtu.be/mCF80HBfUWA) with Maxime Cannoodt: Maxime Cannoodt teaches Marcus how to get started with UI development with Svelte.
* This article goes over [how to take notes while reading on the web](https://beingpax.medium.com/a-better-web-highlighter-for-obsidian-82428c634a24) and mentions this [web highlighter](https://eloquent.works/) for Chrome called Eloquent that works with Obsidian and supports nested bullets, tags, and wikilinks.  It supports a keyboard focused workflow for quick capture, too.
* Here's a really handy infographic [cheat sheet for Obsidian search operators](https://twitter.com/heymichellemac/status/1585980871248867328).
* Here's a video guide for [how to take conceptual lecture notes](https://www.youtube.com/watch?v=PuqGjNJMiZQ) using Obsidian, with the goal of having them be useful after the course is over.
* Here's a step-by-step guide for how to [set up a vault for school using Dataview and Templater](https://www.youtube.com/watch?v=0UTzpIdLbVo).

## Showcases

* Here's a really inspiring story about how [Obsidian helped one user quit smoking marijuana](https://www.reddit.com/r/ObsidianMD/comments/yakp6u/in_a_way_my_experience_with_pkm_and_obsidian_has/), complete with the relevant planning note and a ton of encouragement from the community. Sometimes the most important notes are short and to the point, no complex workflows required.
* Here's a template for [managing data about people](https://dannb.org/blog/2022/obsidian-people-note-template/) that explains how to use Dataview, Templater, and QuickAdd.

## Ancillary Tools

* The [Basic Dataview Query Builder](https://s-blu.github.io/basic-dataview-query-builder/) should be quicker to use now that it adds or skips questions depending on information you give it.

## Housekeeping

I recently wrote a piece explaining how [I need to consolidate my newsletters and rethink some elements of my publication schedule](https://newsletter.eleanorkonik.com/state-of-the-eleanor-01/) for a variety of reasons outlined in the post. 

The upshot of this for the Obsidian Roundup is ironically that there will be more content available soon™. It's nothing to worry about, but I wanted to share it here so y'all know that changes are coming as soon as I can get this squared away on the "hiring a developer to help me pull this off" side of things. The short version is that there have been a lot of changes in newsletter software (and my life!) since I started the Obsidian Roundup, and I need to start taking advantage of some of those changes for my own sanity. 

💚Also, a few people have asked me, so if you've been interested in chipping in to help defer my newsletter hosting fees and the costs of hiring developers, but aren't really interested in [a subscription](https://www.obsidianroundup.org/#/portal/signup), I do have a ko-fi page where you can [buy me a coffee](https://ko-fi.com/eleanorkonik).
%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-10-29%20Supercharged%20tags%20%26%20a%20new%20Zotero%20integration.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-10-29%20Supercharged%20tags%20%26%20a%20new%20Zotero%20integration.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
