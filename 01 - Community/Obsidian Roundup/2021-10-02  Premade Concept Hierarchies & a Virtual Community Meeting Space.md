---
link: https://www.obsidianroundup.org/2021-10-02/
author: Eleanor Konik
published: 2021-10-02T11:30:00
publish: true
---

# 2021-10-02: Premade Concept Hierarchies & a Virtual Community Meeting Space
Templater is looking for an additional maintainer. There's also a new plugin to enforce style guides.

## In The Community

-   Obsidian now has [a persistent virtual meeting space](https://topia.io/obsidiancommunitycoworking). [[Obsidian Community Coworking#Obsidian Community Coworking|Topia]] is a "social engagement platform" with  customizable virtual worlds. The audiovisual feed is based on how close your "toon avatar" is to someone else's, which means you can sort of edge away from a group chat and have a side conversation then wander around to join another conversation, like at a real life conference. It's officially organized through the [[Obsidian Community Talks|community talks]] discord. It's being offered up as an alternative to Zoom for talks that are meant to be more "fireside chat" or "freeform workshop" in nature — the q&a session at the end of my talk on Sunday will be on Topia, so feel free to drop by and check it out then.
-   We're also going to try out using Topia as a [co-working space](https://nomadfinanceandfreedom.com/virtual-coworking-flexible-work-space/) for people in the community to log in and hang out with others wanting an accountability buddy while they do focused personal knowledge management (or whatever related thing). Please fill out this [whentomeet](https://www.when2meet.com/?13103059-rG85D) if you're interested in showing up regularly or "anchoring" a recurring timeslot.
-   It's been about a week since [[Obsidian October 2021]] was first announced, but there's still plenty of time to participate. If you're interested in making a plugin or theme or just hanging out in a community event, check out the [details here](https://publish.obsidian.md/hub/11+-+Events/Obsidian+October+2021).
-  [[00 - Start here|Obsidian Hub]] is a new experimental vault maintained by the obsidian community (that means you, if you want to help out!). I mentioned it in passing last week, but the idea is to try and consolidate some of the amazing resources this community has collected over the last year and a half, so _please_ check it out because I cannot do it justice with one paragraph. It's got vault examples, plugins and template info, events, github contribution guides, information about community events, & more.

### Community Talks

You can subscribe to the calendar of upcoming talks using [this link](https://sesh.fyi/api/calendar/v2/w812YLku4AkwT6LCLSSvko.ics). There's also a [ClickUp Calendar](https://sharing.clickup.com/c/h/4gdf2-36/5b21a6f8588e5c6).

-   Sunday Oct 10 at 4PM EST: [[Project management for fiction writing]] with [[eleanorkonik|Eleanor Konik]] (that's me!) — [zoom link](https://zoom.us/j/91650893242?pwd=aUUxNzF0ak81czZHaUk0SUlTTjVDUT09) (if you run late, we'll be switching over into Topia after the presentation portion).
-   Saturday October 9 at 1PM EST: [[Obsidian and TTRPG]] (panel of 5) — [zoom link](https://us02web.zoom.us/j/85187672826?pwd=VWZtd2hFaDZNSGRmMXNrQzdJZ3Y0QT09)
-   Sunday October 10 at 2PM EST: iOS Shortcusts for Obsidian with @NanoCourse
-   Saturday October 16 at 1PM EST: [[Create Your Own Obsidian Plugin - How To Get Started]] with `@philbr0` (author of this awesome [blog post](https://phibr0.medium.com/how-to-create-your-own-obsidian-plugin-53f2d5d44046) on the topic).

## Plugin News

### New

-  [[kometenstaub|koala]] graciously picked up `@brimwats` suggestion for a controlled vocabulary plugin. It's called [linked data vocabularies](https://github.com/kometenstaub/obsidian-linked-data-vocabularies) and the idea is to help people lean on pre-existing structured hierarchies to organize their vault along an additional axis from folders, tags, & links. It leverages YAML (or inline metadata) and synergizes with the [[breadcrumbs]] plugin.
-   There's a new plugin to [[obsidian-task-collector|manage completed tasks]] that is particularly good for arranging tasks you're done with.
-   [Code Editor Shortcuts](https://github.com/timhor/obsidian-editor-shortcuts) adds keyboard shortcuts normally found in code editors such as Visual Studio Code or [[Sublime Text]].
-   [URI commands](https://github.com/kzhovn/uri-commands-obsidian) pairs with the [URI scheme](https://help.obsidian.md/Advanced+topics/Using+obsidian+URI) plugin and lets users add custom URI commands to the command palette.
-   [ZH Enhancer](https://github.com/shaggyfeng/Obsidian-ZH-Enhanced-editing) adds a bunch of hotkeys for different syntax combinations.
-   [Obsidian Itinerary](https://github.com/coddingtonbear/obsidian-itinerary) is designed to help make it easier to plan trips using Obsidian.
-   [Ozenshare Publish](https://github.com/ozntel/ozanshare-publish-plugin) lets users publish markdown notes with a single click from the vault. It works with [[obsidian-admonition|admonition]] blocks. Note: it requires the purchase of an access token to work.
-   The [plotly](https://github.com/Dmitriy-Shulha/obsidian-plotly) plugin lets users create line graphs and charts in Obsidian using YAML and JSON.

### Updates

-   [the Linter plugin](https://github.com/platers/obsidian-linter) has been updated with a new user friendly settings UI.
-   [Templater (1.9.1)](https://github.com/SilentVoid13/Templater/blob/master/CHANGELOG.md) has a new built-in feature to bind specific templates to a hotkey and now comes with starter templates. There was also a big refactor.
-   [CustomJS v1.0.10](https://github.com/samlewis0602/obsidian-custom-js) will automatically refresh your dataviews whenever one of your custom scripts is updated, so iterating on your custom scripts is much quicker and easier. Requires the latest version of dataview.
-   [Kanban 1.1.0](https://github.com/mgmeyers/obsidian-kanban/issues) supports native drag & drop.
-   [Excalidraw 1.3.14](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/) lets [users copy](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.3.14) a text element that has a link, and it will retain the link. 1.3.12 had a bunch of bugfixes and lets users specify in settings if they want to embed PNG, SVG or Excalidraw files into documents.
-   [Workspace Plus 0.3.1](https://github.com/nothingislost/obsidian-workspaces-plus/releases/tag/0.3.1) has better support for hotkeys with workspaces.
-   [Text Transporter](https://github.com/TfTHacker/obsidian42-text-transporter) got a big refactor to get it ready for the community plugins list (it's available there now). It lets users quickly selecting lines, blocks and more, along with quickly creating block references.

### Betas

-   [Obsidian Wikipedia](https://github.com/jmilldotdev/obsidian-wikipedia) grabs information from Wikipedia for a topic and brings it into your Obsidian notes.
-   [Obsidian Vale](https://forum.obsidian.md/t/new-plugin-obsidian-vale/24869) is an obsidian client for a style guide checker (as opposed to grammar checker) that's normally a command-line tool. It's kind of like a linter for prose.

### Under The Radar

-   This is the best [explanation](https://discord.com/channels/686053708261228577/707816848615407697/893062280370073611) for what [[supercharged-links-obsidian|Supercharged Links]] I've seen. It allows for visual styling of different kinds of links in a bunch of different ways (including the backlinks panel).

### For Developers

-   `@SV` is looking for an experienced Obsidian plugin developer to help maintain Templater. If you're interested, check out [their update](https://discord.com/channels/686053708261228577/855181471643861002/891702342418858066).
-   `@shabegom` shared how they [develop Obsidian plugins on the iPad](http://discordapp.com/channels/686053708261228577/840286264964022302/890214415205543956).
-   The [new documentation for plugin development](https://marcus.se.net/obsidian-plugin-docs/guides/editor) via `@Marcus Olsson` keeps getting better and better. There's some nice documentation for the `editor` interface now.

## Feature Requests

-   Apparently Grammarly opened up their API. There are definitely folks who would love [a grammarly plugin for Obsidian](https://forum.obsidian.md/t/any-way-to-integrate-grammarly-as-plugin/19050).
-   If you are [interested in having a method for signing up to test beta versions of plugins](https://forum.obsidian.md/t/developer-enhancement-ability-to-have-a-release-and-beta-release-for-a-plugin/24971), head on over and share your use-case in support of the feature request.
-   If you think it would be cool if we could [use search operators for YAML metadata](https://forum.obsidian.md/t/search-operators-for-yaml-metadata/24782) head on over and support this feature request. Or, you know, build a plugin for it ;)

## Appearance

-   Here's a [collection of mobile-friendly themes](https://www.reddit.com/r/ObsidianMD/comments/pxgf40/mobile_friendly_theme/) via Reddit.
-   This [CSS](https://gist.github.com/jplattel/42b57ff52c867e7104bf34f4e925bb94) works with the [[workspaces-plus|Workspaces Plus]] plugin to create custom status-bar styling for visual differentiation between workspaces.

## Ancillary Code

-   `@andreiRS` extended the original zettelizer script to [generate the atomic notes inside a folder with the same name](https://gist.github.com/andreiRS/2310d5e84f4b049d6079ded7488f61f2) as the source document, for easier processing of source notes.

## Guides

-   Here's a guide on [how to read and summarize books](https://www.youtube.com/watch?v=fBl0v-AcAKo) using Obsidian that came recommended on Discord.
-   Here's how to use [Readwise with DataviewJS](https://www.jmill.dev/media-inbox-obsidian-readwise) to generate a dynamic table of unprocessed highlight notes, sorted by most recent.
-   Here's a nice [guide to using VIM keybindings in Obsidian](https://youtu.be/yX_Qdr9-7kg).
-   Here's a new [beginner's guide](https://www.youtube.com/watch?v=ctetnQfSdfM).
-   Here's `@Ramses` of RoamStack on how to [set up Obsidian for maximum interoperability with Logseq](https://twitter.com/rroudt/status/1443546446360313859). Here's a nice video about [how to use Obsidian with Logseq](https://www.youtube.com/watch?v=knxDHO3U2_8) guide. PS: [Logseq has a weekly newsletter now](https://logseqweekly.com/)!
-   Here's how `@zsviczian` builds [visual maps of content using Excalidraw](https://www.youtube.com/watch?v=ML0WQlQgu3w).

## Discussions

-   There was a [discussion about when to break off sections of your notes into folders](https://discord.com/channels/686053708261228577/710585052769157141/893207650769195028) that devolved into some really fun Star Wars puns.
-   Here's a nice discussion on Twitter about [why the Obsidian community is so active](https://twitter.com/rroudt/status/1443625748376526859).

## Knowledge Management

-   This [article about the barbell method of reading](https://zettelkasten.de/posts/barbell-method-reading/) was shared and, gotta admit, it's pretty close to how I do most of my nonfiction reading.
-   Here's a neat example of unexpected benefits of [taking notes on fiction and games](https://discord.com/channels/686053708261228577/805952223124520961/893167257952337921).
-   Remember [Mark McElroy](https://markmcelroy.com/mark-mcelroy-3/), the professional writer using Obsidian to write a novel in public, 3 chapters a week? Go check out [his vault](https://publish.obsidian.md/markmcelroy/Parallel+Lines+-+Map+of+Content) it's definitely matured a lot since the last time I mentioned it here, and it's an excellent exemplar for authors.

## Ancillary Tools

-   [Project Meta](https://projectmeta.app/) is a note-taking tool for visual learning that someone [demonstrated a neat way to use with Obsidian-style notes](https://projectmeta.app/vid/read.mp4).
-   Here's a way to [use Tasker to get quick inputs into Obsidian on Android](https://forum.obsidian.md/t/android-quick-input-for-obsidian/16336) that got resurfaced.

## Housekeeping

-   I found this awesome explanation about why it's best to [just ask your question](https://dontasktoask.com/) instead of asking "can I ask a question" or "does anybody know anything about this thing." It pairs nicely with this twitter thread I wrote about [my guidelines for beta-testing and bug-reporting](https://twitter.com/EleanorKonik/status/1443616759441920001).
-   If anybody wants to adapt the current roundup theme to have a JavaScript button to have a dark mode option like my newsletter [The Iceberg](http://newsletter.eleanorkonik.com/) does, I'm happy to send over the files — I just haven't been able to figure it out. In the  meantime, `@Optional#4159` made this [dark theme](https://userstyles.world/style/1266/obsidian-roundup-dark).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-10-02%20%20Premade%20Concept%20Hierarchies%20%26%20a%20Virtual%20Community%20Meeting%20Space.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-10-02%20%20Premade%20Concept%20Hierarchies%20%26%20a%20Virtual%20Community%20Meeting%20Space.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
