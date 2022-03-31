---
link: https://www.obsidianroundup.org/2022-02-26/
author: Eleanor Konik
published: 2022-02-26T13:30:00
publish: true
---

# 2022-02-26: Documentation efforts, Mobile Live Preview, & Improved Startup Time
Ganessh Kumar built a mindblowly good way to navigate plugins, so hopefully developers will take advantage of the features it offers and write good release notes ;) 

-   I wrote a (really long, I'm sorry) ... article? manifesto? about [how I view my work in this community](https://www.obsidianroundup.org/community-role/), why I'm not enthusiastic about creating courseware and guides, and some behind the scenes things I try to do. You can help by telling me what you need, what you want, and what kinds of opportunities you're available for.
-   This week's survey is about the [dataview docs](https://cryptpad.fr/form/#/2/form/view/H-nrhw0AKZBxCF0G73UxMJBQU-VgmS7QlNigWJv-qig/); if you've ever used Dataview, please consider filling this out so the folks helping out with documentation can best direct their efforts.
-   If you've got some time and would like to help out our developers put together more accessible READMEs and documentation, please check out the [plugins seeking documentation help](https://publish.obsidian.md/hub/01+-+Community/Contributing+to+the+Community/Volunteer+Plugin+Doc+Writers) page. You don't need to be any kind of expert for this, but it has the potential to help a lot of people and is a great way to get involved in the community.

## Obsidian Updates

Obsidian Mobile v1.1.0 is now available for public access! This includes all new functionality and bug fixes up to Obsidian Desktop v0.13.24, which means **Live Preview works on mobile now**. So does vim, but only do that if you have a keyboard attached to your device.

If you run into any problems trying to edit things like code blocks, you can get back into source mode by long-holding the 3 dot button on the top right and hitting "Toggle Live Preview/Source mode" (or run a command from the pull down menu or bottom toolbar).

## Plugin News

### New in Community Plugins

💎

Not all new plugins are available in the community list yet, as they need to go through code review first. This [plugin stats page](https://obsidian-plugin-stats.vercel.app/) by Ganessh Kumar is incredible; if you want a quick list of which plugins were recently made available in the community plugins list, click through. Note that it also lets you find _similar_ plugins.

-   [Sekund](https://www.sekund.io/) is a [social network that lets users share notes and collaborate with others](https://forum.obsidian.md/t/i-created-a-social-network-on-top-of-obsidian/31784/6) using Obsidian. Here are [directions for how to use it](https://github.com/Sekund/sekund-plugin-react), but I'm most impressed by the commenting features.
-   [Hotkeys Chords](https://github.com/trenta3/obsidian-hotkeys-chords) by `@trenta3` lets users tie Emacs-like keybinding sequences such as `C-x C-s` to any available Obsidian command. "Hotkey chords" are basically a sequence of hotkeys.
-   [Living Graph](https://github.com/geoffreysflaminglasersword/obsidian-living-graph) by `@geoffreysflaminglasersword` animates the graph so it does a fun little dance.
-   [Digital Garden](https://github.com/oleeskild/obsidian-digital-garden) by `@oleeskild` is one of the easiest free ways to publish your notes to a digital garden that I've seen.

**You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review.**

### Updates

💎

I'm not going to cover every single update to every single plugin that happened this week, because thanks to the [plugin stats](https://obsidian-plugin-stats.vercel.app/) page I know there were sixty-two (!). Here are some highlights:

-   [Better Word Count](https://github.com/lukeleppan/better-word-count) got fixed! Yay! Only update if you use Live Preview mode, though, the dev is still working on adding support for the legacy editor. Please read the Readme for an explanation; it had to be entirely rewritten.
-   [Snippet Manager](https://github.com/Mara-Li/Obsidian-Snippet-Manager/releases) v2.3.1 lets users download and update a particular snippet.
-   [Divide & Conquer](https://github.com/chrisgrieser/obsidian-divide-and-conquer) now has support for bulk disabling of CSS snippets to help with troubleshooting.
-   [Various Complements v5.6.0](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/5.6.0) suggests and completes the text with front matter properties only when the cursor is in the front matter.
-   [File Tree Alternative](https://github.com/ozntel/file-tree-alternative) now supports Folder Note functionality, with or without the Folder Note plugin.
-   [Tabout](https://github.com/phibr0/obsidian-tabout/) now works in live preview. It lets users hit "tab" to move the cursor outside of markdown formatting.
-   [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.6.14) 1.6.13 brings improved handling of saving & sync. You can also compress Excalidraw JSON to keep it from cluttering search results. v1.6.14 lets users search for text elements.
-   [Initiative Tracker v7.2.0](https://github.com/valentine195/obsidian-initiative-tracker/releases/tag/7.2.0) has support for multiple parties, custom status effects, and auto updates for player stats.
-   As of 2.0.9, [Image in Editor](https://github.com/ozntel/oz-image-in-editor-obsidian/releases/tag/2.0.9) works on mobile.
-   The [Rest API](https://github.com/coddingtonbear/obsidian-local-rest-api/) plugin added new `/search/` endpoints.
-   [Tweet to Markdown](https://github.com/kbravh/obsidian-tweet-to-markdown/releases/tag/2.1.0) added toggles to customize tweet downloads: date, frontmatter, etc
-   [Orthography](https://github.com/denisoed/obsidian-orthography/releases), a spellchecker plugin, added support for Grammarly.

### Betas

💎

Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes.

-   v0.2.0 of [Full Calendar](https://github.com/davish/obsidian-full-calendar/releases/tag/0.2.0) now has read-only views of Google Calendar, and multiple calendar colors with configurable colors.
-   [Graphvidian](https://github.com/ooker777/graphvidian) is an Obsidian plugin to generate hierarchical graphs, with the nodes are from your Obsidian vault. It works by converting a breadcrumbs database into a format Graphvis can use. Here's the [overview and proposal](https://forum.obsidian.md/t/graphviz-and-hierarchical-graph-layout-a-review-and-plugin-proposal/) about the problems it solves. I **really** need to get off my butt and set up a proper Breadcrumbs hierarchy for my notes so I can use this.
-   [Quick Jump](https://github.com/tadashi-aikawa/obsidian-quick-jump-plugin) is a port of the Jump to Link plugin that works in Live Preview.

### For Developers

-   The [Spaced Repetition Plugin](https://github.com/st3v3nmw/obsidian-spaced-repetition) has a ton of users and a bunch of open issues looking for feature enhancements. It also has many contributors, so if you were looking for a project where you can help out but not have to take over maintenance of a whole codebase yourself, this seems like a good candidate. The developer is particularly looking for translation help.
-   The Hub now features an automatically generated list of [relatively straightforward problems](https://publish.obsidian.md/hub/01+-+Community/Contributing+to+the+Community/Plugins+seeking+help) developers in the community are looking for help with, thanks to `@joethei`. Here's one for [styling checkboxes in the editor view for the Tasks plugin](https://github.com/schemar/obsidian-tasks/issues/2), and another for [how to fix emojis messing up table alignments](https://github.com/tgrosinger/advanced-tables-obsidian/issues/44).

## Feature Requests

-   I was actually surprised to realize this wasn't in core, but it would be nice if you could ["make a copy" of a folder](https://forum.obsidian.md/t/duplicate-folder-from-inside-obsidian/29370) and all its contents the same way you can a file, without having to navigate into your filesystem.
-   Here is a really neat idea to allow [exporting your entire vault into book format](https://forum.obsidian.md/t/export-entire-vault-as-a-book/32845). Bonus points if it can algorithmically decide which notes should be batched together.
-   Here's a really neat idea about [scoped vaults](https://forum.obsidian.md/t/nested-vault-vault-scoping-plugin/23791) to build out the functionality of nested vaults in a more robust, useful way.
-   It would be nice if we could [sort plugins by enabled status](https://forum.obsidian.md/t/sorting-plugins/27315/2) (among other sorting mechanisms).
-   Imagine the performance improvements that could come from being able to [toggle plugins on with a hotkey](https://forum.obsidian.md/t/command-hotkey-to-toggle-plugins/32272), only when you need them.
-   Some folks would like to [access Obsidian trash from within the app](https://forum.obsidian.md/t/access-obsidian-trash-from-within-the-app/2227).

## Appearance

If you're on the Insider build you should probably update your themes; several were tweaked to accommodate a new change.

-   [Obsidian You](https://github.com/selfire1/obsidian-you-theme/releases/tag/1.0.0) got a big redesign to comply with Google's Material Design standards and now supports live preview. Android users should definitely check it out.
-   [Minimal 5.1.6](https://github.com/kepano/obsidian-minimal/releases/tag/5.1.6) added some support for the Tracker plugin, the ability to add outlines to images, and got some bugfixes and other small improvements.
-   [Willemstad X v0.1.3](https://github.com/tingmelvin/willemstad-x) got a bunch of really incredible table support for Live Preview. Admonitions look the same in Live Preview and Reading modes.
-   The [Dataview cards](https://github.com/SlRvb/Obsidian--ITS-Theme/blob/main/S%20-%20Dataview%20Cards.css) from the "Notion Inspired Color Scheme" from the ITS theme are available as a snippet.

## Guides

-   Here's a guide for [how to use the BRAT plugin to auto-update your themes](https://tfthacker.medium.com/have-more-fun-with-obsidian-themes-557a1ae40a18), switch active themes without digging through your settings, and more!
-   Here's a really interesting demonstration of how to use the [kanban plugin to do course outlining](https://discord.com/channels/686053708261228577/722584061087842365/944512414534221844).
-   Here's a [detailed guide for how to improve startup time](https://tfthacker.medium.com/improve-obsidian-startup-time-on-older-devices-with-the-faststart-script-70a6c590309f) by keeping non-critical plugins from loading immediately and blocking launch. I would honestly love this to be a plugin that lets us toggle which plugins we want to load at startup or delayed start in the settings page.
-   Here's a nice guide about using Obsidian to do a [weekly review](https://www.mishacreatrix.com/weekly-review-obsidian).

## Discussions

-   Here's a thought-provoking Discord discussion about [the relationship between personal knowledge management and fear of death](https://discord.com/channels/686053708261228577/710585052769157141/944440669072683099).
-   Bianca Pereira and Nick Milo did an event on Twitter Spaces about [using PKM for research: PKM mindsets](https://twitter.com/bianca_oli_per/status/1497278843987513347?t=c1F5M3FkIPnZCb0eIa-DMQ) yesterday; there's a recording and it's transcribed. **I'll be joining Bianca next week on Sunday, March 6 at 11:00 AM EST to discuss stuff like [why it's hard to take notes on timelines](https://twitter.com/i/spaces/1yoKMWDaaqOJQ).**
-   Here's one about [taking notes in multiple languages](https://discord.com/channels/686053708261228577/710585052769157141/946307299213996052).
-   Here's [a neat way](https://discord.com/channels/686053708261228577/744933215063638183/944749164808503326) to [apply custom styling to metadata](https://discord.com/channels/686053708261228577/744933215063638183/944728985881964574) that was shared in Discord.

## Knowledge Management

-   Here's an article about [the value of linked data](https://codyburleson.com/blog/awesome-power-of-the-link-in-linked-data).
-   Here's [how to apply information architecture concepts to personal knowledge management](https://medium.com/@cody.burleson/ia-for-pkm-crows-camels-concepts-and-the-cognitive-divide-7523c0bfa5eb)

## Ancillary Tools

-   the MarkDownload browser extension added support for MathJax to LaTeX, some extra keyboard shortcuts, downloading images as Base64 embedded urls (!), and more. The [full release notes](https://github.com/deathau/markdownload/releases/tag/3.1.0) are worth a read.
-   [iDoRecall](https://www.idorecall.com/) is a nifty freemium Anki alternative for creating spaced repetition flashcards. It's designed to be a bit more social, more tightly integrated into the learning materials (they have a browser extension for highlighting), and is meant to be easier to use than Anki. They're interested in developing an Obsidian plugin, and when I mentioned I planned to include it in the Roundup, they created a 20% off coupon code that'll be good until March: `ObsidianCommunity20`
-   [Elicit](https://elicit.org/) is the best implementation of machine learning + natural language search of academic databases I've ever personally seen and as far as I can tell it's free. One of the developers happens to be an Obsidian user, and is [active in Discord](https://discord.com/channels/686053708261228577/722584061087842365/946480247153496124).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-02-26%20Documentation%20efforts%2C%20Mobile%20Live%20Preview%2C%20%26%20Improved%20Startup%20Time.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-02-26%20Documentation%20efforts%2C%20Mobile%20Live%20Preview%2C%20%26%20Improved%20Startup%20Time.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
