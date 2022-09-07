---
link: https://www.obsidianroundup.org/2021-08-14/
author: Eleanor Konik
published: 2021-08-14
publish: true
---

# 2021-08-14: Highlights Syncing & a Minimal Editor GUI
Default view modes, emoji shortcodes, & CLI tools for plugin devs.

## Plugin News

### New

- [Readwise](https://readwise.io/i/ac9) shipped their [[readwise-official|official integration plugin]] this week and it’s generating a ton of buzz. Here's the [forum thread](https://forum.obsidian.md/t/the-official-readwise-obsidian-integration-has-launched/22311/5) but basically, Readwise lets you import highlights and annotations from pdfs, rss readers, twitter, ebooks and more. It also has the best OCR highlighter for dead tree books I’ve ever come across, and while checking it out again for the Roundup I discovered that they have education pricing. Their team is also super nice, too, and have been helping people out in the Obsidian Discord. You can get a month free using [this link](https://readwise.io/i/ac9) if you sync highlights to your account. Here's a pretty good overview of [what to expect from the plugin](https://medium.com/@benenewton/first-look-at-the-official-readwise-obsidian-plugin-5d553c0d0521).
- [[obsidian-pocket|Pocket integration]] plugin allows users to sync [[Pocket]] reading lists into Obsidian.
- It's now possible to use [[YAML]] to force the view-mode of a note, i.e. to set a note with a [[dataview|Dataview]] block to always open in preview mode by default. The plugin is very descriptively called [[obsidian-view-mode-by-frontmatter|Force note view mode]].
- [[macro-plugin|Macros]] lets you combine commands from the command palette, with optional delays between commands.
- Obsidian now has an [[obsidian-toggl-integration|integration with Toggl]] timers.
- The [[customizable-sidebar|Customizable Sidebar]] plugin allows you to add any command, including those of plugins, to the sidebar and assign custom icons to them. Here's information for how [developers can add icons to their commands](http://discordapp.com/channels/686053708261228577/840286264964022302/875393424918999081).
- We now have support for [[emoji-shortcodes|Emoji Shortcodes]] in Obsidian, which makes `:heart:` turn into ❤️.
- You can now [[number-headings-obsidian|automatically number headings]].
- [[alx-folder-note|AidenLx's Folder Note]] iis a bit of an update on the [[folder-note-plugin|OG]] version by `xpgo` that lets you have a folder function as a note.
- This customizable [[obsidian-linter|Linter]] plugin will let you "fix" markdown styling to be more consistent within a note.
- The new [[obsidian-wordnet-plugin|Obsidian42 - WordNet Dictionary]] is a dictionary plugin that works from the command palette instead of sidebar or right-click menu.

### Updates

- The absolutely gorgeous minimal text editor modal plugin [[cmenu-plugin|cMenu]] from the developer of [[Yin and Yang]] now has a setting for custom commands on the little ui bar.
- the original [[todoist-sync-plugin|Todoist Plugin]] released 1.8 with mobile support & a few other nice features.
- [[breadcrumbs]] has had a breaking change update that allows for multiple separate hierarchies.
- [[obsidian-git|Obsidian Git]] [v1.10.0](https://github.com/denolehov/obsidian-git/releases/tag/1.10.0) now has submodules support.
- v1.0.3 of [[longform|Longform]] has some bugfixes.
- v1.6.0 of the [[obsidian-spaced-repetition|Obsidian Spaced Repetition]] plugin has single and multi line reversed cards function, the ability to ignore flashcards using HTML comments, and some caching improvements.

### For Developers

- [Obsidian Tools](https://github.com/obsidian-tools/obsidian-tools) is an unofficial package designed to help devs build plugins that has some nifty CLI stuff.
- Here's a tutorial about how to do stuff with [custom events](https://shbgm.ca/obsidian/docs/plugin-development/custom-events).
- `@TfTHacker` put together this [object model diagram](https://twitter.com/TfTHacker/status/1424051711220625409) to help visualize the Obsidian API.

## Workflow Stuff

- Here's how you can [view your latest readwise highlights in your daily note using the Templater plugin](https://medium.com/@benenewton/how-i-view-my-latest-readwise-highlights-in-my-obsidian-daily-note-3d321dd6ed07)
- Danny Hatcher put together a beginner's guide for [building a second brain from scratch](https://www.youtube.com/watch?v=njibNuFQwjw) using Obsidian.
- Here's a guide for how to [Generate Custom PDFs with Pandoc, Panrun, and The Eisvogel LaTex Template](https://forum.obsidian.md/t/generate-custom-pdfs-with-pandoc-panrun-and-the-eisvogel-latex-template/22237/).
- Here is a [quick guide](https://gist.github.com/chrisgrieser/4f64b0fc656480ea707d2b45a03acdc0) from `@pseudometa` explaining how to deal with the problem that Pandoc does not understand Obsidian's Wiki-Style image links(`![[ ]]`).
- Here's a tutorial on [using Templater, Buttons & Dataview together](https://shbgm.ca/obsidian/docs/insert-dataview-table).
- `@ryanjamurphy` put together this nifty Obsidian environment for [qualitative data analysis](https://axle.design/an-integrated-qualitative-analysis-environment-with-obsidian)
- Here's a nifty guide to how [semantic line breaks](https://sembr.org/) can work with the Markdown spec to help make long text easier to parse.
- Here's a [[MacOS Tools|MacOS]] [guide](https://forum.obsidian.md/t/make-obsidian-a-default-app-for-markdown-files-on-macos/22260) for how to make Obsidian your default markdown editor for files in your vaults + simultaneously make other app of your choice (for example, [[VSCode]]) default markdown editor for files outside of your Obsidian vaults.
- Here's how you can [symlink your Markdownload files into your vault](https://forum.obsidian.md/t/markdownload-markdown-web-clipper/173/121) — without needing fancy plugins.
- `@SlRvb` shared how they use [Obsidian for jouranling](https://forum.obsidian.md/t/slrvbs-journaling-setup/22346)

## Feature Requests

- `@arminta7` requested a plugin that can allow for better automations like what [[Hazel]] and [[Dropbox]] can do automate stuff in vaults via [[Zapier]], etc. Here's an [example](https://twitter.com/hstagner/status/1401175949987753986) of how some folks are _currently_ using [[Zapier]] with Obsidian.
- The request for [Smart Folders](https://forum.obsidian.md/t/smart-folders-notes-can-sort-automatically-to-chosen-folders-based-on-tags/4342/14) is still getting traction!

## Appearance

- the [[Yin and Yang]] now has better mobile optimization, more customizable feature settings in Style SEttings, & some other nice stuff.
- The delightful [[Obsidian Windows 98 Edition]] theme makes Obsidian look like a Win98 program.

## Knowledge Management

- `@joshduffney` has a nice video about [how to categorize and manage fleeting notes](https://www.youtube.com/watch?v=cvYitBS1yOY).
- `@ryanjamurphy` shared a new [framework for understanding Integrated Thinking Environments](https://axle.design/obsidian-roam-and-the-rise-of-integrated-thinking-environments%E2%80%94what-they-are-what-they-do-and-what-s) like Obsidian.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- [Manubot](https://manubot.org/) lets you take a manuscript written in markdown track it with git, automatically convert it to .html, .pdf, or .docx, and deploy it to your destination of choice. Hopefully this helps all the folks trying to figure out how to collaborate using Obsidian.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-08-14%20Highlights%20Syncing%20%26%20a%20Minimal%20Editor%20GUI.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-08-14%20Highlights%20Syncing%20%26%20a%20Minimal%20Editor%20GUI.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
