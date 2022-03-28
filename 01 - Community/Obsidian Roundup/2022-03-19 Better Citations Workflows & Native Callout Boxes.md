---
link: https://www.obsidianroundup.org/2022-03-19/
author: Eleanor Konik
published: 2022-03-19T12:30:00
publish: true
---

# 2022-03-19: Better Citations Workflows & Native Callout Boxes
The hover editor plugin got secondary support from other plugins, there's a new option for dynamic indexes, & a guide for browser-based Obsidian.

## In The Community

-   Matthew Meyers, the developer of Style Settings, Smart Typography, Kanban, Indentation Guides, Contextual Typography, and the California Coast theme — oh, and the new [Zotero Connector](https://github.com/mgmeyers/obsidian-zotero-desktop-connector) (!) plugin — is currently studying to be a therapist and is [looking for part time & contract-based work](https://github.com/mgmeyers). If you have any front end web development work you need done, please [reach out](https://matthewmeye.rs/). Also, if you enjoy his plugins, this is one of those times when money can really make a big difference to one of our wonderful plugin devs, so consider [donating to his ko-fi](https://www.buymeacoffee.com/mgme).

## Obsidian Updates

-   Obsidian Mobile is at parity with code and removed the "open link" popover in Live Preview. You can now click on links directly to open them. Press and hold to edit the link.

As of [Insider 0.14.0](https://forum.obsidian.md/t/obsidian-release-v0-14-0-insider-build/33986)...

-   Obsidian Markdown now allows you to create callout blocks (sometimes called “admonitions”). Callouts are written as a blockquote, inspired by the “alert” syntax from Microsoft Docs. This allows callout boxes to be [supportive natively on Obsidian Publish](https://help.obsidian.md/How+to/Use+callouts). (this [sherlocked](https://en.wikipedia.org/wiki/Sherlock_(software)) Admonitions by `@javalent` congrats on having one less thing to maintain!)
-   Indentation guides (sometimes known as relationship lines) are now available in Live Preview and Reading view. (this [sherlocked](https://en.wikipedia.org/wiki/Sherlock_(software)) Relationship Lines by `mgmeyers` congrats on having one less thing to maintain!)
-   Tasks with checkmark characters other than x will now no longer have the strikethrough formatting applied.
-   There's also an update to fix the `<C-w> <key>` [vim binding not working](https://github.com/esm7/obsidian-vimrc-support/issues/67).

As of [Insider 0.14.1](https://forum.obsidian.md/t/obsidian-release-v0-14-1-insider-build/34103), Live Preview now supports basic markdown tables previewing — thank you `@melvin` (the Willemstad developer) for pioneering this method. [0.14.2](https://forum.obsidian.md/t/obsidian-release-v0-14-2-insider-build/34170) brought support for starred files supporting hover page previews.

## Plugin News

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Hover Editor](https://github.com/nothingislost/obsidian-hover-editor) by `@nothingislost` transforms the Page Preview hover popover into a fully working editor instance — which is enabling people to meaningfully work off the graph view, which is really cool. A bunch of other plugin developers have been working hard to support this functionality, including [Pane Relief](https://github.com/pjeby/pane-relief/releases/tag/0.0.22) and Quick Explorer. I strongly recommend reading their release notes if you're using Hover Editor.
-   [Etherpad](https://github.com/egradman/obsidian-etherpad-lite) by `@egradman` allows users to set up a server as a lightweight collaboration tool / live editor for documents in your vault. It seems like a middle ground between pushing your whole vault to git and copy-pasting everything into hack.md or google documents.
-   [Screwdriver](https://github.com/vrtmrz/obsidian-screwdriver) by `@vrtmrz` is a utility to move files into and out of your vault, which is handy on iOS where you can't otherwise access things in hidden (dot) folders.
-   [Lapel](https://github.com/liamcain/obsidian-lapel) by `@liamcain` adds a marker for headings in the gutter. There's also a menu for quickly switching the heading level.
-   [Daily Notes Viewer](https://github.com/Johnson0907/obsidian-daily-notes-viewer) by `@Johnson0907` gives you a scrollable daily notes interface à la Roam Research.
-   [Waypoint](https://github.com/IdreesInc/Waypoint) by `@IdreesInc` lets users easily generate dynamic MOCs in your folder notes. Enables folders to show up in the graph view.
-   [Obsidian matrix](https://github.com/NastyGamer/obsidian-matrix) by `@NastyGamer` is intended for creating LaTeX matricies more easily.
-   [Zotero Desktop Connector](https://github.com/mgmeyers/obsidian-zotero-desktop-connector) by `@mgmeyers` lets users insert citations, bibliographies, and notes directly from Zotero desktop. There are plans to support extracting annotations from PDFs (including image annotations) but it's already a great bridge for creating Pandoc-friendly citations. Here's an interesting forum [discussion about how to use the new Zotero](https://forum.obsidian.md/t/zotero-beta-export-note-to-md-and-note-templates/33795/2) beta, by the way, and here's one discussing [Zotero best practices](https://forum.obsidian.md/t/zotero-best-practices/164/195).
-   [Telegraph Publish](https://github.com/reorx/obsidian-telegraph-publish) by `@reorx` allows users to easily publish to Telegraph, an [anonymous blogging platform](https://www.theverge.com/2016/11/23/13728726/telegram-anonymous-blogging-platform-telegraph).
-   [Navigate Cursor History](https://github.com/heycalmdown/navigate-cursor-history) by `@heycalmdown` remembers the recent 50 cursor positions history and allows you to jump to them back and forth like VSCode.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

-   The maker of [Obsidian Markmind](https://github.com/MarkMindCkm/obsidian-markmind/releases/tag/1.4.0) created a way to export the interactive tables from the mindmapping tool into extended table markdown, and the tables are _really_ slick.
-   [Sortable](https://github.com/alexandru-dinu/obsidian-sortable/releases) introduced support for sorting Dataview tables in Live Preview.
-   [Remotely-save](https://github.com/fyears/remotely-save) 0.3.5 can bypass CORS issues, which is handy for s3 and webdav. It supports Backblaze B2, TeraCLOUD.jp, and SHOULD support owncloud/nextcloud, NAS webdav, etc.
-   Users of [Obsidian Leaflet](https://github.com/valentine195/obsidian-leaflet-plugin) should update to v5.0.0 if your real-world maps are suddenly rendering blank; an upstream dependency changed.
-   The [jump to link](https://github.com/mrjackphil/obsidian-jump-to-link) plugin now supports both CM6 and LivePreview; users of the "quick jump plugin" via BRAT should switch.
-   [icon shortcode v0.9.0](https://github.com/aidenlx/obsidian-icon-shortcodes/releases/tag/0.9.0) lets you use icon shortcodes in css variables: `--callout-icon` lets you specify custom icons for callouts
-   [Charts](https://charts.phibr0.de/chart%20from%20table/) lets users link Tables to Charts.
-   [Flexible Pomo](https://github.com/grassbl8d/flexible-pomo-obsidian/releases) shows notes with active tasks now.

**Admonitions**

-   Since Admonitions got [sherlocked](https://en.wikipedia.org/wiki/Sherlock_(software)) it also got overhauled; due to conflicts it no longer supports Microsoft's callout syntax.
-   There's a new button available in settings that will automatically convert your existing [MSDoc Syntax](https://help.obsidian.md/How+to/Use+callouts) to the new callout syntax. **This will modify your notes. Please make backups before using.**
-   Admonitions can be used to quickly and easily create custom callout types_._ There is also the ability to export your custom types as valid CSS, or have the plugin maintain a CSS snippet for you.
-   Admonitions now offers several quality-of-life features for callouts, including an editor suggester as you create callouts, a helpful `Insert Callout` command, and the ability to register `Insert Callout` commands for your custom types.
-   You can also use Admonitions to set default titles and default collapse states for your callouts, but that won't work on Publish.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   [Version History Diff](https://github.com/kometenstaub/obsidian-version-history-diff) can display diffs of both the Sync and the File Recovery version history for the currently active file.

### For Developers

-   [Zotero Desktop Connector](https://github.com/mgmeyers/obsidian-zotero-desktop-connector) by `@mgmeyers` is looking for co-maintainers. We're trying to consolidate some of the citations-related and zotero-related plugins under one banner to make things easier on the community, so if that project is useful to you (even if you aren't a dev!) please join us in the `Citations plugin(s) collaboration` thread in the `Academia` channel on Discord, or the Zotero Desktop Connector github repository.
-   As of [v.0.14.0](https://forum.obsidian.md/t/obsidian-release-v0-14-0-insider-build/33986), Plugin inline sourcemaps are now stripped for performance unless the debug startup time option is enabled.
-   To style the new core relationship lines, use the CSS class `cm-indent` and `cm-active-indent`.

## Feature Requests

-   Here's a request to quickly [search a folder with a right-click command](https://forum.obsidian.md/t/right-click-on-a-folder-and-search-within-it/30079) instead of having to use the `path:` stuff in the search bar.

## Appearance

-   Minimal has [support for data task icons](https://minimal.guide/Block+types/Checklists) now in checklists (i.e. `- [!] important`), including an [editable snippet](https://github.com/kepano/obsidian-minimal/blob/master/src/scss/features/checklist-icons.scss).
-   [Spectrum](https://github.com/Braweria/Spectrum/) is up to 1.1.5 and got a bunch of bugfixes and support for Style Settings and plugins like Charts.
-   [Ebullientworks 0.3.23](https://github.com/ebullient/obsidian-theme-ebullientworks) now supports native indentation guides and made the Admonitions and callout boxes match stylistically.
-   [Primary](https://forum.obsidian.md/t/primary-theme/26687)'s modals are now responsive to screen size.
-   Here's a snippet for [highlighting date/timestamps](https://github.com/nothingislost/obsidian-dynamic-highlights/discussions/44).

## Ancillary Code

-   Here's a neat setup to help find [orphan files](https://www.reddit.com/r/ObsidianMD/comments/t89ts1/with_a_bit_of_patience_i_got_form_functionality/) a home.
-   The [obsidian to mkdocs python script](https://github.com/Mara-Li/mkdocs_obsidian_publish) was updated to support the new callout syntax.
-   [Supercharged Citation Picker](https://github.com/chrisgrieser/alfred-bibtex-citation-picker#auxiliary-features) is an Alfred Workflow for using a BibTeX file (`.bib`) that works with page numbers, multiple citations, smart search for citekeys, authors, titles, etc. It's very fast and easy to install... if you're a mac user with Alfred.
-   The Templater and Various Complements plugins combined let users have [autocompletion of citations](https://gist.github.com/chrisgrieser/e589801507b5e91c27ec309e47e7178b) while typing.

## Guides

-   Here's [how to run Obsidian in a docker container for remote/browser access](https://github.com/sytone/obsidian-remote), and here's the discussion on Reddit that includes some [discussion about how to do it with Mac and NAS](https://www.reddit.com/r/ObsidianMD/comments/tei2ye/running_obsidian_in_a_docker_container_with/).
-   Here's a comparison of Interstitial Journaling and Categorical Journaling as part of a [beginner's guide to journaling in your daily note](https://www.youtube.com/watch?v=5dyv2xOfgNs) video on Youtube. Pamela also has a nice one on [tagging conventions](https://www.youtube.com/watch?v=qDvawxz5oOE).
-   Here's a guide on [how to use Obsidian to manage craft projects](https://phoenixblackdove.wordpress.com/2022/03/17/how-i-manage-craft-projects-in-obsidian/), like knitting. This came after extensive discussion in the Discord about how to use [Obsidian for yarn and knitting related projects](https://discord.com/channels/686053708261228577/700466324840775831/953699125122195526).
-   Here's a really thought-provoking guide about [how to weave a web of knowledge](https://forum.obsidian.md/t/zettelkasten-linking-for-surprising-connections/33214/7?u=syncretizm) that threads connections and heavily utilizes the local graph view and plugins like Breadcrumbs to navigate a vault.
-   Here's a really interesting guide about [how to manage the open-source ecosystem](https://matt.life/writing/the-asymmetry-of-open-source) with a lot of thought-provoking points about business models, relationships, boundaries, and goal setting. I'm including it here because I think it's relevant to our developer community, but I honestly think anyone wanting to spend or make money from the internet should read it.
-   Here's a [discussion](https://twitter.com/Pamela_Drouin/status/1501218347316301830) about how to get your "note to yourself" from yesterday into today's daily note, and here's the [template](https://gist.github.com/lguenth/ea65fc3e7ebfa3d4579396a06b0796aa).

## Showcases

-   I made a [chart of my tech stack](https://twitter.com/EleanorKonik/status/1504408466970005511) so I could get a better grip on some pieces of my writing process. It's currently my most popular top-level tweet ever, so I figured I'd share it here.
-   Somebody figured out how to run [Obsidian on a Steam Deck](https://www.reddit.com/r/ObsidianMD/comments/tfs741/does_this_count_as_obsidian_mobile/) (a handheld gaming pc).
-   Here's a [graph shaped like a chicken](https://www.reddit.com/r/ObsidianMD/comments/tdc1rg/my_graph_looks_like_a_chicken/) that got 200 upvotes and an award on Reddit.

## Ancillary Tools

-   Here's a new [markdown-backed highlights and annotations tool](https://www.smort.io/) for articles in your browser that came out this week. I haven't had time to mess with it much, but according to the [discussion on HackerNews](https://news.ycombinator.com/item?id=30673502) works similar to hypothes.is except you don't need to download an extension and make an account, it strips out ads, and you can edit the article content directly using Markdown. You can also do more customizations.
-   Here's a neat project that lets you [serve local HTML files to an eink reader with a pleasant UI for kindles](https://github.com/edgartaor/kindleServer). This [HackerNews discussion](https://news.ycombinator.com/item?id=30669487) also discusses workarounds for getting your content onto kindles readably.
-   Here's a [terminal based markdown reader](https://github.com/charmbracelet/glow).

## Housekeeping

My article about how to [avoid feeling guilty about a big pile of unfinished articles to read](https://www.obsidianroundup.org/rebrand-your-tbr-list/) (or, it must be said, write) just went live to Obsidian Roundup supporters. Embrace having a filtered list of high-quality reading available when you need it ;)

Up on the third Thursday of next month is "Sensemaking through Fiction" aka why storytelling is a deeply underutilized method for gaining & integrating knowledge, as well as conveying information (and wisdom) to an audience.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-03-19%20Better%20Citations%20Workflows%20%26%20Native%20Callout%20Boxes.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-03-19%20Better%20Citations%20Workflows%20%26%20Native%20Callout%20Boxes.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
