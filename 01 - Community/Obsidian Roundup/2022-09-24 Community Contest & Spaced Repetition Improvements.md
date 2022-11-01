---
link: https://www.obsidianroundup.org/obsidian-october/
author: Eleanor Konik
published: 2022-09-24T12:30:10
publish: true
---

# 2022-09-24: Community Contest & Spaced Repetition Improvements
There's a new interactive medical terminology dictionary, & a step-by-step guide to setting up a second brain in minutes per day.

## In The Community

* It's almost October, so it's time to gear up for this year's annual Obsidian October event. The theme is "Back to School" (best creation for college students, graduate students, and specific subject matter will earn bonus prizes) and they've expanded the categories to include: new plugin (or significant update), video, demo vault, or written content. Here's the [daily progress and learnings](https://forum.obsidian.md/t/obsidian-october-2022-daily-progress-and-learnings/43767) thread, and the [official hub page](https://publish.obsidian.md/hub/01+-+Community/Events/Obsidian+October+2022). There's more clarification in Discord. If anyone is looking to contribute to an existing plugin, the [Hub has collected some issues of interest](https://publish.obsidian.md/hub/01+-+Community/Contributing+to+the+Community/Plugins+seeking+help).
* Despite how many fiction options there were, first book for the book club is going to be How to Take Smart Notes. The current season will end December 13. Here's more in Discord about [how the voting looked](https://discord.com/channels/686053708261228577/1009112156064718951/1021767699073867786).

## Obsidian Updates

[Insider v0.16.3](https://forum.obsidian.md/t/obsidian-release-v0-16-3-insider-build/43654) Highlights:

* The new Insider now has per tab history, which marks another plugin feature getting [sherlocked](https://en.wikipedia.org/wiki/Sherlock_(software)) into core; thanks to `@pjeby` for pioneering [Pane Relief](https://github.com/pjeby/pane-relief/releases/tag/0.4.0) and helping out with this feature that I for one rely on. If you are using insider builds, please update your Pane Relief version to 0.4.0 _before_ you launch Obsidian 0.16.3.
* The Sliding Panes plugin will now automatically be disabled on startup.
* They added an option to Export to PDF to show the name of the note at the beginning of the document.
* Legacy themes are no longer deleted when updating to 0.16 compatible themes. This should improve compatibility when syncing to a device that’s not yet 0.16 compatible.

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list._ For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new).

* [Quick snippets and navigation](https://github.com/aciq/obsidian-keyboard-shortcuts) by `@aciq`  adds up/down keyboard navigation for headings and the ability to copy code blocks via a keyboard shortcut.
* [Google Calendar](https://github.com/YukiGasai/obsidian-google-calendar) by `@YukiGasai`  lets users interact a Google Calendar from inside Obsidian.

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

* [HTML Reader](https://github.com/nuthrash/obsidian-html-plugin) by `@nuthrash`  lets Obsidian open documents with ".html" and ".htm" file extensions.
* [Obsidian Sqlite3](https://github.com/windily-cloud/obsidian-sqlite3) by `@windily-cloud`  gives Obsidian the ability to manipulate sqlite3 databases.
* [Aosr](https://github.com/linanwx/aosr) by `@linanwx`  is "another obsidian spaced repetition" plugin.
* [Week Planner](https://github.com/rwirdemann/obsidian-week-planner) by `@rwirdemann`  defines commands for creating planning documents and moving tasks between them.
* [Sakana Widget](https://github.com/Quorafind/obsidian-sakana-widget) by `@Quorafind`  adds a cute character widget to your interface.
* [Imgbb Plugin](https://github.com/notmmaoo/obsidian-imgbb-plugin) by `@notmmaoo`  uploads images to Imgbb for Obsidian.
* [obsidian floating toc](https://github.com/cumany/obsidian-floating-toc-plugin) by `@cumany`  is a floating Toc plugin that hovers a table of content containing a header level on the notes sidebar.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

* [Templater 0.14.2](https://github.com/SilentVoid13/Templater) updated to the most recent version of Obsidian's API and go some nice bugfixes, including that syncing a new note with templates no longer... triggers the template. Also, I have a sneaking suspicion that if enough people joined the `#templater` [thread in Discord](https://discord.com/channels/686053708261228577/875720842443649045) that we filled up the thread and had to add a new channel, `shabogem` (one of the maintainers) would be overjoyed. So if you wanted to say thank you to the devs who work on this project, I suspect that's a good place to do it ;)
* [Bulk Rename](https://github.com/OlegLustenko/obsidian-bulk-rename/releases/tag/0.4.0) lets you use RegExp to search files to rename.
* [Linter](https://github.com/platers/obsidian-linter/releases/tag/1.5.0) has a new project board, and added custom commands, formatting for ordered lists, and the ability to copy tags into the frontmatter.
* [Literate Styles v0.2.0](https://github.com/johanfriis/obsidian-literate-styles/releases/tag/0.2.0), for writing theme css in Obsidian itself, changes the flavour of css from sass to less, to improve bundle size and performance.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

* Here's a plugin to [alert you if a note hasn't been updated](https://github.com/tadashi-aikawa/obsidian-old-note-admonitor) over a specific number of days.
* [Inline Scripts](https://github.com/jon-heard/obsidian-inline-scripts/releases/tag/0.22.2) added an interface with the dice roller plugin and support for virtual cards (here's [a tutorial video](https://www.youtube.com/watch?v=-m4n7d3aKC8)).

### For Developers

* The developer of the new bullet-point-backlinks plugin [Influx](https://github.com/jensmtg/influx) is a bit stumped on how to get it working right in reading view, if you've got any insight into that or want to take a look at the puzzle I'm sure `@jensmtg` would appreciate it.

## Appearance

* There's now an [official dracula theme](https://github.com/dracula/obsidian).
* [Cyber Glow](https://github.com/ArtexJay/Obsidian-CyberGlow) got some new glow effects and bugfixes and tweaks.

## Guides

* I really enjoyed this thread about [how to set up a second brain in 10 minutes or less per day](https://twitter.com/RichardHaggerty/status/1573315004253839361). It maps out the first 7 days for you in pretty solid detail.
* Here's a [beginner's guide to the editor settings](https://denisetodd.medium.com/obsidian-editor-settings-for-beginners-b84610ea6ce3).
* Here's how to create [interactive obsidian-anki flashcards that flip and fade](https://github.com/jeffchiou/obsidiflip), using CSS and two plugins.
* Here's a [task management system](https://forum.obsidian.md/t/my-task-management-system/36198) that got shared recently.

## Showcases

* Here's someone in Discord [taking a video call and taking notes from within Obsidian](https://media.discordapp.net/attachments/916477002909876265/1020709395216224316/unknown.png).
* This is an incredible [interactive medical terminology dictionary](https://forum.obsidian.md/t/interactive-medical-terminology-dictionary/43303) intended for use by medical students, and the best part is that it focuses on teaching Latin and Greek _roots_ that are useful for learning medical terms. It's even got dataview queries to help cross-reference related words. It's probably one of the most useful sample vaults I've ever seen.
* Here's how someone recently [planned a vacation with map view](https://www.reddit.com/r/ObsidianMD/comments/xi42pt/planning_a_vacation_with_map_view/). Incidentally vacation planning is one of my primary uses of Obsidian right now; my 5 year anniversary is coming up 👀 It's not all atomic academic notes, yanno? Although here's a nice [reflection on the atoms of Obsidian](https://samgqroberts.com/posts/the-atoms-of-obsidian-md).
* Here's how [someone uses Obsidian for writing novels](https://www.reddit.com/r/ObsidianMD/comments/xb869d/i_finally_figured_out_obsidian_using_omd_for/).

## Food for Thought

* Here are some thoughts about [why Obsidian isn't really a notetaking app](https://austingovella.medium.com/why-its-hard-to-get-started-obsidian-s-not-really-a-note-taking-app-75bafbebf6f3) and how that can make it hard to get used to.

## Ancillary Tools

* [iOS 16 + Launcher app](https://apps.apple.com/fi/app/launcher-with-multiple-widgets/id905099592?l=fi) enables Obsidian URL shortcuts on Lock Screen. iOS users can [find more details in Discord](https://discord.com/channels/686053708261228577/864046194195431425/1020371125806571530).
* The [Raycast Obsidian extension](https://github.com/marcjulianschwarz/obsidian-raycast) was updated.

## Housekeeping

* I got a chance to see [Noteshare](https://noteshare.space/install) in action in the wild (i.e. used by someone in a discord server totally unrelated to Obsidian) this morning and it was really slick! If you want to quickly share a single Obsidian note with folks, this is a great way.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-09-24%20Community%20Contest%20%26%20Spaced%20Repetition%20Improvements.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-09-24%20Community%20Contest%20%26%20Spaced%20Repetition%20Improvements.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
