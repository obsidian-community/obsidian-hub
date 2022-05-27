---
link: https://www.obsidianroundup.org/2021-12-03/
author: Eleanor Konik
published: 2021-12-04T13:12:00
publish: true
---

# 2021-12-03: Obsidian October winners & a ton of TTRPG stuff
Great & tools for theme developers, a new plugin for chat formatting, & a new method for diagram support.

## In The Community

-   [The results from Obsidian October are out!](https://obsidian.md/october2021) Big congratulations to all the winners, runners-up, and lucky draws. Also, a thank you to all participants for getting involved, and creating something awesome. Here's [Santi Younger](https://www.youtube.com/watch?v=-WnHWQrCC-s) with a video "review" congratulating the winners.
-   Some Realm Works (TTRPG software) users are switching to Obsidian and set up a [Facebook group](https://www.facebook.com/groups/obsidianttrpgusers/) for other folks using Obsidian for TTRPGs. Here's the [export tool](https://github.com/farling42/RWoutput) for Realm Works. Here's a cool [graph of one import](https://discord.com/channels/686053708261228577/709712341066842113/916183808657743922). Also, tabletop games now have their own channel in Discord.

## Obsidian Updates

-   The [releases repository](https://github.com/obsidianmd/obsidian-releases) got a bit of a facelift with some neat information about how plugins and themes work.
-   [v0.13.7](https://forum.obsidian.md/t/obsidian-release-v0-13-7-insider-build/28061) got more improvements and bug fixes for live preview, and spell checker languages can now be changed on Windows and Linux.

## Plugin News

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool (BRAT)](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

### New

-   The [dialogue plugin](https://github.com/holubj/obsidian-dialogue-plugin) lets you format your text file so that dialog looks like a chatbox!
-   You can now get a [page count](https://github.com/ReaderGuy42/Obsidian-Page-Count) on your status bar.
-   You can now launch an image file in your vault in a new Obsidian window thanks to [Image Window](https://github.com/valentine195/obsidian-image-window), which I'm told is handy for TTRPG DMs who can't see their second monitor.
-   Title Serial Number automatically [gives section headings an ID number](https://github.com/yalvhe2009/obsidian-title-serial-number-plugin).
-   This [graphviz](https://github.com/QAMichaelPeng/obsidian-graphviz) integration seems like a nifty alternative to [[Mermaid]].
-   [Preview Mode Keybinds](https://github.com/horriblename/preview-mode-keybinds-obsidian) adds vim-like keybindings to preview mode.

### Updates

-   [Various Complements Plugin v3.0.0](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/3.0.0) was released which complements the text with internal links. This includes links to notes you may have forgotten you’ve created.
-   React Components 0.1.2 added new admonition-style syntax for using components with `src`.
-   [Block Reference Counter 0.3.0](https://github.com/shabegom/obsidian-reference-count) had a major performance rewrite. It now supports non-English languages, relative and full paths, and embeds.

-   [Breadcrumbs](https://github.com/SkepticMystic/breadcrumbs/wiki) has a new "Down" view and you can even `Freeze` it to stop the view from changing. Also, as of 2.0.0, the different alternative hierarchy fields have been standardized.
-   [alx-folder-note](https://github.com/aidenlx/alx-folder-note/releases/tag/0.12.2) got some updates my brain is too mushy to parse, I'm sorry, see `#housekeeping` at the bottom for details.
-   Excalidraw 1.4.14 lets users set a css to format the embedded SVG snapshot of your markdown document. Here's a [walkthrough](https://t.co/nk4bjXq0UR).

### Betas

-   [Expiring Notes v0.0.4](https://github.com/joerncodes/obsidian-expiring-notes) has a new modal so expiration dates don't have to get hand-typed into our frontmatter.
-   Workspaces Plus is looking for beta testers using the BRAT plugin. You can read more about the [features here](https://github.com/nothingislost/obsidian-workspaces-plus/wiki/Readme-for-next-public-release), or [provide beta feedback here](https://discord.com/channels/686053708261228577/855181471643861002/915264349189324830).

### For Developers

-   Theme developers should check out the new [Theme Design Utilities](https://github.com/chrisgrieser/obsidian-theme-design-utilities) plugin.
-   `@arminta7` has put a `@dev for hire` bounty for a task plugin that will take the place of the macOS/iOS task manager, OmniFocus. Key points are recurring tasks, defer dates, low friction ui, ability to add and edit specific task metadata easily. [More information here.](https://discord.com/channels/686053708261228577/840286264964022302/916403851588931664)
-   Dataview has a bunch of open issues, and `@blacksmithgu` could use some help. He flagged some as [“help-wanted”](https://github.com/blacksmithgu/obsidian-dataview/issues?q=is%3Aissue+is%3Aopen+label%3Ahelp-wanted) that are relatively self-contained, if anyone is in a position to help out. This is a great way to do development work for the community without having to commit to maintaining a whole plugin yourself ;)

## Appearance

-   [Shimmering Focus v1.225](https://github.com/chrisgrieser/shimmering-focus/blob/main/Changelog.md) bought some nifty focus view features, a choice between round and squared off shapes, a restyle of the command palette that makes it easier to scan, support for breadcrumbs, and some more refinements.
-   Sanctum v0.4 got a bunch of optimizations, should be better optimized for mobile, and got a neat new way of displaying metadata.

-   Here's the code for [colored relationship lines](https://gist.github.com/GitMurf/5122c0c8405ffa36a03049d9f4434bf4) for bullet points that works in Live Preview.

## Guides

-   [Why and How to use Stylelint for your Obsidian Theme, by pseudometa](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/Why+and+How+to+use+Stylelint+for+your+Obsidian+Theme)
-   [Want some Sass with your Obsidian theme? Here's How and Why, by jdanielmourao](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/Want+some+Sass+with+your+obsidian+theme%E2%80%BD+here%27s+How+and+Why)
-   Here's a whole [youtube playlist](https://www.youtube.com/playlist?list=PLV5XWfKkFpk7MJTKv5YdSSpT9b-vLslWu) with guides about how to use Obsidian for tabletop role playing games like Dungeons & Dragons. There's even a pretty good example of [stress testing Obsidian](https://youtu.be/newKX6mQJ9M).

## Discussions

-   Here’s a discussion about the [collector’s fallacy](https://discord.com/channels/686053708261228577/771575014382108672/914132835584077824) and how to rethink processing information into your vault through questions instead of consumption.
-   Here’s a discussion about how hierarchies with [Breadcrumbs using Dataview fields](https://discord.com/channels/686053708261228577/710585052769157141/914579583490207744) allows for greater creativity and connections.
-   And here’s [a gentle reminder](https://discord.com/channels/686053708261228577/710585052769157141/915770147673882724) that the most important Obsidian workflow is what works for you. There’s a lot of advice out there when it comes to folders, links, and hashtags, but in the end the best way is _your_ way.
-   But speaking of folders, links, and hashtags, `@Whereiscalypso` has [a lovely excalidraw diagram](https://discord.com/channels/686053708261228577/744933215063638183/916205731609473034) of how he uses them.

## Knowledge Management

-   `@aBoppy6` discussed their thought process for reviewing conceptual notes with [[Spaced repetition|spaced repetition]]. You can read more about it on [their Obsidian Publish site](https://publish.obsidian.md/tim/50_Projects/Using+spaced+repetition+for+your+conceptual+notes).

## Ancillary Tools

-   Some folks in the `#off-topic` channel of Discord were [lamenting that Instagram got bought by Facebook](https://discord.com/channels/686053708261228577/700466324840775831/916318322637832202) and hey, did you know that there's a privacy-first, decentralized alternative that runs off the ActivityPub standard? It's called [pixelfed](https://switching.software/replace/instagram/). I went ahead and made [an account](https://pixelfed.social/eleanorkonik) and am going to try to share old vacation photos I ostensibly took for research purposes but never processed into my notes. Maybe this way I'll actually import them all!

## Housekeeping

-   My family had a COVID exposure so we're going into quarantine, and bonus, I'm not feeling well (at-home COVID test read negative, have a dr appt Monday, wish me luck), so sorry if this is a little abrupt and short this week. Happy birthday to me! Anything I missed this week (aka reddit, twitter, the forum, and my bookmarks) I'll try to include next week.
-   Also, thank you to moderator Leah who helped me write this so I could take a nap. I offered to pay her, but she said to [donate to her local Alzheimer Society](https://alzheimer.ca/greybruce/en/take-action/donate), which offers services and support to people living with dementia, their families and their caregivers. If you'd like to join me in thanking her for stepping up so that the Roundup could still happen, I'm sure it would make her day. 💚

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-12-03%20%20Obsidian%20October%20winners%20and%20a%20ton%20of%20TTRPG%20stuff.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-12-03%20%20Obsidian%20October%20winners%20and%20a%20ton%20of%20TTRPG%20stuff.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
