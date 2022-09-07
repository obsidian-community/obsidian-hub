---
link: https://www.obsidianroundup.org/2021-04-24/
author: Eleanor Konik
published: 2021-04-24
publish: true
---

# 2021-04-24: Inline Dataview, Showcases, & a Markdown GUI.
Big Obsidian updates for the API, search, and tasks. Lots of Dataview improvements, some nice Spaced Repetition options, and tools to help developers. CSS tips & PKM discussions.

## In The Community

- The 2nd community talk will be **Zotero 101** with `@argentum` on **Saturday 24th at 16:00 CET**. You can check the time of the talk in your local time [here](https://sharing.clickup.com/c/h/4gdf2-36/5b21a6f8588e5c6).
- Nick Milo posted the 2021-04-17 community session with Tres Brenan, creator of [[dataview|Dataview]], to his [Obsidian Publish site](https://publish.obsidian.md/lyt-kit/Timestamps/2020-04-17+-+Dataview). I took part in the showcase portion, and there was a Q&A as well.
- [Effective Remote Work](https://www.youtube.com/watch?v=_cbB-7Ouudk) has a video about the iOS app for Obsidian.

## Obsidian Updates

the new Insider build [v0.12.0](https://forum.obsidian.md/t/obsidian-release-v0-12-0-insider-build/16809) went live and it was a big one. Definitely read the release notes to get an idea of what's coming if you haven't already, but the short version is:

- you can now use `task` as a search parameter (similar to `block:`), along with `task-todo:` for only unchecked tasks. Tasks aren't limited to `[x]` anymore: you can use custom characters and target them via CSS.
- Search and backlinks are a lot more useful, plus you can get backlinks inside a document on preview mode (edit mode pending a future release).
- You can increase and decrease font size without messing with CSS.
- Lots of improvements to how plugins get enabled and how they handle safe mode.
- Some stuff that will matter to developers, especially theme developers.

Note: it usually takes a week or two for insider builds to go live to everyone.

## Plugin News

- The update that has made the biggest difference to me _personally_ (especially for this roundup) is [[obsidian-auto-link-title|Auto Link Title]] which lets you paste a URL and automatically have it turn into a markdown link with the link's actual title.
- [[obsidian-charts|Obsidian Charts]] via `@doge` now has a GUI to create charts, as well as a live preview option, to make it easier to use.
- [Juggl 1.0.5](https://github.com/HEmile/juggl/releases/tag/1.0.5) is out now, with some additional options and a fix for the empty panes in the right sidebar.
- `@zsviczian` has forked Lars Lockefeer's Obsidian GTD plugin and extended it to add a bunch of features. It's not in the community repo yet, but v0.6 is on [github](https://github.com/zsviczian/Obsidian-GTD-plugin/releases/tag/v0.6).
- `@zsviczian` is also working on an [Obsidian plugin for Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin). I believe it's currently in alpha and not yet available in the community repo but the developer is looking for feedback (via github issues preferred).
- [[obsidian-markdown-formatting-assistant-plugin|Markdown Formatting Assistant]] lets you use snippets for [[Markdown]], [[HTML]] and [[LaTeX]] and a color picker which shows the history of last used colors. It's not new but it's flying under the radar and will probably make a lot of people waiting for WYSIWYG happy.
- There is a new version of the [[obsidian-spaced-repetition|Spaced Repetition]] plugin ([v1.3.0](https://github.com/st3v3nmw/obsidian-spaced-repetition)). It adds support for flashcards that will help keep them from going out of sync. `@bookthief` [described it](https://discord.com/channels/686053708261228577/707816848615407697/833907413764800567) as a "native SRS flashcards plugin."
- There were multiple big updates for [[dataview|Dataview]] this week. [0.2.10] https://github.com/blacksmithgu/obsidian-dataview/releases/tag/0.2.10] added inline fields. [0.2.13](https://github.com/blacksmithgu/obsidian-dataview/releases/tag/0.2.13) allows for views to auto-reload at a configurable interval. Here are some examples: [via arminta7](https://discord.com/channels/686053708261228577/707816848615407697/834485643660099606), [via SkepticMystic](https://discord.com/channels/686053708261228577/707816848615407697/834390000388931604).
- `@mano` made a plugin that allows for a vertical tabs feature: [[koncham-workspace|koncham workspace]]
- `@foreveryone` had a useful explanation of how to split workspaces when using the [Tabs](https://github.com/gitobsidiantutorial/obsidian-tabs) plugin.

### For Developers

- There are some [changes coming to the API](https://github.com/obsidianmd/obsidian-api/commit/0a4b7f048944ff1a7f7603d611f4d7081288e358) that will impact how sections are handled. They're currently live on the Insider release. Discussion [here](http://discordapp.com/channels/686053708261228577/707816848615407697/833482342785875999). For discussion of how to actually deal with this, start [here](https://discord.com/channels/686053708261228577/707816848615407697/835190229794160681).
- `@zephraph` put together some tools for [programmatically working with plugins](https://discord.com/channels/686053708261228577/707816848615407697/833558301928325132). There's also an [unofficial collection of CLI tools](https://github.com/zephraph/obsidian-tools/tree/main/packages/obsidian-plugin-cli) that helps you build plugins for Obsidian. [Apparently](http://discordapp.com/channels/686053708261228577/707816848615407697/833562130698862603) it'll prompt you for which vault you want to develop in (via a select list; it finds all your vaults), sets up and automatically copies over built code, and prompts to you to install the `hot-reload` plugin if you haven't already (it'll do that for you automatically too). It'll even copy over the manifest file if any changes happen to that.
- There was a nifty [discussion] of what people use to [handle documentation for their plugins](https://discord.com/channels/686053708261228577/707816848615407697/833956511897223208).

## Feature Requests

- `@murf` created a [feature request for zooming into headers/headings](https://forum.obsidian.md/t/zoom-into-headers-like-most-outliners-do-with-bullets/17060) similar to how you can zoom into bullets using the [[obsidian-outliner|Outliner]] plugin. Currently the closest you can get is the Outline (not Outliner) plugin, which lets you jump to headers.
- `@arminta` had an [idea for a plugin](http://discordapp.com/channels/686053708261228577/707816848615407697/833106154619666433) that would allow for a way to see what frequently used terms have _not_ yet been linked, to help surface connections that are not necessarily obvious.

## Workflow Stuff

- We've gotten a couple of people asking about how (and whether) people in the medical profession can leverage Obsidian to their advantage. Here's a [graph](https://ptb.discord.com/channels/686053708261228577/709712341066842113/830508714007986269) that focuses on medical/anesthesia knowledge. There was also a reddit thread of [people discussing how they use Obsidian for medical stuff](https://www.reddit.com/r/ObsidianMD/comments/mw1pgw/is_anybody_here_a_medical_student/?utm_medium=android_app&utm_source=share).
- Here's a blog post from `@ton` about how to use Obsidian for [customer relationship management](https://www.zylstra.org/blog/2021/02/personal-crm-as-a-not-linkedin/) ([[Customer Relationship Management|CRM]]). They also have a nifty blog post about how Obsidian has led to a change in their [tagging practice](https://www.zylstra.org/blog/2020/10/new-emergent-tagging-practice/)
- There was as little mini share-and-showcase in Discord for [project workspaces](https://discord.com/channels/686053708261228577/694233507500916796/834897381388189748).
- `@arminta7` put together a really nice example of how she uses [[dataview|Dataview]] [for tasks and projects](https://forum.obsidian.md/t/dataview-task-and-project-examples/17011) with a video and handy links to other useful resources.

## Tips & Tricks

- You can insert page breaks into exported PDFs with the following: `<div style="page-break-after: always;"></div>` (via `@Oliver Balfour`
- [Stack Overflow](https://stackoverflow.com/questions/5612105/add-text-to-the-end-of-each-file-with-notepad-and-regex) has an explanation of mass append a new tag to the bottom of a series of files (preferably in a folder) with [[Notepad++]] but MAKE SURE YOU MAKE A BACKUP FIRST, it's easy to mess up. You can probably do something similar with [[VSCode]] if you need to.
- There was a discussion on Reddit that covered [tips and tricks for using](https://www.reddit.com/r/ObsidianMD/comments/mui5q3/has_any_vim_or_vimlike_user_gotten_comfy_yet/) [[Vim]] with Obsidian.
- There's a new share & showcase for [Note and metadata/YAML templates](https://forum.obsidian.md/t/note-and-metadata-yaml-templates-snippets-showcase/16953) that is intended to serve as a handy meta thread for [[dataview|Dataview]], [[templater-obsidian|Templater]] ( see also: [this showcase](https://forum.obsidian.md/t/templater-plugin-script-collection/17010) from `@pmbauer`)), and [[🗂️ Daily notes|Daily note templates]].

### CSS

- `@foreveryone` figured out how to use CSS to let you create [an inline block embed](https://discord.com/channels/686053708261228577/702656734631821413/833195228940075048). There was a whole discussion about best practices and options so I'm linking you to discord instead of trying to find it on github.
- [This CSS](https://discord.com/channels/686053708261228577/702656734631821413/829852861776134176) from [[SlRvb]] will allow header titles to wrap, which is great for long titles and small screens.
- [[SlRvb]] has a nice update to [aside tag CSS](https://discord.com/channels/686053708261228577/702656734631821413/832944617368322089) that handles maximum width and overlapping aside boxes really smoothly.
- There are a couple of different ways to [caption a local image](https://forum.obsidian.md/t/why-isnt-there-a-way-to-add-a-caption-to-a-local-image-in-one-of-my-obsidian-markdown-notes/16358/3) with Obsidian.
- You can use CSS to [color-code folders](https://forum.obsidian.md/t/adding-color-to-obsidian-a-rainbow-of-possibility/12805/11) thanks to `@Lithou`.
- There's a nifty new way to do [highlights](https://github.com/steveyang331/Obsidian-css/tree/main/8%2B8%20highlight%20colors). There are more [examples on Discord](https://discord.com/channels/686053708261228577/744933215063638183/834866132887535627)

### [[Obsidian Publish|Publish]]

- For [[Obsidian Publish]], it's possible to [hide the file name using CSS](https://discord.com/channels/686053708261228577/768134314864017429/798866681862029352), which is useful if you prefer to use the title from a header.
- You can [add custom analytics](https://just-be.dev/notes/Obsidian/Publish) to publish pages using custom javascript if you have a custom domain.

## PKM Tips

- There was a fun [discussion about different ways to conceptualize maps of contents / indexes](https://discord.com/channels/686053708261228577/744933215063638183/833472754006884393). Actually there were [two](https://discord.com/channels/686053708261228577/710585052769157141/833714262643703891). It's a popular topic.
- `@joshduffney` put together a substack post about [how to leverage Obsidian for smart notetaking](https://knowledgework.substack.com/p/how-to-take-smart-notes-in-obsidian) that is pretty comprehensive and people seemed to enjoy.
- There was a lengthy discussion about [how to use Obsidian for studying for an upcoming AP exam](https://discord.com/channels/686053708261228577/722584061087842365/834046085583863848) that might be useful for students.
- Andy Matuschak had a discussion with a redditor over at the Slate Star Codex subreddit that was really interesting about [the nature and purpose and value (or lack thereof) of reading nonfiction books](https://www.reddit.com/r/slatestarcodex/comments/mvs0vf/what_books_are_for_a_response_to_why_books_dont/) that touches on the importance of engagement and salience.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- [Research Rabbit](https://researchrabbitapp.com/) had a big update that makes it a lot easier to use for discovering relevant scholarly articles on a topic.
- [Gingko](https://gingkoapp.com/) is fairly popular in this community: it's a tool that lets you do lists, outlines, and cards in a clean pyramid-like interface.
- There was a nice discussion on Reddit about [other tools Obsidian users might enjoy](https://www.reddit.com/r/ObsidianMD/comments/mvslt6/any_other_gems_like_obsidian/).

## Housekeeping

- I fiddled a bit with the email that this "officially" comes from, so now it should be possible to directly reply to this email so that it'll send to my personal email address (ek@eleanorkonik.com)

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-04-24%20Inline%20Dataview%2C%20Showcases%2C%20%26%20a%20Markdown%20GUI.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-04-24%20Inline%20Dataview%2C%20Showcases%2C%20%26%20a%20Markdown%20GUI.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
