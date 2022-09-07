---
link: https://www.obsidianroundup.org/2021-07-17/
author: Eleanor Konik
published: 2021-07-17
publish: true
---

# 2021-07-17: Obsidian Mobile, Community Events & Graph Tips
I'm doing an AMA. There's a new plugin for better logseq/obsidian interoperability. QuickAdd macros are incredible. TTRPG stuff & new themes!

## In The Community

- I’ll be joining Nick Milo for the inaugural [[LYT House]] feature, with a grand reveal of my (sanitized) vault for people to see. We’ll probably talk about managing writing projects and tasking, but the thing I’m most excited about is the 30-minute “Ask Me Anything” portion. It’ll be held on [Zoom](https://www.linkingyourthinking.com/lyt-house) at [10AM PT (UTC-7) on Sunday, July 18th](https://everytimezone.com/s/5f50ccb7).
- If you have ideas to improve the Obsidian documentation, **pull requests are welcome**. You can contribute to the process of [documenting Obsidian on GitHub](https://github.com/obsidianmd/obsidian-docs)
- `@nickmilo` shared this really heartwarming [Love Letter to Obsidian](https://www.youtube.com/watch?v=ho1EfhXQ8iE&feature=youtu.be) that some Discord users recorded made them tear up a bit.
- Paul Bricman is organizing a one-day online “unconference” about building tools for thought where participants host their own sessions (a bit like the community talks). It’s free on July 25th. Learn more [here](https://opencollective.com/psionica/events/augment-minds-7d13842a)
- `@Silverica` is looking for community members to contribute T-shirt designs for Obsidian merch 👀 Details on [Discord](http://discordapp.com/channels/686053708261228577/700466324840775831/865612406323281940).
- there's a [Japanese subreddit](https://www.reddit.com/r/ObsidianMD_Japanese/) now.

## Obsidian Updates

The big news this week is that **obsidian for mobile has released!** This brought a whole host of questions about best practices and methods for syncing files between different devices. I’ve put together a meta list of all the [resources for sync](https://forum.obsidian.md/t/meta-post-syncing-between-devices/20983) and advice I was able to find.

Other tips include: if startup time feels like it’s taking too long, try:

- lock the app so that it doesn’t get killed.
- let the app run in the background
- check to see if your plugins are causing long load times.
- Make sure you don’t have any “markdown” files that are actually long files of another type, like xml. This can sometimes cause the parser to choke.
- Make sure you don’t have any illegal characters in your filenames. Different operating systems have different requirements, but `?` and `%` have been common culprits.

Insiders will continue to get access to early beta builds and features.

## Plugin News

### New

- The new [[obsidian-timeline|Timeline]] plugin looks incredible for having a timeline of stuff in one file. It uses codeblocks.
- This plugin [makes Obsidian’s preview of LogSeq-flavored markdown more pleasant](https://github.com/ruivieira/obsidian-plugin-logseq).
- The new [[obsidian-map-view|Map View]] plugin is in the community plugins list. It’s a great way to work with notes on vacation notes, reflections on places you’ve visited, etc. Although by default it works with coordinates, `@Christian` put together a [QuickAdd macro](https://github.com/chhoumann/quickadd/blob/master/docs/Examples/Macro_AddLocationLongLatFromAddress.md) (seriously, [[quickadd]] is amazing) to find the longitude and latitude for the given address and creates a YAML property called location in the active file.
- You can now easily [open your vault in Visual Studio Code](https://forum.obsidian.md/t/open-vault-in-vscode-plugin/20963) from a ribbon icon, which should make stuff like mass find&replace easier.
- Here’s a nifty way to [paste a multi-line code block or blockquote to the level of indent you’re at](https://github.com/publicus/obsidian-paste-to-current-indentation).

### Updates

- [[Linux Tools|Linux]]-only: The [Ulauncher plugin for obsidian](https://github.com/mikebarkmin/ulauncher-obsidian) now supports direct access to Daily Note and Quick Capturing.
- The [[obsidian-excalidraw-plugin|Excalidraw]] plugin has a nice [video walkthrough](https://www.youtube.com/watch?v=sY4FoflGaiM) of the big 1.2.1 update: This is a major release moving Excalidraw to [[Markdown]] and implementing linking, transclusion, aliases, tagging, backlinking, etc. feature set into Excalidraw.
- [[file-tree-alternative|File Tree Alternative Plugin]] [version v.1.2.7](https://github.com/ozntel/file-tree-alternative/releases/tag/1.2.7)allows users to use keyword `all:` which helps with searching all files under the vault rather than the currently active folder.
- [[obsidian-imgur-plugin|Imgur Plugin]] [2.0](https://github.com/gavvvr/obsidian-imgur-plugin/releases/tag/2.0.0) now allowed users to authenticate and upload images tied to their account.
- [[quickadd]] [0.3.5](https://github.com/chhoumann/quickadd) adds support for inline JavaScript execution. It also supports syntax highlighting out of the box.
- [[breadcrumbs]] [0.8.15](https://github.com/SkepticMystic/breadcrumbs) now has a grid view and is in the community plugins list now after getting through code review. I am very excited to start using this to mimic folgezettels, personally.
- [[obsidian-advanced-uri|Advanced URI]] now supports opening files by UUID.
- Version 0.3.0 of [[obsidian-amazingmarvin-plugin|Amazing Marvin]] plugin adds a ribbon, more support for bringing tasks into your daily notes in Obsidian, and more customizations.
- the [[initiative-tracker|Initiative Tracker]] plugin lets you add players, create homebrew creatures, and run a combat from within Obsidian, and includes the full 5e SRD creature list.

### Under The Radar

- For those who have gotten used to the handy way that the mobile toolbar can cycle between `-` and `- [ ]` and `- [x]` don’t forget that [[hotkeysplus-obsidian|Hotkeys++]] exists and lets you do something similar on desktop.

### For Developers

- Obsidian will be adding a native bypass for `navigator.clipboard.readText/writeText` on mobile to make it work; the bypass itself just replaces `readText/writeText` so no new API will be introduced.
- There’s a lengthy discussion over on the GitHub repo for [[obsidian-git|Obsidian Git]] about the [challenges of getting obsidian git working on mobile](https://github.com/denolehov/obsidian-git/issues/57). If anybody has any insight or wants to help out, I think it would be appreciated by a lot of people.
- The developer of the [[better-word-count|Better Word Count]] plugin is a bit swamped by the [issues facing their home country](https://discordapp.com/channels/686053708261228577/840286238928797736/865188193560559677) and requested that if anyone is able to submit a pull request to help with the issue where [wordcounts are unusually high](https://discordapp.com/channels/686053708261228577/840286238928797736/864548416093028352).
- [Obsimian](https://github.com/motif-software/obsimian) is an Obsidian simulation framework for integration testing Obsidian plugins without an actual Obsidian App instance.
- If you’re trying to [debug Obsidian using Android](https://forum.obsidian.md/t/debugging-obsidian-mobile-plugins/20913) you can use [Android Debug Bridge](https://developer.android.com/studio/command-line/adb). It’s a lot harder on iOS.

## Workflow Stuff

- Here’s an explanation for [how to add shortcuts to notes to your Android homescreen](https://forum.obsidian.md/t/how-to-add-a-note-shortcut-to-the-homescreen-on-android/20889)
- `@viticci` is sharing his Obsidian workflow today in his newsletter. He also discusses the release of the mobile app on [Connected](https://overcast.fm/+FXx6_WZ-Y) at 14:54.
- Here’s a great thread about how to [use Logseq as your outliner for Obsidian](https://discuss.logseq.com/t/making-obsidian-play-nice-with-logseq/1185).
- `@Christian` the developer of [[quickadd|QuickAdd]] and [[metaedit|MetaEdit]] shared how he semi-automatically imports literature notes to his Obsidian vault and his workflow for [processing them](https://bagerbach.com/blog/how-to-take-smart-book-notes-in-obsidian/) into atomic, evergreen notes. He also shared how he [captures what he wants to include in his newsletter](http://discordapp.com/channels/686053708261228577/805952223124520961/863758164297777183).
- `@Christian` also helpfully put together a [“how-to” guide]((https://github.com/chhoumann/quickadd/blob/master/docs/Examples/Macro_Zettelizer.md) for my [Zettelizer workflow with QuickAdd](http://discordapp.com/channels/686053708261228577/722584061087842365/864533595212480512) which I use to automatically create atomic notes from source notes using descriptive headers.
- This [[quickadd]] script to [quickly capture a task and add it to a kanban](https://github.com/chhoumann/quickadd/blob/master/docs/Examples/Capture_AddTaskToKanbanBoard.md) is also pretty nifty.
- [Effective Remote Work](https://www.youtube.com/watch?v=oETBOXhdGPs&feature=youtu.be) has a new video about how effective Obsidian is for productivity and task management.
- Folks using [[Obsidian and TTRPG|Obsidian for TTRPG]] games should check out this [detailed discussion post](https://github.com/valentine195/obsidian-leaflet-plugin/discussions/130) on the [[obsidian-leaflet-plugin|Obsidian Leaflet]] plugin GitHub repository. It image maps easier to work with. It also discusses parameters you can use to automatically place markers defined in your notes, and a discussion of how to use GeoJSON to create features on your map.
- If you're looking to organize a campaign, this video](https://www.youtube.com/watch?v=tdDFlSJtUIU is useful. For an example of campaign notes from a player perspective, check out the newest mod `@Leah`'s [vault](https://publish.obsidian.md/leah/60+Games/62+Two+and+a+Half+Strahds/62.00+Two+and+a+Half+Strahds) There’s also this excellent [D&D Reference for Obsidian](https://github.com/twisterghost/5e-obsidian) and a great discussion about [how to use collapsible admonitions for branching choices](https://discord.com/channels/686053708261228577/805952223124520961/865659802502823936).
- `@hstagner` shared their workflow for getting [emails into your vault](https://twitter.com/hstagner/status/1414578734703816706) using [[Zapier]].
- `@alex_the_glad_stork` shared a [workflow for managing meeting notes and using anki flashcards in documents](https://discordapp.com/channels/686053708261228577/709712341066842113/865177908241498122) on Discord.

## Feature Requests

## Appearance

- The new [[Illusion]] theme (optimized for light mode) is absolutely gorgeous. Its primary benefit is that things are a bit bigger with better contrast.
- [[California Coast]] theme got some major updates including better mobile support.
- A couple of people have asked for a “Getting Started” guide for making CSS themes for Obsidian. [Reggie has one](https://publish.obsidian.md/reggienotes/Quickstart+CSS+Guide/010+Obsidian+CSS+Themes) over on Publish.
- `@mgmeyers` shared a [method](https://discord.com/channels/686053708261228577/702656734631821413/865318907832172555) to define the shape of icons using css and `web-mask-image` that will work a bit better than `aria-label`s to replace svgs. This lets theme developers swap out icons without needing users to download the icon swapper plugin and download icon files, which should let theme developers do more with icons on mobile too.
- If you want a custom font on mobile, you can [Base64 encode the font](https://transfonter.org/) into your theme. You can't refer to other files from css snippets directly - relative links won't work there because the files are loaded as a blob instead. Once you’ve encoded the font, copy it into the theme file and change fonts wherever you want either in the theme file itself or through one of the plugins.
- the [[Everforest]] theme [has been updated](https://forum.obsidian.md/t/theme-everforest-dark-light-theme/20139)
- There’s a new theme called [[Darkyan]].

## Knowledge Management

- I thought you guys might enjoy this piece from r/askHistorians about the [history of notetaking](https://www.reddit.com/r/AskHistorians/comments/oi3x16/how_did_university_students_take_notes_during/) How far we’ve come!
- `@Calhistorian` shared this Loom [prototyping a method for organizing a Zettelkasten in Obsidian that demonstrates the utility of the graph view](https://twitter.com/calhistorian/status/1415396711988535296?s=20) for more than just a "map" of your Vault. It impressed a lot of prominent thinkers. It’s meant as a [demonstration to show how a linear exploration might occur through a note sequence](https://www.loom.com/share/1143aa8d5153417387d751bbcfda027a): you might follow different branches of the note sequence by following tags and folgezettels, and related notes. ^9d3b2a
- `@Cat` (who put together the directions for the [[Zotero]]/[[Mdnotes]] workflow) shared a [snapshot of their indicies and metadata](http://discordapp.com/channels/686053708261228577/722584061087842365/864508091725512704).
- There was a nice [discussion of why atomic notes are helpful](https://discordapp.com/channels/686053708261228577/694233507500916796/865383608369545256) in the Discord.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- Several people asked about tools for sharing and collaboratively editing and commenting on markdown files. [HackMD is a Collaborative Markdown Knowledge Base](https://hackmd.io/) and [HedgeDoc](https://hedgedoc.org/) is an open-source alternative.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-07-17%20Obsidian%20Mobile%2C%20Community%20Events%20%26%20Graph%20Tips.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-07-17%20Obsidian%20Mobile%2C%20Community%20Events%20%26%20Graph%20Tips.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
