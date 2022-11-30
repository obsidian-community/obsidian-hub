---
link: https://www.obsidianroundup.org/2022-11-19/
author: Eleanor Konik
published: 2022-11-19T13:54:41
publish: true
---

# 2022-11-19: Doom! & Scrollable Daily Notes
A request for python devs to help out with the community hub vault, a new comprehensive tutorial for beginners, & discussion of YAML APIs.

## In The Community

If there is anyone who would like to help out, perhaps 1 or 2 hours a week for a few weeks, on overhauling the Obsidian Hub Python code so that it can update existing pages as well as create new content, we could do amazing things, and learn a lot. If anyone would like a no-commitment chat about how code pairing works, with a view to helping contribute to the Python code in the Hub, please reach out in the [hub-website](https://discord.com/channels/686053708261228577/915679988118863933/1042825618938658876) channel in Discord. This would be very beneficial to the community; one of the projects has been to automatically get [the Obsidian Roundup into the community knowledge base vault](https://publish.obsidian.md/hub/01+-+Community/Obsidian+Roundup/%F0%9F%97%82%EF%B8%8F+Obsidian+Roundup) so it can be indexed.

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list._ For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new).

* [Copy document as HTML](https://github.com/mvdkwast/obsidian-copy-as-html) by `@mvdkwast`  copies the current document to clipboard as HTML, including images.
* [Dynbedded](https://github.com/MMoMM-org/obsidian-dynbedded) by `@MMoMM-org` allows for things like the execution of dynamic queries like dataview from a different note in the context of the current note, and dynamic date substitution.
* [Page Gallery](https://github.com/tokenshift/obsidian-page-gallery) by `@tokenshift`  creates an embeddable gallery based on selected page contents.
* [Obsidian42 - Strange New Worlds](https://github.com/TfTHacker/obsidian42-strange-new-worlds) by `@TfTHacker`  makes it easier to see connections between notes.

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

* [Daily Notes Editor](https://github.com/Quorafind/Obsidian-Daily-Notes-Editor) by `@Quorafind`  makes it easier to edit a bunch of daily notes in one page(inline), which works similar to Roam Research's default daily note view. I don't use Daily notes, but I think folks have been waiting for something like this for a long time, so I'm really excited to see it.
* [Split Pane View Helper](https://github.com/luckman212/obsidian-split-pane-view) by `@luckman212`  lets users quickly open a split source/preview view via hotkey or toolbar
* [SamePage](https://github.com/samepage-network/obsidian-samepage) by `@dvargas92495`  is a client into the inter-TFT-protocol.
* [Obsidian markdown export](https://github.com/bingryan/obsidian-markdown-export-plugin) by `@bingryan`  is a markdown export plugin for Obsidian.
* [obsidian-doom](https://github.com/twibiral/ObsiDOOM) by `@twibiral`  lets users play the well-known FPS game DOOM in your Obsidian app. You can also play Prince of Persia, Mortal Combat, GTA, Sim City, and Need for Speed. I'm surprised it took this long for someone to make this 😂
* [Audio Player](https://github.com/noonesimg/obsidian-audio-player) by `@noonesimg` has background playback, bookmarks and wave visualiser instead of the default html5 audio.
* [Numerals](https://github.com/gtg922r/obsidian-numerals) by `@gtg922r`  turns any code block into an advanced calculator and evaluates math expressions on each line of a code block, including units, currency, and optional TeX rendering.
* [Transcription](https://github.com/djmango/obsidian-transcription) by `@djmango`  makes it easier to create high-quality transcriptions from markdown linked audio files
* [AWS DynamoDb For Obsidian](https://github.com/leenattress/obsidian-plugin-dynamodb) by `@leenattress`  allows users to query AWS DynamoDb and render tables inside documents.
* [Mini Toolbar](https://github.com/Quorafind/Obsidian-Mini-Toolbar) by `@Quorafind`  adds a mini context toolbar in the editor, like cMenu.
* [Image Layouts](https://github.com/vertis/obsidian-image-layouts) by `@vertis`  adds beautiful image layouts to your notes
* [BPMN Plugin](https://github.com/joleaf/obsidian-bpmn-plugin) by `@joleaf`  enables viewing BPMN diagrams using bpmn-js.
* [Smart Links](https://github.com/kemayo/obsidian-smart-links) by `@kemayo`  allows users to define custom link formats
* [Auto Glossary](https://github.com/ennioitaliano/obsidian-auto-glossary) by `@ennioitaliano`  makes it easier to automatically create a file with an index and/or glossary.
* [Webpage HTML Export](https://github.com/KosmosisDire/obsidian-webpage-export) by `@KosmosisDire`  exports an obsidian document as an HTML document / webpage / website (correctly!). It also has interactive embedded dark / light theme toggle, and document outline.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

* [Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/7.4.0) versions 7.3 & 7.4 got improved front matter handling in searches.
* [Divide & Conquer](https://github.com/chrisgrieser/obsidian-divide-and-conquer/releases/tag/1.0.0) got a new 1.0 release and a new maintainer; there are new UI buttons in the community plugins and snippets tabs.
* [Full Calendar 0.8.0](https://github.com/davish/obsidian-full-calendar/releases/tag/0.8.0) added task events; you can add checkboxes to events and check them off as complete from the calendar, and it will update the front matter with a time of completion.
* [Colorful Tag 1.2.2](https://github.com/rien7/obsidian-colorful-tag/releases/tag/1.2.2) supports nested tags, removing hashtags, and tag names.
* [Omnisearch 1.8.0](https://github.com/scambier/obsidian-omnisearch/releases/tag/1.8.0) added a URL scheme for integration with external tools, and OCR for images.

## Feature Requests

* Here's a [concept video](https://www.youtube.com/watch?v=J0EuJF2kf3E) for a new SmartOutline plugin; the idea is to help users quickly and visually sift through their vault, extract what they need, and organize it while auto-inserting backlinks to prevent lost connections. Andrew is looking for feedback from the community to help refine the idea.
* Here's the "super feature request" for how to [enhance Obsidian with a type system for notes and database like views](https://forum.obsidian.md/t/super-fr-enhance-obsidian-with-a-type-system-for-notes-and-database-like-views-metadata/46444).

## Appearance

* [Prism v3.0.0](https://github.com/damiankorcz/Prism-Theme/releases/tag/3.0.0) is a complete rewrite and compatible with Obsidian 1.0.0. Definitely check out the release notes if you're an existing user.
* [Listive](https://github.com/efemkay/obsidian-listive-theme) by `@efemkay`  is a new theme for outliner focused writing with differentiated headers.

## Guides

* There's a new 2 hour video tutorial for [Everything you need to know to use Obsidian as a Second Brain](https://www.youtube.com/watch?v=WqKluXIra70) and a lot of folks really seemed to like it.
* Here's a [step by step guide to installing AI in Obsidian](https://uxplanet.org/installing-ai-in-obsidian-step-by-step-guide-92b47a850a21). Here's a [showcase of someone using it](https://www.reddit.com/r/ObsidianMD/comments/yv3i76/using_the_gpt3_ai_writer_inside_obsidianthis_is/).
* Here's a tutorial for how to get [a beautiful homepage](https://github.com/faroukx/obsidian-homepage).
* Here's how to create a Notion-like content calendar with t[he Obsidian Projects plugin](https://www.youtube.com/watch?v=ny8lksaQ5A8).
* Here's [how to set up a zettelkasten](https://mattgiaro.com/obsidian-zettelkasten/) in Obsidian, for those looking for a a system for organizing and storing information that focuses on using backlinks instead of folders and tags.
* Here's [how to embed Glasp's highlight as a card on note-taking apps](https://medium.com/glasp/how-to-embed-glasp-highlights-on-note-taking-apps-websites-23db1381901e).
* Here's how to use the Influx and Strange New Worlds plugins to [enhance your backlinks](https://www.youtube.com/watch?v=nDjlMBu-HSk).

## Discussions

* Licat and a few plugin developers discussed how [having a stable API for YAML not specific to a plugin would be good](https://discord.com/channels/686053708261228577/840286264964022302/1040912541758541985)
* There was a nice discussion on pkm.social about [daily notes vs. themed logs](https://pkm.social/@erankatz/109331203302863544) and how to implement both.

## Showcases

* Andrew Roddick gave a talk: [From Info-Glut to Connected Notes: Obsidian and Digital Note-Taking in Academia](https://scds.github.io/dmds-22-23/Obsidian.html) at McMaster University's center for Digital Scholarship. He walked through vaults for teaching and for literature reviews.
* Apparently you can use [Obsidian to control a smart home](https://www.youtube.com/watch?v=UaCzRBJCdYg); Obsidian can even brew coffee!
* This is [a pretty cool book dashboard](https://talk.macpowerusers.com/t/book-dashboard-and-notetaking-in-obsidian/31359).

## Food For Thought

* This article about how [the bubble is popping for unprofitable software companies](https://world.hey.com/dhh/the-bubble-has-popped-for-unprofitable-software-companies-2a0a5f57) was really thought provoking and made me grateful that the vast majority of my notes are in a non-proprietary format that I access using software from a bootstrapped company.
* Here's a [comparison of the big-note mindset and the small-note mindset](https://www.obsidianroundup.org/one-size-fits-all-how-to-take-big-notes-and-how-to-take-small-notes/), and how they require different types of plugins. Note that it's hosted on the Obsidian Roundup but I didn't write it, `@pseudometa` did; if anyone else wants to write a couple of one-off articles and don't feel like dealing with Medium or what-have-you, let me know and I'm happy to set you up with a contributor account.
* Does anybody listen to to [Andrew Huberman's podcast](https://hubermanlab.com/)? He's apparently a neuroscientist with lots of productivity advice; I don't listen to podcasts but some folks who do recommended it. I'd be curious about others' thoughts.

## Ancillary Tools

* [HTNotes](https://github.com/0x4xel/HTNotes) for Linux integrates a Vault Workspace in obsidian that will help you in the first steps of taking machine notes of Hack The Box. Here is [a demo](https://youtu.be/tjHShmUzWM0).

## Housekeeping

Things are still pretty blurry on the vision front and extremely stressful on the teaching front, but I'm hanging in there and am very grateful to the support of our community 💚 

But also, Twitter has been intermittent for me and some replies people are making aren't actually showing up in my notifications feed, so if you've reached out about something over a week ago and I haven't responded, try pinging me again. I have not ignored anyone on purpose, although I do have some emails I need to get to this weekend. 


%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-11-19%20Doom%21%20%26%20Scrollable%20Daily%20Notes.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-11-19%20Doom%21%20%26%20Scrollable%20Daily%20Notes.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
