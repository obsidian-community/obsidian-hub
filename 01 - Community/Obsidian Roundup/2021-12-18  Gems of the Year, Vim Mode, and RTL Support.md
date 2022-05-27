---
link: https://www.obsidianroundup.org/2021-12/
author: Eleanor Konik
published: 2021-12-18T13:30:00
publish: true
---

# 2021-12-18: Gems of the Year, Vim Mode, & RTL Support
There's a new sample plugin for the Codemirror 6, which developers can now access the API for.

## In The Community

-   Check out the [pinned Meta posts](https://forum.obsidian.md/c/meta/16) at the forum to see how the Gems of the Year event is going.

## Obsidian Updates

### [Insider 0.13.8](https://forum.obsidian.md/t/obsidian-release-v0-13-8-insider-build/28329/2)

-   [[Obsidian Sync]] now has a bulk restore functionality for deleted files.
-   “Preview mode” has been renamed to “Reading view” to avoid confusion.
-   Vim mode is now available for both Live Preview and Source mode.
-   You can now set the default editing mode to Live Preview or Source Mode.
-   Completed task lists are now crossed out and greyed out to match reading view.
-   Improved handling of up/down arrow keys interacting with blocks like embeds and code blocks.

### [Insider 0.13.9](https://forum.obsidian.md/t/obsidian-release-v0-13-9-insider-build/28550)

-   Empty headings will now keep the `#` characters in view to help see that it’s an empty heading.
-   Markdown formatting commands now ignores whitespace characters at the beginning or ending of the selection when being applied.
-   Backlink in document can now be turned on by default in the settings page of the core plugin “Backlinks”

### [Insider 0.13.10](https://forum.obsidian.md/t/obsidian-release-v0-13-10-insider-build/28622)

-   Added basic RTL (right-to-left) text support. The option can be found in Settings > Editor.
-   Internal links that start with # for heading sections will now hide the # when not selected to avoid confusion with tags.

## Plugin News

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

### New

-   [File Info Panel](https://github.com/CattailNu/obsidian-file-info-panel-plugin) creates a small File Info view that displays the active file's date created, date modified, file size, and links to open the file in its native application and to open the file's folder
-   The [emotion picker](https://github.com/dartungar/obsidian-emotion-picker) is designed to provide an easier way to add entries to daily journal, emotions / mood tracker, etc.
-   You can now [render your plantuml diagrams locally](https://github.com/joethei/obsidian-local-plantuml)
-   If you ever wanted to use a controlled vocabulary that already exists so you don't have to come up with your own categories, check out the [Linked Data Vocabularies](https://github.com/kometenstaub/obsidian-linked-data-vocabularies) plugin. You'll need the [helper plugin](https://github.com/kometenstaub/linked-data-helper) to install it.

### Updates

-   `@javalent` updated Initiative Tracker so you can use dice for amounts in encounters, re-order initiative with drag&drop, and added some nifty stuff to work with the TTRPG statblocks plugin.
-   [Code Editor Shortcuts](https://github.com/timhor/obsidian-editor-shortcuts/releases/tag/1.4.0) has shortcuts to jump to the next/previous heading or select the word under the cursor.
-   [Style Setting 0.4.3](https://github.com/mgmeyers/obsidian-style-settings/issues)  now allows editing style settings in a new pane. This means you can now see your changes in real time
-   [Embedded note titles](https://github.com/mgmeyers/obsidian-embedded-note-titles/issues) now supports Live Preview.
-   Cooklang 0.3.0 support the latest spec, and has clickable timers that can play sound.
-   [Various Complements v3.3.0](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/3.3.0) can now cycle thru suggestions and add newlines (`\n`) and tabs (`\t`) to the custom dictionary.
-   [Smart Typography](https://github.com/mgmeyers/obsidian-smart-typography/) was updated to work in Live Preview.
-   Leaflet now has the ability to specify additional tile servers as overlays on the base map now. This lets you add something like OpenRailMap as an overlay you can toggle on and off.
-   [RSS Reader](https://github.com/joethei/obsidian-rss) has support for youtube and importing feeds as OPML, and got a bunch of bugfixes.

### Betas

-   [Emails](https://github.com/SkepticMystic/email-templates) is a plugin that imports `.eml` files into your vault using a customizable markdown template.
-   The [auto linker](https://github.com/nothingislost/obsidian-auto-linker) lets users create links to `[[aliases]]` instead of always needing to write `[[reallink|alias]]`. Here was [the feature request](https://forum.obsidian.md/t/plugin-to-match-pre-existing-wiki-links-to-pre-existing-aliases-of-the-same-name/28575) if you're curious about the use-case.
-   [Big Calendar](https://github.com/Quorafind/Obsidian-Big-Calendar) can fetch all tasks and journal from dailynotes and show them in a big calendar view (similar to fantasy calendar). It supports month/week/day/agenda views.

### For Developers

-   Here's a [reference plugin for CodeMirror 6](https://github.com/nothingislost/obsidian-cm6-zoom)
-   Breaking change: the data-task css class has been moved to the line element, rather than being on each piece of `<span>`.
-   The API for CodeMirror 6 has now been opened up. To deeply integrate with CodeMirror 6, you will be required to write an Extension to augment the editor. More details and tutorials will be available later.

## Feature Requests

-   People would like to [set & forget backlinks on different folders](https://forum.obsidian.md/t/option-to-set-and-forget-backlinks-on-different-folders/28584)
-   Some folks would like to use [Obsidian to manage headless sync](https://forum.obsidian.md/t/possibility-for-headless-syncing-with-a-cli/26162).

## Guides

-   Here are some tips for [migrating from Bear](https://reddit.com/r/bearapp/comments/rftc7d/_/hogq844/) that tries not to get too far into the weeds.
-   Here's a great template to use when [reviewing literature](https://discord.com/channels/686053708261228577/771575014382108672/920622085141827604) in Academia.
-   Here's a guide for [how to add shortcuts to notes to your Android homescreen](https://forum.obsidian.md/t/feature-android-features-shortcuts-widgets/19402/3)
-   How `@pdworkman` manages [a prolific novel writing career with Obsidian](https://pdworkman.com/writing-a-novel-in-markdown/).
-   Here's a [neat flowchart](https://publish.obsidian.md/tim/40_Evergreens/my+TO(DO)+and+EVER(GREEN)+structure) about assigning status to evergreen notes.
-   Here's a [list of plugins relevant for TTRPG](https://www.patreon.com/posts/59873493).
-   Here's a really nice writeup about how to decide whether to use [links vs. tags](https://forum.obsidian.md/t/a-guide-on-links-vs-tags-in-obsidian/28231)

## Appearance

-   [Things v1.5](https://twitter.com/colineckert/status/1470250265882226690) has improved support for Live Preview.

## In The Wild

-   Obsidian is the [2021 App of the Year](https://www.macstories.net/stories/macstories-selects-2021-recognizing-the-best-apps-of-the-year/#app-of-the-year) for MacStories.

## Ancillary Tools

-   Here's a new proof of concept tool for [automatically making text highlights stand-alone](https://paulbricman.com/thoughtware/decontextualizer)

### iOS/Mac Only

-   [Raycast](https://www.raycast.com/marcjulian/obsidian) is an Alfred alternative that people have been describing as being a bit more intuitive and easy to use.
-   The folks at [Matter](https://getmatter.app/) shared a [how-to guide](https://www.loom.com/share/a86707aff6854e5da5a5b60d6f3fdd04) for how to use their read later app with their new Obsidian plugin.

## Housekeeping

-   I am at Worldcon 2021 and wrote this on Wednesday on a couch with hotel wifi, so this edition is probably not up to my usual standards, sorry! Next week is Christmas, so I should be able to get caught up then.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-12-18%20%20Gems%20of%20the%20Year%2C%20Vim%20Mode%2C%20and%20RTL%20Support.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-12-18%20%20Gems%20of%20the%20Year%2C%20Vim%20Mode%2C%20and%20RTL%20Support.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
