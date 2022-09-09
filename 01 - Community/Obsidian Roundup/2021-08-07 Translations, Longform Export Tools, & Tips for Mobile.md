---
link: https://www.obsidianroundup.org/2021-08-07/
author: Eleanor Konik
published: 2021-08-07
publish: true
---

# 2021-08-07: Translations, Longform Export Tools, & Tips for Mobile
The writing experience in Obsidian really leveled up this week. The PARA starter kit got a major facelift & there's a new web clipper.

## In The Community

- There was a really great discussion about [how to evaluate the security risks that Obsidian plugins (and all apps) represent](https://www.reddit.com/r/ObsidianMD/comments/oxgazv/community_plugin_and_security_concerns/) over at Reddit. Recommended reading for everyone who uses software and isn’t rock-solid certain about how to evaluate risk.
- `@curtismcshale` shared a video of [6 Excellent Obsidian Resources](https://youtu.be/KwxxrSb2Uyc) on YouTube.

## Obsidian Updates

- Insider v0.12.13 has some nifty timelapse improvements.

## Plugin News

- There’s been some discussion about how to translate plugins into various languages. For example, if you want to translate the [Spaced Repetition plugin](https://github.com/st3v3nmw/obsidian-spaced-repetition), there’s a “[how to](http://discordapp.com/channels/686053708261228577/707816848615407697/872541667616509962)” message in Discord. Conversely, here’s how the [excalidraw plugin handles it](http://discordapp.com/channels/686053708261228577/840286264964022302/872364516996968478).

### New

- [[cmenu-plugin|cMenu]] is a plugin that adds a minimal and user friendly text editor modal for a smoother writing/editing experience. This plugin makes text editing easier for those that don't wish to configure a multitude of hotkeys.
- [[longform|Longform]] is a plugin for Obsidian that helps you write and edit novels, screenplays, and other long projects. You can finally reorder scenes using (an alternate) file explorer, and compile them into a single file. It even lets you customize the appearance of exported using css! This is the plugin authors have been hoping for for as long as I’ve been using Obsidian and I am HYPE to sit down and play with it.
- The [[markdown-attributes|Markdown Attributes]] plugin enables [[Pandoc]]-style markdown attributes, which allows you to add HTML attributes directly to an element, which means users can style two lists differently on the same page, or change the background color of a single highlight, or cause a paragraph to display in all caps. Here’s an explanation in the [discord](https://discord.com/channels/686053708261228577/855181471643861002/872925697612582912).
- You can now set Obsidian to [[obsidian-hide-sidebars-when-narrow|automatically hide sidebars when Obsidian is at a particular width]].
- `@ownjoke` figured out a way to make Obsidian intelligently switch between edit and preview mode depending on whether you’re typing. The plugin is called [[obsidian-budget-wysiwyg|Budget WYSIWYG]].
- You can text or email (among others) notes directly to your daily note using this [[phone-to-roam-to-obsidian|“phone to roam” client]] for Obsidian.

### Updates

- [[obsidian-tasks-plugin|Tasks]] [version 1.2.0](https://github.com/obsidian-tasks-group/obsidian-tasks/releases/tag/1.2.0) had a bunch of updates, the main one seems to be that it lets you filter by recurring and hide elements from query results.
- [[obsidian-excalidraw-plugin|Excalidraw]] [1.2.13](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.2.13) now support links in View mode.
- [[obsidian-map-view|Map View]] works much better on mobile now, and there are some other quality of life improvements.
- It’s now easier to use [[obsidian-leaflet-plugin|Obsidian Leaflet]] to track travel paths (i.e. run routes) thanks to GPX support.
- [[obsidian-collapse-all-plugin|Collapse All]] is now available on mobile.
- [0.1.4](https://github.com/kzhovn/statusbar-pomo-obsidian/releases/tag/0.1.4) of the [[obsidian-statusbar-pomo|status bar pomodoro]] plugin has some bugfixes and allows users to add a link in your log to whichever note was active when you started your pomodoro.
- [0.2.0](https://github.com/alexandru-dinu/obsidian-sortable/releases/tag/0.2.0) of Obsidian Sortable now supports resetting the sorting order on the third click (like Wikipedia).
- [[obsidian-dice-roller|Dice Roller]] [5.2.0](https://github.com/valentine195/obsidian-dice-roller) can return a random link using `dice: #tag|link` (or a global setting to always return links from tags).
- [[media-extended|Media Extended]] [v2.10.0](https://github.com/aidenlx/media-extended/releases/tag/2.10.0) has mobile support and nifty timestamp stuff.
- [[obsidian-style-settings|Style Settings]] [v0.3.0](https://github.com/mgmeyers/obsidian-style-settings) lets users export and import global and scoped settings, and has some nifty toggles.
- [[breadcrumbs]] has a new Visualization View! This lets you see the structure of your vault using various different visualizations to get big picture views of your vault hierarchy.

### Magic

- Did you know that you can do [map layers with the leaflet plugin](https://discordapp.com/channels/686053708261228577/805952223124520961/873011203805417532)? Find out more neat tips and tricks from this [github discussion](https://github.com/valentine195/obsidian-leaflet-plugin/discussions/130).

### For Developers

- A request: where possible, it’s helpful to lean in to Obsidian’s local-first, no-internet-required ethos, and where possible avoid including things in themes and plugins that require internet, for example it’s helpful to base64 encode fonts instead of relying on Google font imports.
- There was [discussion](https://discordapp.com/channels/686053708261228577/840286264964022302/873305771625021500) about how the format for links in YAML in the future will be handled.

## Workflow Stuff

- There was a [great discussion](https://discord.com/channels/686053708261228577/722584061087842365/869942005210423397) in Discord about how to use citations and obsidian to best prepare for publication.
- Here’s a really nice guide for [how to use mermaid to make flow charts in Obsidian](https://www.mishacreatrix.com/knowledge-management-flow-diagram-in-obsidian).
- : There’s now a [Espanso (text expander) Snippet Showcase](https://forum.obsidian.md/t/espanso-text-expander-snippet-showcase/21852) in the forums, for those of us using Espanso, a cross-platform, system-wide text expander. (via `@Moonbase59`)
- via a couple of [folks in Discord](https://discord.com/channels/686053708261228577/744933215063638183/873033503976087622): You can use [[obsidian-focus-mode|Focus Mode]] & [[obsidian-hider|Hider]] & [WindowTop](https://windowtop.info/) (or [Autohotkey](https://discord.com/channels/686053708261228577/744933215063638183/873046760853999646), apparently) to turn Obsidian into a transparent (using [[obsidian-electron-window-tweaker|Electron Window Tweaker]]) scratchpad on top of other windows, i.e. a browser or PDF.

### Mobile

- [Quick Capture (mac/iOS) and Inbox Processing](https://forum.obsidian.md/t/quick-capture-mac-ios-and-inbox-processing/21808) keeps coming up, here are some tips!
- [[Android Apps|Android]] users can [use keyboard shortcuts on Android phone](http://discordapp.com/channels/686053708261228577/864046194195431425/872781020913598464) without a physical keyboard by installing the [Hacker's Keyboard](https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard) app. (via `@ichmoimeyo`)
- [Here’s how to use a .nomedia folder to get your phone’s gallery to stop including Obsidian images](https://www.reddit.com/r/ObsidianMD/comments/ovatlr/is_there_a_way_to_not_show_images_on_your_gallery/h7a1x2q/)
- There’s a new [fork of the todoist task management plugin](https://github.com/Finnvoor/obsidian-todoist-plugin) that works on mobile.

## Tiny Tips

- This keeps coming up, so, if you zoom in a bunch on your screen can’t get it “back to normal,” try using `ctrl+0` (`cmd+0` for Mac) to reset your font sizes. If that doesn’t work, try fiddling with the `Quick font size adjustment` setting in `settings > appearance`.
- You can continuously nest code blocks by adding more back ticks (via `@javalent`)

## Feature Requests

- [Clickable image link, using wikilinks](https://forum.obsidian.md/t/clickable-image-link-using-wikilinks-from-the-discord/21954)

## Appearance

- A bunch of people apparently didn’t know about the nifty [css options for the calendar plugin](https://github.com/liamcain/obsidian-calendar-plugin/wiki) which can, for example, let you make the calendar view a bit slimmer, or add emoji markers behind a day in the calendar view thanks to YAML.
- Here’s how to make a [linear gradient](http://discordapp.com/channels/686053708261228577/707816848615407697/872277959094984756) for a progress bar with CSS.
- Here’s how to make all numbers have the same width ([make them tabular](https://discord.com/channels/686053708261228577/702656734631821413/872192379485052950)) so they look nicer.

## Knowledge Management

- `@cotemaxime` refactored the [PARA starter kit](https://forum.obsidian.md/t/para-starter-kit/223) and also “forked” the PARA system into a “[PAAN](https://forum.obsidian.md/t/paan-starter-kit/21782)” designed to work a little more intuitively with Obsidian’s strengths, like links and the graph.
- This is a periodic reminder to [back up your data](https://www.maximecote.me/blog/how-to-make-your-critical-data-last-decades/), and that means properly, one local, one remote, and one in the cloud. Sync is not a backup!
- I wrote a blog post about how [there's real value in "literature review" style notes](https://eleanorkonik.com/lit-review-value-gestalt-reflection/) and I don't see them discussed often.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- [Meta](https://metanote.netlify.app/) is a nifty (alpha) visual notecard / whiteboard organizer / mindmap thing for notes.
- `@kepano` (the [[Minimal]] theme developer) put together [a 90 second demo](https://www.youtube.com/watch?v=Vy1MdjickAI) of their new [Web Clipper bookmarklet](https://gist.github.com/kepano/90c05f162c37cf730abb8ff027987ca3). It allows you to grab entire pages or selections from the web into Obsidian in one click.

## Housekeeping

- I updated some of the “static pages” for the Roundup, notably the [Resources](https://obsidianroundup.org/resources/) page (which now segments out the Obsidian-related paid courses) and the [About](https://obsidianroundup.org/about/) page (which now has a better explanation of how things get “chosen” to be added to the Roundup), since I’ve been getting more questions about that lately.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-08-07%20Translations%2C%20Longform%20Export%20Tools%2C%20%26%20Tips%20for%20Mobile.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-08-07%20Translations%2C%20Longform%20Export%20Tools%2C%20%26%20Tips%20for%20Mobile.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
