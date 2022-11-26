---
link: https://www.obsidianroundup.org/2022-11-12/
author: Curtis McHale
published: 2022-11-12T13:30:50
publish: true
---

# 2022-11-12: Stable Diffusion, Clean Dashboards and 2022 Workflows
A new social media instance for personal knowledge management & a theme to bring back old-style Obsidian.


> Eleanor got Lasik on Thursday so she's trying to take it easy this weekend. This issue was guest edited by [Curtis McHale](https://curtismchale.ca).

## In The Community

_Note: a bunch of great things happen in Discord every week, but the links require you to be logged in to [the community server](https://obsidian.md/community) and generally launch in the browser version of Discord unless you paste them into your app directly. Sorry!_ 

* The Obsidian October submission window closes November 13, 2022 (extended due to 1.0 release and addition of the theme categories) [anywhere on Earth](https://en.wikipedia.org/wiki/Anywhere_on_Earth) – if you created a theme, blog post, plugin, sample vault, major update to something, video, etc... you can submit via [this form](https://airtable.com/shraMn6xDv4LwgRvA).
* This is a [very clean note look](https://discord.com/channels/686053708261228577/744933215063638183/1040346301331669012) from `@ruru`
* `@Anubis` has some [nice looking folders with image masks](https://discord.com/channels/686053708261228577/744933215063638183/1040069917728317450).
* From `@dhniceday` – [sometimes the little things that make you happy](https://discord.com/channels/686053708261228577/744933215063638183/1038941359081533440) will make your note taking better.
* Nicole van der Hoeven and Marcus Olsson set up a Mastodon instance for personal knowledge management enthusiasts: <https://pkm.social/>

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list._ _For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new)._

* [Ava](https://github.com/louis030195/obsidian-ava) by [_louis030195_](https://github.com/louis030195) is a new plugin that uses Stable Diffusion to generate images directly in Obsidian. It does look like it takes a bit to setup, but could be worth it if you're interested in generating these images.
* [Obsidian Scroll to Top](https://github.com/cloudhao1999/obsidian-scroll-to-top-plugin) by [cloudhao1999](https://github.com/cloudhao1999) gives you an icon to click that will take you to the top of your Obsidian note.
* [Obsidian OCR](https://github.com/MohrJonas/obsidian-ocr) by [MohrJonas](https://github.com/MohrJonas) brings optical character recognition to Obsidian so you can search for text in images and PDFs.
* [Obsidian Gitlab Issues](https://github.com/benr77/obsidian-gitlab-issues) by [benr77](https://github.com/benr77) loads your Gitlab Issues in an output directory of your choice.
* [Tag Summary](https://github.com/macrojd/tag-summary) by [macrojd](https://github.com/macrojd) creates summaries with paragraphs and blocks that have matching tags.
* [Obsidian Account Linker](https://github.com/qwegat/Obsidian-Account-Linker) by [qwegat](https://github.com/qwegat) lets you define different social accounts in note frontmatter and have them reslove to links to the accounts on their services. Could be useful if you're tracking sales contacts in Obsidian.
* [Linter](https://github.com/platers/obsidian-linter) by `@pjkaufman` Formats and styles your notes. It can be used to format YAML tags, aliases, arrays, and metadata; footnotes; headings; spacing; math blocks; regular markdown contents like list, italics, and bold styles; and more with the use of custom rule options as well.
* [Obsidian Symbols Prettifier](https://github.com/FlorianWoelki/obsidian-symbols-prettifier) by [FlorianWoelki](https://github.com/FlorianWoelki) takes typed symbols like `->` and makes them look nicer.
* [Obsidian MTG](https://github.com/omardelarosa/obsidian-mtg) by [omardelarosa](https://github.com/omardelarosa) is for managing your Magic: The Gathering card collections and decks in Obsidian.
* With [Obsidian Editing Toolbar](https://github.com/cumany/obsidian-editing-toolbar), [cumany](https://github.com/cumany) picked up the development of [cmenu](https://github.com/chetachiezikeuzor/cMenu-Plugin). This plugin gives you ways to format your text in Obsidian without needing to know markdown.
* [Obsidian Floating TOC](https://github.com/cumany/obsidian-floating-toc-plugin) by [cumany](https://github.com/cumany) gives you a floating table of contents to make navigating big documents faster.
* [Obsidian Things3 Sync](https://github.com/royxue/obsidian-things3-sync) by [royxue](https://github.com/royxue) lets you add tasks to Things3 and toggle their status from Obsidian.

### Pending (as of Friday morning)

_Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

* [Toggle Meta Yaml](https://github.com/hua03/obsidian-toggle-meta-yaml-plugin) by `@hua03` this is a simple plugin to toggle meta yaml.
* [Code Preview](https://github.com/zjhcn/obsidian-code-preview) by `@zjhcn` provides a Code Preview of specified files in your vault.
* [Incremental ID](https://github.com/adziok/obsidian-incremental-id) by `@adziok` lets users generate Jira like ids.
* [Obsidian asciimath](https://github.com/widcardw/obsidian-asciimath) by `@widcardw` adds asciimath support for Obsidian.
* [Achievements](https://github.com/Zachatoo/obsidian-achievements) by `@Zachatoo` adds achievements to Obsidian.
* [Markdown to Jira Converter](https://github.com/muckmuck96/obsidian-md-to-jira) by `@muckmuck96` is a markdown to jira markup and backwards converter plugin for Obsidian.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

* [Obsidian ABC.JS Plugin](https://github.com/abcjs-music/obsidian-plugin-abcjs) updated so you can note the language in codeblocks. This is a music notation plugin.
* [Obsidian Hover Editor](https://github.com/nothingislost/obsidian-hover-editor) now has better support for 1.0 tabs.
* [Obsidian Party](https://github.com/shap-po/obsidian-party) allows you to have confetti appear when you click buttons or checkboxes. It resolved a few bugs with window dragging and duplication of buttons.
* [Obsidian Switcher Plus](https://github.com/darlal/obsidian-switcher-plus/releases) added more formatting options when you're searching for files in the switcher.
* [Obsidian Full Calendar](https://github.com/davish/obsidian-full-calendar/releases) added some cosmetic fixes this week.
* [Obsidian Custom Sort](https://github.com/SebastianMC/obsidian-custom-sort/releases) added support for more alphabetical sorting options.
* [Obsidian Kindle Plugin](https://github.com/hadynz/obsidian-kindle-plugin/releases) fixed an issue with templates that started with `if` statements.
* [Tag Wrangler](https://github.com/pjeby/tag-wrangler/releases) now allows you to drag tags into the editor as text.
* [PodNotes](https://github.com/chhoumann/podnotes/releases) will now create the folders you need if they don't exist.
* [Obsidian Bible Linker](https://github.com/kuchejak/obsidian-bible-linker-plugin/releases) will now let you copy an entire book of the bible.
* [Obsidian Quiet Outline](https://github.com/guopenghui/obsidian-quiet-outline/releases) has better mobile support, and fixed a bug when switching between light/dark mode.
* [Lumberjack](https://github.com/ryanjamurphy/lumberjack-obsidian/releases) will now let you create Timber files in the root of your vault.
* [Obsidian Digital Garden](https://github.com/oleeskild/obsidian-digital-garden/releases) now has support for search.
* [Obsidian Tasks](https://github.com/obsidian-tasks-group/obsidian-tasks/releases) has lots of updates and fixes in this week. You'll need to restart after updating.
* [Novel Word Count](https://github.com/isaaclyman/novel-word-count-obsidian/releases) fixed an issue with showing you the wordcount when you update workspaces.
* [Todoist Completed Tasks](https://github.com/Ledaryy/obsidian-todoist-completed-tasks/releases) now supports the v9 API and has other various bug fixes.
* [Obsidian Projects](https://github.com/marcusolsson/obsidian-projects/releases) added legibility features and squashed some bugs.
* [Obsidian Chat View](https://github.com/adifyr/obsidian-chat-view/releases) has updated to support the latest version of Code Mirror which means it should work again in current versions of Obsidian.
* [Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases) had a bug for Grep searches in Linux, but that's fixed now.

### Betas

* [Various Complements](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/7.4.0-beta1) has 7.4.0-beta1 out for the brave.
* [Obsidian Carry Forward](https://github.com/jglev/obsidian-carry-forward/releases) has a beta out for 1.4.4.
* [Obsidian Paste to Current Indentation](https://github.com/jglev/obsidian-paste-to-current-indentation/releases) 5.0-beta is available. This lets you download files locally when you paste.

## Appearance

* [ion](https://github.com/zamsyt/obsidian-ion) by `@zamsyt` is a nice dark and pastel theme.
* [Aura](https://github.com/ashwinjadhav818/obsidian-aura) by `@ashwinjadhav818` is a minimal theme with some gradients in the sidebars.
* [deeper work](https://github.com/lucas-fern/obsidian-deeper-work-theme) by `@lucas-fern` is inspired by the deep work theme, which is no longer maintained.
* [Mado Miniflow](https://github.com/hydescarf/Obsidian-Theme-Mado-11) by `@hydescarf` is a minimal theme inspired by Windows 11
* [Doctorfree](https://github.com/doctorfree/Obsidian-Doctorfree) by `@doctorfree` – I love the hot pink and high contrast in this theme
* [Oldsidian Purple](https://github.com/ltctceplrm/oldsidian-purple) by `@ltctceplrm` if you're missing the pre 1.0 look of Obsidian, this is the theme for you.

## Guides

* Nicole and Marcus did a long stream talking about the [Obsidian Projects plugin](https://www.youtube.com/watch?v=LdaMe2rzAW8&t=326s). This plugin is on my list to dig into.
* Nicole also talked about using [multiple vaults in Obsidian](https://www.youtube.com/watch?v=IV3PHeyCHvc).
* [What is Justin's setup in 2022](https://www.youtube.com/watch?v=UBDIevN_iZk&list=WL&index=5)?
* Sergio shared how he uses [Obsidian to learn new things](https://www.youtube.com/watch?v=DwSNZEW6jCU&list=WL&index=2).
* Here's how [you can make your notes colourful](https://www.youtube.com/watch?v=sBDkNXLRSFw&list=WL&index=3).

## 


%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-11-12%20Stable%20Diffusion%2C%20Clean%20Dashboards%20and%202022%20Workflows.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-11-12%20Stable%20Diffusion%2C%20Clean%20Dashboards%20and%202022%20Workflows.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
