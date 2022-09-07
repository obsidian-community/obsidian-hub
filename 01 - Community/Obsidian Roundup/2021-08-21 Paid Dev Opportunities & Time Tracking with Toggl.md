---
link: https://www.obsidianroundup.org/2021-08-21/
author: Eleanor Konik
published: 2021-08-21
publish: true
---

# 2021-08-21: Paid Dev Opportunities & Time Tracking with Toggl
Advanced pdf processing, spellchecker requests & a vault for the meta-game Nomic.

## In The Community

- There was a Reddit thread about [why Obsidian sync is great](https://www.reddit.com/r/ObsidianMD/comments/p7f6gc/obsidian_sync_is_great/h9kizzf/), and during the discussion `@ruanviljoen` helpfully shared this super useful from `@curtismcshale` that addresses [how to evaluate which sync method you should use](https://www.youtube.com/watch?v=JHAhE8QNokw).
- `@Chetachi` will be giving the [customizable workspaces](https://discordapp.com/channels/686053708261228577/876257648624939008/877223790256468008) talk today, Aug 21, 2021 at 12:30 PM Central Time. The talk will be a showcase of the newest updates to [[cmenu-plugin|cMenu]] and [[Yin and Yang]], namely, the setting for custom commands with cMenu and the color changing settings with Yin & Yang. She'll explain how a user can customize their menu bar and theme for their own needs.
- `@shabegom` is going to be giving a talk on the Buttons plugin on August 28. If you would like to get involved in community talks, you can find more information on [this forum post](https://forum.obsidian.md/t/meta-community-talks/16686). You can request talks, vote on which one should be next, and also offer to give a talk.
- `@Nick_At_day` is trying to put together some folks for [mutual critique of Obsidian workflows](https://www.reddit.com/r/ObsidianMD/comments/p62hpw/mutual_critique_of_obsidian_workflows_writing/) as a sort of informal workshop environment.

## Plugin News

### New

_Remember, you can manually install any plugin by copying the `main.js`, `manifest.jso` and (optionally) the `styles.css` files into `{vault}/.obsidian/plugins/{plugin-folder}`. it can then be enabled like any other plugin (you may need to refresh the list first). usually these files can be found at the github repo under Releases_

- [[tag-page-preview|Tag Page Preview]] isn't published yet, but it was shared on [Reddit](https://www.reddit.com/r/ObsidianMD/comments/p4hrzw/how_to_create_a_popup_window_like_this_when_you/) and it's pretty cool. If you click on a tag, it'll open a little dialog box with pages that use that tag.
- This [[window-collapse|plugin]] lets you use commands to toggle the sidebars of obsidian.
- [[ObsidianAnkiSync|Obsidian Anki Sync]] uses a different and more powerful markup based syntax for making flash cards.
- [[luhman|Luhmann]] adds support for using 1a2b3c style folgezettels by letting users automatically create a new filename immediately "below" the current file, i.e. if you're on `1a2b3c` it will create `1a2b3c1` or the next available sibling name. Incidentally, `@Nick_At_Day` put together a [[templater-obsidian|templater]] script to [turn folgezettels into an easy-to-read outline format](https://discord.com/channels/686053708261228577/840286238928797736/878331775556939826).

### Updates

- [[obsidian-tracker|Tracker]] [v1.10](https://github.com/pyrochlore/obsidian-tracker) has a fancy new annotation mode for month view, different date format upgrades, and more.
- [[quickadd|QuickAdd]] [v0.4](https://discord.com/channels/686053708261228577/855181471643861002/877788312679624734) has a bunch of API improvements, advanced settings, and more.
- Unfortunately, FreeDictionaryAPI will be ending support for non-English languages soon. If you know any free APIs for non-English languages, please reach out to `Philbr0`, the developer of the [[obsidian-dictionary-plugin|Dictionary]] plugin. More details [on github](https://github.com/phibr0/obsidian-dictionary/issues/43).
- The [[emoji-shortcodes|Emoji Shortcodes]] has a dynamic Suggester now.

### Under The Radar

- The plugin that [[obsidian-auto-link-title|automatically fetches a page title when you link to it]] got resurfaced this week.
- The [[extract-highlights-plugin|Extract Highlights]] plugin lets you create and extract highlights from a current markdown note in Obsidian onto your clipboard.

### For Developers

- `@arvn` is interested in hiring (this is a paid gig!) experienced Obsidian plugin developers to [create some plugins](https://publish.obsidian.md/arun/Tech/Obsidian/New+Features+that+Would+Make+Obsidian+More+Voice+Accessible) to _make Obsidian more voice accessible_. You can find [more details in Discord](https://discord.com/channels/686053708261228577/840286264964022302/877647079466471444).

## Workflow Stuff

- `@bianca_oli_per` has a holistic [academic workflow](https://www.youtube.com/watch?v=fGJv6hiXPmk) up over on [[Linking Your Thinking]]. It covers MOCs, [[LaTeX]] equations, [[Obsidian queries]], PDF extraction and more.
- `@ASRenner1` shared how she uses Obsidian to provide a [minimalist but organized workspace](https://www.youtube.com/watch?v=OX_UKIzRALs) for her fiction and nonfiction writing process.
- Remember, you can search for any heading or paragraph in your vault without knowing the file: `[[##` for headings, `[[^^` for blocks.
- This [guide](https://publish.obsidian.md/arun/Tech/Obsidian/Using+Obsidian+with+Dragon+Dictation+-+Edit+Your+Notes+With+Full+Voice+Control) serves as a quick how-to for switching between editing notes in Obsidian and [[Dragon speech recognition|Dragon]]-friendly word processors with full text control and without reaching for the mouse or keyboard.

### Advanced

- `@Chetachi` shared how she uses tags to [highlight her Readwise highlights](http://discordapp.com/channels/686053708261228577/707816848615407697/877196058764144691) in [different colors as appropriate](https://discord.com/channels/686053708261228577/707816848615407697/877375585456898048).
- `@Christian` put together a writeup for how he uses [QuickAdd and Zotero to process pdfs with hotkeys](https://bagerbach.com/blog/how-i-read-research-papers-with-obsidian-and-zotero/). It's a little technical but it's a nice complement to the [zotfile -> mdnotes](https://forum.obsidian.md/t/zotero-zotfile-mdnotes-obsidian-dataview-workflow/15536) workflow from Cat. Incidentally, the [[Zutilo]] plugin for Zotero which allows you to assign hotkeys to [[Zotfile]] & [[Mdnotes]] commands.
- `@Christian` also shared a [Toggl Track macro](https://github.com/chhoumann/quickadd/blob/master/docs/Examples/Macro_TogglManager.md) that uses the new [[obsidian-toggl-integration|Toggl Track]] plugin. More details [in Discord](http://discordapp.com/channels/686053708261228577/707816848615407697/876069796553293835). `@Maximo` shared their usecase for how [Toggl](https://discord.com/channels/686053708261228577/700466324840775831/877639056828276746) helps them track how much time they spend on different projects. Note: the Toggl API got hinky so if you're using this plugin update to version 0.2.4 or it won't work.
- `@Christian` _also_ shared a [QuickAdd script](https://github.com/chhoumann/quickadd/blob/master/docs/Examples/Macro_MoveNotesWithATagToAFolder.md) to automatically move files with a certain tag into a particular folder. More details [in Discord](http://discordapp.com/channels/686053708261228577/716028884885307432/876494826122657852).
- This [bash script](https://forum.obsidian.md/t/clipboard-snippets-in-your-inbox-for-later-review-even-when-obsidian-closed/22850) from `@Moonbase` lets users use a hotkey to quick-copy text, HTML and images from the clipboard into a "Clipboard" note within your vault, without the need of opening Obsidian each time.

## Feature Requests

- `@Bibi53` is hoping somebody can help out with integrating the [Antidote spellchecker API](https://forum.obsidian.md/t/plugins-antidote/22653) into an Obsidian plugin.

## Appearance

- `@Chetachi` shared a snippet you can use to make the headers in [[Yin and Yang]] be a [long background highlight](http://discordapp.com/channels/686053708261228577/702656734631821413/877508873207050281) and like everything she does, it's beautiful.
- `@Mara` updated her github repository of [WYSIWYG snippets](https://github.com/Mara-Li/Obsidian-Snippet-collection).
- For those who prefer a more retro appearance for their vault, here's the [Win98 edition](https://github.com/SMUsamaShah/Obsidian-Win98-Edition) theme.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- this [guide](https://www.simonlindgren.com/notes/2019/11/15/setup-for-writing-in-markdown-citing-with-zotero-and-publishing-with-pandoc) explains the use of [[Pandoc]] for markdown with [[Zotero]] pretty well.
- `@Koechiliniana` shared a [ready-made Obsidian vault](https://github.com/Bartlebooth1424/obsidian-nomic) for the government-mimicing metagame [[Nomic]],

## Housekeeping

- I sat down to update and consolidate my various writeups about all the different pieces of my workflow and put them all in one place and instead wound up waxing philosophical about how notetaking really is like gardening for two thousand words instead, so oops but also if you're interested here's [my philosophy of gardening, digital and otherwise](https://eleanorkonik.com/the-konik-philosophy-of-gardening-digital-otherwise/).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-08-21%20Paid%20Dev%20Opportunities%20%26%20Time%20Tracking%20with%20Toggl.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-08-21%20Paid%20Dev%20Opportunities%20%26%20Time%20Tracking%20with%20Toggl.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
