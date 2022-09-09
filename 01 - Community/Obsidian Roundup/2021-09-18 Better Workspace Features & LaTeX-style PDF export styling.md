---
link: https://www.obsidianroundup.org/2021-09-18/
author: Eleanor Konik
published: 2021-09-18
publish: true
---

# 2021-09-18: Better Workspace Features & LaTeX-style PDF export styling
You can kind of hack together a way to get Obsidian into a browser now, and Drafts on iOS has new Obsidian integration options.

## In The Community

- `@SlRvb` and `@mikeschmitz` will be showcasing how they use Obsidian for journaling today at 3pm EST. There's more [information in Discord](https://discord.com/channels/686053708261228577/876257648624939008/888086347510865950).
- The [[obsidian-kanban|Kanban]] is looking for community help keeping the documentation up to date, so if you have any workflow tutorials (like [this German-language one](https://www.youtube.com/watch?v=6aU2lYGsRzw)) or such you'd like to add, you can [submit a pull request](https://github.com/mgmeyers/obsidian-kanban/tree/main/src/docs) to the GitHub repository.

## Obsidian Updates

[v0.12.16 is out for Insiders](https://forum.obsidian.md/t/obsidian-release-v0-12-16-insider-build/24166)!

- You can now undo closing a pane.
- Core now supports copying a code block in preview mode.
- Empty panes will be removed on startup if the plugin that created it has been uninstalled or disabled.
- `{{date}}` and `{{time}}` will now work with the core daily notes and [[Zettelkasten|zettelkasten]] prefixer plugins. Previously you needed to add the format, for example `{{date:YYYY-MM-DD}}`
- Creating new files from in note composer will now show an error if it contains illegal characters.
- You can now use Ctrl/Cmd+click or middle-click the icon or the command palette item to open daily note/new [[Zettelkasten|zettelkasten]] in a new pane

### Developers

- There is now access to the following bundled libraries: PDF.js, [[Mermaid]], Prism, MathJax. Each library does things a bit differently but Obsidian now exposes functions to load them if they weren’t loaded already: `loadPdfJs`, `loadMermaid`, `loadPrism`, `loadMathJax`.
- `request` can now set HTTP headers.

## Plugin News

### New

- [Blue Pill](https://github.com/dyldog/blue-pill) is a plugin designed to rename files from numerical UUIDs to a new file name based on the first header.
- [[Simple Embeds](https://github.com/samwarnick/obsidian-simple-embeds/tree/main) will allow twitter cards and youtube links to render in preview.
- [[workspaces-plus|Workspaces Plus]] comes with some nice features for making workspaces easier to work with, and includes handy features like auto-saving workspaces on switching, status bar indicators to let you visually see which workspace you're working in, etc. Here's how [Josh Duffney uses Workspaces](https://www.youtube.com/watch?v=EiI1ekkiB2k) if you're looking for a use-case example.
- This plugin lets you [add commands to the right click menu](https://github.com/kzhovn/obsidian-customizable-menu)
- The [copy command](https://github.com/kzhovn/copy-command-obsidian) makes the "make a copy" command available to the command palette and file menu. Shoutout to the dev for reading my mind because I was just lamenting the lack of this on Wednesday.

### Updates

- [[obsidian-kanban|Kanban]] is now out of beta with v1.0.0. Lanes are scrollable, cards can contain newlines, the input fields supports markdown editing, block embeds are supported, and there are some more action buttons functionality. Note: may contain breaking changes for some themes (but I haven't heard much chatter about this so you'll probably be fine).
- [[pane-relief|Pane Relief]] has a hotfix to support the new Insider build (0.12.16); please be sure to close any orphan panes!
- [[obsidian-dice-roller|Dice Roller]] had a major backend update that should speed things up, and you can modify and condition dicerolls, i.e. create formulas and variables. More details in the Readme!
- [[oz-image-plugin|Image in Editor]] can render [[Mermaid]] diagrams in transclusions in the editor. Which should give you an idea of the complexities WYSIWYG mode faces — and by the way, **WYSIWYG mode has been moved to the "In Progress" section of the Obsidian Roadmap.**
- The [[obsidian-linter|Linter]] plugin allows for footnotes to be moved and reindexed, which is useful for concatenation i.e. with the longform plugin, and also will reformat tags with hashtags in [[YAML frontmatter]] to be correct, i.e. removes the hashtag.
- [v1.11.0](https://github.com/denolehov/obsidian-git/releases/tag/1.11.0) of [[obsidian-git|Obsidian Git]] comes to us from the incredibly tenacious `@Vinadon` (who has faced some truly demoralizing struggles developing this plugin) and features support for initializing new repos and selecting upstream branches for pushing and pulling from.
- Users of the Folder Note plugin should be aware that most of the features have been migrated to the [Folder Note Core](https://github.com/aidenlx/folder-note-core): check out the [migration guide](https://github.com/aidenlx/alx-folder-note/wiki/migrate-from-v0.10.0-and-lower).
- [[obsidian-dictionary-plugin|Dictionary]] [2.18.0](https://github.com/phibr0/obsidian-dictionary) lets you override the language for an individual note by noting the preferred language in the YAML.

### Betas

- [Text Transporter](https://github.com/TfTHacker/obsidian42-text-transporter/releases) is currently rapidly iterating through beta testing (aka will require manual install) and `@TFTHacker` is looking for testers to help put it through its paces before code review. It's an Obsidian riff off of his Roam workflow, and offers a bunch of features, including replace a link with its original text, slinging text around, bookmarks, quick capture, and more.

## Feature Requests

- People used to IDEs like [[VSCode|Visual Studio Code]] would love it if it were possible to ["tab out" of markup](https://forum.obsidian.md/t/pressing-tab-when-inserting-a-link-should-move-the-cursor-to-the-next-brackets/11953) instead of needing to use the arrow key.
- Is it possible to [assign a hotkey to readable line width](https://forum.obsidian.md/t/is-there-a-way-to-set-readable-line-length-option-to-a-hotkey/24255)? I know there have been times when I really wanted this, too, especially when dealing with tables.

## Appearance

- The [LaTeX insipired CSS Snippet for PDFs](https://www.buymeacoffee.com/phibr0/e/42263) is designed to help with page breaks, automatically number headings, and more.
- The [[ITS Theme]] had an update that [reduces the filesize by moving icons to an external snippet and some new Style Settings toggles](https://forum.obsidian.md/t/theme-its-dark-light-theme/12838/132).
- [[Yin and Yang]] theme got an update to change the darkness value of the base color that should help with reflective screens.

## Ancilliary Code

- the [Web Clipper bookmarklet](https://gist.github.com/kepano/90c05f162c37cf730abb8ff027987ca3) from `@kepano` has some more features, like removal of illegal characters and variables for tagging things more easily.
- `@Ckain` figured out how to get [Obsidian as a dockerfile to use Obsidian in a browser](https://discord.com/channels/686053708261228577/694233507500916796/888512777336021044). I understand about half of the instructions but I feel like this is an incredible thing for developers who want to access their Obsidian notes from a locked down computer at work, so if you know what "[[Docker]] file" and "container" and "reverse proxies" mean, check this out! If you don't, this is an advanced option, please don't try.

## Guides

- Here's why you [probably should not store plain text passwords in Obsidian](https://www.reddit.com/r/ObsidianMD/comments/pmscaz/is_obsidian_safe_for_storing_your_passwords_there/).
- Here's a guide of _why_ to use [Obsidian for RPGs](https://www.youtube.com/watch?v=cLMcRiacY3g). Even if you don't care about TTRPGS, though, it has some really nifty looks at how people can use timelines, kanban boards, and statblocks.
- `@_Nick` shared a nice overview of [different notetaking methods they iterated through](https://www.nickseitz.com/writing/take-less-stupid-notes) looking for the one that worked for them.
- `@nvanderhoevan` shared how she uses [Obsidian for work](https://nicolevanderhoeven.com/blog/20210518-how-i-use-obsidian-at-work/); her notes are available to coworkers via git.
- Here's a neat video guide on how to [do mindmapping in Obsidian](https://www.youtube.com/watch?v=pWcHBmJLvLc&feature=youtu.be)
- Here's a writeup about how to use [Obsidian for cultivating a writing habit with morning pages](https://www.cultivatingmentalsilence.com/blog/using-the-obsidian-app-to-do-morning-pages).
- Here's a video guide about [how to take concept notes](https://www.youtube.com/watch?v=MYJsGksojms) that leverages the linking your thinking philosophy.
- Here's how `dannyhatcher` takes [notes from a bunch of different sources](https://www.youtube.com/watch?v=tLa2tNuXau0&feature=youtu.be) in a consistent way.

## Knowledge Management

- Here's a nice discussion in Discord about [how to deal with information overload](http://discordapp.com/channels/686053708261228577/722584061087842365/888244420728741938).
- Here's a discussion on Reddit about how to use [Obsidian as a lab notebook](https://www.reddit.com/r/ObsidianMD/comments/pojd73/does_anyone_use_obsidian_as_a_lab_notebook/).
- Here's a discussion about [how to leverage Obsidian for a Master's thesis](https://forum.obsidian.md/t/start-using-obsidian-for-masters-thesis-when-you-already-have-a-rough-outline-in-mind/24228/3).

## In The Wild

Every now and then someone shares a link to a popular outlet "discovering" Obsidian and writing about it and I'm never sure about adding it to the Roundup because I'm never sure if it's teaching _us_ anything — we already know about Obsidian — but ultimately, I think it's fun to see what "new users" are saying about Obsidian and it's kind of neat to see my niche notetaking tool mentioned "in the wild" so maybe you feel the same way.

- Here's Andrew Myrick of Android Central on why [Obsidian is the best notetaking app most people have never heard of](https://www.androidcentral.com/obsidian-best-note-taking-app-youve-never-heard).

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- [[Drafts App|Drafts]] [v28](https://forums.getdrafts.com/t/drafts-28-released-ready-for-new-ios-macos-folder-bookmarks-and-more/11201) for iOS makes it possible to grant permissions to additional folders outside the [[Drafts App]] Sandboxl their release notes specifically mention that it should now be easier to integrate it with Obsidian.

## Housekeeping

- I think I sorted the database problems. I haven't had time to sit down and write a postmortem but suffice it to say that without the support of this community (especially moderator `@Leah` and her incredible excel skills) I would probably still be deep in database hell. For those curious about the topline result, I managed to salvage most of the Roundup database but had to wipe the Iceberg back to nothing, and I'm not totally convinced that some of the weirder problems we ran into won't recur, but I'm hopeful that things should be alright going forward. Thanks for all your kind words during a dark time 💚.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-09-18%20Better%20Workspace%20Features%20%26%20LaTeX-style%20PDF%20export%20styling.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-09-18%20Better%20Workspace%20Features%20%26%20LaTeX-style%20PDF%20export%20styling.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
