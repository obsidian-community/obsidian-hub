---
link: https://www.obsidianroundup.org/2021-11-05-graph-analysis-podcast-notes-8-more-themes/
author: Eleanor Konik
published: 2021-11-06T12:11:00
publish: true
---

# 2021-11-05: Graph Analysis, Podcast Notes, & 8 More (!) Themes
The initial load-in on mobile got some improvements. There's new courseware, and lots of new integration opportunities with Alfred.

## In The Community

-   There's an important discussion on the forum about [implementing a standard date format among plugins](https://forum.obsidian.md/t/task-management-devs-add-date-format-standard/26464). Please consider adding your input!
-   If you'd like to [help out with the community vault](https://publish.obsidian.md/hub/CONTRIBUTING), here are some [open issues](https://github.com/obsidian-community/obsidian-hub/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) that are meant to be pretty straightforward way to get started with github collaboration.

## Obsidian Updates

-   Insider v1.0.5 (build 29) for mobile comes with a bunch of loading screen improvements.

## Plugin News

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

### New

-   There's a new plugin that [displays note titles that are different from file names](https://github.com/Shinigami072/file-explorer-note-title) (based on YAML `title:` field). It also replaces the titles in the graph view with the note's title.
-   [Graph Analysis](https://github.com/SkepticMystic/graph-analysis) lets users use cool graph algorithms to find useful relations between notes in your vault.
-   [Card Board](https://github.com/roovo/obsidian-card-board) is a neat alternative to kanban.
-   Snipd released their first Obsidian integration to [export podcast highlights/notes from the Snipd podcast player to Obsidian](https://blog.snipd.com/how-to-export-your-podcast-highlights-to-obsidian-54208c06d491).
-   There now's a [metadata extractor obsidian plugin](https://github.com/kometenstaub/metadata-extractor) that lets users write Obsidian vault metadata (only accessible via plugin) onto the hard drive. This enables 3rd-party apps (for example Alfred or Ulauncher) to access Obsidian metadata they normally wouldn't be able to access. You can use it with `@pseudometa`'s [workflow documentation](https://github.com/chrisgrieser/shimmering-obsidian#feature-overview) — the Alfred workflow literally got a dozen new features, most of which enabled by this new metadata extractor.
-   You can now gamify your projects in Obsidian using the [success plan](https://github.com/joshwingreene/obsidian-success-plan) plugin.
-   With [Obsidian auto class](https://github.com/OfficerHalf/obsidian-auto-class), users can automatically apply CSS classes to the markdown preview view to have different snippets applied to different paths in a single vault without having to add any HTML or CSS classes.
-   You can now [Reveal Active File](https://github.com/claremacrae/obsidian-manually-reveal-active-file) with the click of a button.
-   There's a new plugin to add [strict note types](https://github.com/konodyuk/obsidian-typing) that automatically adds a lot of the repetitive content. It also supports different "fast actions" depending on what kind of note you're in.
-   [Language Translator](https://github.com/twentytwokhz/language-translator) is based on Azure Translator and can translate text between languages.

### Updates

-   [CodeMirror Options 0.7.0](https://github.com/nothingislost/obsidian-codemirror-options) supports showing backlinks in the edit mode footer, rendering Tasks plugin tasks in the edit mode, and a bunch of code block rendering improvements. v0.8.x supports rendering embeds in edit mode. This includes the ability to render block embeds, inline, as if they were part of the normal document flow.
-   [Another Quick Switcher v1.3.0](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/1.3.0) supports searching by tags when you input queries start with `#`. v1.2.0 can move a file to another folder without using the file explorer plugin.
-   [BRAT 0.5.4](https://github.com/TfTHacker/obsidian42-brat) has a ribbon button, lets users update themes via the command palette, and switch themes via the command palette. 5.0 introduced disable/enable plugins through command palette.
-   [Word Sprint 0.2.0](https://github.com/kinabalu/obsidian-word-sprint) includes integration with National Novel Writing Month, a pomodoro-style timer, goals, nudges, stats, and more.
-   [Excalidraw 1.4.3](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.4.3) has LaTeX support.
-   [Obsidian Git](https://github.com/denolehov/obsidian-git/releases/tag/1.14.0) has UI support for staging and committing individual files.
-   [Tasks v1.4.0](https://github.com/obsidian-tasks-group/obsidian-tasks/releases/tag/1.4.0) has new sorting options, reminder plugin integration support, expanded documentation, priorities, scheduled and start dates, recurring tasks, and more.
-   [Advanced Cursors](https://github.com/SkepticMystic/advanced-cursors) can now insert an incrementing value at each of your multiple cursors.

### Betas

-   You can now hotkey underlines for bold & italics, as well as html tags like `<cite>` and `<aside>` using the [extra markdown & html syntax](https://github.com/chrisgrieser/obsidian-extra-md-html-syntax) plugin.
-   [Cardboard (0.2.0-beta)](https://github.com/roovo/obsidian-card-board) allows for custom styling of tags.

### For Developers

-   When working with the inspector, you can do `Cmd/Ctrl-Shift-P` and type focused then select Emulate a focused page, and clicking `dev tools` will no longer affect the actual page. More information [here](http://discordapp.com/channels/686053708261228577/702656734631821413/905598865141563433).

## Appearance

-   Here's a new [icon for Obsidian](https://gnelson.gumroad.com/l/obsidian2) meant for macOS and iOS.
-   There's a way to get [admonition blocks on custom publish domains](https://discord.com/channels/686053708261228577/768134314864017429/900775733188759603). Here's [an example](https://notes.gnotract.com/80+📓+Literature+Notes/87+🗄️+Filed/vesoulis2021jperinatol). Caveat: markdown is not rendered.

### Theme updates

-   [Sanctum](https://github.com/jdanielmourao/obsidian-sanctum/releases/tag/v0.3.0) got some bug fixes and QoL improvements, along with support for the word sprint plugin & fantasy map calendar. There's also a new style setting so you can change the size of modals. There's also a high contrast mode for accessibility.
-   [Golden Coffee](https://github.com/kinmury/GoldenCoffeeTheme) got a major revamp.

### New Themes

-   [Terminal](https://github.com/zcysxy/Obsidian-Terminal-Theme) is a _very_ minimalist theme with a very ASCII aesthetic.
-   [Typomagical](https://github.com/hungsu/typomagical-obsidian) is very fancy and features small caps instead of underlines for links.
-   [Primary](https://github.com/ceciliamay/obsidianmd-theme-primary) is very warm and functional. Gruvbox users should probably check it out.
-   [Wyrd](https://github.com/curio-heart/obsidian-wyrd) is a purple-hued, low-contrast, dual-mode theme with very bright colors.
-   [Things](https://github.com/colineckert/obsidian-things) is intended to look and feel native on iOS. It's already been [updated once](https://twitter.com/colineckert/status/1456693780841578496?t=PDpHo0u6FGRnEfdaiqY3lg).
-   [Turquoise](https://github.com/gracejoseph1236/obsidian-turquoise), [Limestone](https://github.com/gracejoseph1236/obsidian-limestone) & [Sapphire](https://github.com/gracejoseph1236/obsidian-sapphire).
-   [Bubble Space](https://github.com/Emrie-Candera/Bubble-Space-Theme) is a lot of fun.
-   [Purple Aurora](https://github.com/AndreasStandar/Obsidian-Theme---Purple-Aurora) has a neat gradient border around blockquotes.

## Ancillary Code

-   There's a free [web app to format Kindle book notes for Obsidian](https://www.reddit.com/r/ObsidianMD/comments/qmhw2e/i_made_an_app_to_format_kindle_book_notes_for/).

## Guides

-   Here's how you can use the [advanced URI plugin](https://discord.com/channels/686053708261228577/864046194195431425/904323421310173185) and Shortcut Maker to get note shortcuts on Android. You can also have [multiple vaults open](a couple write ups on how I use URIs and have multiple vaults open at once on android) using [this method](https://grimoire.wychwit.ch/notes/how-to-have-two-obsidian-vaults-open,-and-open-obsidian-uris-in-them).
-   Josh Duffney has a book out on Gumroad. It's about how to adapt the Smart Notes philosophy to Obsidian. Here's the [discount link](https://joshduffney.gumroad.com/l/take-smart-notes-obsidian/obsidian) for $5 off the regular price. It looks like there's also a video guide.
-   Nick Milo's Obsidian Flight Sale pre-sales start tomorrow. It looks like the price will be $99 until November 19, when the price will go up to $129. If you're interested, you can [sign up for the waitlist](https://lyt.ck.page/ace689c709).
-   Here's how you can use the [obsidian webhooks](https://github.com/trashhalo/obsidian-webhooks) plugin to use [Google Home to send notes to Obsidian](https://www.youtube.com/watch?v=45Q9bxmZbiM).
-   Here's an overview of the new [Life Disciplines Project](https://www.youtube.com/watch?v=XTwDhiDGk50) framework for Obsidian.

## In The Wild

-   I was poking around adding my "obscure history & science" newsletter, [The Iceberg](https://newsletter.eleanorkonik.com/), to some newsletter directories when I stumbled across [10+1 Things](https://rishikesh.substack.com/about). It's a curated newsletter about climate change, personal development, and obscure artists. It's written using Obsidian and I'm delighted by it.
-   Joseph DiCastro showcased a visualization of the Stanford Encyclopedia of Philosophy (SEP) over at the [LYT House](https://www.youtube.com/watch?v=xrz_TvdPcy4) with Nick Milo.
-   [Stationary Adjacent](https://stationeryadjacent.com/episodes/022) featured Obsidian on their 22nd episode.
-   Here's a [Twitter Thread](https://twitter.com/EleanorKonik/status/1456317253931057158) showcasing how I created an index of short stories in my fantasy universe — there are some screenshots of how the "map of content" plugin makes my vault structure apparent, and how everything in my vault feeds back into my ultimate goal of writing interconnected stories.
-   Obsidian was mentioned in an episode of [Week in OSINT](https://sector035.nl/articles/2021-42).

## Ancillary Tools

-   Snipd lets users [export podcast highlights to Obsidian](https://blog.snipd.com/how-to-export-your-podcast-highlights-to-obsidian-54208c06d491).
-   Here's a nifty list of [name generators](https://discord.com/channels/686053708261228577/805952223124520961/904118778160377917).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-11-05%20%20Graph%20Analysis%2C%20Podcast%20Notes%2C%20and%208%20More%20Themes.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-11-05%20%20Graph%20Analysis%2C%20Podcast%20Notes%2C%20and%208%20More%20Themes.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
