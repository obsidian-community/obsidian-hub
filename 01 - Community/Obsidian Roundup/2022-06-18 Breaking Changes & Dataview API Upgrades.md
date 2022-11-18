---
link: https://www.obsidianroundup.org/2022-06-18/
author: Eleanor Konik
published: 2022-06-18T12:30:00
publish: true
---

# 2022-06-18: Breaking Changes & Dataview API Upgrades
Multiple windows is now a core feature, allowing for improved dual monitor use of Obsidian. There's also a great new beginner's guide to Dataview.

## In The Community

-   It's moderator `@argentum`'s two year anniversary of using Obsidian. Check out [her graph](https://discord.com/channels/686053708261228577/744933215063638183/986956536976924693) in Discord.

## Obsidian Updates

-   The Obsidian team expanded! Based on this [Discord message](https://discord.com/channels/686053708261228577/702717892533157999/986349167582531675) it looks like Liam, long-time moderator and the developer of Calendar and Periodic Notes, is now officially an Obsidian employee.
-   [Insider 0.15.0](https://forum.obsidian.md/t/obsidian-release-v0-15-0-insider-build/38948) is a pretty major update that brings coveted new functionality: the ability to create multiple windows of the same vault. A few months ago `@javalent` wrote a hacky plugin to allow this, but having it in core allows for a lot more neat tricks, like the window title including the active file name. 0.15.0 also merged the account and about tabs, allows for checking for theme updates, cleaner delineation between core and community plugins in the settings tab, and various improvements I'm sure mac users will care about. Note that some of the new features and changes to make this necessary busted a handful of plugins, so make sure you update your plugins and keep a sharper eye out than normal. If you need a rollback guide, here's a quick [one in Discord](https://discord.com/channels/686053708261228577/711427230143742022/987733175809757265).
-   [Insider 0.15.1](https://forum.obsidian.md/t/obsidian-release-v0-15-1-insider-build/39021) was mostly bugfixes, but there's now keyboard navigation for the tag pane, more mac improvements, and vim mode improvements for ghost characters.

## Plugin News

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Obsidian Sage](https://github.com/Exr0nProjects/obsidian-sage) by `@Exr0n`  allows for interactive Sage Math in Obsidian with sagecell server, Live Preview, and custom code blocks.
-   [Google Calendar and Contacts Lookup](https://github.com/ntawileh/obsidian-google-lookup) by `@ntawileh`  lets users import contact and calendar event information from a Google account.
-   [Zotero Bridge](https://github.com/vanakat/zotero-bridge) by `@MunGell` is another Zotero integration.
-   [Obsidian better Internal Link Inserter](https://github.com/salmund/obsidian-better-link-inserter) by `@salmund`  allows users to use the selected word as an alias in link suggestion.
-   [Code Block](https://github.com/paddan/code-block-plugin) by `@paddan`  converts text into code blocks with automatic language detection.
-   [PostgreSQL Obsidian](https://github.com/clouedoc/postgresql-obsidian) by `@clouedoc`  will upload note metadata to a PostgreSQL database. I'm pretty sure that this means that if you ever wanted to do _real_ mysql-esque queries on your dataview-optimized metadata, you can now. This, along with the [SQL Powered Tasks Fork](https://github.com/sytone/obsidian-tasks-x/releases/tag/2.3.0) is starting to make me think I should learn more about SQL...
-   [Wielder](https://github.com/victorb/obsidian-wielder) by `@victorb`  lets you run Clojure scripts inside your Obsidian documents, similar to how Templater lets you do JavaScript. Here's the [introduction tutorial](https://wielder.victor.earth/Tutorials/01-Introduction).

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

-   You can now [execute arbitrary Dataview queries via the Dataview API](https://github.com/blacksmithgu/obsidian-dataview/issues/374) (as of 0.5.32).  Incidentally, [dataview development has continuous integration and build costs](https://github.com/sponsors/blacksmithgu), so do consider financially supporting `@blacksmithgu`'s tremendous work on this plugin.
-   [Another Quick Switcher plugin v4.14.0](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/4.14.0) now has numbers for quicker result selection and added a "hide gutter icons" option.
-   [Obsidian Rewarder](https://github.com/Gnopps/obsidian-rewarder) allows users to ignore unwanted rewards, add images to rewards, and log all completed tasks to a daily note.
-   [Tasks Plugin 1.8.0](https://github.com/obsidian-tasks-group/obsidian-tasks/releases/tag/1.8.0) got a dependencies update, so make sure to restart Obsidian after you update (This is a good habit to be in anyway, honestly), a [sample vault](https://github.com/obsidian-tasks-group/obsidian-tasks/tree/main/resources/sample_vaults/Tasks-Demo), and new date abbreviations. Here's a [quick reference](https://obsidian-tasks-group.github.io/obsidian-tasks/quick-reference/) for Tasks and a [discussion about workarounds for OR combinations of filters](https://github.com/obsidian-tasks-group/obsidian-tasks/discussions/746).
-   [Media DB Plugin - 0.3.0](https://github.com/mProjectsCode/obsidian-media-db-plugin) added bulk importing, the ability to select multiple results at once, and a bugfix.
-   Obsidian Social (Sekund), which lets users share notes with other people and get comments, [now works on mobile](https://forum.obsidian.md/t/obsidian-social-sekund-now-works-on-mobile/39046?u=ryanjamurphy).
-   [Smarter Markdown Hotkeys](https://obsidian.md/plugins?id=obsidian-smarter-md-hotkeys) allows you to increase heading levels, toggle readable line length, toggle line numbers, and `toggle Between CASES`.
-   [Theme Design Utilities](https://obsidian.md/plugins?id=obsidian-theme-design-utilities) makes it easier to toggle between your installed themes.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   [Obsidian Translate](https://github.com/Fevol/obsidian-translate/releases/tag/1.0.1.1) integrates with 5 different translation APIs to translate text after automatically identifying the text's language. There's also a neat custom view.
-   The [Meta Bind](https://github.com/mProjectsCode/obsidian-meta-bind-plugin) plugin (which I almost typo'd as "mind bend," whups) can create input fields inside notes and bind them to metadata fields.

### For Developers

-   CodeMirror 6.0 is finally stable. That means we’ll be migrating from CM6 v0.19 (aka v6.0-beta) to v6.0 soon. The migration will have some breaking changes, but Licat helpfully put together this [migration guide](https://forum.obsidian.md/t/plugin-developers-codemirror-6-migration-guide-for-v6-0/38947).

-   [Insider 0.15.1](https://forum.obsidian.md/t/obsidian-release-v0-15-1-insider-build/39021) deprecated several Workspace functions whose behavior conflicted with user expectations because sidebar views are able to receive focus. It also added the `.is-focused` class to the window body of the currently focused window.
-   The [API reference docs](https://marcus.se.net/obsidian-plugin-docs/api) got regenerated based on the latest version of `obsidian.d.ts`
-   The developer of Dataview is looking for someone with CodeMirror experience to help solve [inline queries and inline javascript expressions working in live preview](https://github.com/blacksmithgu/obsidian-dataview/issues/729) (although note: apparently you can make it work in a callout? but it's a bit awkward).

## Feature Requests

-   Wouldn't it be nice if we could have [multiple graph view filters and color groupings saved?](https://forum.obsidian.md/t/multiple-graph-view-filters-and-color-grouping-for-each/39076)
-   Is it possible to [scrape an instagram feed to pipe our images into a daily note](https://discord.com/channels/686053708261228577/707816848615407697/984876336847913000)?
-   It would be neat if there were a `Link Summaries` pane (like "outgoing links") that [leveraged dataview to show notes linked from the current note](https://github.com/blacksmithgu/obsidian-dataview/issues/1181) and instead of just showing the title or context, showed the `summary:: information` or `abstract:: information`  or whatever, eh?
-   It would be pretty cool if we could [make Obsidian our default app for opening markdown files](https://forum.obsidian.md/t/add-ability-to-use-obsidian-as-a-markdown-editor-on-files-outside-vault/38937) that aren't in a vault.
-   Some folks would like [timestamp file names anywhere](https://forum.obsidian.md/t/zettelkasten-prefixer-create-anywhere/39078), not just in a specific folder.

## Appearance

-   Obsidian 0.15.0 got some font changes, so make sure to check for theme updates.
-   Here's a [card view css snippet](https://gist.github.com/raisabelatrix/a92a2c9c43c2deb2ebb5175f11631608), with more details from the developer [in Discord](https://discord.com/channels/686053708261228577/744933215063638183/987090821922832399).
-   [Monokai](https://github.com/IORoot/Obsidian-Monokai) by `@IORoot`  was submitted for review, it's described as being clean and minimal.

## Guides

-   Here's a fantastic [beginners guide to dataview - what can go wrong and how to fix it](https://denisetodd.medium.com/obsidian-dataview-for-beginners-a-checklist-to-help-fix-your-dataview-queries-11acc57f1e48) from Denise (Dee) Todd.
-   Here's a nice explanation of how `@ryadaj` combines [meeting notes into a project note](https://discord.com/channels/686053708261228577/710585052769157141/984498140772171836) and takes advantage of header folding to reduce clutter.
-   Here's a guide to help TTRPG players [use Initiative Tracking with Database Folder](https://youtu.be/hiBzgSGJuxU), which lets you view and edit the entire party from a single table and have any changes you make in the table be instantly reflected in the Initiative Tracker. Here's why [Obsidian is the perfect free campaign manager](https://www.reddit.com/r/worldbuilding/comments/v9uorp/obsidianmd_the_perfect_free_campaign_manager/), by the way.
-   The Life Disciplines Projects system has evolved into the [Memory Flow Interface](https://github.com/uwidev/memory-flow-interface) framework intended to help people externalize working memory for mental processing.
-   `@brimwats` shared a method for using an [anki deck to memorize icon meanings](https://discord.com/channels/686053708261228577/710585052769157141/986711140287520868).
-   Here's how to [dictate notes with geolocation metadata](https://twitter.com/roddick_a/status/1537069088446595073) with Drafts (iOS only) and then port it into Obsidian for the map plugin to use. This is particularly useful for archaeological and anthropological fieldwork.

## Discussions

-   My article about why I'm happier [using themed logs than daily notes](https://www.obsidianroundup.org/themed-logs-not-daily-notes/) went out to financial supporters of the Roundup on Thursday. The first third is available as a public preview, and there's a [twitter thread with lots of related discussion](https://twitter.com/EleanorKonik/status/1535243789362675712) you can check out.
-   Here's a great thread about [quick capture workflows](https://twitter.com/zsviczian/status/1536811464702451712) (with some discussion from `@zsviczian` and I about how often we honestly just wind up using email inboxes most of the time. Here's a similar thread on [Reddit](https://www.reddit.com/r/ObsidianMD/comments/vduh9x/the_way_i_keep_track_of_tangentialrandom/) with some more options. Also, `@StPag` shared an iOS/macOS [shortcut for inputting tasks](https://discord.com/channels/686053708261228577/965681451297304596/984935845188476948) on Discord, it  works with the tasks plugin.
-   Here was a good discussion about [the limitations of using Obsidian for longform academic writing](https://www.reddit.com/r/ObsidianMD/comments/vc35ey/limitations_in_using_obsidianmarkdown_for/) and what alternatives people with different high-level use-cases use for their actual drafting.

## Ancillary Tools

-   Here's a neat tool that lets you [link to arbitrary text fragments](https://github.com/GoogleChromeLabs/link-to-text-fragment) on a website.
-   Here's a [markdown editor called MarkText](https://github.com/marktext/marktext) that is apparently a FOSS alternative to Typora.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-06-18%20Breaking%20Changes%20%26%20Dataview%20API%20Upgrades.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-06-18%20Breaking%20Changes%20%26%20Dataview%20API%20Upgrades.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
