---
link: https://www.obsidianroundup.org/2022-02-12/
author: Eleanor Konik
published: 2022-02-12T13:30:00
publish: true
---

# 2022-02-12: Open Notes in a New Window, Improved iPad sketch support, & Dockable Settings
Easily share one-off notes & code, automatic note moving, & no-code supercharged linked. Plus, migration tips &  use-case discussions. 

## In The Community

-   Here's a (very) [short feedback survey](https://airtable.com/shr94ZN7tfQt6tv5n) for the Workspaces Plus plugin in Obsidian.

## Obsidian Updates

-   Desktop [Insider 0.13.24](https://forum.obsidian.md/t/obsidian-release-v0-13-24-insider-build/31864) upgraded the engine from Electron 13 to 16, so download the latest intaller (grab the link from the pins in Discord). This version improved the behavior of Obsidian Sync so that you're less likely to run into weird conflicts from old devices having stored versions. There were also a bunch of small fixes.
-   Desktop Insider 1.1.0 (Build 38) brings mobile up to parity with desktop 0.13.24. Licat also mentioned that they're working on getting mobile out to public, just waiting on the approval process to take its sweet time. If you're impatient for Live Preview on mobile, remember you can always buy an Insider license :)

## Plugin News

### New in Community Plugins

**These plugins went through code review and are now available in Obsidian's plugin list.**

-   [Excel to Markdown Table](https://github.com/ganesshkumar/obsidian-excel-to-markdown-table) by `@ganesshkumar` will **paste** data from Microsoft Excel, Google Sheets, Apple Numbers and LibreOffice Calc **as properly formatted Markdown tables**.
-   [Save as Gist](https://github.com/ghedamat/obsidian-save-as-gist) by `@ghedamat` saves the current note as Gist on github, which his handy for easily sharing your templates & dataviewjs queries and such. It also makes it super easy to **share one-off notes**!
-   [Multi-Column Markdown](https://github.com/ckRobinson/multi-column_markdown) by `@ckRobinson` adds functionality to create markdown documents with **multiple columns** of content viewable within Obsidian's preview mode.
-   [Topic Linking](https://github.com/liammagee/obsidian-topic-linking) by `@liammagee` **converts PDF files and web links to Markdown**.
-   [File Info Panel](https://github.com/CattailNu/obsidian-file-info-panel-plugin) by `@CattailNu` is a plugin for Obsidian that creates a File Information view that displays the active file's date created, date modified, file size, and links to open the file in its native application and to open the file's folder. It also has **writing statistics** (character, word, sentence, and paragraph counts) and a word frequency analysis. It is **amazingly** useful for writers of any kind.
-   [Power Search](https://github.com/aviral-batra/obsidian-power-search) by `@aviral-batra` searches Anki Notes based on your current line
-   [Code Block Labels](https://github.com/stbowers/obsidian-codeblock-labels) by `@stbowers` adds labels to fenced code blocks
-   [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) by `@coddingtonbear` lets users get, change or otherwise interact with your notes in Obsidian via a REST API.
-   [Simple note quiz](https://github.com/dorisxx/Obsidian-simple-note-quiz) by `@dorisxx` starts a simple quiz on your current note
-   [Frontmatter Tag Suggest](https://github.com/jmilldotdev/obsidian-frontmatter-tag-suggest) by `@jmilldotdev` autocompletes tags in the frontmatter tags field
-   [Better Command Palette](https://github.com/AlexBieg/obsidian-better-command-palette) by `@AlexBieg`
-   [Copy as HTML](https://github.com/jenningsb2/copy-as-html) by `@jenningsb2` converts selected markdown to HTML and copies it to the clipboard.
-   [Core Search Assistant](https://github.com/qawatake/obsidian-core-search-assistant-plugin) by `@qawatake` enhances built-in search with a better keyboard interface, card previews, and bigger preview. If that sounds appealing, make sure you also check out the [Vantage](https://github.com/ryanjamurphy/vantage-obsidian) plugin, which helps you build complex queries using Obsidian's native search tools in a user-friendly graphical way.

### Pending (as of Friday morning)

**Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review.**

-   [Settings Search](https://github.com/valentine195/obsidian-settings-search) by `@valentine195` lets users globally search settings in Obsidian.md
-   [Sidekick](https://github.com/hadynz/obsidian-sidekick) by `@hadynz` suggests new connections by highlighting text that could match existing links and tags
-   [Front Matter Tag Wizard](https://github.com/Tohsig/obsidian-front-matter-tag-wizard) by `@Tohsig` adds tag autocompletion and optional autoformatting to note front matter.
-   [Insert Heading Link](https://github.com/signynt/insert-heading-link) by `@Signynt`
-   [Auto Note Mover](https://github.com/farux/obsidian-auto-note-mover) by `@farux` will automatically move the active notes to their respective folders according to the rules.
-   [Persistent Graph](https://github.com/Sanqui/obsidian-persistent-graph) by `@Sanqui` adds commands to save and restore the positions of nodes on the global graph view.
-   [Todoist Text](https://github.com/wesmoncrief/obsidian-todoist-text) by `@wesmoncrief` integrates your Todoist tasks with markdown checkboxes.

### Updates

-   [Excalidraw 1.6.1](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.6.1) improved freedraw flow, and includes a fix for iPad scribble. It should now be even easier to create links to drawings, and build a vault of interconnected sketches.
-   Using the new Style Settings plugin support in [Supercharged Links](https://github.com/mdelobelle/obsidian_supercharged_links), you can now customize your note links without a single line of CSS. Here's a [discussion of why that can be useful](https://www.reddit.com/r/ObsidianMD/comments/sm2lqa/using_the_new_style_settings_plugin_support_in/).
-   [Block Reference Counter](https://github.com/shabegom/obsidian-reference-count) has been updated to support showing references in Live Preview
-   [BRAT](https://github.com/TfTHacker/obsidian42-brat/) got some updates and fixes most around how notifications work.
-   MetaEdit 1.7.2 got some fixes so it should stop conflicting with Kanban and Excalidraw.
-   [Linter 1.2.10](https://github.com/platers/obsidian-linter/releases/tag/1.2.10) has a new rule so that the first H1 is inserted as the title attribute. If not found, inserts the filename.
-   v1.8.0 of [Obsidian-Memos](https://github.com/Quorafind/Obsidian-Memos/) supports sharing images with backgrounds, using shift to select days on a heatmap, customizing composition, custom filenames for the DELETE and QUERY files, and showing all tags from the vault. It also has translations for French & Portuguese.
-   [Various Complements v5.1.0](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/5.1.0) added regex patterns, better handling of whitespace, a status bar, and better suggests for aliases. 5.3.0 has an open source file key option.
-   [Smarter Markdown Hotkeys](obsidian://show-plugin?id=obsidian-smarter-md-hotkeys) has improved support for mathjax, delete, and casing.
-   [KOReader Highlights 0.6.0](https://github.com/Edo78/obsidian-koreader-synccan) now automatically detect any changes just to the text of the note itself (ignoring every other element of the note)) and update the frontmatter properties without any intervention from the user.
-   [Metadata Extractor](https://github.com/kometenstaub/metadata-extractor) now exports the frontmatter as well. Duplicate file names in links and backlinks should be resolved properly as of 1.0.0.

### Betas

**Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes.**

-   You can now [pop your notes out into a second window](https://github.com/valentine195/obsidian-image-window). It's incredibly useful but also, be warned (and please don't spam the dev with feature requests, he knows!), very limited — the data is read-only. Embeds and links don't work. Plugins that generate static rendered HTML will work (i.e. Admonitions) but essentially none of the others (i.e. Dataview).
-   Here's [a fork of Obsidian Tasks](https://github.com/dcao/obsidian-tasks) that adds some features like agenda view, date autocomplete, and mobile widgets. Here's the [developer announcing it on Reddit](https://www.reddit.com/r/ObsidianMD/comments/sm7ozt/my_obsidian_tasks_workflow_agenda_views_date/).
-   [Bartender 0.5.0](https://github.com/nothingislost/obsidian-bartender/releases/tag/0.5.0) can now fuzzy filter the file explorer contents. Also, the drag to rearrange behavior is now toggled via a nav button and should make it easier to move things around/keep them locked in place

### For Developers

-   Github is allowing users to [set up sponsors-only repositories](https://techcrunch.com/2022/02/02/github-introduces-sponsor-only-repositories/), for folks who are looking for an easier way to manage things like "insider betas" for plugins and themes, or members-only plugins. That's the sum total of what I know about it, but I'm curious if anyone finds a way to use this.

## Feature Requests

-   Here's a feature request for [intelligently suggesting ways to filter search results](https://forum.obsidian.md/t/interface-to-filter-search-results-by-frequently-used-words-links/31957)
-   Here's a feature request for [card view of Obsidian files](https://forum.obsidian.md/t/hepta-as-a-plugin/31955), modeled on how tools like [Heptabase](https://twitter.com/Heptabase/status/1437781867474849798?t=k9DmtYEpoMQgkSUGN9zflw) and [Scrintal](https://www.scrintal.com/) work.
-   Here's a request to make [updating themes easier](https://forum.obsidian.md/t/surface-theme-update-to-main-appearance-screen/31977).

## Appearance

-   Here's a discord post on how to get [dataview tables to wordwrap](http://discordapp.com/channels/686053708261228577/702656734631821413/940691880801341502) that personally saved me oodles of stress.
-   [Minimal 5.1.0](https://github.com/kepano/obsidian-minimal/releases/tag/5.1.0) adds translucent sidebars, colorful headings, and dozens of customization options. [5.1.1](https://github.com/kepano/obsidian-minimal/releases/tag/5.1.1) has some new settings and improvements. [5.1.2](https://github.com/kepano/obsidian-minimal/releases/tag/5.1.2) adds the macOS color scheme.
-   Here's a css snippet to [omit the search terms from query blocks](https://gist.github.com/GitMurf/b939ae2ea81411b530a335083a86564f), which makes them look a little cleaner.
-   [Sanctum v0.6.3](https://forum.obsidian.md/t/sanctum-theme/25455/105?u=eleanorkonik) added some new Style settings, support for Kepano's image grid and minimal cards snippets, and a bunch of other small changes.
-   [Catppuccin](https://github.com/mbeckrich/obsidian) by `@mbeckrich` is a soothing pastel theme.
-   [Sparkling Wisdom](https://github.com/learnerfvs/Sparkling-Wisdom-obsidian-theme-) by `@learnerfvs` is very bright.
-   The [Shimmering Focus](https://forum.obsidian.md/t/theme-shimmering-focus/32027theme) variant [Willemstad v0.15 Amstel](https://github.com/tingmelvin/willemstad) has 2 new color palettes and a bunch of options.
-   Here's a [way to dock Obsidian settings on the sidebar à la devtools](https://gist.github.com/nothingislost/52dc60c207664062b1c8073e494de5a3). It does mess with the general modal container, so things like the command palette get adjusted in weird ways. If you use it, make it a snippet you can toggle on and off.
-   Here's a special snippet called [Absolve](https://github.com/mulfok/obsidian-absolve) designed to function as a "theme overlap" with custom design schemes (i.e. for ttrpgs and academic uses), colors, kanban styles, popular features from different themes, etc.
-   [Bubble Space Theme v1.5](https://github.com/Emrie-Candera/Bubble-Space-Theme/releases/tag/v1.5) comes with preset colors, custom checkboxes, new theme icons, and more.
-   [Prism v1.5.0](https://github.com/damiankorcz/Prism-Theme/releases/tag/1.5.0) added animations, contrast improvements, and a bunch of visual improvements and other fixes.

## Ancillary Code

-   Here's a custom compile step that will turn `+++` into the syntax required for a page break in Word when converting with Pandoc, on [Discord](https://discord.com/channels/686053708261228577/722584061087842365/940381694119260180).
-   Here's a python script to download and update css snippet from github ([Discord link](https://discord.com/channels/686053708261228577/855181471643861002/941305517354131456)).

## Guides

-   Here's how to [make flashcards and vocabulary notes](https://gist.github.com/TakuanPickle/e3ef3e2743bd813ade41733ec11c7ada) for language learning.
-   Here's an article about [the fundamental design principles that underlie Obsidian's development](https://medium.com/p/obsidian-understanding-its-core-design-principles-7f3fafbd6e36).
-   Here's a guide for [creating a simple habit tracker in Obsidian using Dataview](https://twitter.com/chrisbbh/status/1490724059323240451)
-   Here's a guide for how to [use clip web content to Obsidian](https://www.youtube.com/watch?v=PZnytCMbR-A)
-   Here are [six different ways to use note links](https://jamierubin.net/2022/02/08/practically-paperless-with-obsidian-episode-17-six-ways-i-use-note-links/).
-   Here's an article I like that talks more about the [notetaking as gardening metaphor](https://www.nickang.com/2021-08-29-types-of-notes-in-a-pkm-explained-with-a-gardening-analogy-part-i/) that came up in Discord.
-   Here's a discord post about [how Dataview can help track upcoming courses](https://discord.com/channels/686053708261228577/744933215063638183/939850584754888755).

## Discussions

-   Here are [Dan Allosso's reflections from Week 1 of the Smart Notes book club](https://www.youtube.com/watch?v=1N02UyrTQJo). Here's the public vault for the previous [book club for David Graeber's The Dawn of Everything](https://publish.obsidian.md/bookclub/Start+Here).
-   Here's a Reddit thread where someone shared how they used Obsidian to [create a field guide for trauma survivors](https://www.reddit.com/r/ObsidianMD/comments/soo85b/i_used_obsidian_to_make_a_field_guide_for_trauma/). It's published [as an obsidian publish site](https://publish.obsidian.md/integral-guide-to-well-being/Start+Here/About) and is a really interesting resource.
-   Here's an interesting discussion about [switching from Emacs Org-Mode to Obsidian](https://www.reddit.com/r/ObsidianMD/comments/smui4k/did_anyone_else_also_switch_to_obsidian_from/).
-   Here's one about [switching from Notion to Obsidian](https://www.reddit.com/r/ObsidianMD/comments/sl8l63/notion_to_obsidian/).
-   Here's a discussion about how to use [Obsidian as an engineering student](https://www.reddit.com/r/ObsidianMD/comments/sluf4m/question_for_engineering_student/).
-   Here's a discord discussion about [categories and types of notes](https://discord.com/channels/686053708261228577/710585052769157141/939428520730435614).
-   Here's a discord discussion about [how following some notetaking methods can force you to think in different ways](https://discord.com/channels/686053708261228577/710585052769157141/939496811276664842).
-   Here's a Discord discussion about [how Obsidian tangibly increased someone's academic performance](http://discordapp.com/channels/686053708261228577/722584061087842365/941016285393850458).

## Ancillary Tools

-   According to [this discussion](http://discordapp.com/channels/686053708261228577/744933215063638183/939227280201379881) you can iframe Notion tables into Obsidian. You can also link to block ref with Notion using methods described in that Discord discussion.

## Housekeeping

My first exclusive article will go out to financial supporters on Thursday (the third Thursday of the month, which is what I'm shooting for now). It will be about **the value of consistent naming conventions**. Afterwards, I'll probably raise the price a bit soon (I've been poking around and Substack says $5 is normal), so if you'd like to lock in the current $3/mo or $30/year...

[BECOME A MEMBER](https://www.obsidianroundup.org/membership/)

Also, several people signed up for one-on-one meetings with me this week. I was able to give individualized help and advice, and I really enjoyed it. More importantly, I felt like I genuinely was able to help those people and save them time, as well as offer hope and energy.

🗓️

If you want to book a one-on-one meeting with me, here's my [calendar](https://obsidianroundup.org/consult). If the time zones don't align with my autobook times, just shoot me an email (or use my [contact form](https://www.obsidianroundup.org/contact/)) and we'll work something out.

Lastly, a request: Does anybody use obsidian for something like private practice psychology, social work, etc., where you have to balance session notes, keeping up with the literature, client paperwork, etc., who would be willing to write a guide or advise me on writing a guide for this? There's interest in this from folks in these fields, and one way or another I'm going to make it a point to help them. I initiated some [discussion about HIPAA considerations](https://twitter.com/EleanorKonik/status/1491789570182025216) on Twitter, but I would love to speak with or signal boost an expert on this.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-02-12%20Open%20Notes%20in%20a%20New%20Window%2C%20Improved%20iPad%20sketch%20support%2C%20%26%20Dockable%20Settings.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-02-12%20Open%20Notes%20in%20a%20New%20Window%2C%20Improved%20iPad%20sketch%20support%2C%20%26%20Dockable%20Settings.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
