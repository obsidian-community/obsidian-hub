---
link: https://www.obsidianroundup.org/2022-01-29/
author: Eleanor Konik
published: 2022-01-29T13:30:00
publish: true
---

# 2022-01-29: 5x8 Virtual Event, Persistent Graph Layouts, & New Category Visualizations
The Gems of the Year were announced, Obsidian won ProductHunt's Golden Kitty, we're now tracking plugin/theme compatibility, & there's improved code block behavior available. 

## In The Community

-   The [results of Gems of the Year 2021](https://obsidian.md/goty2021) have been posted. I am deeply honored to have been voted Content Creator of the year and to have had the top achievement. Thank you to everyone who voted 💚 but also, go check out the other awesome stuff this community has done! Several winners donated parts of their prizes to active & helpful members of the community, which has been heartwarming.
-   There have been lots of questions about whether particular plugins work on mobile or Live Preview. There's now a [community Google Sheet to track plugins _and_ themes](http://www.tinyurl.com/obsidian-community) that can be updated by community members and developers for _basic_ data. If you've been looking for a way to help out but don't have time to maintain a plugin or theme, this is a great way.
-   The Discord server now has 50,000 members. 🤯

## Obsidian Updates

-   0.13.23, which includes  [v0.13.20](https://forum.obsidian.md/t/obsidian-release-v0-13-20-insider-build/30790), [v0.13.201](https://forum.obsidian.md/t/obsidian-release-v0-13-21-insider-build/30799), [v0.13.22](https://forum.obsidian.md/t/obsidian-release-v0-13-22-insider-build/31304), & [v0.13.23](https://forum.obsidian.md/t/obsidian-release-v0-13-23/31439), is now available for public access. This release is mostly focused on improvements and bugfixes for Live Preview, but my favorite little thing is that they added an option in community plugin pane to help debug slow plugin startup times. This should make it easier for people whose vaults feel like they're opening slowly to figure out which plugin is the culprit.

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list. Licat had a busy week! You may have read about some of these as betas last week, but they're now available in community plugins, so I'm mentioning it again._

-   [Obsidian shortcut launcher](https://github.com/macstories/obsidian-shortcut-launcher) runs iOS shortcuts as Obsidian commands. Federico Viticci wrote about [how much the shortcut launcher changed how he uses Obsidian](https://www.macstories.net/stories/obsidian-shortcut-launcher/).
-   [Sortable](https://github.com/alexandru-dinu/obsidian-sortable) by `@alexandru-dinu`  offers wiki-like table sorting. Note that this is similar to functionality offered by the  [Advanced Tables Plugin](https://github.com/tgrosinger/advanced-tables-obsidian). Sortable works more like Wikipedia (and works with dataview tables), whereas Advanced Tables works more like excel. Sortable won't change the actual markdown, Advanced Tables will.
-   [Snippetor](https://github.com/ebullient/obsidian-snippetor) by `@ebullient`  lets users create and tweak common snippets (starting with custom tasks). The goal with this plugin is to make styling `- [?]` sorts of data-task icons consistent across themes according to user preference.
-   [Dynamic Highlights](https://github.com/nothingislost/obsidian-dynamic-highlights) by `@nothingislost`  lets users dynamically highlight text based on cursor selection or search query with full regex, mobile, and live preview support.  There's also a built-in CSS editor that allows for attaching CSS styles directly to highlighters.
-   [ObsidianTweaks](https://github.com/JeppeKlitgaard/ObsidianTweaks) by `@JeppeKlitgaard`  adds some convenient tweaks including improved toggling and ergonomic commands.
-   [PARA Shortcuts](https://github.com/gOATiful/para-shortcuts) by `@gOATiful`  makes it easy to archive and un-archive files.
-   [Local File Interface](https://github.com/qawatake/obsidian-local-file-interface-plugin) by `@qawatake`  provides commands for moving files in and out of the vault, sort of like how you can use a "browse" menu on a web-based file picker to "import" files into, for example, a photo album. It's nice if you want to avoid leaving the Obsidian workspace to go find a file.
-   [Obsidian Memos](https://github.com/Quorafind/Obsidian-Memos) by `@Quorafind`  is a plugin for quickly capturing ideas in Obsidian. [1.7.0](https://github.com/Quorafind/Obsidian-Memos/releases/tag/1.7.) added support for sharing. 1.7.9 allows users to copy and paste the results of queries and searches.
-   [Completr](https://github.com/tth05/obsidian-completr) by `@tth05`  plugin provides advanced auto-completion functionality, similar to how [Various Complements](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin) works. The main difference is in how they handle LaTeX.

#### Sync External Tools

-   [Siteswap](https://github.com/tdresser/obsidian-siteswap) by `@tdresser`  is useful for jugglers.
-   [Weather Fetcher](https://github.com/fyears/weather-fetcher) by `@fyears`  will fetch and insert current weather into the editor of Obsidian.
-   [Wordle](https://github.com/dbarenholz/obsidian-wordle) by `@dbarenholz`  creates a view where you can play Wordle.
-   [Pinboard Sync](https://github.com/Automatt/obsidian-pinboard-sync) by `@Automatt`  syncs Pinboard.in links with Daily Notes
-   [KOReader Highlights](https://github.com/Edo78/obsidian-koreader-sync) by `@Edo78`  syncs highlights and notes taken in KOReader.

#### Advanced

-   [Link Server](https://github.com/moelody/link-info-server) by `@moelody`  will open a reverse proxy server at port 3333 to get wikiLink information Obsidian API.
-   [Binary File Manager](https://github.com/qawatake/obsidian-binary-file-manager-plugin) by `@qawatake`   will detect new binary files in the vault and create markdown files with metadata.

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Remember, though, this is not as safe as waiting for them to go through code review._

-   [Frontmatter Tag Suggest](https://github.com/jmilldotdev/obsidian-frontmatter-tag-suggest) by `@jmilldotdev`   autocompletes tags in the YAML tags field, which is an excellent quality of life improvement — I've heard a ton of people complain about this and have always been a little surprised it wasn't a core feature.
-   [Better Command Palette](https://github.com/AlexBieg/obsidian-better-command-palette) by `@AlexBieg`  helps slash commands prioritize recent commands, lets users backspace to close, supports opening a new file, and file creation.
-   [Simple note quiz](https://github.com/dorisxx/Obsidian-simple-note-quiz) by `@dorisxx`  lets users create quizzes in their notes, similar to Anki cards, except it'll also grade your answers.
-   [Multi-Column Markdown](https://github.com/ckRobinson/multi-column_markdown) by `@ckRobinson`  adds functionality to create markdown documents with multiple columns of content viewable within Obsidian's preview mode
-   [Copy as HTML](https://github.com/jenningsb2/copy-as-html) by `@jenningsb2`  converts  selected markdown to HTML and copies it to the clipboard.
-   [Code Block Labels](https://github.com/stbowers/obsidian-codeblock-labels) by `@stbowers`  adds labels to fenced code blocks so that you can, for example, "title" a code block. It does not currently plan to support Live Preview.

#### Advanced

-   [Save as Gist](https://github.com/ghedamat/obsidian-save-as-gist) by `@ghedamat`   lets you save your current note as a Gist on GitHub.
-   [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) by `@coddingtonbear`  lets users get, change or otherwise interact with Obsidian notes via a REST API.

### Betas

-   You can now drag and recorder icons on the ribbon bar and status bar (desktop & mobile) with the new [Bartender](https://github.com/nothingislost/obsidian-bartender)  plugin. It also has hide/collapse functionality.
-   [Codeblock Completer](https://github.com/SkepticMystic/codeblock-completer) adds an editor suggestor modal for you to quickly complete codeblock names, i.e. autocomplete admonitions.
-   [Persistent Graph](https://github.com/Sanqui/obsidian-persistent-graph) lets users **save and restore the locations of nodes on your graph**. This has been a long-requested feature, but note that the developer is not planning to submit it to the community list because it relies on some potentially unstable APIs.

### Updates

-   [Templater 1.10.0](https://github.com/SilentVoid13/Templater) now supports user functions (i.e. can now run JS templater scripts) on mobile.
-   Tag Wrangler 0.5.0 now has [support for tag pages](https://github.com/pjeby/tag-wrangler/#tag-pages).
-   [Breadcrumbs](https://github.com/SkepticMystic/breadcrumbs/blob/master/CHANGELOG.md) now supports [juggl codeblocks](https://github.com/SkepticMystic/breadcrumbs/wiki/Codeblocks) and [juggl view](https://github.com/SkepticMystic/breadcrumbs/wiki/Views#juggl-view). This is enough of a game-changer that I'm planning to devote a chunk of February to integrating this with my slipbox along with the [Linked Data Vocabularies](https://github.com/kometenstaub/obsidian-linked-data-vocabularies) plugin and [this script to automatically generate a file for each header of a controlled vocabulary](https://discord.com/channels/686053708261228577/710585052769157141/936303111323127838) (there's also one for [creating folders](https://forum.obsidian.md/t/lcc-automatic-folder-creation/31406)).
-   [Longform](https://github.com/kevboh/longform/) 1.1.0  revamped the Compile feature that lets you build custom workflows to turn your projects into compiled manuscripts. There's new support for user scripts. Find out more [from the compile documentation](https://github.com/kevboh/longform/blob/main/docs/COMPILE.md).
-   [Emoji Toolbar v0.3.0](https://github.com/oliveryh/obsidian-emoji-toolbar) supports skin tones, has fuzzy search functionality, and lets users select recently used emojis.
-   [Remotely-save](https://github.com/fyears/remotely-save) got some bugfixes and now lets users trigger sync using a command.
-   Various Complements 5.5.0 has [new documentation](https://tadashi-aikawa.github.io/docs-obsidian-various-complements-plugin/), support for multi-word completions, improved suggestions, and better handling of yaml and code blocks.
-   [Obsidian Map View](https://github.com/esm7/obsidian-map-view) has a bunch of new features, including dark mode and the ability to switch map sources.
-   [TTRPG Statblocks v2.0](https://github.com/valentine195/obsidian-5e-statblocks) involved a rewrite of the entire rendering engine, which makes it faster and more consistent. Users can also create their own statblock layouts, integrate with dice roller, create a bestiary from frontmatter, and a ton of other awesome updates for tabletop gamers. This involves a **breaking change** for Initiative Tracker, which no longer handles homebrew creatures because that got moved to Statblocks.
-   [Supercharged Links](https://forum.obsidian.md/t/supercharged-links-showcase/18219) got a big performance update and now lets you supercharge your quick switcher, links suggestor, and backlinks in document.

### For Developers

from [v0.13.22](https://forum.obsidian.md/t/obsidian-release-v0-13-22-insider-build/31304):

-   Added: an option in community plugin pane to help debug slow plugin startup times.
-   Fixed: `editorLivePreviewField` not dynamically updated when Live preview is turned on/off.
-   Added data-type to tab header elements.

## Feature Requests

-   Here's a nice [article about migrating from Roam and what aspects of web-based outliners feel "missing" from the Obsidian experience](https://arborcogitandi.com/blog/migrating-from-roam-to-obsidian-my-experience).

## Appearance

-   Here's an example of a [pdf stylesheet](https://forum.obsidian.md/t/a-pdf-stylesheet-example/31345) to make exporting to PDF a bit nicer.
-   [Primary](https://github.com/ceciliamay/obsidianmd-theme-primary/releases/tag/v.1.0.0) now has Live Preview support and a bunch of fixes. The developer's birthday is tomorrow, by the way — here's her [ko-fi page](https://ko-fi.com/ceciliamay).
-   Shimmering Focus (the most aggressively "minimalistic" theme I'm aware of) now has [a full-blown documentation site](https://chrisgrieser.github.io/shimmering-focus/) to showcase & explain all its features — including sidebar navigation & full-text search.
-   [ITS Theme](https://github.com/SlRvb/Obsidian--ITS-Theme/) got some restylings and the ability to toggle off alternate checkboxes to support the Snippetor plugin.
-   Minimal [4.4.4](https://github.com/kepano/obsidian-minimal/releases/tag/4.4.4) & [4.4.5](https://github.com/kepano/obsidian-minimal/releases/tag/4.4.5) added more support for cards, style settings, and progress bar styling.
-   [Cyber Glow v6.4](https://github.com/ArtexJay/Obsidian-CyberGlow) added support for Live Preview and some other small improvements.
-   [Sanctum v0.6.1](https://github.com/jdanielmourao/obsidian-sanctum/releases/tag/v0.6.1) got a big update. It now handles strike-throughs differently, has support for new table styles and the Indentation Guides plugin, and are also now toggleable to support the Snippetor plugin.
-   Prism v1.3.1 has better calendar support. [1.4.0](https://github.com/damiankorcz/Prism-Theme/releases/tag/1.4.0) now supports Icon Folder and Map view.

## Ancillary Code

-   Here's a script to create [a folder structure according to Library of Congress Classification](https://forum.obsidian.md/t/lcc-automatic-folder-creation/31406).
-   Here's a neat little [timeline for your daily note](https://forum.obsidian.md/t/svg-year-timeline-in-your-daily-note/31418) that shows how far into the  year we are.
-   There now exists [a script](https://discord.com/channels/686053708261228577/840286238928797736/934479341579038731) (in Discord) to support a process by which dataview renders a table, buttons puts a button in the table, you can click the button, Templater will prompt you for a date, and Natural Language Dates gives Meta Edit a properly formatted number to update the YAML of the specified note with. This lets you easily update notes from a dataview table.

## Courses & Consulting

-   Bianca Pereira, along with "Linking Your Thinking", is offering [3 scholarships for Masters and PhD students for their upcoming workshop](https://www.getrevue.co/profile/bianca_oli_per/issues/the-hidden-rules-of-academia-by-bianca-pereira-issue-2-992687). The deadline to apply is end of day Sunday anywhere on Earth. Her new newsletter is designed to [help academics navigate academia](https://www.getrevue.co/profile/bianca_oli_per).
-   Curtis McHale announced a [new 4-week cohort course](https://curtismchale.ca/make-better-connections/). It's designed to help people focus on making connections.
-   I set up a page to facilitate one-on-one [consultations](https://www.obsidianroundup.org/consult/). **If you want me to hop on Zoom and help you with something related to Obsidian, notetaking, writing, or knowledge management, you can now book directly to my calendar.** Spots are limited right now, but I'll adjust depending on how things go.

## Guides

-   Here's a guide for [Creating your own Obsidian iOS Widget](https://tfthacker.medium.com/creating-your-own-obsidian-ios-widget-b2320268ab6f).
-   Here's a discussion about how to get [averages and sums from Dataview](https://forum.obsidian.md/t/is-there-a-good-tutorial-on-how-to-do-averages-and-sums-in-dataview/31372/2).
-   Here's [documentation for the process of figuring out what kinds of notes and tags worked for one individual](https://forum.obsidian.md/t/a-process-for-figuring-out-what-organizational-tags-i-need-in-my-vault/31221).
-   Here's a guide on [how to make use of the graph view](https://youtu.be/4T0q2kQwc2o).

## Discussions

-   Here's an [interesting discussion about having one big "daily notes" file](https://www.reddit.com/r/ObsidianMD/comments/scdgo6/practically_paperless_with_obsidian_episode_15_is/), instead of individual daily notes. It also discusses some standardizations that help with search.
-   Here's a lengthy (and really insightful, brass-tacks) discussion from HackerNews about [why programmers & developer-adjacent communities seem really into notetaking lately](https://news.ycombinator.com/item?id=30098219).

## In The Wild

-   Obsidian won the [Golden Kitty Award](https://www.producthunt.com/posts/obsidian-for-mobile) for best mobile app over at ProductHunt, yay!
-   Here's a nice metaphor about how Obsidian works, as part of a longer piece on using python to manipulate your notes:  [many programs build a fence and give you a few gates through it. Obsidian avoids building the fence](https://birrellwalsh.medium.com/obsidian-data-without-fences-58f3dcdc1d10)

## Ancillary Tools

-   Here's some information about [why iCloud sometimes causes problems](https://9to5mac.com/2022/01/24/icloud-syncing-issues-are-plaguing-third-party-apps-as-apple-stays-silent/); the issue is not limited to Obsidian.
-   One of my biggest pain points about having multiple vaults open is that, unlike when I have two Chrome profiles open, my vaults get grouped on my taskbar as one item. It turns out that Windows has an option to disable this in Windows 10. Here's [a utility](https://github.com/valinet/ExplorerPatcher) to get the old-school taskbar where you can actually see each "window" — which makes it much easier to work with nested vaults 🥳 Don't laugh, but **this was the biggest find for me this week personally**.
-   A couple of people have asked [how to get spreadsheets and HTML tables into Obsidian](https://www.reddit.com/r/ObsidianMD/comments/se2dw7/google_spreadsheets_to_obsidian/) and there are a couple of answers depending on what you're doing, so I thought I'd share the discussion.
-   Here's [an in-browser text editor to easily create static html pages](https://triplelog.com/writer/) from markdown, which looks handy for one-off sharing of files if you don't want to be fussed with pandoc.
-   [Heyday](https://heyday.xyz/) is a subscription-based memory aid app that is designed to give you a daily summary of what you looked up and resurface useful content in the context you might need it again. I haven't tried it, but it apparently indexes documents, emails, and messages and sort of serves as a search companion to remind you of stuff you already found.
-   Here's a list from Discord of [useful tools and generators](https://discord.com/channels/686053708261228577/916477002909876265/935197818962993243).

## Housekeeping

Since last week, when I announced that I'm exploring the idea of not going back to work teaching in the fall, things have been pretty exciting.

My article about [why folders shouldn't be villainized](https://eleanorkonik.com/yet-another-hot-take-on-folders-versus-tags/) got featured in The Browser (which has like 75k subscribers), and then hit [the front page of HackerNews](https://news.ycombinator.com/item?id=30063301). As exciting as this is (front page of HackerNews is literally a dream come true — people in my "personal life" got to see one of my articles "in the wild"), the traffic spike also crashed my website and I had to figure out [Cloudflare caching](https://support.cloudflare.com/hc/en-us/articles/360021806811-Getting-Started-with-Cloudflare-Caching) on the fly.

Also, almost 10% of Roundup subscribers have upgraded to a paid plan, which is about what Substack says is what a "high quality" newsletter can expect (although apparently I'm underpriced, oops). I am very encouraged by this! In addition to [opening up my calendar for helping people in 30min one-on-one sessions](https://www.obsidianroundup.org/consult/), Tuesday morning (EST) I'm planning to combine the best parts of a book club, a 5x15 event (5 speakers, 15 minutes each) and a powerpoint party. The event will be hosted on Zoom.

[LEARN MORE](https://www.obsidianroundup.org/thank-you-wanna-hop-on-zoom/)

I have a steep road ahead of me before I can meaningfully replace my teaching income by working from home, but the guideposts are well-marked and my fellow travelers have been very kind. Thank you 💚

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-01-29%205x8%20Virtual%20Event%2C%20Persistent%20Graph%20Layouts%2C%20%26%20New%20Category%20Visualizations.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-01-29%205x8%20Virtual%20Event%2C%20Persistent%20Graph%20Layouts%2C%20%26%20New%20Category%20Visualizations.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
