---
link: https://www.obsidianroundup.org/2021-05-15/
author: Eleanor Konik
published: 2021-05-15
publish: true
---

# 2021-05-15: Better Footnotes, Plugin Synergy, & an Electron Update
New showcases, typography convos & lots of great knowledge management discussions. New plugins like incremental writing, inline variable support, & OCR support via Templater.

## In The Community

- There is a new [when2meet](https://www.when2meet.com/?11861492-Aihza) link for `@bri`'s [Knowledge Organization in Obsidian](https://forum.obsidian.md/t/knowledge-organization-cataloging-and-classification-in-obsidian-community-talk-by-brimwats/) talk, which we needed to reschedule from next week to the 1st or 2nd week in June:
- You can still [vote for a time slot](https://www.when2meet.com/?11752321-UHqgS) for `@phnx`'s [Deep Learning on Networks](https://forum.obsidian.md/t/deep-learning-on-networks-community-talk-by-phnx/).
- If you're interested in a Discussing [[Spaced repetition|Spaced Repetition]] talk/discussion by `@Jamesb`, please vote [here](https://forum.obsidian.md/t/obsidian-talks-voting-post-which-talks-do-you-want-to-hear/15705/40):

## Obsidian Updates

- v0.12.3 rolled out to the public. It bundles [12.0](https://forum.obsidian.md/t/obsidian-release-v0-12-0/16809), [12.1](https://forum.obsidian.md/t/obsidian-release-v0-12-1/16904), [12.2](https://forum.obsidian.md/t/obsidian-release-v0-12-2/17602), and [12.3](https://forum.obsidian.md/t/obsidian-release-v0-12-3/17957). Highlights include better plugin management, the ability to pin commands in the command palette, and improvements to search. "Backlinks in document" is now a core feature.
- The biggest news is that you should grab the new installer from [the website](https://obsidian.md/) because there was an Electron update that has a bunch of security and speed improvements.

## Plugin News

### New

- [[better-fn|Better Footnotes]] is pending review for admission into the community plugins list, but the long-awaited feature of getting preview-on-hover for footnotes is finally here (and I am HYPE).
- The [[obsidian-incremental-writing|Incremental Writing]] plugin (in the community plugins list, doesn't require manual install). There are a bunch of great videos
- [Inline Variables](https://github.com/flip-md/obsidian-inline-variables) allows the setting, referring, and rendering of inline-variables in real-time. Requires manual install.
- [[supercharged-links-obsidian|Supercharged Links]] allows for customization of internal links based on the target note's front-matter attributes. It also lets you trigger Array, Boolean and Number in front-matter values to style your internal links. There is a [showcase](https://forum.obsidian.md/t/supercharged-links-showcase/18219) on the forum.

### Updates

- [[buttons]] had a big update, with a nifty button maker command, inline buttons, and the ability to put a [[templater-obsidian|templater]] command inside of a button.
- [[dataview|Dataview]]'s new `link(url, alias)` function allows you to create aliased wikilinks ([example](http://discordapp.com/channels/686053708261228577/840286238928797736/840599798176022529) via `@SkepticMystic`). The `contains(key,value)` function is also pretty useful if you have more than one value possible for a key and therefore can't use `where x = y`.
- There's a new [showcase](https://forum.obsidian.md/t/buttons-showcase/18044) for the [[buttons]] plugin.
- [v0.0.7](https://github.com/renehernandez/obsidian-readwise/releases/tag/0.0.7) of the [[obsidian-readwise|Readwise Community]] plugin lets you configure a sync interval so that the plugin will pull new highlights from Readwise every X hours.
- The [[obsidian-spaced-repetition|Spaced Repetition]] plugin now has support for flashcard decks.
- [[obsidian-tracker|Tracker]] [v1.4.0](https://github.com/pyrochlore/obsidian-tracker) has better support for chart scaling and positioning.
- [[hotkey-helper|Hotkey Helper]] [0.3.2](https://github.com/pjeby/hotkey-helper) has an enhanced plugin browser.
- [[obsidian-kanban|Kanban]] [v0.3.0](https://github.com/mgmeyers/obsidian-kanban/discussions/89) has some bugfixes and added time picker & time support.
- There's a new plugin that adds [[obsidian-org-mode|Org Mode]]support for Obsidian.

### Magic

- `@zsviczian` figured out how to [leverage dataviewjs with the excalidraw plugin to automagically generate mind map graphics](https://discord.com/channels/686053708261228577/840286238928797736/840606013341696040). Similar magic can be used to create [family tree graphics](https://discord.com/channels/686053708261228577/840286238928797736/840644541270982716).
- `@Mara` created a [script for espanso](https://discord.com/channels/686053708261228577/694233507500916796/841422069694201896) to make using the admonition plugin even easier.
- `@ryanjamurphy` combines [[dataview|Dataview]], [[templater-obsidian|templater]], and kanban boards to [automate the creation of linked lists for kanban](https://discord.com/channels/686053708261228577/840286238928797736/841745942025207857). There's also a [simpler version](https://discord.com/channels/686053708261228577/840286238928797736/841779336398504017) that leverages only kanban and core features.
- `@ryanjampurphy` also shared [a way to use dataviewjs to dynamically show past and future tasks in your daily notes](https://discord.com/channels/686053708261228577/840286238928797736/842152590379712563).
- `@pmbauer` figured out how to do [basic OCR with Templater](https://forum.obsidian.md/t/basic-ocr-in-obsidian/18087), which might actually be the the thing that makes me try out [[templater-obsidian|Templater]].

### Under the Radar

- This plugin lets you [[convert-url-to-iframe|easily convert a URL into an iframe]].
- [[obsidian-hotkeys-for-specific-files|Hotkeys for specific files]] by `@Vinadon` does exactly what it claims to, and is probably really nice for keyboard-first users.

### For Developers

- `manifest` defines which version to look for as the latest version, while `versions` defines which version works with which Obsidian version. (Thanks, `@zsviczian`!)
- `@Liam` shared the `obsidian-daily-notes-interface` lib, which handles lookups and weird edge cases for date formats and supports the Periodic Notes plugin.
- Obsidian uses [Icons8](https://icons8.com/) for icons. It's a membership, but if developers need an icon for a plugin that Obsidian doesn't currently support, `@Silver` is willing to add them. (Discussion [here](https://discord.com/channels/686053708261228577/840286264964022302/841732418439610388)). Here is the [list of icons currently available](https://github.com/obsidianmd/obsidian-api/issues/3#issuecomment-724665569). `@Chetachi` recommends anyone needing icon use [Iconify](https://iconify.design/icon-sets/) & the [Icon Swapper plugin](https://forum.obsidian.md/t/obsidian-icon-swapper-plugin/17539).

## Workflow Stuff

- `@mktahmasbi` had a tip for [how to import highlights](http://discordapp.com/channels/686053708261228577/694233507500916796/841790522397294623) from Google Play Books using UltraEdit.
- There was a really nice [example](http://discordapp.com/channels/686053708261228577/702656734631821413/840937390498775062) of how to pair the Admonition plugin with reference notes from `@Chetachi`
- This GitHub discussion showcases `@dork`'s setup for [getting hypothes.is notes into Obsidian](https://github.com/out-of-cheese-error/gooseberry/discussions/73).

### Mobile

- `@Vinadon` was able to use MGit with their vault, although it's not automatic (requires manual push/pull, but it has GUI buttons so you don't have to mess with the command line on your phone).
- `@ankushg` uses [Toolbox Pro](https://toolboxpro.app/) (the free version) to get into the dotfolders (i.e. `.obsidian`) on iOS.

## Feature Requests

- [Folder Nodes on Graph View](https://forum.obsidian.md/t/folder-graph-view/4641) has 25 upvotes on the forum, and I'm resurfacing it rather selfishly because it's something I've been wanting for awhile, as someone who does a lot with folders.
- There's been some interest around functionality to make it easier to [resurface old notes](https://forum.obsidian.md/t/note-aging/467/11).

## Appearance

- `@Blund` shared a reminder that [html symbol codes](http://cactus.io/resources/toolbox/html-symbol-codes) (like `&rarr;` for &rarr; ) work in Markdown.
- `@Chetachi` shared a `.css` file that includes all of [the codes for changing things around on the graph](http://discordapp.com/channels/686053708261228577/702656734631821413/841353144856084500).
- There were a lot of typography & font discussions this week; here's a link to the [forum thread](https://forum.obsidian.md/t/your-favourite-fonts-choice-and-why-thread/18129) on the topic. `@Korban` also shared some [typography resources](http://discordapp.com/channels/686053708261228577/702656734631821413/842671647550078996).
- The forums had a handy writeup about [how to add Google fonts to theme CSS](https://forum.obsidian.md/t/fyi-how-to-add-google-fonts-to-any-themes-css/18115).
- You can use `Ω` to sort files to the _bottom_ of a list, similar to how `!` usually will get something at the top of your file list.
- You can use [anchor links](https://www.reddit.com/r/ObsidianMD/comments/nbbskz/anchor_links/) in Obsidian to jump to a particular subheading. Incidentally, this also works for the roundup!

## Knowledge Management

- There was a nice discussion about [the dangers of 'reading like an academic' when you're not actually an academic'](http://discordapp.com/channels/686053708261228577/710585052769157141/840298881462960138) and how "productivity culture" can inhibit enjoyment and depth of learning.
- There was a nice discussion about how to [get started writing an essay](https://discord.com/channels/686053708261228577/722584061087842365/840989959053246495).
- There was an interesting discussion about [the difference between an index and a MOC](http://discordapp.com/channels/686053708261228577/710585052769157141/841885329572495360).
- There was a fascinating discussion about [how to take notes for inherently visual mediums](http://discordapp.com/channels/686053708261228577/710585052769157141/842458593444888636) like choreography.
- There was a nice discussion of [how to use Obsidian as a law student](https://www.reddit.com/r/ObsidianMD/comments/n8g5zs/looking_for_a_law_school_example_using_obsidian/) over on Reddit.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- [iris.ai](https://iris.ai/) came up as a useful research tool with a nifty GUI for tracking down articles related to a starting point.
- [Nebo](https://www.nebo.app/) is a mobile app with excellent handwriting detection, it can indent bullet points and exports well to clipboard, allowing for easy pasting into Obsidian.
- A lot of people enjoyed this [color palette generator](https://coolors.co/generate) for creating color schemes for graphs and folders and such.
- [LiquidText](https://www.liquidtext.net/) was recommended as a great tool for projects, as it allows for the opening of multiple PDFs in a single "project" and has a nice highlighting app.
- You can use [AutoHotKey](https://www.autohotkey.com/) to rebind the `insert` key to do literally anything else, which I highly recommend based on how often people think that its behavior of deleting everything after the cursor as you type is an Obsidian bug.
- `@koala` created a [CSV to Markdown converter](https://github.com/kometenstaub/csv-to-md).

## Housekeeping

- I added some [resources for beginners](https://obsidianroundup.org/resources/#for-beginners) to the Resources portion of the roundup.
- I also added some resources for [personal knowledge management](https://obsidianroundup.org/resources/#personal-knowledge-management).
- I've been making more of an effort to engage with folks over on [Twitter](https://twitter.com/EleanorKonik) about Obsidian-related things, if that's a place you prefer to interact.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-05-15%20Better%20Footnotes%2C%20Plugin%20Synergy%2C%20%26%20an%20Electron%20Update.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-05-15%20Better%20Footnotes%2C%20Plugin%20Synergy%2C%20%26%20an%20Electron%20Update.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
