---
link: https://www.eleanorkonik.com/2022-04-22/
author: Eleanor Konik
published: 2023-04-22T12:30:15
publish: true
---

# 2023-04-22: Huge Publish Improvements, a Telegram integration, & more LLM options
New plugins for scientists & storytellers. Guides for knowledge management & new features. Plus, a review of a year in Obsidian.

## In The Community

* A grad student at Georgia Tech is doing [a survey about improving the Obsidian interface for better human-computer interaction](https://www.reddit.com/r/ObsidianMD/comments/12rg7ox/survey_followup_research_for_obsidian_for/?ref=eleanorkonik.com). Consider filling it out if you've got some time.

## Obsidian Updates

* Obsidian Publish [now offers more for less](https://forum.obsidian.md/t/obsidian-publish-now-offers-more-for-less-a-lower-price-with-new-features-improved-seo-and-accessibility/58272?ref=eleanorkonik.com): a lower price, with new features, improved SEO and accessibility. For Insiders on v.1.2.5 there's also new [navigation customization options](https://forum.obsidian.md/t/obsidian-release-v1-2-5-insider-build/58384?ref=eleanorkonik.com), along with a series of fixes. Specifically Obsidian Publish now supports overriding SEO/social metadata with three new YAML keys: `description` overrides the meta description (you can remove Markdown that way if you want). `permalink` overrides the URL/slug. `image` or `cover` accepts an image URL or vault asset, and overrides the auto generated share card. Kepano also [announced on Reddit](https://www.reddit.com/r/ObsidianMD/comments/12qtwt3/comment/jgrzwff/?utm_source=reddit&utm_medium=web2x&context=3) that there will be news about plugin support for Publish in the future.

## Plugin News

### New in Community Plugins

__These plugins went through code review and are now available in Obsidian's plugin list.__ For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new?ref=eleanorkonik.com).

* [Find orphaned files and broken links](https://github.com/Vinzent03/find-unlinked-files?ref=eleanorkonik.com) by `@Vinzent03` lets users find files that are not linked anywhere and would otherwise be lost in your vault.
* [Draw Harada Method](https://github.com/yildbs/obsidian-harada-method-plugin?ref=eleanorkonik.com) by `@yildbs` is used to draw the harada method for goal setting.
* [Vim Toggle](https://github.com/conneroisu/vim-toggle?ref=eleanorkonik.com) by `@conneroisu` enables the toggling vim mode to on and off inside of the editor.
* [Bulk open selected links](https://github.com/autohub7/obsidian-open-selected-links?ref=eleanorkonik.com) by `@autohub7` allows users to easily open all selected links in edit mode.
* [Tab Rotator](https://github.com/autohub7/obsidian-tab-rotator?ref=eleanorkonik.com) by `@autohub7` rotates opened files to the left or right with a specified interval
* [No Tabs](https://github.com/TS-Tobias/obsidian-no-tabs?ref=eleanorkonik.com) by `@TS-Tobias` replaces the previous tab when creating a new note.
* [File Order](https://github.com/lukasbach/obsidian-file-order?ref=eleanorkonik.com) by `@lukasbach` makes it easier to use number-prefixes in your file names to define a custom order, and drag-and-drop the files to update that order.
* [Frontmatter Alias Display](https://github.com/muhammadv-i/obsidian-frontmatter-alias-display?ref=eleanorkonik.com) by `@muhammadv-i` shows front-matter aliases as display names in the File Explorer.
* [Whisper](https://github.com/nikdanilov/whisper-obsidian-plugin?ref=eleanorkonik.com) by `@nikdanilov` facilitates hands-free note-taking with Whisper.
* [Get Stock Information](https://github.com/mikejongbloet/obsidian-get-stock-information?ref=eleanorkonik.com) by `@mikejongbloet` takes a stock symbol and returns a callout block with the latest stock information.
* [Character Insertion](https://github.com/TakamiChie/Obsidian_CharacterInsertionPlugin?ref=eleanorkonik.com) by `@TakamiChie` makes it easier to insert a specified symbol under the cursor
* [Search Obsidian in Google](https://github.com/qazxcdswe123/search-obsidian-in-google?ref=eleanorkonik.com) by `@qazxcdswe123` includes your Obsidian notes in browser-based search engines.
* [Colorful Note Borders](https://github.com/rusi/obsidian-colorful-note-borders?ref=eleanorkonik.com) by `@rusi` makes it easier to add customizable colorful borders to notes based on folder location or frontmatter metadata, enhancing visual organization in Obsidian.
* [Unfilled Stats Highlighter](https://github.com/White7292/obsidian-hd-unfilled-stats-highlighter?ref=eleanorkonik.com) by `@White7292` is designed to streamline your stat/habit tracking process by automatically identifying and prefixing unfilled stats, making them easier to spot and fill out.
* [Cron](https://github.com/cdloh/obsidian-cron?ref=eleanorkonik.com) by `@cdloh` is a simple CRON / schedular plugin to regularly run user scripts or Obsidian commands.
* [Code Files](https://github.com/lukasbach/obsidian-code-files?ref=eleanorkonik.com) by `@lukasbach` allows users to edit code files in Obsidian with VSCode's powerful Monaco Editor.
* [WuCai highlights Official](https://github.com/makediff/obsidian-wucai?ref=eleanorkonik.com) by `@makediff` is an official WuCai highlights <-> Obsidian integration
* [Companion](https://github.com/rizerphe/obsidian-companion?ref=eleanorkonik.com) by `@rizerphe` adds a github copilot-like interface for obsidian that can use ChatGPT under the hood.

### Pending (as of Friday morning)

__Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat?ref=eleanorkonik.com). Note, though, that this is not as safe as waiting for them to go through code review.__

* [ZettelGPT](https://github.com/OverRaddit/ZettelGPT?ref=eleanorkonik.com) by `@OverRaddit` is optimized for creating question notes and answer notes, where the answer notes use the question from the question note and the history of the conversation up to that point; the goal is that by providing only the relevant conversation history, you can save GPT tokens and optimize the plugin's efficiency.
* [Footnote Shortcut](https://github.com/Comprehensive-Jason/obsidian-footnotes?ref=eleanorkonik.com) by `@Comprehensive-Jason` makes it easier to insert and write footnotes faster
* [Telegram Sync](https://github.com/soberhacker/obsidian-telegram-sync?ref=eleanorkonik.com) by `@soberhacker` makes it easier to transfer messages and files from Telegram bot to Obsidian.
* [BMO Chatbot](https://github.com/longy2k/obsidian-bmo-chatbot?ref=eleanorkonik.com) by `@longy2k` is a highly customizable chatbot option.
* [Ketcher](https://github.com/yuleicul/obsidian-ketcher?ref=eleanorkonik.com) by `@yuleicul` makes it easier to view or draw chemical structures and reactions using Ketcher, a web-based molecule sketcher.
* [Game Search](https://github.com/CMorooney/obsidian-game-search-plugin?ref=eleanorkonik.com) by `@CMorooney` helps you find games and create notes.
* [AI Mentor](https://github.com/clementpoiret/ai-mentor?ref=eleanorkonik.com) by `@clementpoiret` is oriented around asking questions, getting answers, and learning new things.
* [April's Automatic Timelines](https://github.com/April-Gras/obsidian-auto-timelines?ref=eleanorkonik.com) by `@April-Gras` is a simple timeline generator for story tellers.
* [Persistent Links](https://github.com/ivan-lednev/obsidian-persistent-links?ref=eleanorkonik.com) by `@ivan-lednev` will automatically repair internal links to blocks and headings.

### Updates

__If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates?ref=eleanorkonik.com) by Ganessh Kumar.__

* [Make.md](https://make.md/?ref=eleanorkonik.com) improved sync support, got a new backend that's more reliable and responsive, supports "smart spaces," dynamic views, and [new documentation](http://make.md/docs?ref=eleanorkonik.com).
* [Tasks 3.2.0](https://github.com/obsidian-tasks-group/obsidian-tasks/releases/tag/3.2.0?ref=eleanorkonik.com) added "created today" to the autosuggest menu. [3.3.0](https://publish.obsidian.md/tasks/Reference/Task+Formats/Dataview+Format?ref=eleanorkonik.com) supports Dataview's bracketed inline fields.
* [Notion Like Tables v6.3.0](https://github.com/trey-wallis/obsidian-notion-like-tables/releases/tag/6.3.0?ref=eleanorkonik.com) thru [6.3.3](https://github.com/trey-wallis/obsidian-notion-like-tables/releases/tag/6.3.3?ref=eleanorkonik.com) added improvements for mobile as well as date format options to date cells, settings for table file paths, the ability to drag and drop rows, aria labels to buttons, and more.
* [Task Collector](https://github.com/ebullient/obsidian-task-collector?ref=eleanorkonik.com) fixed a bunch of bugs and now has a modal for selecting checkboxes in reading or live preview modes.

## Appearance

* [Synthwave '84](https://github.com/G2Jose/synthwave-84-obsidian-theme?ref=eleanorkonik.com) by `@G2Jose` is a yellow and purple theme that reminds me a bit of Dracula with a hint of Rose Pine.
* [Olivier’s Theme](https://github.com/OlivierPS/Olivier-s-Theme?ref=eleanorkonik.com) by `@OlivierPS` focuses on legibility and simplicity, and takes inspiration from pencil and paper.
* [Prism 3.2.4](https://github.com/damiankorcz/Prism-Theme/releases/tag/3.2.4?ref=eleanorkonik.com) improved hover states, padding, and spacing.

## Guides

* Here's a new guide for [Making a Desktop-only Plugin Work on your Phone or Tablet](https://tfthacker.medium.com/hacking-obsidian-making-a-desktop-only-plugin-work-on-your-phone-or-tablet-d49ed357b02c?ref=eleanorkonik.com).
* Here's a pretty good explanation of [how the new Bookmarks feature can impact your workflows](https://www.youtube.com/watch?v=SVlMpzaAAT0&ref=eleanorkonik.com).
* Here's a pretty interesting writeup of an [org-mode knowledge management system](https://cpbotha.net/2023/04/11/note-taking-strategy-2023/?ref=eleanorkonik.com) that seems easy to port to Obsidian, so I wanted to share.
* Here's a [guide to Obsidian for people who like Outliners](https://tfthacker.medium.com/demystifying-obsidians-outlining-superpowers-20c077793356?ref=eleanorkonik.com).
* Here's a guide to [getting your own API key so you can use plugins that use openAI](https://tfthacker.medium.com/how-to-get-your-own-api-key-for-using-openai-chatgpt-in-obsidian-41b7dd71f8d3?ref=eleanorkonik.com); hopefully those plugins will add something like this to their documentation 😅
* Here's how to [install Obsidian on your Synology NAS](https://mariushosting.com/how-to-install-obsidian-on-your-synology-nas/?ref=eleanorkonik.com).
* Here's a great [beginner's guide to Obsidian as a Zettelkasten](https://mattgiaro.com/obsidian-zettelkasten/?ref=eleanorkonik.com).
* Here's a guide on [how to use Dataview queries as part of automating your daily notes](https://ricraftis.au/obsidian/automating-obsidian-daily-notes-part-4-using-dataview-queries/?ref=eleanorkonik.com).

## Discussions

* Here's a lengthy Reddit discussion about [the one feature you most want](https://www.reddit.com/r/ObsidianMD/comments/12n8vbu/whats_the_1_feature_that_is_needed_in_obsidian_if/?ref=eleanorkonik.com). "Better tables" was the most upvoted response.
* Here's a [year of Obsidian use in review](https://medium.com/technology-hits/my-obsidian-setup-my-notes-and-my-theme-settings-8f434eb377ba?ref=eleanorkonik.com).

## Showcases

* In light of the new Publish changes, kepano highlighted a few great examples of Publish sites: [https://lab.marconoris.com/](https://lab.marconoris.com/?ref=eleanorkonik.com) (2) [https://www.andricheli.com/](https://www.andricheli.com/?ref=eleanorkonik.com) (4) [https://mister-chad.com/](https://mister-chad.com/?ref=eleanorkonik.com) (3) [https://notes.joschua.io/](https://notes.joschua.io/?ref=eleanorkonik.com)

## Ancillary Tools

* The [Alfred Workflow for Obsidian](https://alfred.app/workflows/chrisgrieser/shimmering-obsidian/?ref=eleanorkonik.com) has now been admitted to the Alfred Gallery as a featured workflow, and now is easier to auto-update and install.
* [Duckbase](https://www.duckbase.io/?ref=eleanorkonik.com) centralizes information from Obsidian, Notion, Evernote and Chrome, then uses a LLM to answer questions based on your personal knowledge base.

## Programming Note

* The Roundup is taking a week off; the next edition will ship on May 6. I'll be flying home from Ireland on April 29 and it seems irresponsible to promise that I'll manage to get much done given the week I'm expecting to have 😅

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2023-04-22%20Huge%20Publish%20Improvements%2C%20a%20Telegram%20integration%2C%20%26%20more%20LLM%20options.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2023-04-22%20Huge%20Publish%20Improvements%2C%20a%20Telegram%20integration%2C%20%26%20more%20LLM%20options.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
