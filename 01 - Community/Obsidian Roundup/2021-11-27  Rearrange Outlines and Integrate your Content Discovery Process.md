---
link: https://www.obsidianroundup.org/2021-11-27/
author: Eleanor Konik
published: 2021-11-27T13:11:00
publish: true
---

# 2021-11-27: Rearrange Outlines & Integrate your Content Discovery Process
A new way to save tweets to Obsidian, more flexible hierarchy options, text to speech, and a new focused writing theme

## In The Community

-   Our newest moderator, `@tzhou`, is collecting [tips you wish you knew when starting Obsidian](https://docs.google.com/forms/d/e/1FAIpQLSfqKs2UTvKrGvoFlO77pD0rmxuZxmVTPz6JcPOAqEfdg3cR3A/viewform). Note that this information will be public in an unsanitized Google sheet, so don't put anything private in there. Here's [the announcement on Discord](https://discord.com/channels/686053708261228577/694233507500916796/912510676545708082)
-   `@ClareMacrae` is [looking for people](http://discordapp.com/channels/686053708261228577/840286264964022302/911915924758614066) who would like to get some automated tests added for their plugin. It's background research for a new Community Talk called something like: "Easy automated testing for Obsidian plugin developers: find broken things before your users do..."
-   After some small bugs were found in a bunch of Obsidian themes, `@pseudometa` [requested](http://discordapp.com/channels/686053708261228577/702656734631821413/912089899744755753) that someone write a guide for how to do CSS linting (particularly as it relates to Obsidian themes). I also think this would be helpful, so if you know of any such guides or can write one, please share.
-   `@ryanstraight` is organizing a conference panel for [Online Learning Consortium’s Accelerate](https://onlinelearningconsortium.org/attend-2021/accelerate/) focused on Obsidian. Check out the discussion [here](http://discordapp.com/channels/686053708261228577/722584061087842365/911833418642378824) if you're an academic and want to get in on this.
-   Moderator `@ryanjamurphy` was featured on [the Automators podcast with David Sparks](https://www.relay.fm/automators/88), where he discussed automation tips for Obsidian (and parenting!).

## Obsidian Updates

The [0.13.5](https://forum.obsidian.md/t/obsidian-release-v0-13-5-insider-build/27527/2) Insider Build allows users to use drag and drop to re-arrange heading sections from the Outline pane. You can also drop an outline item into the editor to generate a heading link.

Additionally, Live Preview mode is iterating fast. There were a bunch of fixes, and [0.13.6](https://forum.obsidian.md/t/obsidian-release-v0-13-6-insider-build/27676) brought support for Inline LaTeX, HTML blocks, iframes, fancy checkbox css, and code syntax highlighting.

There is now a “copy share link” in the community plugin’s information page.

## Plugin News

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

### New

-   For folks who like the idea of saving Twitter threads to Readwise but don't want to get a whole Readwise subscription just to do that, check out the [Tressel](https://www.tressel.xyz/) app, which now has an [Obsidian plugin](https://github.com/aseem-thakar/obsidian-tressel/).
-   The new [Calibre plugin](https://github.com/caronchen/obsidian-calibre-plugin) lets users access Calibre libraries and read books directly in Obsidian.
-   [Obsidian Overdue](https://github.com/parente/obsidian-overdue) Obsidian plugin that marks items as `[[Overdue]]` if they are not checked off by their due date

### Updates

-   [Flexible Pomo](https://github.com/grassbl8d/flexible-pomo-obsidian) added an option for persistent workbenches for tracking multiple files during a Pomodoro sequence.
-   [Breadcrumbs](https://github.com/SkepticMystic/breadcrumbs) (which [deserves to be more popular](https://www.reddit.com/r/ObsidianMD/comments/r18dnn/the_breadcrumbs_plugin_deserves_to_be_more_popular/), got a _bunch_ of updates. It now supports folder & tag notes (which I am hype for). You can add `BC-folder-note: true` to any note in a folder (or tag), and all other notes in that folder will now point upwards to that folder-note. You can also specify the exact upward fieldname to use with: `BC-folder-note-up: fieldName`. You can now specify "sibling" relationships with directionality, "next" and "previous."
-   the Contextual Typography plugin (v2.2.0) now surfaces detailed information relating to embeds and codeblock languages.
-   [Excalidraw 1.4.11](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.4.11) has a bunch of fixes and small improvements, along with a new library element that allows users to publish icons from the stencil library to excalidraw.com (except on iOS).
-   [Various Complements v2.0.0](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/2.0.0) got some bugfixes and a breaking change: custom dictionaries support description and aliases, but paths only support a relative path from Vault.
-   [Dice Roller 7.8.0](https://github.com/valentine195/obsidian-dice-roller#dataview-integration) adds support for inline dataview variables in dice rolls.

### Betas

-   [Text to speech](https://github.com/joethei/obsidian-tts) is looking for beta testers for every platform except Android.
-   [Obsidian-Task-Changer](https://github.com/Quorafind/Obsidian-Task-Changer) allows users to change task status with just one click.

## Tips

-   `@Murf` [recommends](http://discordapp.com/channels/686053708261228577/716028884885307432/912547664393027645) that if you're trying to use codeblock syntax highlighting in Live Preview, the best combo that works is to use Editor Syntax Highlight + CodeMirror Options + Style Settings.
-   `@Necromant` shared a nifty explanation of how they use [sublists to get more context in the Backlinks pane](http://discordapp.com/channels/686053708261228577/710585052769157141/912820424096751696).
-   Here's a discussion with [tips on how to write LaTeX more efficiently](https://discord.com/channels/686053708261228577/722584061087842365/912338492762259526).

## Appearance

-   This [CSS for Live Preview mode](https://gist.github.com/GitMurf/9f448ca1b19ab8026a00bfd3d71221cf) will change the bullets to be similar to Microsoft Word / Outlook where each level is a different symbol
-   Here's some [CSS to ensure monospace ligatures are working](https://gist.github.com/pmbauer/42d67769c419ebf799938db62b1671bf).
-   [Typewriter](https://github.com/crashmoney/obsidian-typewriter) is a nice clean theme designed for a focused writing experience.
-   [Typomagical](https://github.com/hungsu/typomagical-obsidian) uses small caps for links, has some fancy ligatures, and a bunch of color schemes available via the Style Settings plugin.
-   Primary got a bunch of fixes and now supports sidenotes.
-   [Minimal 4.1.3](https://github.com/kepano/obsidian-minimal/releases/tag/4.1.3) added support for the Insider build's backlinks in document feature. [4.1.7](https://github.com/kepano/obsidian-minimal/releases/tag/4.1.7) added a new set of composable helper classes for table and Dataview styling.
-   Ebullientworks got some cosmetic fixes.
-   There's a new [Theme That Shall Not Be Named](https://github.com/ChopTV/Obsidian-Theme-That-Shall-Not-Be-Named) that sort of blends the Cybertron and Slytherin themes.

## Ancillary Code

-   The Alfred workflow [Shimmering Obsidian](https://github.com/chrisgrieser/shimmering-obsidian/releases/tag/2.3.6) got a hotfix to the setup process, so if you were having trouble before, try again.

## Guides

-   `@TFTHacker` wrote about [leveraging backlinks in Obsidian and Readwise export](https://tfthacker.medium.com/leveraging-backlinks-in-obsidian-and-readwise-export-aebb52ffa9d4).
-   After some discussion with the Discord community,  `@Tomodachi` created a lightweight blog on [https://write.as](https://write.as) (which seemed like the easiest / cheapest / most ethical option) to try and start building a writing habit. Their first post is about [how to digitize handwritten notes](https://tomodachi.writeas.com/how-i-transcribe-notes-in-obsidian).

## Discussions

-   `@nickmilo` took part in a nice discussion in the Discord about [making maps of content](http://discordapp.com/channels/686053708261228577/710585052769157141/912864011496865832).
-   Here's a discussion about [how to make Obsidian more like an outliner](https://www.reddit.com/r/ObsidianMD/comments/r1urvd/best_plugins_to_make_obsidian_more_logseqroamlike/).
-   Here's a discussion about different ways to [organize quotes](https://www.reddit.com/r/ObsidianMD/comments/r0zitr/does_anyone_store_quotes_if_so_in_what_way_do_you/).

## Knowledge Management

-   This [Discord conversation](https://discord.com/channels/686053708261228577/700466324840775831/912870233495203850) about an [awesome visualization of royal families](https://royalconstellations.visualcinnamon.com/) inspired me to try out Juggl for [organizing the interconnections between my stories](https://discord.com/channels/686053708261228577/805952223124520961/913641805889802240), and it was [very valuable](https://twitter.com/EleanorKonik/status/1464105930350604290).
-   `@manedblackwolf` shared her [daily template](https://discord.com/channels/686053708261228577/744933215063638183/913155409311834192).
-   Here's a nice example of [a totally complete and polished literature note](https://discord.com/channels/686053708261228577/744933215063638183/912474855876730931) created by someone working on their PhD

## In the Wild

-   [Paras Chopra](https://invertedpassion.com/start-here/) (one of the Forbes 30 under 30 folks who seem pretty famous in the marketing sphere) shared [his knowledge garden](https://notes.invertedpassion.com/_Start+here_), and it's pretty impressive.

## Ancillary Tools

-   Mac users can use [popclip](https://pilotmoon.com/popclip/) to [clip from Safari](https://forum.popclip.app/t/clip-selection-to-obsidian/359).
-   [Readwise](https://readwise.io/i/ac9) can now import highlights from [Refind](https://refind.com/EleanorKonik?invite=209801a8ad), which is probably best summed up by Liza Sperling: "Refind is a productivity game changer. Follow topics to stay on top of what matters to you. Search in the community to find the top links on any subject. Save links with the extension, and you’ll never hunt for a link again."
-   In the same vein, [The Sample](https://thesample.ai/?ref=9937) will send you a different newsletter each day (or week) based on your interests. It's my favorite newsletter discovery engine because it's got a ton of small, niche information instead of pulling from the "big names."
-   This link about [how to get started with building a fictional world](https://www.worldbuildingmagazine.com/2021/3/getting-started-2/) is totally unrelated to Obsidian, but it _did_ hit the Discord starboard, so I guess it counts as Obsidian-adjacent.

## Housekeeping

This week was Thanksgiving in America, which means two things:

-   First, I want to take a moment to thank everyone who has signed up for a [recurring membership](https://www.obsidianroundup.org/membership/) or [donated on ko-fi](https://ko-fi.com/eleanorkonik) to help defer my hosting costs. This newsletter currently has 2,963 subscribers, and once we hit 3k, the hosting fees go up a fair bit 😅
-   Second, my life is about to get _really hectic_. This week was Thanksgiving _and_ my husband's birthday, next weekend is my birthday, the weekend after that we're taking our toddler on his first vacation, the weekend after _that_ is [WorldCon](http://www.worldcon.org/), and the weekend after that is Christmas, then New Year's, then my son's birthday. I fully intend that the Roundup's publishing schedule not be interrupted, but if I'm slightly less responsive for the next month, please be gentle 💚

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-11-27%20%20Rearrange%20Outlines%20and%20Integrate%20your%20Content%20Discovery%20Process.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-11-27%20%20Rearrange%20Outlines%20and%20Integrate%20your%20Content%20Discovery%20Process.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
