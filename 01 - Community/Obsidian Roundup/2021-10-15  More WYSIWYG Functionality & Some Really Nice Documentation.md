---
link: https://www.obsidianroundup.org/2021-10-15/
author: Eleanor Konik
published: 2021-10-16T11:30:00
publish: true
---

# 2021-10-15: More WYSIWYG Functionality & Some Really Nice Documentation
Improved snippet management, a GUI for multi-color highlighting, & chart generation from markdown tables.

## In The Community

-   [Capiche](https://capiche.com/e/final-showdown-obsidian-vs-mem) is doing a "notetaking app showdown" and Obsidian is in the "final showdown" with Mem. Apparently they're a "community for app power users" to crowdsource information about different products instead of relying on marketing-speak.
-   The [Obsidian Hub](https://publish.obsidian.md/hub/00+-+Start+here) community vault is growing exponentially. Most of the Roundup's back issues have been added, along with the Obsidian Awesome project. It does incredible work at consolidating community resources and categorizing plugins and themes.

## Obsidian Updates

-   [Insider v0.12.18](https://forum.obsidian.md/t/obsidian-release-v0-12-18-insider-build/25541)  has a bunch of fixes.
-   [Insider v0.12.19](https://forum.obsidian.md/t/obsidian-release-v0-12-19-insider-build/25666) does too, and also comes with a command for renaming headings instead of always needing to use the context menu.

## Plugin News

### New

-   [Pipe Tricks](https://github.com/marcusolsson/obsidian-pipe-tricks) will convert `[[Apple (fruit)|]]`s into `[[Apple (fruit)|Apples]]` (etc).
-   [MySnippets](https://github.com/chetachiezikeuzor/MySnippets-Plugin) adds a status bar menu for snippet management.
-   [Key Promoter](https://github.com/joethei/obsidian-key-promoter) will tell you the keyboard shortcut of an action when you do something with the mouse. Maybe now I'll actually remember all my shortcuts 😅
-   [Limelight](https://github.com/smikula/obsidian-limelight) spotlights your active pane to make it more obvious which pane you're working in.
-   [Lumberjack](https://github.com/ryanjamurphy/lumberjack-obsidian) lets users jump straight into edit mode on a logging note or daily note.
-   [Mousewheel image zoom](https://github.com/nicojeske/mousewheel-image-zoom) lets you increase or decrease the size of an image.
-   [Highlightr](https://github.com/chetachiezikeuzor/Highlightr-Plugin) adds a menu with pre-defined colors for the `<mark>` html tag to allow for an easier multi-color highlighting experience.
-   [Obsidian Hypothesis](https://github.com/weichenw/obsidian-hypothesis-plugin) syncs highlights from Hypothesis.
-   [Calculator](https://github.com/meld-cp/obsidian-calc) evaluates math expressions right inside your notes using the [Fcaljs](https://github.com/5anthosh/fcal) library.
-   [Link Headers Directly](https://github.com/Signynt/link-headers-directly) hides the file name in preview mode so you only see the heading name. So for example `One of my favorite trees is the [[Trees#Birch]], because it reminds me of spring.` would render in preview as `the Birch, because` instead of `the Trees > Birch, because`

### Updates

-   The new [Image in Editor](https://github.com/ozntel/oz-image-in-editor-obsidian/releases/tag/1.6.0) update only works with the new Insider build for Obsidian, but it now renders MathJax blocks, file transclusions, has better excalidraw support and allows for custom css for the transclusions.
-   [CodeMirror Options 0.3.1](https://github.com/nothingislost/obsidian-codemirror-options/releases/tag/0.3.1) has a ton of new WYSIWYG-supporting features and bugfixes. `@NothingIsLost` is doing incredible things with this plugin. I think the main things this week are better table and inline image support.
-   [Supercharged Links](https://github.com/mdelobelle/obsidian_supercharged_links) got some updates that allow CSS styling of links based on tags and frontmatter. It really extends the functionality of the backlinks pane.
-   [Obsidian Charts](https://github.com/phibr0/obsidian-charts) has some exciting new features including an API that can be used with Dataview, chart generation from markdown tables, and more.
-   [File tree alternative](https://github.com/ozntel/file-tree-alternative) is now much "smarter."
-   [Linter](https://github.com/platers/obsidian-linter) has a bunch of new rules and settings and improvements.
-   [Ghost Fade Focus](https://github.com/skipadu/obsidian-ghost-fade-focus/releases/tag/2.1.0) lets users change opacity levels from the plugin settings.

### Betas

-   [Citation Translation](https://github.com/SkepticMystic/citation-translation) works with the Citations plugin to convert regular in-text citations to Pandoc citations.

### Advanced

-   [Livesync](https://github.com/vrtmrz/obsidian-livesync/) lets users use self-hosted CouchDB or Cloudant server to sync their vault between devices. _This is a beta. Make backups._

### For Developers

-   There have been a bunch of updates to Marcus' [plugin docs](https://marcus.se.net/obsidian-plugin-docs/), which are incredible.
-   Here's a [discussion on Discord](https://discord.com/channels/686053708261228577/840286264964022302/896154025253273600) about how to add plugin dependencies to your plugin.

## Feature Requests

-   A way to [export your vault structure into a note in your vault](http://discordapp.com/channels/686053708261228577/889616783458304001/898623912819191808).
-   A way to filter the graph based on the [number of note links](https://forum.obsidian.md/t/add-the-ability-to-abstract-note-details-based-on-the-number-of-links/25619).

## Appearance

-   There's a new [Sodalite](https://github.com/tomzorz/Sodalite) theme for Obsidian. Dark mode only.
-   This [Agora theme](https://github.com/Seraaron/agora-obsidian-theme) is designed to be used with the Agora TTRPG
-   The new [Faded](https://github.com/JoshKasap/Obsidian-Faded-Theme) theme  has some nice advanced sliding panes support.
-   Amethyst now comes in [Emerald](https://github.com/gracejoseph1236/obsidian-emerald).
-   `@Kepano` is looking for users of Minimal to [share screenshots and use-cases](https://forum.obsidian.md/t/share-your-minimal-theme-screenshots-configuration/8983/99) to help focus improvement on things people care about.
-   Here's some [fancy emoji markers and highlighting](http://discordapp.com/channels/686053708261228577/722584061087842365/898089959339200572) codes based on tags.

## Guides

-   My community talk about [project management in Obsidian](https://youtube.com/watch?v=F4LE-nIzefM) is live on YouTube. I focused mostly on fiction, but it's a comprehensive overview of my workflow from beginning (ideation) to end (tracking the marketing for a finished product).
-   Here's a new and very comprehensive [getting started" guide for PKM in Obsidian](https://www.nickseitz.com/writing/obsidian-day-one-starterpack) from `@_Nick`
-   `@ryanjamurphy` put together a guide to creating [an Obsidian homescreen](https://axle.design/an-obsidian-homescreen-for-iphone-and-ipad) for iOS. It includes detailed instructions for each of the shortcuts and a video walkthrough of what it looks like to use each button/widget.
-   `@joshduffney` tried out a paper [[Zettelkasten]] and then re-read _How to Take Smart Notes_ to get a better understanding of the practice and shared his new understanding [on YouTube](https://www.youtube.com/watch?v=OP2WnLgvYBs).
-   Here's a guide for [how to build a plugin using Svelte](https://marcus.se.net/obsidian-plugin-docs/guides/svelte).

## Discussions

-   Here's a really nice discussion on Reddit about [worst practices](https://www.reddit.com/r/ObsidianMD/comments/q60d1c/are_there_any_bad_ideapractices_for_obsidian_that/) in Obsidian, i.e. things that might seem like a good idea to a beginning user but will run them into trouble down the line. There was good discussion about using Obsidian as a "task manager" too.
-   Here's another nice one on Reddit about [making daily notes useful](https://www.reddit.com/r/ObsidianMD/comments/q8nj34/how_do_you_make_daily_notes_useful/).
-   [Reddit discusses future proofing and Obsidian](https://www.reddit.com/r/ObsidianMD/comments/q7aimp/how_futureproof_is_in_fact_obsidian/).

## Ancillary Tools

-   [Keypoints](https://keypoints.app/) is a forthcoming macOS PDF Annotation Extracting App. The plan is for it to save annotations locally as markdown files. You can sign up to get alerts.

## Housekeeping

-   Sorry I sent this early last week — I know I confused a couple of people! I hit the wrong button in Ghost because I was in a hurry, totally my own fault.
-   If the lack of dark mode for the Obsidian Roundup website has been annoying you, please buy `@phibr0` [a coffee](https://www.buymeacoffee.com/phibr0), because he fixed the [Roundup's CSS](https://www.obsidianroundup.org/) so that it updates based on your system preferences (and made a few other tweaks that I have been putting off).
-   I did not forget about the topia community coworking space, but we ran into some technical limitations that didn't get caught in testing (we uh, we have more than 9 people who show up to events). I have some meetings with various software folks next week to see if we can't find something that works for the numbers of people who show up. Most stuff seems geared mostly for workplaces or conventions? If you have any recommendations please reach out!

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-10-15%20%20More%20WYSIWYG%20Functionality%20%26%20Some%20Really%20Nice%20Documentation.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-10-15%20%20More%20WYSIWYG%20Functionality%20%26%20Some%20Really%20Nice%20Documentation.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
