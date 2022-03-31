---
link: https://www.obsidianroundup.org/2022-03-05/
author: Eleanor Konik
published: 2022-03-05T13:30:00
publish: true
---

# 2022-03-05: Dashboards, Dataview Tips, & global publish graphs
A new GPT-3 plugin for generating text, support for Microsoft Document Syntax style admonition blocks, and "live preview" inside search panels. 

## In The Community

-   I'm going to be joining researcher Bianca Pereira (of Linking Your Thinking) for a [Twitter Spaces event about tracking history timelines](https://twitter.com/i/spaces/1yoKMWDaaqOJQ), i.e. how to take research notes on concepts and ideas that change across time, aren't necessarily bounded by space, and vary by perspective. Stuff like social identity and geopolitical changes can be tricky to classify neatly. Join us Sunday, March 6 at 11am EST.
-   400+ people on the Obsidian subreddit voted about [whether they use folders to organize their vault](https://www.reddit.com/r/ObsidianMD/comments/t2gk0j/folders_or_no_folders/) (not including things like templates, attachments, and plugin stuff). The answer was pretty much "yes."

## Obsidian Updates

-   Publish sites now support viewing the global graph. It can be opened using the button on the top right of the graph, next to the expand button. You can check it out on the [Obsidian Hub](https://publish.obsidian.md/hub/00+-+Start+here) & contrast with my [public notes](https://publish.obsidian.md/eleanorkonik/) (which were recently updated).

In addition to the normal bugfixes, Desktop [Insider v0.13.27](https://forum.obsidian.md/t/obsidian-release-v0-13-27-insider-build/33223):

-   Added new "Cycle bullet/checkbox" command that cycles between regular bullet, checkbox, and checked checkbox.
-   Reduced chance of Obsidian Sync overwriting instead of merging when a rare race condition happens.

## Plugin News

### New

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Creases](https://github.com/liamcain/obsidian-creases) by `@liamcain` provides tools for efficiently folding markdown sections in Obsidian and has a really fun README; it's worth checking out just for the chance to smile at all the puns.
-   [Footnote Shortcut](https://github.com/MichaBrugger/obsidian-footnotes) by `@MichaBrugger` lets users insert and write footnotes faster thanks to some fancy automations and hotkeys.
-   [Full Calendar 0.5.0](https://github.com/davish/obsidian-full-calendar/releases/tag/0.5.1) by `@davish` supports one-way sync for any calendar in .ics format, which includes private Google calendars, iCloud calendars, and most public calendars on the web. The plugin now uses Obsidian's CSS variables to accommodate theming. It also works on mobile.
-   [Daily notes new tab](https://github.com/reorx/obsidian-daily-notes-new-tab) by `@reorx` adds command and sidebar button to open daily notes in new tab.
-   [Text Generator](https://github.com/nhaouari/obsidian-textgenerator-plugin) by `@nhaouari` is a handy plugin for Obsidian that helps you generate text content using GPT-3 (OpenAI).
-   [Task Planner](https://github.com/eoghano4321/TaskPlanner) by `@eoghano4321` is a new task planning plugin.
-   [Markdown Table Editor](https://github.com/ganesshkumar/obsidian-table-editor) by `@ganesshkumar` provides an editor for Markdown tables. It can open CSV, Microsoft Excel/Google Sheets data as Markdown tables from Obsidian Markdown editor.
-   [Key Sequence Shortcut](https://github.com/anselmwang/obsidian-key-sequence-shortcut) by `@anselmwang` lets users execute commands with short key sequences. For example, `tp` for 'Toggle Preview' and `tb` for 'Toggle Sidebar'.
-   [Kobo Highlights Importer](https://github.com/bitwiseops/obsidian-kobo-highlights-import) by `@bitwiseops` lets users import highlights from Kobo devices.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

-   The developer of the [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases) plugin set up [donation tiers](https://ko-fi.com/zsolt); the highest tier will get access to quarterly community meetings on Zoom about the future of the plugin. There's also a new tools panel to make it easier to access Excalidraw commands and scripts on mobile.
-   [Admonitions v7.0.0](https://github.com/valentine195/obsidian-admonition/releases/tag/7.0.0) has a few breaking changes; it now supports Microsoft Document Syntax instead of Python style. There are also now icon packs, as well as a bunch of pdf-related bugfixes.
-   [Another Quick Switcher v.4.4.0](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/4.4.0) added a "show aliases on top" option.
-   The [PlantUML](https://github.com/joethei/obsidian-plantuml) diagramming plugin lets users edit .puml files directly and link to notes in them.
-   0.3.1 of [remotely-save](https://github.com/fyears/remotely-save) allows syncing deletion operations which means users no longer need to manually delete files from all devices.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   the [Query Control plugin](https://github.com/nothingislost/obsidian-query-control/releases/tag/0.3.0) lets you _render search results_ which means checkboxes look "checked" in the search panel instead of being plain text. Since it had a rename (used to be Embedded Query Control) you might need to uninstall the old version and restart first.

### For Developers

-   The developer of a solution for [writing in tree structure for long form writing](https://forum.obsidian.md/t/writing-in-tree-structure-the-solution-to-long-form-writing-gingko/20727/67) is in Ukraine and looking for help to polish up and publish the plugin. It's almost ready to go, just needs some documentation and maybe a couple of bugfixes. Contact Santi Younger to get involved.
-   Someone on the forum is looking to sponsor (i.e. pay for) an open source plugin to [export the whole vault as a pdf](https://forum.obsidian.md/t/will-pay-for-dev-vault-to-pdf/33335). I will note that I would personally be very grateful if it also supported epub or mobi, if anyone is interested in picking it up. Among other things, it would make it easier to bundle the contents of your vault up and send to tools like [BundleIQ](https://www.bundleiq.com/) (an AI assistant).

As of Desktop [Insider v0.13.27](https://forum.obsidian.md/t/obsidian-release-v0-13-27-insider-build/33223):

-   There is a new deleted event on `MetadataCache` now.
-   `DataAdapter.stat` now returns the OS `mtime` and `ctime` for folders.
-   Obsidian’s icon library now supports all icons from [lucide](https://lucide.dev/), a currently maintained fork of feather-icons with 547 supported icons. No need to import feather-icons anymore.

## Feature Requests

-   It would be neat if Obsidian Publish could ["pull down" updates from a github repository](https://forum.obsidian.md/t/github-webhooks-for-obsidian-publish/33457) like static site generators do, to help make it easier to keep collaborative vaults like the Obsidian Hub up to date without requiring one individual to handle everything. If you have a use-case for this, please add your situation to the replies.

## Appearance

-   Minimal has its own website with detailed documentation. [Version 5.1.7](https://github.com/kepano/obsidian-minimal/releases/tag/5.1.7) has support for the Charts and Metatable plugins as well as some new style settings.
-   [Primary](https://github.com/ceciliamay/obsidianmd-theme-primary/releases/tag/v.1.3.0) now has support for alternative checkboxes. There are also new tab header styling options. I use Primary on my iPad and the new checkboxes are really cute!
-   Willemstad now supports Minimal-style Cards and Image Grids. There are also a bunch of new Style Settings options.

## Guides

-   Here's a new css-based method of [creating simple dashboards](https://tfthacker.medium.com/dashboard-a-simple-organization-and-navigation-method-for-obsidian-vaults-2b1982d023a0) that leverage horizontal space.
-   Here's a comprehensive writeup of someone's system for using [Obsidian as a project manager](https://forum.obsidian.md/t/using-obsidian-at-work-project-manager-project-lead/33137).
-   Here's is an incredibly detailed, flexible, and well-explained [guide for transitioning to Obsidian from Roam](https://denisetodd.medium.com/the-road-from-roam-to-obsidian-f40d2333a676).
-   Here is a [collection of Chinese-language guides and tutorials](https://medium.com/pm%E7%9A%84%E7%94%9F%E7%94%A2%E5%8A%9B%E5%B7%A5%E5%85%B7%E7%AE%B1/obsidian-%E4%BD%BF%E7%94%A8%E6%95%99%E5%AD%B8-%E7%B8%BD%E7%9B%AE%E9%8C%84-%E6%8C%81%E7%BA%8C%E6%9B%B4%E6%96%B0%E4%B8%AD-2d23dce3ef02) for Obsidian.
-   Here's a nice explanation of how to use [daily notes and dataview's task queries](https://www.workings.tools/p/how-i-use-daily-notes-in-obsidian).
-   Episode 20 of Practically Paperless discusses [practical uses of the dataview plugin](https://jamierubin.net/2022/03/01/practically-paperless-with-obsidian-episode-20-experimenting-with-the-dataview-plug-in/).
-   The hub has a great new guide for [how to debug why Obsidian is running slowly](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/How+to+debug+why+Obsidian+is+running+slowly).

## Discussions

-   Here's a discussion about various ways to [replicate the Scrivener corkboard view](https://www.reddit.com/r/ObsidianMD/comments/t4e2l4/does_anyone_know_how_to_make_a_corkboard/) in Obsidian.
-   Here's one about using Obsidian to [manage gardening notes](https://www.reddit.com/r/ObsidianMD/comments/t1yte6/garden_management_in_obsidian/).
-   Here was a discussion about how Obsidian can be helpful during [political crises](https://www.reddit.com/r/ObsidianMD/comments/t2m3q8/the_prospect_of_being_disconnected_from_the_rest/).
-   Here's a really insightful discussion about using Obsidian for [thematic analysis](https://www.reddit.com/r/ObsidianMD/comments/t3bjuw/using_obsidian_for_thematic_analysis/) and what other tools might be better at certain aspects of that.
-   Here was a nice discussion in Discord about [what sorts of things to take notes on in lectures](https://discord.com/channels/686053708261228577/710585052769157141/949012707993075762) — the main suggestion was to take notes on your reactions to content, not just the content itself.

## Knowledge Management

-   Here's a video that provides [an alternative to the fleeting/literature/permanent note paradigm](https://www.youtube.com/watch?v=t4vKPhjcMZg).
-   Here's an article about [information architecture for personal knowledge management](https://cody-burleson.medium.com/ia-for-pkm-crows-camels-concepts-and-the-cognitive-divide-7523c0bfa5eb) that discusses labeling concepts.

## Examples

-   Here are some really beautiful [note templates for periodic notes](https://github.com/mulfok/periodic-note-templates). .
-   Here's a [task management system](https://www.reddit.com/r/ObsidianMD/comments/t3s8ek/i_turned_my_task_management_system_into_a/) with a sample vault available for download.

## Ancillary Tools

-   There's a new [custom icon for Mac](https://www.reddit.com/r/ObsidianMD/comments/t2zps9/the_app_icon_didnt_fit_my_dock_style_so_i_made_a/).
-   The [Obsidian To Mkdocs python script](https://github.com/Mara-Li/mkdocs_obsidian_publish) for publishing has more options and an updated README.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-03-05%20Dashboards%2C%20Dataview%20Tips%2C%20%26%20global%20publish%20graphs.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-03-05%20Dashboards%2C%20Dataview%20Tips%2C%20%26%20global%20publish%20graphs.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
