---
link: https://www.obsidianroundup.org/2021-10-09/
author: Eleanor Konik
published: 2021-10-08T21:09:00
publish: true
---

# 2021-10-09: Style Guide Enforcement & Sitemap-style view
The Codemirror Options plugin added some new WYSIWYG functionality & you can mass-convert links between wiki-style and markdown Link Converter.

## In The Community

-   The folks at [Readwise](https://readwise.io/i/ac9) did an [interview with Nick at LYT](https://www.youtube.com/watch?v=n12iIZwL4S4) about their Obsidian plugin, which brings highlights from around the web into Obsidian. I personally learned stuff from it so I'm glad I watched.
-   I'm pretty sure this is the first [Obsidian fanfiction](http://discordapp.com/channels/686053708261228577/805952223124520961/893614070165540874) I've seen so far, and it's frankly delightful.
-   Here's a really heartwarming story about someone [doing their master's degree research in Obsidian](https://www.reddit.com/r/ObsidianMD/comments/q37y8u/practical_results_obsidian_helped_me_write_my/).

## Obsidian Updates

[Insider v0.12.17](https://forum.obsidian.md/t/obsidian-release-v0-12-17-insider-build/25270) comes with:

-   a big upgrade to the theme store.
-   a new `/slash commands` core plugin that lets you use the `/` key to trigger any command.
-   a bunch of bugfixes
-   a _bunch_ of new stuff for developers, if you do anything with plugins or themes _please_ click thru to the release notes.

## Plugin News

### New

-   The [Map of Content](https://github.com/Robin-Haupt-1/Obsidian-Map-of-Content) plugin offers another way to visualize connections in your vault. It creates an outline of your vault based on your link structure and a home note that you specify. It's like Breadcrumbs and [Journey](https://publish.obsidian.md/alexisrondeau/Obsidian+Journey+Plugin) had a baby that grew up to be a sitemap.
-   The [Vale plugin](https://github.com/marcusolsson/obsidian-vale) brings a highly customizable (also free and open source!)tool for automated style guide enforcement to Obsidian.
-   [Link converter](https://github.com/ozntel/obsidian-link-converter) scans all your links in the vault and convert them to WikiLinks or Markdown format.
-   [Obsidian 42: Beta Reviewers Auto-update Tester](https://github.com/TfTHacker/obsidian42-brat) ("BRAT") makes it easier to update plugins that aren't in the plugin store.
-   [Paste that Shizz](https://github.com/shabegom/paste-that-shizz) lets you add "paste" to your mobile toolbar, which should help iOS users most.
-   There's [Another Quick Switcher Plugin](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher) option available.
-   [Obsidian Enlightenment](https://github.com/ryanjamurphy/enlightenment-obsidian) is another focus-mode option.
-   [Cyptsidian](https://github.com/triumphantomato/cryptsidian/) will encrypt your Obsidian files with a password but _warning this can also result in data corruption, make sure you know what you're doing before you use this._
-   [Obsidian vocabulary view](https://github.com/nnshi-s/obsidian-vocabulary-view-plugin) is meant to help users review vocabulary flashcard style.
-   The [truth table plugin](https://github.com/insertish/obsidian-truth-table-plugin) should be useful for people working with low-level computer math.
-   [SimpRead Unreader Sync](https://github.com/Kenshin/simpread-obsidian) exists now, for SimpRead users (which seems to be a browser extension for a clean online reading experience).

### Updates

-   [CodeMirror Options v0.2.1](https://github.com/nothingislost/obsidian-codemirror-options/releases/tag/0.2.1) has a bunch of new WYSIWYG functionality. **If you're waiting for WYSIWYG mode, check this out.**
-   [Templater](https://github.com/SilentVoid13/Templater) now has per-folder templating. This used to be possible with a combination of Vinzent's Hotkeys for Templates plugin combined with Templater, but now works natively in Templater.
-   [Initiative Tracker](https://github.com/valentine195/obsidian-initiative-tracker) now displays encounter difficulty if players have levels.
-   [Block Reference Counts 0.2.0](https://github.com/shabegom/obsidian-reference-count) moved indexing to a Web Worker and should therefore run much more smoothly.
-   [Dice Roller](https://github.com/valentine195/obsidian-dice-roller) now has lookup tables. They even support recursion & nesting.

### Betas

-   Here's a plugin to build [simple monster stat blocks](https://github.com/g-bauer/obsidian-quick-monsters) in your notes for D&D 5e.

### For Developers

-   `@Licat` gave a good explanation of [why not to statically reference a view](https://github.com/obsidianmd/obsidian-releases/pull/504) and some other plugin best practices.

## Feature Requests

-   There was a request for a plugin that adds [PGF/TikZ](https://forum.obsidian.md/t/tikz-support/9601) support for vector graphics.
-   `@Namworld` mentioned that it would be awesome for screenwriters if there was [a plugin to add interoperability with Highland 2](http://discordapp.com/channels/686053708261228577/805952223124520961/894587104846315600). It should theoretically be do-able because they both work off of local markdown files, they just use different syntax for comments.

## Appearance

-   [Minimal](https://github.com/kepano/obsidian-minimal) had a major update, along with the Minmal Theme Settings plugin, to make it feel more native on iOS/macOS.
-   [Creature](https://github.com/marcusolsson/obsidian-creature-theme) is a new minimal dark theme.
-   Here's an article about [UX practices for Markdown editors](https://css-tricks.com/considerations-for-using-markdown-writing-apps-on-static-sites/) for theme designers to consider.
-   This [css code from Discord](https://discord.com/channels/686053708261228577/702656734631821413/789297866769825883) allows for picture-in-picture for a specific note.

## Guides

-   Here's a really cool interactive [Zettelkasten guide](https://binnyva.com/zettelkasten/)
-   `@curtismchale` published a [beginner's course on Obsidian](https://www.skillshare.com/site/join?teacherRef=685311&via=teacher-referral&t=Getting-Started-with-Obsidian&sku=704822481) on Skillshare.
-   Here's a [vim cheat sheet](https://rumorscity.com/wp-content/uploads/2014/08/10-Best-VIM-Cheat-Sheet-02.jpg).
-   `@Usara` shared their  [Life-Disciples-Projects](https://github.com/uwidev/life-disciplines-projects) framework for productivity.
-   Here's a detailed walkthrough about how `@nvanderhoeven` uses [Obsidian for D&D](https://nicolevanderhoeven.com/blog/20210930-non-lazy-dms-use-obsidian-for-dnd/).

## Discussions

-   Here's a [nice entry point for using Obsidian as an undergrad](https://discord.com/channels/686053708261228577/722584061087842365/895123275611525160). Here's a useful [discussion on Reddit](https://www.reddit.com/r/ObsidianMD/comments/q25z8e/how_to_use_obsidian_for_university_whats_the_best/) about the same topic.

## Ancillary Tools

-   [Apparently, Pandoc got an update](http://discordapp.com/channels/686053708261228577/710585052769157141/894661122286821466) that makes its markdown-slide-syntax compatible with Obsidian's.

## Housekeeping

-   I'm working on migrating to Ghost Pro managed hosting (the headaches are just not worth the handful of dollars I'm saving at this point) so if things are slightly weird for the next week, I'm sorry and also, please let me know.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-10-09%20%20Style%20Guide%20Enforcement%20%26%20Sitemap-style%20view.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-10-09%20%20Style%20Guide%20Enforcement%20%26%20Sitemap-style%20view.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
