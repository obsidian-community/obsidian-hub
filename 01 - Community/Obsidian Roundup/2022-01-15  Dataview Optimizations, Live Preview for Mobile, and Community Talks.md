---
link: https://www.obsidianroundup.org/2022-01-14/
author: Eleanor Konik
published: 2022-01-15T13:30:00
publish: true
---

# 2022-01-15: Dataview Optimizations, Live Preview for Mobile, & Community Talks
Browse plugins by category, sync & publish alternatives, & more Zotero tricks. Plus, are you a consultant? Help me help you find clients!

## In The Community

-   Obsidian is up for the [Golden Kitty Award](https://www.producthunt.com/golden-kitty-awards-2021/mobile-app) at ProductHunt for Obsidian Mobile. Go vote — and check out the other top contenders, because there's some interesting software being developed and shared over there.
-   Alexander Rink has been doing performance benchmarks of different "tools for thought." The [results for Obsidian](https://www.goedel.io/p/tft-performance-obsidian) "blew away the competition up to a factor of more than 100." Make sure to read the comments! There's an _excellent_ discussion (featuring plugin dev extraordinaire `@pjeby`) about how to get Obsidian to be able to do all the "outliner" and "block" functionality. Pjeby is very knowledgeable about stuff that not everyone realizes is possible in Obsidian. This comment thread also gives a neat look "under the hood" of how hard Licat has worked to make Obsidian so performant.  Some of the key points have been [migrated to the Obsidian forum](https://forum.obsidian.md/t/understanding-obsidian-and-how-it-works/30603) for posterity.
-   The AppStories podcast has been doing an in-depth series on Obsidian, and I particularly enjoyed the discussion in [Part 3](https://overcast.fm/+I5ClvB3Dk) about cleaning up no-longer-used plugins and taking a moment to think about how you're using your tools (and what potential conflicts might have snuck into your workflow). Incidentally, here's a [discussion about which Tools for Thought & productivity podcasts are worth a listen](https://twitter.com/thoresson/status/1479836948768477190).
-   The [plugins by category](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.01+Plugins+by+Category/%F0%9F%97%82%EF%B8%8F+02.01+Plugins+by+Category) list in the Obsidian Hub has far surpassed what I can personally maintain for the Roundup's plugins page, so I took that down. I _highly_ recommend perusing the Hub's plugin list.
-   The Obsidian Community talks are leveraging the new Discord events features. You can find out more about the upcoming talks about [plugins that won Obsidian October](https://discord.com/events/686053708261228577/928414264950128660) (today) and [themes that won Obsidian October](https://discord.com/events/686053708261228577/928415936963289148) (tomorrow) on Discord.
-   There's a new [Discord thread](https://discord.com/channels/686053708261228577/700466324840775831/931635167997595748) for sharing ideas of what Obsidian merchandise you'd consider buying. Leah made some beautiful T-shirt/mug mockups if you'd like to get a sneak peek.

## Obsidian Updates

-   Live Preview has come to the Insider build for Mobile. The only [announcement](https://discord.com/channels/686053708261228577/817515900349448202/930508939987124224) I was able to find was in Discord.

## Plugin News

### New in Community Plugins

_These plugins went through code review and are now available in Obsidian's plugin list._

-   [Import Foundry VTT journal entries](https://github.com/farling42/obsidian-import-foundry) by `@farling42` Imports your journal entries from Foundry virtual tabletop worlds into Obsidian, which should be useful for the tabletop role playing game (TTRPG) users (of which we've been getting a lot more of!)
-   [TimeStamper](https://github.com/Gru80/obsidian-timestamper) by `@Gru80` lets users insert customized time/date stamps into their notes, which should be useful for people who like to take a lot of timestamped meeting and lecture notes. Note that the [Natural Language Dates](https://github.com/argenos/nldates-obsidian) allows for similar functionality. You can format your date as a timestamp, or set up a hotkey for inserting date or time.

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Enhanced Live Preview Features](https://github.com/mirnovov/elf) by `@mirnovov` brings some link behaviors from reading view into live preview mode, i.e. you can click a link to open it without holding down `ctrl`/`cmd`. There are some other features, but that's the main one.
-   [Sortable](https://github.com/alexandru-dinu/obsidian-sortable) by `@alexandru-dinu` lets you sort tables by different columns, like Wikipedia. If you use dataview tables or any tables at all, I highly recommend this.
-   [Pinboard Sync](https://github.com/Automatt/obsidian-pinboard-sync) by `@Automatt` syncs Pinboard.in links with Daily Notes
-   [Wordle](https://github.com/dbarenholz/obsidian-wordle) by `@dbarenholz` will let you play Wordle from inside an Obsidian view. You can also share your results in the new Discord thread in the `#off-topic` channel.
-   [13th Age Statblocks](https://github.com/ben/obsidian-13th-age-statblocks) by `@ben` is another TTPRG plugin. It lets users render 13th Age statblocks in Obsidian.
-   The [Notes Publish Plugin](https://github.com/SaraVieira/obsidian-notes-publish-plugin) uses Airtable and something like Netlify to  publish your notes. It's one of many "alternate publish methods," including this [guide for how to use Netlify and Zola to make a static site from your Obsidian notes](https://www.reddit.com/r/ObsidianMD/comments/s2vecw/a_quick_way_to_share_your_obsidian_pkm/).
-   [Obsidian Tweaks](https://github.com/JeppeKlitgaard/ObsidianTweaks) changes some hotkey behaviors, most notably adding more intuitive toggling behavior for things like italics, copying lines, and toggling headers. Some features are similar to the [Smarter Markdown Hotkeys](https://github.com/chrisgrieser/obsidian-smarter-md-hotkeys) plugin. It supports Live Preview & Mobile.
-   [PARA Shortcuts](https://github.com/gOATiful/para-shortcuts) by `@gOATiful` has some helpful commands to setup and manage your knowledge using the PARA method.
-   [Siteswap](https://github.com/tdresser/obsidian-siteswap) by `@tdresser` is designed to help jugglers visualize juggling patterns.
-   [Phrasebank](https://github.com/viktorbezdek/obsidian-phrasebank) by `@viktorbezdek` adds shortcodes with various pre-written phrases to improve quality and productivity of your writing, similar to an [espanso package](https://espanso.org/).

### Updates

-   [Dataview 0.4.22](https://github.com/blacksmithgu/obsidian-dataview/releases/tag/0.4.22) got a _huge_ performance update. Make sure you update and then restart Obsidian (you should honestly always restart obsidian after updating your plugins).
-   [Templater 1.9.11](https://github.com/SilentVoid13/Templater/blob/master/CHANGELOG.md) now has autocompletion of modules and function names when you type `tp.` — the [templater docs](https://silentvoid13.github.io/Templater/) also got a big update.
-   [Various Complements v.4.1.0](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/4.1.0)  added a "suggest with alias" option. This plugin, by the way, is basically an autocomplete tool that pops up automatically. Currently, it works for single words and filenames, but there's an [open issue](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/issues/24) for support for longer phrases. I saw settings for Korean and Arabic in addition to the default.
-   The [indentation guides plugin](https://github.com/mgmeyers/obsidian-indentation-guides/) now supports adding guides to lists in reading modes.
-   [Admonitions v6.8.0](https://github.com/valentine195/obsidian-admonition#microsoft-document-syntax) adds a new type of non-code block admonitions based on the Microsoft Document Syntax for blockquotes.
-   [Obsidian Git v1.20.0](https://github.com/denolehov/obsidian-git/releases/tag/1.20.0) lets users open files (and file history) on github, get a diff view, add a folder tree view to the sidebar, and allow multiline commit messages in the sidebar.
-   The [Pomodoro plugin](https://github.com/kzhovn/statusbar-pomo-obsidian/releases/tag/0.1.13) got some updates and bugfixes, including support for a log file.
-   [Key Promoter](https://github.com/joethei/obsidian-key-promoter) (which helps you learn hotkeys) now has statistics on your most used buttons and hotkeys, and descriptions of actions (which is useful for presentations!)
-   The [co-citations for graph analysis](https://github.com/SkepticMystic/graph-analysis) got updated so that it renders previews into markdown, and has outline support which allows outliner-style queries. The [release notes](https://discord.com/channels/686053708261228577/855181471643861002/930156176623169586) in Discord are really useful.
-   [Typewriter Scroll](https://github.com/deathau/cm-typewriter-scroll-obsidian) now supports Live Preview.

### Betas

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   Here's a [floating outline plugin](https://github.com/curtgrimes/obsidian-floating-toc-plugin) that was prototyped. It's still in progress, but looks promising!
-   There's an awesome new [citations plugin](https://discord.com/channels/686053708261228577/722584061087842365/928953214114619393) in process that was discussed extensively on Discord. It lets users import all literature notes in one go, works off of inline and footnote references, has new citation fields, and allows for bibliography style referencing. Academics are highly encouraged to check this out.
-   [Task Collector 0.6.3](https://github.com/ebullient/obsidian-task-collector/releases/tag/0.6.3) is now available via BRAT. It can now run commands that mark all tasks (complete, cancel, or reset) in all modes, handle moment formats, and has a toggle to remove checkboxes when moving tasks. [0.6.4](https://github.com/ebullient/obsidian-task-collector/releases/tag/0.6.4) has a modal popup and a few breaking changes.
-   The [memos plugin](https://github.com/Quorafind/Obsidian-Memos/releases/tag/1.1.2) has a tag suggester and a new settings button. It also has a dark theme and custom colors.
-   [Multi Select](https://github.com/mdelobelle/obsidian-multiselect) will enable you to write a dataviewJS query to narrow the list of links (based on your own criteria), then select the ones that you want to include in your current note with some formatting capabilities.
-   [TTRPG Statblocks v2.4.0](https://github.com/valentine195/obsidian-5e-statblocks/releases/tag/2.4.0) has a new text layout block type, the ability to render markdown inside of the blocks, and improved CSS handlers.
-   Here's some exciting [Breadcrumbs x Juggl](https://github.com/SkepticMystic/breadcrumbs/releases/tag/2.35.0) interoperability that's currently in beta. Here's the [announcement on Discord](https://discord.com/channels/686053708261228577/929513881041248266/931643782254972988). Breadcrumbs has a thread in the `#plugins-advanced` channel of Discord, by the way, if you'd like to learn more about it.

### For Developers

-   [Link to Obsidian](https://github.com/moelody/link-to-obsidian) creates an API to Obsidian files, similar to the metadata extractor.
-   Paras Chopra is looking to pay $100 to whoever [implements a dynamically updating RSS feed for Obsidian Publish](https://twitter.com/paraschopra/status/1481608908959789060), which has been an open [feature request](https://forum.obsidian.md/t/really-simple-syndication-rss-in-digital-gardens/15431) for quite some time. I would also find this very valuable from the perspective of following updates from the [Obsidian hub](https://publish.obsidian.md/hub/00+-+Start+here). Note: the discussion on the twitter thread from Paras has some useful workarounds and ideas, I recommend checking it out.
-   The developer of the Vale plugin, which is essentially a "linter for prose" (it helps enforce style guides), is looking for help [migrating from CM5 to CM6](https://github.com/marcusolsson/obsidian-vale/issues/7#issuecomment-1008299813). He's collated some resources but it looks like a codemirror extension might be necessary? If you have any guidance or know any tricks (or have some time and are looking for a project you wouldn't necessarily have to maintain), please check out the issue linked above. Vale is _really useful_ for writers.
-   Here's an [outline of topics in computer science and recommendations of best available books for each of those subjects](https://teachyourselfcs.com/) along with a [MIT challenge](https://www.scotthyoung.com/blog/myprojects/mit-challenge-2/) designed to help people learn to code on their own. It came up [in discussion in Discord](https://discord.com/channels/686053708261228577/722584061087842365/931583337930293269) (during which someone shared all their CS notes via Google Drive!) and I know a lot of Obsidian devs are solo learning to code, so I wanted to share it with y'all.

## Feature Requests

-   The ability to [open a ghost vault so Obsidian can be the default app for markdown files](https://forum.obsidian.md/t/have-obsidian-be-the-handler-of-md-files-file-association/314/38) is getting a lot of traction. Here's a [related request](https://forum.obsidian.md/t/single-md-file-vault/30490).
-   There's a new feature request for [improving how backlinks are rendered in live preview](https://forum.obsidian.md/t/live-preview-in-backlinks-improvements-to-how-they-are-displayed/30487).
-   It would be awesome if we could [center the graph around our active note](https://forum.obsidian.md/t/center-to-location-for-graph-view/30534)
-   It would be nice if we could have a [delete and _always_ ask again](https://forum.obsidian.md/t/option-to-hide-the-delete-and-dont-ask-again-button/30576) option to compliment the "delete and don't ask again" button.
-   Here's one for [better pandoc citation style support](https://forum.obsidian.md/t/support-pandoc-style-citations-with-citeproc-js-engine-citekey-citekey-and-relative-bibliography/17549).

## Appearance

-   Here's a [new cite syntax](https://discord.com/channels/686053708261228577/702656734631821413/929764620376350770) that doesn't involve a bunch of HTML. It comes in snippet form but also is "core" in Sanctum, ITS and Shimmering Focus (at least).
-   `@viticci` came up with [a system to save rich links and display them as an interactive grid with thumbnail previews](https://twitter.com/viticci/status/1481687474753658890). It seems like it makes for an awesome dashboard.
-   Cybertron got a facelift — Nick commissioned Cecilia May (creator of the award-winning Primary theme) to create the [LYT Mode](https://github.com/nickmilo/LYT-Mode) theme.
-   [Minimal 4.4](https://github.com/kepano/obsidian-minimal/releases/tag/4.4.0) moved to SCSS, got a rewrite of all the documentation, and has very nice support for movie and tv show dashboards.
-   [Shimmering Focus v1.603](https://github.com/chrisgrieser/shimmering-focus#table-of-contents) added a ton of features including built-in styling for supercharged links, gutter indicators for unresolved links, a new css-only admonitions, and some other fancy features.
-   [Ebullilentworks](https://github.com/ebullient/obsidian-theme-ebullientworks) removed the corner blockquote icon, got rid of strikethroughs for some `data-task` values in live preview (yaaay!) and truncates long folder names.
-   [Spectrum v1.1.1](https://forum.obsidian.md/t/theme-spectrum-version-1-1-1/12688) got some bugfixes and lets users toggle titlebar text.
-   [Sanctum v0.6.0](https://github.com/jdanielmourao/obsidian-sanctum/releases/tag/v0.6.0) got a bunch of print support, and supports the use of  `>>>` for paraphrases. There are also a bunch of new style settings, and some UI tweaks.
-   [ITS Theme](https://forum.obsidian.md/t/theme-its-dark-light-theme/12838/150) has new Live Preview and Style Settings updates. It also has improved styling for slides, Cooklang, Fantasy Calendar, and Admonitions.

## Ancillary Code

-   Here's a script that will [fetch movie and tv show metadata into your vault](https://github.com/chhoumann/quickadd/blob/master/docs/Examples/Macro_MovieAndSeriesScript.md).

## Guides

-   Here's a guide that explains [how to sync Obsidian on iOS via Rclone](https://gist.github.com/agmm/ea97a3c2b5bf713567aad89672116e12). With Rclone you can sync files to remote SFTP servers, WebDAV servers, Google Drive, Amazon S3, and many other providers.
-   Here's a [simple note-taking setup](https://www.youtube.com/watch?v=E6ySG7xYgjY) guide that uses [[Zettelkasten]] methodology.
-   There's a new Contributed Video up on the Community Talks channel. It gives an in-depth look into [use-cases for the co-citations algorithm in the Graph Analysis plugin](https://www.youtube.com/watch?v=rK6JVDrGERA&ab_channel=ObsidianCommunityTalks). This is high on my list of things to try and figure out before spring.
-   Here are [two methods of creating a 'Game Master' screen in Obsidian](https://youtu.be/0tTZZa7u92w), using a kanban board and the Obsidian sidebar.

## Discussions

-   I never thought I'd see another person in the wild who annotates their academic texts with "ORLY" when they come across something that seems sketchy. Here's Rob Heaton's guide on [how to annotate](https://robertheaton.com/2018/06/25/how-to-read/), read, and summarize books to support actual learning. It was shared during a Discord [discussion of different annotation methods](http://discordapp.com/channels/686053708261228577/710585052769157141/931336758522687528).
-   Here's a discussion on the forum about [approaching and designing your PKM system](https://forum.obsidian.md/t/what-has-your-pkm-actually-help-you-achieve/30249/).
-   Here's a discussion in Discord about how to [use Obsidian as a STEM researcher](http://discordapp.com/channels/686053708261228577/722584061087842365/930564993806651404), another about using [Obsidian for clinical medical notes](https://forum.obsidian.md/t/clinical-medical-notes/29062) and also some [project managers discussing how they use Obsidian for work](https://forum.obsidian.md/t/any-product-managers-here-how-do-you-leverage-obsidian/30596).
-   There was some [discussion about how to use Obsidian as a collective knowledge management tool](http://discordapp.com/channels/686053708261228577/710585052769157141/930532848631427154), and it turns out that the folks over at Dendron are [putting together a public registry for knowledge](https://blog.dendron.so/notes/qTeL51LFD0Y8uC9ect7QV/). Since Dendron is essentially an extension for Visual Studio Code, which is a text editor, I believe you should be able to use it with an Obsidian vault without too much trouble. [It probably isn't seamless, though](https://forum.obsidian.md/t/open-vault-in-vscode-plugin/20963/6).
-   Here's a discord discussion featuring `@Leah` explaining how she [cleaned up and dealt with thousands of unread but potentially useful articles](https://discord.com/channels/686053708261228577/710585052769157141/929128798115483669).
-   Here's a really in-depth discussion with lots of examples of people [sharing their use-cases](https://www.reddit.com/r/ObsidianMD/comments/s22xoh/could_you_please_share_some_of_your_use_cases/) for Obsidian.
-   Here's a discussion about the value of the [notes to self paradigm of note-taking](https://twitter.com/EleanorKonik/status/1481771392723038216). It's on Twitter, so it's a bit hard to parse, but I recommend reading the whole thread and poking around in the broader discussion, because it was very thought-provoking.

## Ancillary Tools

-   Here's a nice blog post from the folks at [Readwise](https://readwise.io/i/ac9) (which lets you sync highlights from Kindle and Pocket and Instapaper etc. into Obsidian, along with having spaced repetition features) about [how to tag your highlights while you read](https://blog.readwise.io/tag-your-highlights-while-you-read/). You can also [add chapters to your highlights](https://blog.readwise.io/add-chapters-to-highlights/) and [combine them on the fly](https://blog.readwise.io/combine-highlights-on-the-fly/amp/).
-   Here's a manually curated aggregator of "timeless articles" and snippets of "short perspectives" that you can save off, take notes on, etc. It's called [Read Something Great](https://www.readsomethinggreat.com/) and seems pretty similar to [The Browser](https://thebrowser.com/) (also hand-curated lists of 5 links, but a newsletter and skews toward "newer" things) or [Refind](https://refind.com/?utm_source=newsletter&utm_medium=barter&utm_campaign=Mn6vY1aQFu5DtmSrH9P7sg) (which uses machine learning to try to give you things you're more likely to enjoy).
-   The [ZoteroObsidianCitations](https://github.com/daeh/zotero-obsidian-citations) add-on searches your Obsidian Vault and adds a tag to the corresponding items in your Zotero database. It basically adds colored tags to Zotero items that have associated Markdown notes in an external folder. Here's more about it from the [forum](https://forum.obsidian.md/t/new-plugin-citations-with-zotero/9793/317?u=argentum).
-   Here's a [discussion about how to link to Zotero entries from Obsidian without worrying about exporting stuff](https://www.reddit.com/r/ObsidianMD/comments/s3i4tb/obsidian_zotero_to_refer_to_a_note/).
-   Here's a bot that [tweets out a random block from your obsidian vault](https://github.com/adithyabsk/tftbot). It relies on Google Drive.
-   Windows 11 users who find the lack of clock customization annoying, check out this [awesome tool called ElevenClock](https://github.com/martinet101/ElevenClock).

## Housekeeping

We're starting to see more [startup CEOs and small companies asking for referrals to expert business consultants for Obsidian usage](https://www.reddit.com/r/ObsidianMD/comments/s3ez0y/any_organizational_consultants_who_specialize_in/). I'm considering putting together a list of people willing to be contacted about this, probably to be hosted on [the hub](https://publish.obsidian.md/hub/). If this is something you'd be interested in doing, please reach out and let me know.

You may have noticed the slightly new format of the Roundup's _plugins_ section.  It turns out many people don't like rolling beta plugins and prefer to wait for them to enter into the "official store," but were having trouble getting alerts when that actually happened. As such, I'm experimenting with separating those out into two different lists. You might see the same plugins pop up twice in a row because one week they've been submitted and a later week they've passed code review.

This was made possible by the generous coding skills of my fellow moderators `@argentum` and `@tzhou`, who took pity on me and created scripts to collate some information coming from Github and some critical channels in Discord like the starboard and updates channels. This lets me focus on things that require a human touch, like dredging up interesting conversations on Twitter!

It definitely didn't mean that I spent less overall time on the Roundup 🤣

💚

If you'd like to support my work (and potentially fund the purchase of a new iPad so I can try out some of the nifty iPad workflows I've been reading about!), you can sign up for a [membership](https://www.obsidianroundup.org/membership/) (thanks to those of you who already have!) or make a [one-time donation](https://ko-fi.com/eleanorkonik) via ko-fi. 

In more personal news, my son just started daycare. To celebrate, I'm getting ready for a major refactor of my vault to bring some of my older files in line with my newly developed "best practices." **If there's anything you'd like me to write an article about or host a community talk for, let me know.** I'll have my hands in the guts of my system, so it's a good time to showcase what I used to do, what I do now, and why  I'm changing it.

I'll try to set aside time for more writing about knowledge management if there's interest. Mostly I default to focusing on [writing about obscure history and science](http://newsletter.eleanorkonik.com/) over on my fiction + research newsletter, but I'm pretty open to answering questions about Obsidian if you have any.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-01-15%20%20Dataview%20Optimizations%2C%20Live%20Preview%20for%20Mobile%2C%20and%20Community%20Talks.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-01-15%20%20Dataview%20Optimizations%2C%20Live%20Preview%20for%20Mobile%2C%20and%20Community%20Talks.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
