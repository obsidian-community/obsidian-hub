---
link: https://www.eleanorkonik.com/2023-03-04/
author: Eleanor Konik
published: 2023-03-04T20:56:44
publish: true
---

# 2023-03-04: New APIs, + Curated Lists for Vim Users & Interoperability Fans
Digital Decluttering, GitHub Auto Scans, Obsidian on e-ink devices, & a handy autohotkey script for folks who want to control youtube in the background.

## In The Community

* Nick Milo proposed [Sensemaking Sundays](https://twitter.com/NickMilo/status/1631681072353394688?ref=eleanorkonik.com) on Twitter. Since this is when I usually write my other newsletters, I might join in 👀

## Obsidian Updates

* [Obsidian v1.1.16](https://forum.obsidian.md/t/obsidian-release-v1-1-16/55572?ref=eleanorkonik.com) & [mobile 1.4.3-95](https://forum.obsidian.md/t/obsidian-mobile-v1-4-3-build-95/55574?ref=eleanorkonik.com) fixed some bugs, mostly related to Canvas.

## Plugin News

### New in Community Plugins

__These plugins went through code review and are now available in Obsidian's plugin list.__ For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new?ref=eleanorkonik.com).

* [MSG Handler](https://github.com/ozntel/obsidian-msg-handler?ref=eleanorkonik.com) by `@ozntel` makes it easier to display and search files from Outlook in your Obsidian Vault
* [Marp](https://github.com/JichouP/obsidian-marp-plugin?ref=eleanorkonik.com) by `@JichouP` makes it possible to integrate the Markdown Presentation Ecosystem for making beautiful slide decks.
* [Heading Level Indent](https://github.com/svonjoi/obsidian-heading-level-indent?ref=eleanorkonik.com) by `@svonjoi` makes it easier to indent content under headers based on their level
* [Open files with commands](https://github.com/LostPaul/ob-open-files-with-commands?ref=eleanorkonik.com) by `@LostPaul` makes it easier to create commands that only open one file at the time. It can be used with the commander plugin.
* [LaTeX Algorithms](https://github.com/SamZhang02/obsidian-latex-algorithms?ref=eleanorkonik.com) by `@SamZhang02` facilitates writing algorithm blocks in LaTeX
* [Awesome Reader](https://github.com/AwesomeDog/obsidian-awesome-reader?ref=eleanorkonik.com) by `@AwesomeDog` syncs reading process for epubs and pdfs as well as create book notes based on a table of contents.
* [O2](https://github.com/songkg7/o2?ref=eleanorkonik.com) by `@songkg7` makes obsidian markdown syntax compatible with Jekyll syntax.
* [No Empty Windows](https://github.com/popscallion/obsidian-no-empty-windows?ref=eleanorkonik.com) by `@popscallion` closes Obsidian window with cmd+W on Mac when the last tab is closed.
* [Create Note in Folder](https://github.com/Lisandra-dev/obsidian-create-note-in-folder?ref=eleanorkonik.com) by `@Lisandra-dev` adds command to create a note in a specific folder.
* [Apple Books Highlights](https://github.com/atfzl/obsidian-apple-books-plugin?ref=eleanorkonik.com) by `@atfzl` syncs your Apple Books highlights automatically.
* [Mixa](https://github.com/mixasite/obsidian-mixa?ref=eleanorkonik.com) by `@mixasite` makes it easier to publish your notes and blog posts with Mixa directly from Obsidian
* [Material Symbols](https://github.com/cberane/obsidian-material-symbols?ref=eleanorkonik.com) by `@cberane` adds the material symbols (outlined) to obsidian

### Pending (as of Friday morning)

__Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat?ref=eleanorkonik.com). Note, though, that this is not as safe as waiting for them to go through code review.__

* [Home tab](https://github.com/olrenso/obsidian-home-tab?ref=eleanorkonik.com) by `@olrenso` is a browser-like search tab for your local files.
* [Callout Manager](https://github.com/eth-p/obsidian-callout-manager?ref=eleanorkonik.com) by `@eth-p` makes creating and configuring callouts easy.
* [Global Search and Replace](https://github.com/MahmoudFawzyKhalil/obsidian-global-search-and-replace?ref=eleanorkonik.com) by `@MahmoudFawzyKhalil` lets users search and replace in all vault files
* [File Publisher](https://github.com/yiglas/obsidian-file-publisher?ref=eleanorkonik.com) by `@yiglas` publishes a file to a given api.
* [Emoji Titler](https://github.com/HyeonseoNam/obsidian-emoji-titler?ref=eleanorkonik.com) by `@HyeonseoNam` makes it easier to insert an emoji in the title using a keyboard shortcut.

### Updates

__If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates?ref=eleanorkonik.com) by Ganessh Kumar.__

* The [QuickAdd](https://github.com/chhoumann/quickadd/releases?ref=eleanorkonik.com) API is now public, you can duplicate choices, there's improved format syntax, new specification abilities, and a bunch of bugfixes.
* [Version history diff](https://github.com/kometenstaub/obsidian-version-history-diff?ref=eleanorkonik.com) now has better support for the Git diff command (you may need to update Obsidian Git).
* [Group Snippets](https://github.com/Lisandra-dev/obsidian-group-snippets?ref=eleanorkonik.com) now allows users to edit groups in a modal.
* [Plugin Groups 2.0](https://github.com/Mocca101/obsidian-plugin-groups/releases/tag/2.0.0?ref=eleanorkonik.com) will now let you define plugin loading order, along with improved managing.
* [Github Publisher](https://github.com/ObsidianPublisher/obsidian-github-publisher?ref=eleanorkonik.com) got a cleaner UI and a series of other improvements.
* [Obsidian GPT](https://github.com/jmilldotdev/obsidian-gpt?ref=eleanorkonik.com) v1.1.1 now supports the ChatGPT API, including the code-davinci-002 model.
* [Text Generator Plugin](https://github.com/nhaouari/obsidian-textgenerator-plugin/releases?ref=eleanorkonik.com) has auto suggest functionality, title generation, and more.
* [Various Complements 8.0.0](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/8.0.0?ref=eleanorkonik.com) now has fuzzy match and improved conflict avoidance.

### For Developers

* GitHub released free [Secret Scanning](https://github.blog/2023-02-28-secret-scanning-alerts-are-now-available-and-free-for-all-public-repositories/?ref=eleanorkonik.com) for all repos, which you can/should enable to scan your repo (and repo history) for accidentally leaked API keys or Access Tokens. ([h/t Chris Grieser](https://twitter.com/pseudo_meta/status/1631036193113505792?ref=eleanorkonik.com))
* The [Obsidian Tasks Contributing Guide](https://publish.obsidian.md/tasks-contributing/?ref=eleanorkonik.com) is now hosted on Obsidian Publish!

## Appearance

* [Tokyo Night](https://github.com/tcmmichaelb139/obsidian-tokyonight?ref=eleanorkonik.com) by `@tcmmichaelb139` is designed to match the VSCode and Neovim themes of the same name.
* [Obsidianotion](https://github.com/diegoeis/obsidianotion?ref=eleanorkonik.com) by `@diegoeis` is designed to make Obsidian feel more like Notion.
* [Cyber Glow](https://github.com/ArtexJay/Obsidian-CyberGlow/releases/tag/v7.8.8?ref=eleanorkonik.com) got a series of fixes, including contrast control and better buttons.
* [Aura](https://github.com/ashwinjadhav818/obsidian-aura?ref=eleanorkonik.com) now supports Light Mode!
* [Prism 3.2.1](https://github.com/damiankorcz/Prism-Theme/releases/tag/3.2.1?ref=eleanorkonik.com) improved Style Settings info, has improved support for customizations, the mark highlight system, and a bunch of other improvements.
* [Origami](https://github.com/7368697661/Origami?ref=eleanorkonik.com) has a bunch of new color schemes.
* Here's how to get a [wikipedia style custom style preview](https://github.com/zamsyt/obsidian-snippets/wiki/Custom%20page%20preview?ref=eleanorkonik.com), which looks [like this](https://media.discordapp.net/attachments/702656734631821413/1060325551413411840/image.png?ref=eleanorkonik.com).

## Discussions

* [Dan Allosso](https://twitter.com/AllossoDan?ref=eleanorkonik.com) will be hosting the next Obsidian Book Club on __Myth America: Historians Take On the Biggest Legends and Lies About Our Past__, by Kevin M. Kruse and Julian E. Zelizer. It is a recently-published volume of twenty essays by different historians on issues they think are misunderstood or misrepresented, especially in popular culture and contemporary politics. The Book Club meets on Saturdays for four weeks. Reach out to him if you're interested in joining.

## Food For Thought

* Here's a great review of [how Obsidian performs of the Onyx Boox](https://thesweetsetup.com/a-mindfulness-monday-review-of-the-onyx-boox-tab-ultra/?ref=eleanorkonik.com) e-ink tablet.
* Here's [how and why to use Obsidian for creating simple mobile notes](https://www.forbes.com/sites/tjmccue/2023/02/28/why-and-how-i-use-obsidian-for-creating-simple-mobile-notes/?sh=3be58fb46b0c&ref=eleanorkonik.com) via Forbes.
* Here's an interesting [guide to digital decluttering](https://www.reddit.com/r/digitalminimalism/wiki/declutter-guide/?ref=eleanorkonik.com).
* Here's a neat way to [use the statblock plugin for medical school](https://discord.com/channels/686053708261228577/744933215063638183/1079381102180970648?ref=eleanorkonik.com) (via Discord).
* Here's a [list of Obsidian plugins for vim users](https://nanotipsforvim.prose.sh/obsidian-plugins-for-vim-users?ref=eleanorkonik.com), and a nice compilation of [apps that work well with Obsidian](https://www.reddit.com/r/ObsidianMD/comments/11eeoi0/obsidian_integrations_apps_that_work_with_obsidian/?ref=eleanorkonik.com).
* Here's a nice [curated list of Obsidian and knowledge-management articles on Medium](https://medium.com/@icycold/list/pkm-975f29b6d043?ref=eleanorkonik.com), via Rick Elliot.

## Ancillary Tools

* Here's an [autohotkey script for controlling youtube media without losing focus on Obsidian](https://www.reddit.com/r/ObsidianMD/comments/11e3jpx/autohotkey_script_for_controlling_youtube_media/?ref=eleanorkonik.com).

## Housekeeping

* While getting ready to do my taxes (groan), I trawled through my purchase history & wrote up [a list of the stuff I'm glad I bought](https://www.eleanorkonik.com/some-stuff-im-surprisingly-happy-i-bought/). None of these are affiliate links, I just thought I'd share which pens, notebooks, blankets, cooking supplies, etc really felt worth it.
* [Financial supporters](https://www.eleanorkonik.com/#/portal) of this newsletter are now [able to view](https://eleanorkonik.com/thanks?ref=eleanorkonik.com) the zip file of my [newly updated notes, featuring a condensed folder structure](https://publish.obsidian.md/eleanorkonik/?ref=eleanorkonik.com), the Discord server where I mess around with [image generating AI bots](https://www.midjourney.com/?ref=eleanorkonik.com), and record quick notes-to-self while out and about, as well as commentary on [links I share](https://rw-discord-bot-production.herokuapp.com/guilds/links/954068589885923389?ref=eleanorkonik.com). It's a relatively small community, but a decent insight into my process and a nice way to chat with like-minded folks. The [Thanks page](https://www.eleanorkonik.com/thanks/) also now features a new PDF compilation of my (very) short stories. Thank you to everyone who helps me afford to maintain this newsletter! Tax season is definitely a stark reminder of how much it helps :)

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2023-03-04%20New%20APIs%2C%20%2B%20Curated%20Lists%20for%20Vim%20Users%20%26%20Interoperability%20Fans.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2023-03-04%20New%20APIs%2C%20%2B%20Curated%20Lists%20for%20Vim%20Users%20%26%20Interoperability%20Fans.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
