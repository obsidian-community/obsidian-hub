---
link: https://www.obsidianroundup.org/2021-07-31/
author: Eleanor Konik
published: 2021-07-31
publish: true
---

# 2021-07-31: Leveraging Graphs, a QuickAdd guide, & Plugin Changelogs
Code formatters, the Zettlr beta, & CSS admonitions.

## Community Events
-   `@NickMilo` is hosting a live event on Sunday, August 1 2021 at 10:00 AM PDT / 17:00 UTC to roll out version 5 of the LYT kit. You can [ask & upvote questions](https://lytkit.featureupvote.com/) for Nick to answer. Find out more from [this Twitter thread](https://twitter.com/NickMilo/status/1421253164070674434).

## Obsidian Updates

[Insider 0.12.12](https://forum.obsidian.md/t/obsidian-release-v0-12-12-insider-build/21564) has arrived. Here are the highlights:

- There is now a search bar to find core plugins better.
- You can now use the keyboard to navigate and select context menus.
- There is now a [[YAML frontmatter]] flag for `publish:`. This flag affects the UI when uploading files to your publish site.

## Plugin News

### New

- [[plugin-changelogs|Plugin Changelogs]] allows you to view the plugin changelogs right in Obsidian with a little Button next to the Update Button.

### Updates

- [[advanced-toolbar|Advanced Mobile Toolbar]] now allows you to change all Toolbar Icons.
- [[obsidian-tracker|Tracker]] [v1.9.0](https://github.com/pyrochlore/obsidian-tracker) lets users create pie charts. There are also some [breaking changes](https://discord.com/channels/686053708261228577/855181471643861002/869592821001236480) involving `{{sum}}`
- [[initiative-tracker|Initiative Tracker]] [2.0.0](<(https://github.com/valentine195/obsidian-initiative-tracker#creating-encounters-in-notes)>) adds support for creating & encounters directly in your notes.
- [[media-extended|Media Extended]] [v2.9.0 Update](https://github.com/aidenlx/media-extended/releases/tag/2.9.0) adds timestamp template, option to blur on pause for Youtube videos, bilibili support, and embed size control and better options for player controls.
- [[obsidian-tasks-plugin|Tasks]] [version 1.2.0](https://github.com/obsidian-tasks-group/obsidian-tasks/releases/tag/1.2.0) lets users filter by recurring, can hide more stuff, and more.

### For Developers

- `@Licat` strongly recommends using `Editor` when possible rather than directly using `cmEditor` because `Editor` is an abstraction that bridges the gap between Codemirror 5 & 6, and Codemirror 5 stuff won’t work on mobile. You can read the [full discussion on Discord](https://discord.com/channels/686053708261228577/840286264964022302/870514620450873464)
- `@Licat` also recommends avoiding using `basePath` directly, and [here’s more about why](https://discord.com/channels/686053708261228577/840286264964022302/851183938542108692).

## Workflow Stuff

- `@NickMilo` shared a great [live notetaking session](https://www.youtube.com/watch?v=68huyTJjBF0) that includes he uses the graph view to become a better thinker.
- `@Christian` shared a blog post on a couple of different [ways to use QuickAdd](https://bagerbach.com/blog/how-to-use-quick-add-for-obsidian-with-examples/), with examples! There’s also a really nice [video](https://www.youtube.com/watch?v=gYK3VDQsZJo).
- Did you know that [[YAML]] [supports multiline strings](http://discordapp.com/channels/686053708261228577/840286238928797736/868314054702297128)?
- `@ichmoimeyo` shared three showcase videos for the mobile app they found useful. [One](https://www.youtube.com/watch?v=66WnTCt77uU), [Two](https://www.youtube.com/watch?v=_ufMj-4cdIM), [Three](https://www.youtube.com/watch?v=Ke_m3y-6_DI)
- There was a discussion about how to [use Obsidian on a Chromebook](https://www.reddit.com/r/ObsidianMD/comments/ost772/best_way_to_use_obsidian_on_a_chromebook_perhaps/).
- You can [Update Obsidian by Voice with Dropbox, Google Assistant, & IFTTT](https://publish.obsidian.md/arun/Tech/Update+Obsidian+By+Voice+with+Dropbox+and+Google+Assistant+and+IFTTT)

### Showcases

- `@markmcelroy` is planning to write a novel using Obsidian, a chapter a day, in public. He’s going to share access to his notes as he goes; backstories, outlines, and commentary. [Find out more](https://markmcelroy.com/ive-decided-to-write-a-novel-in-public-using-obsidian-md/).
- `@trulymavical` has a [GitHub repository for Obsidian resources](https://github.com/ransurf/obsidian-resources/tree/main/templates) including their [daily note template](https://www.youtube.com/watch?v=OFFTIIUDNK4), which they shared in a video about how they use daily notes as their bullet journal.
- [obsidian.garden](https://obsidian.garden) is a open-source guide to creating your own [[Digital garden]] with Obsidian. It’s heavy on emojis but can be cloned via git or downloaded as a zip file to become a sort of starter vault.

## Feature Requests

- `@ontheexam` created a feature request for a [plugin that lets you assign (for example) hotkey defaults that match your muscle memory from various programs](https://forum.obsidian.md/t/muscle-memory/21391), for example Ulysses or [[Drafts App|Drafts]].

## Appearance

- The community showcase for `@SlRvb`’s Image Adjustment CSS Snippet is live on the [Obsidian Community Talks](https://www.youtube.com/watch?v=VRoBNWvw8sU) channel.
- Did you know you can set the alt text of embed with a `|` pipe, i.e. `[image.jpg|alt text]`
- `@SlRvb` shared [CSS snippets to emulate admonitions](https://github.com/SlRvb/Obsidian--ITS-Theme/blob/main/S%20-%20Admonitions.css) on [[Obsidian Publish]]. It’s not as fully featured as the plugin, but it’s a nice alternative for folks who don’t want to feel locked into the plugin and prefer pure CSS/HTML.
- `@chetachi` shared [how to set different icons based on file type](https://discord.com/channels/686053708261228577/702656734631821413/866399284437843978) using `[data-type$(file type here)]`

## Knowledge Management

- the [[LYT Kit]] has been translated into [Chinese](http://discordapp.com/channels/686053708261228577/694233507500916796/870493440885010473).

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- [Prettier](https://prettier.io/) is a nifty code formatter that is opinionated and can clean up not only programming langauges like Typescript, it can also clean up markdown and YAML! It works with [[Emacs]], [[Vim]], [[Sublime Text]], and [[VSCode]].
- Folks who use Zettlr on top of Obsidian files for stuff like the [[Pandoc]] integration: [Zettlr 2.0 is entering beta](https://twitter.com/zettlr/status/1420750610807222294).
- Here’s a nice [free resource for learning git](https://git-scm.com/book/en/v2/).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-07-31%20Leveraging%20Graphs%2C%20a%20QuickAdd%20guide%2C%20%26%20Plugin%20Changelogs.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-07-31%20Leveraging%20Graphs%2C%20a%20QuickAdd%20guide%2C%20%26%20Plugin%20Changelogs.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
