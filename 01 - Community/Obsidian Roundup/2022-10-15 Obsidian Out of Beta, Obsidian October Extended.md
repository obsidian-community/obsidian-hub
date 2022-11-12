---
link: https://www.obsidianroundup.org/2022-10-15/
author: Eleanor Konik
published: 2022-10-15T12:30:44
publish: true
---

# 2022-10-15: Obsidian Out of Beta, Obsidian October Extended
Table generators, advanced project management options, & a guide to Charles Darwin's note taking method.

## In The Community

_Note: a bunch of great things happen in Discord every week, but the links require you to be logged in to [the community server](https://obsidian.md/community) and generally launch in the browser version of Discord unless you paste them into your app directly. Sorry!_ 

* 1.0 has dramatically changed how to create new themes, which is why the original Obsidian October event did not include a "Theme" category. Now that 1.0 is available to everyone, they added a Theme category and extended the deadline for Obsidian October entries by 2 weeks. The deadline is now November 13th. You can find out more in [the Discord channel for the event](https://discord.com/channels/686053708261228577/1022167089345216522/1030509531568025671).

There will be an hour long live session every Saturday throughout October.

* At 1PM Eastern, Stephan (`@kepano`), designer of Minimal and the new default theme, will be doing a live walkthrough of how to create a theme for Obsidian 1.0. Here's the [Discord](https://discord.gg/6kzvuPE9?event=1030119583392223302) link, the [YouTube](https://www.youtube.com/watch?v=8fbw2VRQAhk) link, and the [Twitch](https://www.twitch.tv/obsdmd) link.

Also, the videos of the 2nd week of Obsidian October live sessions are up!

* [Accept user input using commands and ribbon actions](https://www.youtube.com/watch?v=4B8imQQYM94) with Marcus Olsson walks you through accepting user input using commands and ribbon actions to make your plugin more useful.
* [Templater 101](https://www.youtube.com/watch?v=-PYyO7y0aBs) with Sam Morrison talks about how they started maintaining the Templater plugin, as well as giving some basic examples on how powerful Templater can be. Here are some of the examples that were shown; [daily note, IMDB, and logging](https://shbgm.ca/blog/obsidian/O__O+Templater/O__O+2022+Talk).

## Obsidian Updates

Obsidian is officially out of beta! [Version 1.0](https://forum.obsidian.md/t/obsidian-release-v1-0-0/44873) launched on [ProductHunt](https://www.producthunt.com/posts/obsidian-1-0) and [HackerNews](https://news.ycombinator.com/item?id=33190433). It was also announced on [Reddit](https://www.reddit.com/r/ObsidianMD/comments/y2y2p2/obsidian_release_v100/), the community [discord](https://discord.com/channels/686053708261228577/702717892533157999/1030508945594392637) and [Twitter](https://twitter.com/obsdmd/status/1580548874246443010). Some of the discussions with the team were pretty interesting 👀

As per the shiny new in-app release notes, it comes with a big redesign and the introduction of tabs – which you can now stack, a la the (now mostly deprecated) Sliding Panes plugin. It's a big redesign so might be a little jarring at first, but the devs have been saying that 1.0 means the API will stabilize for as long as I've been using Obsidian, so hopefully this should be the last big breaking update for a good long while. 

Here's a video from Nicole van der Hoeven [going over the update](https://t.co/BVKPgGLgu1). And here was a great discussion about [options for if the change to file titles displays impacted you](https://www.reddit.com/r/ObsidianMD/comments/y3udh4/good_morning_to_everyone_else_who_is_spending/). 

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list._ _For the full list, check out the [plugin stats page](https://obsidian-plugin-stats.vercel.app/new)._

* [Sakana Widget](https://github.com/Quorafind/obsidian-sakana-widget) by `@Quorafind` add a fun little Sakana! Widget to your vault.
* [Table Generator](https://github.com/Quorafind/Obsidian-Table-Generator) by `@Quorafind` is a plugin to generate markdown tables quickly like in Typora.
* [Min Width](https://github.com/doitian/obsidian-min-width) by `@doitian` can set the minimum width of the Active Pane.
* [Aosr](https://github.com/linanwx/aosr) by `@linanwx` is another obsidian spaced repetition option.
* [Custom File Explorer sorting](https://github.com/SebastianMC/obsidian-custom-sort) by `@SebastianMC` allows for manual and automatic, config-driven reordering and sorting of files and folders in the File Explorer.

### Pending (as of Friday morning)

_Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

* [Projects](https://github.com/marcusolsson/obsidian-projects) by `@marcusolsson` enables advanced project management for Obsidian. It lets users create folder-based projects and switch between three different views: Table, Board, and Calendar. It also lets you configure note templates for each project. It's beautiful and makes me desperately wish I could use Obsidian at work. Here's a really [thoughtful post](https://discord.com/channels/686053708261228577/1022167089345216522/1029042785078235187) in Discord he wrote about his motivations for writing it, and how he's planning an API so more views can be integrated 👀
* [Colorful Tag](https://github.com/rien7/obsidian-colorful-tag) by `@rien7` makes it easier to style your tags.
* [Obsidian ava](https://github.com/louis030195/obsidian-ava) by `@louis030195` uses OpenAI API and stable diffusion to generate text and enhance reflection in Obsidian.
* [Capitalize My Titles](https://github.com/joss-enet/obsidian-capitalize-my-titles) by `@joss-enet` will automatically capitalize titles.

### Updates

_If you want a comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

* Tasks plugin 1.15.1 improved the next-date calculation for monthly and yearly recurring tasks, to prevent skipping months and years in many cases. Check out the [detailed documentation](https://obsidian-tasks-group.github.io/obsidian-tasks/getting-started/recurring-tasks/#how-the-new-date-is-calculated-repeating-monthly).
* [CardBoard](https://github.com/roovo/obsidian-card-board/releases/tag/0.5.0) (which provides a kanban-style board for your tasks wherever they are in your vault) updated so that boards can be scaled using a css snippet, tags used in the definition of Boards can be hidden from view on Cards., or Board filters can be used in either Allow (previous behavior) or a Deny (new behavior) mode.
* Among other things, Metadata Menu can now create a custom values list with a dataview query. Here's [a demo](https://youtu.be/vc55ivQuHuY).
* The appearance of the [Floating Table of Contents](https://github.com/cumany/obsidian-floating-toc-plugin/) plugin can now be more easily styled, using the Style Settings plugin.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

* [Omnisearch](https://github.com/scambier/obsidian-omnisearch/releases/tag/1.6.5-beta.3) can now handle PDF indexing – on desktop. Results are cached, and this is still in beta, but it's a really neat feature.
* The [2.0 beta of Longform](https://github.com/kevboh/longform/releases/tag/2.0.0) (which is useful for handling long form writing projects) corrects outstanding bugs and updates styling to use the 1.0 style system. If you're using BRAT you'll need to manually remove and re-add the plugin, as the version number hasn't changed.

## Appearance

* [Obsidianite](https://github.com/bennyxguo/Obsidian-Obsidianite/releases/tag/v2.0.0) now supports Live Preview mode.

## Guides

* Here's a really comprehensive article about [how tags work in Obsidian](https://medium.com/@noteapps/my-obsidian-tags-are-mine-all-mine-802e4b24682c). Here's a related article from Richard Carter explaining [a really nice, straightforward set of tags](http://richardcarter.com/sidelines/my-notes-tagsonomy/) that complement a book research system. Richard also put together a neat write-up of [Charles Darwin's note taking system](http://richardcarter.com/sidelines/charles-darwins-note-making-system/).
* This video covers [creating concept notes from literature notes](https://www.youtube.com/watch?v=m6uIoQIKLA4&t=1s). It's pretty similar to some parts of my process, which I finally wrote a comprehensive article describing. If you've ever wanted a written guide to [the Konik Method of Making Notes](https://www.obsidianroundup.org/the-konik-method-for-making-notes/), it went live this week. Financial supporters got it as an email on Monday 💚
* Here are some thoughts on [the choice to use multiple Obsidian vaults or not](https://medium.com/@noteapps/multiple-obsidian-vaults-oh-my-370b5f007e6e).
* Here's a [guide for keeping track of people and connections](https://medium.com/@noteapps/keeping-track-of-people-and-connections-in-obsidian-cfd6339b50c), along with an [accompanying discussion on Twitter](https://twitter.com/NoteApps/status/1579134644687364097).
* Here's an overview of how to use [Obsidian to make technical documentation](https://www.youtube.com/watch?v=cBzc5r-FNW0).

## Showcases

* This is a nice showcase of [the value of the Omnisearch plugin](https://preslav.me/2022/05/31/omnisearch-hidden-gem-for-discovering-content-in-obsidian/), which some folks like because the search feels more comprehensive and natural.
* Here's a nice example of [using Obsidian to create a flexible working environment for biodiversity researchers](https://twitter.com/nickynicolson/status/1579114497385828353). It takes special advantage of kanbans and workspaces.
* I really loved this discussion about [how different people use Obsidian for work](https://www.reddit.com/r/ObsidianMD/comments/y0ecbo/how_do_you_use_obsidian_for_work/).
* Leah in Discord shared how she uses the [Kanban plugin for planning holiday meals](https://discord.com/channels/686053708261228577/744933215063638183/1028450671252480011). Happy belated Thanksgiving to her fellow Canadians.

## Ancillary Tools

* There is an unofficial Chrome extension for Obsidian that allows you to [create or add to existing entries in your notes](https://chrome.google.com/webstore/detail/obsidian-web/edoacekkjanmingkbkgjndndibhkegad) with information you've found online in your browser. It uses the "Local REST API" plugin, which is also helpful for automations.
* [nb](https://xwmx.github.io/nb/) is a command line and local web note‑taking, bookmarking, archiving, and knowledge base application with pretty good compatibility with Obsidian as far as I can tell. If you decide to try it out, let me know how you liked it!

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-10-15%20Obsidian%20Out%20of%20Beta%2C%20Obsidian%20October%20Extended.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-10-15%20Obsidian%20Out%20of%20Beta%2C%20Obsidian%20October%20Extended.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
