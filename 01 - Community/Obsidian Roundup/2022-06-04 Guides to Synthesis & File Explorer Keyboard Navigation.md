---
link: https://www.obsidianroundup.org/2022-06-04/
author: Eleanor Konik
published: 2022-06-04T12:30:00
publish: true
---

# 2022-06-04: Guides to Synthesis & File Explorer Keyboard Navigation
Lots of exciting updates and forks of the Tasks plugin, a quickstart guide for Breadcrumbs, & new zettelkasten discussions.

## In The Community

-   I'm working on collecting resources for [using Obsidian for spiritual purposes & religious studies](https://github.com/obsidian-community/obsidian-hub/issues/449) if you can think of any I missed, please consider adding them to that issue so we can get them collected on the Hub. There's a similar collection for [medical discussions & guides](https://github.com/obsidian-community/obsidian-hub/issues/369). If you've got some time and want to help out with the Hub, turning those issues into a useful note is a great way to get started.

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list._ For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new).

-   [Advanced Codeblock](https://github.com/lijyze/obsidian-advanced-codeblock) by `@lijyze`  adds line numbers and line highlights to code blocks.
-   [Simple Dice Roller](https://github.com/yeeshue99/SimpleDiceRoller) by `@yeeshue99`  is a _simple_ plug and play solution that allows you to average and simulate dice formulas.
-   [Copy Image and URL in Preview](https://github.com/NomarCub/obsidian-copy-url-in-preview) by `@NomarCub`  can copy images and URLs, as well as open PDFs externally using the context menu in preview mode.
-   [Booksidian](https://github.com/MichaBrugger/booksidian_plugin) by `@MichaBrugger`  can connect Obsidian to your Goodreads.
-   [Obsidian Camera](https://github.com/aldrinjenson/obsidian-camera) by `@aldrinjenson`  lets users take photo and video recordings and have them saved in vault, and create and paste links to the recording automatically if a markdown file is open.
-   [Expand Bullet](https://github.com/Quorafind/Obsidian-Trans-Them) by `@Quorafind`  lets users transform bullet contents into individual notes.
-   [ExcaliBrain](https://github.com/zsviczian/excalibrain) by `@zsviczian`  is a clean, intuitive and editable graph view for Obsidian
-   [Media DB Plugin](https://github.com/mProjectsCode/obsidian-media-db-plugin) by `@mProjectsCode`  can query multiple APIs for movies, series, anime, games, music and wiki articles, and import them into your vault.
-   [Packrat](https://github.com/therden/packrat) by `@therden`  makes it easier to process completed recurring Tasks
-   [Note Auto Creator](https://github.com/SimonTC/obsidian-note-autocreation) by `@SimonTC`  will automatically create notes when links are created to them. It also now lets users trigger link insertion with a character like `@` and automatically create a new note when inserting a link to a non-existing note. It also supports applying Templater templates to new notes.
-   [State Switcher](https://github.com/lijyze/obsidian-state-switcher) by `@lijyze`  adds a graphical user interface for changing YAML metadata more safely.
-   [Sequence Hotkeys](https://github.com/moolmanruan/obsidian-sequence-hotkeys) by `@moolmanruan`  lets users set hotkeys with key sequences instead of a single chord.
-   [Local Quotes](https://github.com/ka1tzyu/local-quotes) by `@ka1tzyu`  collects your quotes from all over the repository and embed them in different locations with refresh delays.
-   [Obsidian Functionplot](https://github.com/leonhma/obsidian-functionplot) by `@leonhma`  is another plugin for displaying mathematical graphs in obsidian.
-   [Bellboy](https://github.com/shakedlokits/obsidian-bellboy) by `@shakedlokits`  automatically renames files with `kebob-case` based on the first header.
-   [DB Folder](https://github.com/RafaelGB/obsidian-db-folder) by `@RafaelGB`  gives users the capability to store and retrieve data from a folder like database. It's intended to feel Notion-like. It's up to 1.5.0 now and has a new "file task" column, supports checkbox columns, sorting improvements, and support for frontmatter arrays.

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [obsidian echarts](https://github.com/cumany/obsidian-echarts) by `@cumany`  allows users to render apache echarts in Obsidian.
-   [Stack Overflow Answers](https://github.com/bramses/obsidian-stack-overflow) by `@bramses`  is exactly the sort of thing I expect to see from this community 😂 it lets you copy and paste stack overflow answers directly into Obsidian using their "share" link.
-   [Linkify](https://github.com/matthewhchan/linkify) by `@matthewhchan`  lets users set up regex patterns to automatically turn matching text into links, for example everything prepended with `@` to become a link to twitter or github.
-   [Table to CSV Exporter](https://github.com/metawops/obsidian-table-to-csv-export) by `@metawops`  allows for exporting tables from a pane in reading mode into CSV files.
-   [Tasks SQL Powered](https://github.com/sytone/obsidian-tasks-x) by `@sytone`  is a preview fork of the Tasks plugin that is backed by SQL queries.
-   [Tag Summary](https://github.com/macrojd/tag-summary) by `@macrojd`  will pull together lists of paragraphs or blocks of text that share the same tag(s). It's not designed for task management but if I'm reading the example correctly, it could be pretty handy for a tag-based task management system.

### Updates

-   The [Tasks](https://github.com/obsidian-tasks-group/obsidian-tasks) plugin got a big update, with some nice sorting for tags, more documentation for contributors, css class support, and more. It has also _moved_, as ClareMacrae is now the core maintainer. The documentation [also moved](https://obsidian-tasks-group.github.io/obsidian-tasks/), but everything else should work as normal.
-   The [Text to Speech](https://github.com/joethei/obsidian-tts) plugin now has automatic language detection and supports listening to the text, as seen in reading mode, if the note is in reading mode.
-   The [Extract URL](https://github.com/trashhalo/obsidian-extract-url) plugin added a custom site extractor for github repos. Now if you archive a link to a github repo it will pull down the readme for later reference. Here's a [video guide](https://www.youtube.com/watch?v=6bm83DPFA-Q) on how it works.
-   [Latex Suite 1.2.0](https://github.com/artisticat1/obsidian-latex-suite) has a new "conceal" feature that should make it easier to read big unwieldy expressions.
-   [Code Editor Shortcuts v1.9.0](https://github.com/timhor/obsidian-editor-shortcuts/releases/tag/1.9.0) now has support for delete to start of line and a couple of other nice enhancements.

### Betas

-   [File Explorer Keyboard Navigation](https://github.com/kzhovn/file-explorer-keyboard-nav) adds commands to move to the next/previous note in the file explorer, per [this feature request](https://forum.obsidian.md/t/iterate-through-files-in-the-file-sidebar-with-keyboard/)
-   Here's one that lets you [post to LinkedIn directly from your Obsidian notes](https://github.com/mw2000/linkedin-sync).
-   [Strange New Worlds](https://github.com/TfTHacker/obsidian42-strange-new-worlds) helps you to see the connections between the different parts of your vault.

## Feature Requests

-   It would be neat if we could [password protect things at the folder level on Obsidian Publish](https://forum.obsidian.md/t/feature-request-publish-folders-with-password/35900), and not just vault level. Or, you know, [maybe even the file level](https://forum.obsidian.md/t/password-protection-for-individual-notes-in-obsidian-publish-would-be-great/17844)?

## Appearance

-   [Minimal 5.2.9](https://github.com/kepano/obsidian-minimal/releases/tag/5.2.9) has new helper classes for wide and max sizes, some improvements with Style Settings and the Minimal Theme Settings plugin, support for notion-like tables, and more.
-   [Willemstad v0.5.2 Jordaan](https://github.com/tingmelvin/willemstad-x/releases/tag/v0.5.2) has [a new Cornell Notes CSSClass](https://willemstad.cc/Examples/CSSClass-Cornell) that styles callouts to look like paper notes. It also fixed mobile and got some print improvements.

## Guides

-   Here's [Scaling Synthesis](https://scalingsynthesis.com), a living hypertext notebook outlining discussing how Tools for Thought can facilitate synthesis. I particularly enjoyed this note on [how, when, and what to structure](https://scalingsynthesis.com/Q-How-might-we-navigate-the-structure-now-or-later-tradeoffs/).
-   Here's a new [introductory guide to Excliadraw](https://www.youtube.com/watch?v=erKrXsIwbAg) for visual notetaking.
-   Here's how to [add default page redirects to folders in Obsidian Publish](https://forum.obsidian.md/t/how-to-redirect-to-note-when-clicking-on-folder-in-publish/38042).
-   Here's another example of [how to use Obsidian to study the Bible](https://www.youtube.com/watch?v=3TeRR9KnLDg).
-   [Rainbell's example vault (v.0.0.2)](https://github.com/Rainbell129/Obsidian-Homepage/releases/tag/v0.0.2) was released in both English & Chinese. It's _beautiful_.
-   There's a new [breadcrumbs quickstart guide](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/Breadcrumbs+Quickstart+Guide) on the Hub.
-   Here's a neat heuristic for a ["compass" of notetaking](https://feeei.substack.com/p/the-essence-of-the-zettelkasten-method?s=r), it's essentially a written guide to the LYT Conference talk on the same topic.
-   Here's a [starter kit](https://developassion.gumroad.com/l/obsidian-starter-kit) from Sébastien Dubois with recommended plugins, explanations of common terms and organizational structures, etc.
-   Here's a nice explanation of [what exactly backlinks are](https://austingovella.medium.com/what-exactly-are-backlinks-891a7db6d9bc) and how they work, along with [five tips to make backlinks more useful](https://austingovella.medium.com/five-tips-more-useful-backlinks-e7408e7de99a).

## Discussions

-   There were a lot of discussions about the fundamental nature of zettelkasten (and a new thread got created in Discord for it, under `#knowledge-management`) but my favorite part was [this photo of these slipboxes](https://discord.com/channels/686053708261228577/710585052769157141/979754301025058906) used by `@slono`'s father and grandfather.
-   There was a heartwarming discussion about how [the Bubble Space theme is delightful](https://discord.com/channels/686053708261228577/744933215063638183/980715327711240242) and how some use-cases call for minimalist color schemes and others call for joyful ones.

## Ancillary Tools

-   [Smort v2](https://smort.io), the markdown-based highlighting & annotation app, lets users save articles permanently and build a library. Here's [a demo](https://smort.io/demo/home).

## Housekeeping

I will be hosting another "5x8 Event" for financial supporters on June 9. The name is an index card reference, but mostly refers to 5 people presenting on an interesting topic for no more than 8 minutes each. The last one was really fun!

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-06-04%20Guides%20to%20Synthesis%20%26%20File%20Explorer%20Keyboard%20Navigation.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-06-04%20Guides%20to%20Synthesis%20%26%20File%20Explorer%20Keyboard%20Navigation.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
