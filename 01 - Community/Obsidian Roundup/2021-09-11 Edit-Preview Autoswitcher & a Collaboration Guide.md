---
link: https://www.obsidianroundup.org/2021-09-11/
author: Eleanor Konik
published: 2021-09-11
publish: true
---

# 2021-09-11: Edit/Preview Autoswitcher & a Collaboration Guide
Save the date for October community talks, a defense of graph view, and a bunch of ancillary tool info.

# Collaboration Guide,

## In The Community

Upcoming community talks (save the date, links to follow later in the month!):

- Sunday, October 3, 2021 4:00 PM EST: `@Eleanor Konik` (that's me!) will discuss a comprehensive project management workflow for fiction writing: using folders, [[dataview|Dataview]], and tags. From ideation to completion, submitting to markets, tracking market preferences, branding work, and ancillary avenues for outreach like newsletters and tweets. If there's anything in particular you want to see, reach out. For now I'm working off of [this request](https://forum.obsidian.md/t/obsidian-talks-voting-post-which-talks-do-you-want-to-hear/15705/15).
- Sunday, October 10, 2021 2:00 PM EST: In this showcase, presenters will share how they set up and use [[iOS Shortcuts]] in Obsidian Mobile.

## Plugin News

### New

- We've got another proto-WYSIWYG plugin on the scene: [Autoview](https://github.com/mmhobi7/obsidian-autoview) will auto-switch the active window to edit mode when a keystroke is detected, and then switch back to preview mode a delay after the last keystroke is detected.
- `@luckman212` put together a small quality of life plugin that will let you assign a hotkey to [[obsidian-reset-font-size|reset your zoom level]] back to "normal" even on operating systems and keyboards that don't make it easy.
- [[podcast-note|Podcast Note]] lets you easily pull metadata for podcasts and take notes on them.
- I had to do a double-take because I wrote this last week about a different plugin: There's a new riff off of focus mode! This week we got [[obsidian-stille|Stille]].
- [[obsidian-carry-forward|Carry-Forward]] lets users copy a link to the current block.

### Updates

- the [[file-tree-alternative|File Tree Alternative Plugin]] allows users to view the file and folder lists in a single view to have Evernote similar experience instead of switching between the views. Here's a [demo](https://www.youtube.com/watch?v=fbz8IZtXuUE) video.
- [[obsidian-excalidraw-plugin|Excalidraw]] 1.3.1 has drag & drop support to create links from files in the file manager and improved zoom to fit. Images will fit fullscreen, (almost) regardless of image size. Also, the full package is now in one file and chunks no longer get loaded from the web.
- The [[obsidian-dictionary-plugin|Dictionary]] plugin (which by the way has a fantastic thesaurus) just got a redesign to look more like the native Obsidian views, i.e. the search panel.
- The [[extract-url|Extract url content]] now has [mobile support](https://forum.obsidian.md/t/extract-url-plugin-mobile-support/23664).

### For Developers

- `@NothingIsLost` shared a plugin to help theme designers inspect the "Export to PDF" styling output interactively in Dev Tools which should make debugging print mode easier.

## Workflow Stuff

- A group of pentesters (which is to say, white hat hackers) shared a really nice and comprehensive article about how they use [Obsidian for collaboratively documenting group knowledge](https://www.trustedsec.com/blog/obsidian-taming-a-collective-consciousness/) in the cybersecurity field. If you wanted to use Obsidian collaboratively and are not terrified of git, this is a must-read in my opinion. Here's the [associated git repo](https://github.com/trustedsec/Obsidian-Vault-Structure).
- I wrote an article about how [the graph view isn't just a pretty gimmick](https://eleanorkonik.com/its-not-just-a-pretty-gimmick-in-defense-of-obsidians-graph-view/), and there were some great comments in the [reddit thread](https://www.reddit.com/r/ObsidianMD/comments/plc4ny/its_not_just_a_pretty_gimmick_in_defense_of/) about using the graph view for fiction writing and different kinds of knowledge graphs.
- Ben shared how they use [Obsidian for tracking tasks](https://medium.com/geekculture/how-i-track-my-tasks-in-obsidian-47fd7ad80364). Note though that other people prefer to [keep task management and knowledge management separate](https://publish.obsidian.md/leah/40+Digital+Garden/Simplicity%2C+strategic)
- Here's a nice [collection of daily notes templates](https://www.reddit.com/r/ObsidianMD/comments/pjp8d1/daily_note_templates_please_share/) on Reddit.
- This [collection of templates](https://filipedonadio.com/6-useful-templates-for-obsidian/) also got resurfaced if you're looking for inspiration about how to set up Cornell notes, meeting notes, book notes, blog posts or an Einsenhower Matrix. Also, Filipe has a bunch of Obsidian content on YouTube that I wasn't aware of, like this video from last month about how he used [only Obsidian for a week](https://www.youtube.com/watch?v=1UCAlCAvXhk).

### Advanced

- Here's a [powershell script](https://forum.obsidian.md/t/insert-title-into-front-matter-powershell-script/23966) to insert file titles into the front matter of all your notes.

## Feature Requests

- You can [add your support](https://forum.obsidian.md/t/obsidian-send/23899) to the feature request to send things to Obsidian via email and tweets and stuff, a la IFTTT but with [[Obsidian Sync]].

## Appearance

- This absolutely incredible css snippet will make [your vault look like a Diablo game](http://discordapp.com/channels/686053708261228577/700466324840775831/885715893919825990). For a laugh, try it in light mode.
- The [[Firefly]] theme is pending review, but is one of the few examples I've personally seen of a repository using [[SCSS]], a Rubyprogram written in that assembles CSS style sheets for a browser, and for information, SASS adds lots of additional functionality to CSS like variables, nesting and more which can make writing CSS easier and faster.
- CSS for [rainbow relationship line colors](https://discord.com/channels/686053708261228577/702656734631821413/884586663064535141) was shared in the Discord by `@NothingIsLost`.
- Here's how you can [hide attachment subfolders](https://forum.obsidian.md/t/hiding-attachments-folders/23929).
- Here are some nice [tips for printing to PDF](https://www.reddit.com/r/ObsidianMD/comments/pl29cs/better_pdf_printing/).

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- `pseudometa` shared a [detailed academic workflow](https://chris-grieser.de/Comprehensive-Academic-Workflow-from-Reading-to-Writing-in-Markdown) that offers alternatives to the [[Zotero]]/[[Mdnotes]] process and discusses when to do what and why and what else you can do.
- The creator of [[Gingko app]], a pane-based outliner-setup longform writing app is also an obsidian user and [swung by the forums](https://forum.obsidian.md/t/writing-in-tree-structure-the-solution-to-long-form-writing-gingko/20727/24?u=eleanorkonik) to share that Gingko now allows for importing from markdown and is looking for some discussion on how people would like to see the feature develop.

### Research Rabbit

- [Research Rabbit](https://www.researchrabbit.ai/) (yes it's free) put together [a playlist of Youtube videos](https://www.youtube.com/watch?v=wHBql2JncyU&list=PLLrc8QKmOs9btNMYi8zsNRKlGuIZgPTZK) with tutorials from users, starting with `@dannyhatcher` and his workflow (follow up with [this video](https://www.youtube.com/watch?v=AQdKBhCaCcI) to see how he processes things into Obsidian afterwards).
- `@brimwats` and Bryan Jenks and I also did a community talk on Thursday with some interested folks sharing our workflows with [[Research Rabbit]]: here's my writeup about [how I use Research Rabbit for Worldbuilding Research](https://eleanorkonik.com/using-research-rabbit-for-worldbuilding-research/).
- PS: I'm deliberately not giving you a referral code because I don't want to take their money, it's such a good tool and they're so nice, but if you have trouble signing up (they require some kind of 'institutional' email for the forum) you can reach out via email and let them know you found them though the PKM community and they'll set you up.

### Readwise

- The folks at [[Readwise]] (subscription-fee app but too many pkm people love it to not include it here) just announced a big update coming — [a read-later app with RSS, newsletter and pdf-reading capabilities](https://readwise.io/read). They're adding people to the waitlist now and while I'm not personally in the beta I'm pretty excited for it — I've heard it's great, and has nice hotkey support.
- They're also working on a web highlighter. Some Obsidian users are excited at the idea of replacing products like Highlights and Instapaper with their new Reader app.
- While I'm talking about Readwise, they also shipped [focused highlight review](https://twitter.com/hstagner/status/1435593578194120706?s=21).
- Here's [Dan Ollosso](https://www.youtube.com/watch?v=XnG9beuXmJw) on the Readwise Obsidian plugin. Here's [Curtis McShale](https://youtu.be/tUfTaEhqZU8)'s. (I told you it was popular with Obsidian folks).

## Housekeeping

- both `@liam`’s [[calendar|Calendar]] and `@tgrosinger`’s [[table-editor-obsidian|Advanced Tables]] community plugins have surpassed 100,000 downloads in the Obsidian plugin gallery. So exciting!
- When I logged in to work on this yesterday, my dashboard let me know that there are over 2,000 of you subscribed to this newsletter, which is orders of magnitude more than I thought would ever find value from it, so thanks for checking in with me every week! Ghost reports that about 70% of you read this pretty consistently (so I guess I'm not getting lost in the ether!), which is incredibly motivating. Thank you!

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-09-11%20Edit-Preview%20Autoswitcher%20%26%20a%20Collaboration%20Guide.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-09-11%20Edit-Preview%20Autoswitcher%20%26%20a%20Collaboration%20Guide.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
