---
link: https://www.obsidianroundup.org/2022-03-12/
author: Eleanor Konik
published: 2022-03-12T13:30:00
publish: true
---

# 2022-03-12: Pin Preview Popups & an Intro to Dataview Guide
Tags, glossaries, & beginner-friendly classification methods. 

## In The Community

-   The [Apply Patterns](https://github.com/jglev/obsidian-apply-patterns-plugin) plugin lets users search & replace with regex. Ben Hamilton is trying to encourage users to create a [gallery of patterns](https://github.com/jglev/obsidian-apply-patterns-plugin/discussions/43) to help users understand the value; if you have something to contribute, please consider adding your own examples.
-   Some folks on Reddit are trying to collect [printable learning guides](https://www.reddit.com/r/ObsidianMD/comments/t9msb3/anybody_have_useful_obsidianmarkdown_printables/) for Obsidian and markdown.
-   We just passed [the 500 plugin mark](https://obsidian.md/plugins)! Thank you to all the wonderful developers who have helped build the Obsidian ecosystem.

### Hub

The Obsidian Hub is a community knowledge base designed to help organize information about the Obsidian ecosystem. It's an excellent companion to this Roundup, which tends to be very chronological in nature. Here are some of the [recent updates](https://github.com/obsidian-community/obsidian-hub/pulls?q=is%3Apr+is%3Amerged+sort%3Aupdated-desc+-label%3A%22scripted+update%22+-label%3A%22hub+tools+%26+scripts%22+%3E+):

-   There's a new [index for spaced repetition plugins](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.01+Plugins+by+Category/Spaced+Repetition+Plugins).
-   Here's a new overview about [pitfalls of using Obsidian for protected health information](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/HIPAA+Requirements+and+Obsidian+Primer)
-   Here's a really helpful [introduction to dataview](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview).
-   There's a new [iOS Shortcuts index](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.04+Auxiliary+Tools+by+Category/iOS+Shortcuts).

If you'd like to help out with the project, check out the [good first issue](https://github.com/obsidian-community/obsidian-hub/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) tasks or, for example, search the Roundup archives for "iOS shortcuts" and add them to the index above.

## Obsidian Updates

-   Obsidian got a major update from Electron 13 to 16, please grab [the latest installer](https://obsidian.md/) from the website, not just in the app. Insider builds were mostly bugfixes, but you can check the [release notes](https://forum.obsidian.md/c/announcements/13) on the forum.

## Plugin News

### New in Community Plugins

_A bunch of plugins went through code review and are now available in Obsidian's plugin list. Licat had a busy week! Here are some highlights, but for the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new)._

-   [Extract PDF Annotations](https://github.com/munach/obsidian-pdf-annotations) by `@munach` extracts PDF Annotations (Notes and Highlights) and sorts them by topics
-   [File Cleaner](https://github.com/Johnson0907/obsidian-file-cleaner) by `@Johnson0907` helps you to clean empty files in the vault.
-   [Kindle](https://github.com/SimeonLukas/obsidian-kindle-export) by `@SimeonLukas` lets users send `.md` files as `.mobi` to Kindle.
-   [Steemit](https://github.com/anpigon/obsidian-steemit-plugin) by `@anpigon` helps with publishing Obsidian documents to Steemit, a blockchain-based blogging and social media website.
-   [Text Generator](https://github.com/nhaouari/obsidian-textgenerator-plugin) by `@nhaouari` uses OpenAI to "finish" texts based on inputs. Here are [some examples](https://github.com/nhaouari/obsidian-textgenerator-plugin/blob/master/recipes.md).
-   [Full Calendar](https://github.com/davish/obsidian-full-calendar) by `@davish` lets you create a "proper" calendar in Obsidian, complete with connections to your notes.
-   [Digital Garden](https://github.com/oleeskild/obsidian-digital-garden) by `@oleeskild` is a new third party publish option with a handy guide. It supports transclusions, code blocks, admonitions, and footnotes.
-   [Remember File State](https://github.com/ludovicchabant/obsidian-remember-file-state) by `@ludovicchabant` remembers your cursor position, selection, and scroll location after you navigate away.
-   [Todoist Text](https://github.com/wesmoncrief/obsidian-todoist-text) by `@wesmoncrief` integrates Todoist tasks with markdown checkboxes.

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Novel word count](https://github.com/isaaclyman/novel-word-count-obsidian) by `@isaaclyman` displays a word or page count for each file, folder and vault in the file pane. I was surprised how useful I found this for deciding what to work on next.
-   [Card View Switcher](https://github.com/qawatake/obsidian-card-view-switcher-plugin) by `@qawatake` is an alternate quick switcher that has a card view so users have more context when searching files.

### Updates

_If you want a more comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

-   [Settings Search](https://github.com/valentine195/obsidian-settings-search/releases) can now open directly to the setting you searched for, instead of just the plugin that has the setting.
-   [Banners](https://github.com/noatpad/obsidian-banners/releases/tag/1.3.1) now supports Live Preview. You can also lock banners in place.
-   [Icon Shortcode v0.8.3](https://github.com/aidenlx/obsidian-icon-shortcodes/releases/tag/0.8.3) supports the new icon packs, live preview, and loads faster.
-   Smart Typography, Indentation Guides, and LanguageTool now have mobile support.
-   The [Backend for Sekund](https://github.com/Sekund/realm-backend) is now open source. If you're interested in how to use it, [contact the developer](https://twitter.com/sekund_io/status/1501549226630778882).

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   [Hover Editor](https://github.com/nothingislost/obsidian-hover-editor#features) enhances the core Page Preview plugin by **turning the popover into a fully functional editor instance** which can be dragged, resized, and **pinned** to the workspace. It is _incredible_.
-   Here's a way to access the [Obsidian Sync version history](https://github.com/kometenstaub/obsidian-sync-version-history) over the command palette/with a hotkey. The dev isn't likely to submit to the community list, but it would be wonderful if someone could figure out how to add it to the Hotkeys++ plugin as a pull request...

## Appearance

-   [Primary](https://github.com/ceciliamay/obsidianmd-theme-primary/releases/tag/v.1.3.1) got some nice bugfixes and redesigned panes.
-   [Willemstad](https://github.com/tingmelvin/willemstad-x/releases/tag/v0.2.4) added support for the Full Calendar plugin, and improvements to a bunch of modals and panes.
-   [Cardstock](https://github.com/cassidoo/cardstock) now has a dark mode option.

## Guides

-   Here's a guide on how to do [card-based writing outlines using the Kanban plugin](https://www.workings.tools/p/card-based-writing-in-obsidian-using?s=w), with a good overview of the benefits and limitations.
-   Tracy Winchell wrote [a tutorial and a template](https://twitter.com/tracyplaces/status/1499080517286834176) to demonstrate how the "note to next day self" journaling technique works.

## Discussions

-   I participated in a great discussion about why taking notes on messy concepts like "democracy" and "oligarchy" and "Phoenician identity" can be difficult, and how very specific notes focused on the questions and problem spaces can help. You can [listen to the recording](https://twitter.com/bianca_oli_per/status/1500524483391672328) if you're interested in learning more about history timelines & the difficulties of classification.
-   Here's a handy discussion about [best practices for iCloud on Windows](https://www.reddit.com/r/ObsidianMD/comments/ta3ba5/obsidian_slow_to_load_workspace_and_indexing/) to help troubleshoot slow loading and other problems.
-   Here's a discussion about [using Obsidian for cybersecurity work](https://www.reddit.com/r/ObsidianMD/comments/t7ewmx/obsidian_for_cybersecurity_work/).
-   Here's a discussion about [the limitations of Obsidian as a team wiki](https://www.reddit.com/r/ObsidianMD/comments/t98p1a/is_obsidian_stable_enough_for_a_small_business/).
-   Here's a pretty good discussion about [practical ways to use tags](https://www.reddit.com/r/ObsidianMD/comments/t9gf6c/practically_paperless_with_obsidian_episode_21/) and the struggle to create a good tagging taxonomy.
-   Here's a discussion about different ways to manage a [glossary in Obsidian](https://www.reddit.com/r/ObsidianMD/comments/t9eow3/is_there_some_sort_of_a_glossary_plugin/).
-   Here was a good one about [how to denote ideas you disagree with in your notes](https://forum.obsidian.md/t/what-if-i-disagree/33677/9).

## Events

-   Nick Milo will be giving a presentation called [The Joy of Thinking and the Rise of the Note Maker](https://lu.ma/84yf2gzu) as part of Tiago Forte's free, virtual [Second Brain Summit](https://www.secondbrainsummit.com/). The Summit is March 14-18. Nick's presentation will be Fri, March 18 at 12 pm ET. Dan from Readwise will also be presenting on Wed, March 16 at 12 pm ET.

## Knowledge Management

-   An archivist wrote a guide for a [simple way to categorize things in your vault that is designed to grow in complexity as your notes do](https://forum.obsidian.md/t/cut-ter-away-the-chaos-of-your-vault-with-this-one-two-three-four-five-six-simple-method/33700).
-   Here's a neat visual for [how to track team interests](https://twitter.com/dasaptaerwin/status/1500354351159603201).

## Ancillary Code

-   Here's [a QuickAdd macro](https://gist.github.com/davish/90935658e1a43dc4e0e22e61b3eaf2eb) that pulls in github issues from a github repository specified in the `gh-repo` frontmatter on the current file and formats them in a list.

## Ancillary Tools

-   [The Sample](https://thesample.ai/?ref=9937) is my favorite way to find niche, high-quality newsletters written by real people. They just added a neat new feature; now instead of just getting one algorithmically selected newsletter in your inbox each morning, they have a "show a random newsletter" page where you can get on-demand recommendations.

## In The Wild

-   The [Obsidian Icon was spotted at the Apple Event](https://twitter.com/leahthedesigner/status/1501272834286526469).

## Housekeeping

Last week's Roundup got emailed to over 4,000 people. When I originally started this project, I only thought about 30 of the most active people hanging out in Discord would read it — and even then, I assumed it would only get used for catching up after things like illnesses and vacations.

Knowing that so many of you get so much value out of the Roundup is incredibly motivating. Thank you all for your kind words, encouragement, and support 💚

[SUPPORT MY WORK](https://www.obsidianroundup.org/#/portal/signup)

Next Thursday is the third Thursday of the month, which means I'll be sending a new supporters-only article. Continuing my theme of pushing back against popular wisdom, this month the topic is the value of creating an index of quality resources, _even if you never have time to read them_.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-03-12%20Pin%20Preview%20Popups%20%26%20an%20Intro%20to%20Dataview%20Guide.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-03-12%20Pin%20Preview%20Popups%20%26%20an%20Intro%20to%20Dataview%20Guide.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
