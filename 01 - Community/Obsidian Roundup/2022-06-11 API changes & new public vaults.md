---
link: https://www.obsidianroundup.org/2022-06-11/
author: Eleanor Konik
published: 2022-06-11T12:30:00
publish: true
---

# 2022-06-11: API changes & new public vaults
A big release with improved collaboration, Sync, and sharing. Customize kindle imports, fancy databases, and improvements for task management.

## In The Community

-   There's a community talk about daily notes & habits on 11-Jun-22 at 1pm Eastern (~5 hours after you get this email). Here's the [link to Zoom](https://discord.com/events/686053708261228577/983391524995858493), here's the link to the [Discord Event](https://discord.com/events/686053708261228577/983391524995858493).

## Obsidian Updates

-   Obsidian Desktop v0.14.15 is now available for public access, which includes everything from [v14.7](https://forum.obsidian.md/t/v0-14-7/36491) to [v14.15](https://forum.obsidian.md/t/v0-14-15/38085)) — Obsidian Publish collaboration, Obsidian Sync shared vaults, an improved Obsidian Sync setup flow, renaming blockIDs, and plugin errors in the console showing the plugin's name.
-   Obsidian Mobile v1.2.2 is also available for public access, which includes all of the above functionality, the iOS share sheet, and a bunch of bugfixes.

## Plugin News

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Task Progress Bar](https://github.com/Quorafind/Obsidian-Task-Progress-Bar) by `@Quorafind` is a task progress bar plugin for tasks in Obsidian.
-   [Share as Gist](https://github.com/timrogers/obsidian-share-as-gist) by `@timrogers` lets users share an individual note as a GitHub.com gist.
-   [Text Expander JS](https://github.com/jon-heard/obsidian-text-expander-js) by `@jon-heard` lets users type text shortcuts that expand into javascript generated text.
-   [Alias from heading](https://github.com/basham/obsidian-alias-from-heading) by `@basham` will implicitly add an alias matching the first heading in a document.
-   [Obsidian Raindrop](https://github.com/mtopping/obsidian-raindrop) by `@mtopping` will integrate your Raindrop.io bookmarks with Obsidian.
-   [Douban](https://github.com/Wanxp/obsidian-douban) by `@Wanxp` can import movies, books or musics info data from Douban for Obsidian .
-   [Clock](https://github.com/RosiePuddles/obsidian-clock) by `@RosiePuddles` puts a clock in the status bar
-   [List Callouts](https://github.com/mgmeyers/obsidian-list-callouts) by `@mgmeyers` is a neat way to create simple callouts in lists.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

-   [Kindle Highlights 1.6.0](https://github.com/hadynz/obsidian-kindle-plugin/releases/tag/1.6.0) gives users the ability to customize the default template used for your highlights. This allows you to include your own front matter and even use double colon idioms to integrate your Kindle highlights with Dataview.
-   [Novel Word Count v2.5](https://github.com/isaaclyman/novel-word-count-obsidian/releases/tag/2.5.0) added options for aligning data (word count, creation date, etc) relative to file/folder names: inline, right-aligned, or below. This is a really handy plugin for getting a sense of where most of your note contents lie: I am pretty proud to have 340k words of "products," more than my 266k words of "references" :>
-   [Github Publisher](https://github.com/Mara-Li/obsidian-github-publisher) can now convert wikilinks to markdown links _without_ changing the file in Obsidian.
-   [Various Complements plugin v7.0.0](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/7.0.0) has improved support for Chinese, case-insensitive match options, character size requirements, and more.
-   Customizable Menu now allows users to [hide items from context menus](https://github.com/kzhovn/obsidian-customizable-menu/releases/tag/2.2.0) across Obsidian. This is a great way to declutter those menus from having buttons you never use.
-   [Obsidian TikZJax](https://github.com/artisticat1/obsidian-tikzjax) now supports tikz-cd and chemfig.
-   [Tasks Plugin 1.7.0](https://github.com/obsidian-tasks-group/obsidian-tasks/releases/tag/1.7.0) has new filters for "has done date," "no done date," "has happens date," "no happens date," and other group options. Here's a new [guide to the master query](https://discord.com/channels/686053708261228577/965681451297304596/984308925732098148) in Discord. There's also a [tasks quick reference page](https://obsidian-tasks-group.github.io/obsidian-tasks/quick-reference/) now.
-   [Database Folder](https://github.com/RafaelGB/obsidian-db-folder/releases/tag/1.7.0) has customizable row height, sticky a reference column, new type of data, and more. Here's a neat [video showcase](https://youtu.be/2v7LO64-C08) of how it works.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   [Omnisearch Update 1.3.5-beta1](https://github.com/scambier/obsidian-omnisearch/releases/tag/1.3.5-beta1) allows the search index to be saved on disk, to avoid a full reindex at each startup. You can also now ignore diacritics.

### For Developers

-   [CodeMirror 6.0 is finally stable](https://news.ycombinator.com/item?id=31666186). That means Obsidian will be migrating from v0.19 to v6.0 soon. Once the next Obsidian insider build is available, Licat plans to write up a summary of the breaking changes so you can make sure your plugin continues to work.
-   The [Obsidian Checklist Plugin](app://obsidian.md/%5Bhttps://github.com/delashum/obsidian-checklist-plugin%5D(https://github.com/delashum/obsidian-checklist-plugin)) is seeking a new maintainer to help get it working on mobile again.
-   The developer of [Linked Data Helper](https://github.com/kometenstaub/linked-data-helper/issues/10) is looking for someone to rewrite the helper plugin parser for the new data format and structure, feel free to reach out. If nobody gets to it in the next month or so, he plans to archive these plugins.
-   The [Tasks plugin](https://github.com/obsidian-tasks-group/obsidian-tasks) maintainer is looking for someone with user interface development experience in Typescript to help progress go faster.
-   A [discord user](https://discord.com/channels/686053708261228577/840286264964022302/983844700006023208) is looking to financially support the development of a plugin to get a new kind of reading view.
-   Here's an implementation of [two plugins talking to each other](https://www.npmjs.com/package/@vanakat/plugin-api) along with a 2-function for exposing/consuming APIs. The developer is looking for feedback and hopes it will bring a little bit of standardization to inter-plugin communications.

## Appearance

-   [Callout Typesetting](https://github.com/sailKiteV/Obsidian-Snippets-and-Demos/tree/master/CalloutTypesetting) is a CSS snippet that allows you to apply custom typesetting to any of your callouts through their metadata attribute, so for example you can do `> [!quote|rtl]`
-   [Minimal 5.2.10](https://github.com/kepano/obsidian-minimal/releases/tag/5.2.10) got a bunch of improvements for mobile, specifically to help facilitate distraction-free writing on the iPad.
-   [Prism v2.2.0](https://github.com/damiankorcz/Prism-Theme/releases/tag/2.2.0) improved the progress bars, got some consistency improvements, support for Quiet Outline, new style settings toggles, and more.
-   [Bubble Space v1.6](https://github.com/Emrie-Candera/Bubble-Space-Theme/releases/tag/v1.6) got some fixes.
-   [Typomagical 1.3](https://github.com/hungsu/typomagical-obsidian) has a breaking change for style settings, to facilitate the new Style Settings sliders for Font Weight for Titles, Headings, Bold and all other text.
-   [Red Solitude](https://github.com/MajorEnkidu/red-solitude-obsidian-theme/releases/tag/2.2.1) is a new dark theme with a strong accent color and a 3D look.
-   Here's a [Rose Pine spin on the Primary theme](https://github.com/maudlinmandrake/primary-pine).

## Guides

-   Here's a nice guide, aimed at beginners, for [using Obsidian as a personal wiki](https://www.online-tech-tips.com/computer-tips/how-to-use-obsidian-as-a-personal-wiki-on-your-computer/).
-   Here's a guide for task management in Obsidian that was [posted to Discord](https://discord.com/channels/686053708261228577/965681451297304596/984206825991864381).
-   Here's a guide for [project notes](https://discord.com/channels/686053708261228577/710585052769157141/984498140772171836) that was posted to Discord.
-   This is a wonderful step-by-step guide to using [Obsidian as a Dungeon Master](https://www.patreon.com/posts/67310539), designed for folks who have never used Obsidian before.
-   Here's a video about [how to schedule notes for review in the future](https://youtu.be/gqWT0mXoK0Q).

## Discussions

-   Here's a nice discussion on Reddit about why different people [started their vaults](https://www.reddit.com/r/ObsidianMD/comments/v5qzfp/why_do_you_want_a_second_brain_what_ma) that also had an incredibly useful peek into a doctor's workflow of versioning instead of editing.
-   Here's the latest [discussion about our favorite "must-have" plugins](https://discord.com/channels/686053708261228577/707816848615407697/983882863160201236) in Discord.
-   Here's the recording of a Twitter Spaces event about [Zettelkasten](https://twitter.com/i/spaces/1vAGRkqPXDNJl) methodologies.

## Public Vaults

-   Nikola Milekic, a software engineer based in Germany, shared his vault, which is mostly centered around [politics & democracy, computer science, & math](https://notes.nikolamilekic.com/).
-   Here's a nice open source public vault for [data engineering](https://github.com/data-engineering-community/data-engineering-wiki) that took inspiration from the Obsidian Hub.

## Ancillary Tools

-   Here's a cute, self-hosted, free and open source [tag-based time tracking tool](https://traggo.net/) called traggo.

## Housekeeping

-   The supporters-only live event went well! Among other things, we had a nice discussion about how individual successes benefit human communities, based on this piece about how [risky food-finding strategies might be the key to human success](https://archaeologynewsnetwork.blogspot.com/2022/01/risky-food-finding-strategy-could-be.html), which nicely complements this article about [how kangaroo hunting relates to the decision to pursue high-risk/high-gain resources](https://royalsocietypublishing.org/doi/10.1098/rspb.2013.1210). Unfortunately, I got so caught up in chatting that I forgot to ask if people minded if I recorded. That said, my son is shifting to full day daycare on Monday, so in the future I should be able to pick times that are a little more forgiving to folks farther west than New York, heh.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-06-11%20API%20changes%20%26%20new%20public%20vaults.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-06-11%20API%20changes%20%26%20new%20public%20vaults.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
