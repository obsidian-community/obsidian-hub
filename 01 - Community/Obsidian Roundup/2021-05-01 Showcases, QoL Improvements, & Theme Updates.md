---
link: https://www.obsidianroundup.org/2021-05-01/
author: Eleanor Konik
published: 2021-05-01
publish: true
---

# 2021-05-01: Showcases, QoL Improvements, & Theme Updates
The Community Talks are ramping up, there were lots of great little plugin updates especially in the "importing things as markdown" space, and we're starting to see some organized writeups about workflows that utilize dataview and templater.

## In The Community

- Obsidian Mobile is now available for all tiers of Obsidian Catalyst.
- `@Wace` will be presenting [Notetaking for Community Students](https://forum.obsidian.md/t/notetaking-for-university-students-community-talk-by-wace/17007) at 11:30 EST.
- [Voting for the date/time](https://forum.obsidian.md/t/leveraging-metadata-and-bending-markdown-community-talk-by-tallguyjenks/17070) of the [Leveraging Metadata and Bending Markdown](https://forum.obsidian.md/t/leveraging-metadata-and-bending-markdown-community-talk-by-tallguyjenks/17070) community talk via `@tallguyjenks` is currently underway.
- [Voting for the date/time](https://www.when2meet.com/?11752321-UHqgS) of the [Deep Learning on Networks](https://forum.obsidian.md/t/deep-learning-on-networks-community-talk-by-phnx/17235)] community talk by `@phnx` is currently underway.
- [Voting for the time slot](https://www.when2meet.com/?11790436-pKi9l) of the [Knowledge Organization, Cataloging and Classification in Obsidian](https://forum.obsidian.md/t/knowledge-organization-cataloging-and-classification-in-obsidian-community-talk-by-brimwats/17442) talk by `@bri` is now open.
- [[templater-obsidian|Templater]] now has [a showcase on github](https://github.com/SilentVoid13/Templater/discussions/categories/templates-showcase) where people can share useful [[templater-obsidian|templater]] scripts. `@Murf` also has some [gists](https://gist.github.com/GitMurf) that seem like useful [[templater-obsidian|templater]] scripts.

## Plugin News

### Updates

- [[obsidian-imgur-plugin|Imgur Plugin]] [v1.1.0](https://github.com/gavvvr/obsidian-imgur-plugin/releases/tag/1.1.0 "https://github.com/gavvvr/obsidian-imgur-plugin/releases/tag/1.1.0") is out. You can now upload on 'drag-and-drop' which enables uploading gifs and multiple files.
- Page preview now works in [[obsidian-kanban|Kanban]]. You can also do "new note from card." There are settings for specifying a template and output folder for new notes. `@Santi Younger` put together a [[YouTube|YouTube Video]] to explain [how to get the most out of visual boards](https://www.youtube.com/watch?v=vRZXT4ynKxE&lc=UgxqaLTyYyb27cjTwkZ4AaABAg).
- The [[obsidian-kindle-plugin|Kindle Highlights]] now brings in notes along with highlights. The developer is really responsive to requests and the plugin saw a lot of other quality of life improvements. There's an (unreleased) working prototype for importing from myclippings.txt as well, which will allow this to be used for books not officially connected to the Amazon account. Here's an [example](https://discord.com/channels/686053708261228577/744933215063638183/836759090762874900) of the plugin in action!
- [[argenos]] and [[liamcain]] released [v0.5.0](https://discord.com/channels/686053708261228577/707816848615407697/836333522921717793) of the [[nldates-obsidian|Natural Language Dates]] plugin, with a keyboard-friendly date picker, improved date autosuggestions that uses `@`, and more.
- The [[extract-url|Extract URL plugin]] now has [special support for youtube videos](https://forum.obsidian.md/t/extract-url-plugin-0-8-extended-youtube-support/17131). Extracting channel name and description as well.

### Releases

- This [[obsidian-filename-heading-sync|plugin]] plugin will keep the filename and the first heading of a file in sync. Straightforward, but convenient!
- [[obsidian-recall|Recall]] is a [[Spaced repetition]] plugin that just entered early-release (manual install required). It allows the use of different algorithms and lets you track or untrack notes.
- [[ryanjamurphy]] put together the [Enlightment](https://github.com/ryanjamurphy/enlightenment-obsidian) plugin, which greys out things you aren't focused on. I think the pull request to get it into the community plugins list is pending.
- [[obsidian-excalidraw-plugin|Excalidraw]], a full featured sketching plugin in Obsidian is [now available in the community plugins list](https://forum.obsidian.md/t/excalidraw-full-featured-sketching-plugin-in-obsidian/17367).
- `@mrjackphil` put together a plugin that will let you [copy markdown/obsidian links](https://github.com/mrjackphil/obsidian-copy-search-link) from the file explorer or search bar as a markdown or wiki link (instead of just the obsidian URI), as well as the header from the first result of a search, which is pretty nifty. Requires manual install.
- `@mrjackphil` also put together this nifty plugin to allow [outliner-style zooming in on headers](https://github.com/mrjackphil/obsidian-zoom-in-headers). It also requires manual install, but the directions are essentially the same.

### For Developers

- [[ryanjamurphy]] put together a [guide on getting started fiddling with plugins](https://forum.obsidian.md/t/plugins-mini-faq/7737/26?u=ryanjamurphy).

## Feature Requests

- There's a [feature request](https://forum.obsidian.md/t/inline-intext-yaml-fields/17092) for Obsidian to provide functionality similar to dataview with the inline YAML fields in core that is being discussed on the forums (there are pros and cons).
- A couple of people are interested in a way to [hide YAML metadata in edit mode](https://forum.obsidian.md/t/hiding-yaml-in-edit-mode/17394).

## Workflow Stuff

### [[dataview|Dataview]]

- Here's an explanation of how to [Replicate Notions' tables with Obsidian](https://input.sh/replicating-notions-tables-with-obsidian-plugins/). `@riddyrayes` also put together a [writeup for how to leverage dataview for relational databases](https://forum.obsidian.md/t/toying-with-relational-databases-using-dataview/17433?u=riddyrayes), so the possibilities here are definnitely capturing people's imagination.
- `@arminta7` has a useful description of why she likes dataview's new [inline YAML fields](http://discordapp.com/channels/686053708261228577/707816848615407697/835396767066488842) functionality and how she uses it.
- `@arminta7` also put together a [writeup about how she uses dataview for processing media](https://forum.obsidian.md/t/dataview-for-reviewing-and-processing-media/17136). It includes her roundup of related posts, such as how she uses [[dataview|Dataview]] for tracking fitness, task management, and daily/weekly reviews. Her CSS is available [here](https://forum.obsidian.md/t/my-theme-and-custom-css-clean-and-notion-like/17140).

### Academic

- for Apple: This [DEVONthink, PDF, Bookends References, and Obsidian summary notes script/workflow](https://axle.design/connect-devonthink-pdfs-bookends-references-and-obsidian-summary-notes-with-this-script) by `@ryanjamurphy` got resurfaced. PS: [DevonTHINK added support for Obsidian transclusions](http://discordapp.com/channels/686053708261228577/694233507500916796/837610035902283787).
- `@smithtjosh` was kind enough to share a [guide](https://docs.google.com/document/d/1Ti90jJG2b9cnKbOoGZyT6ve5P_iyhva6lLRrlL9sCek/edit#heading=h.jcidduny8pla) they wrote in a professional capacity. It's aimed at college students doing research, but covers some useful stuff about customizing search engines, using zotero, notetaking in general, and more!
- [[argenos]] put together a bunch of really helpful [notes with tips and tricks about Zotero](https://publish.obsidian.md/argenos/).
- `@cat` put together some [nifty placeholders for Zotero](https://discord.com/channels/686053708261228577/722584061087842365/836340716485476373) that utilize [[dataview|Dataview]]'s inline fields.

## Tips & Tricks

### [[dataview|Dataview]]

- Dataview allows for basic `if then` statements. Here's an [example](https://discord.com/channels/686053708261228577/694233507500916796/835867022780530758).
- When you use `group by` in Dataview you also need to use `rows` — `@SkepticMystic` explains it better than I can on [the forum](https://forum.obsidian.md/t/dataview-plugin-snippet-showcase/13673/93).

### CSS Tips

- There's a new theme in town from the maker of [[Obsidianite]]: [Aurora](https://github.com/auroral-ui/aurora-obsidian-md).
- `@manedblackwolf` is working on adding [link icons](https://discord.com/channels/686053708261228577/702656734631821413/835824144414539787) (i.e. for Twitter, YouTube, etc.) to the [[Spectrum]] theme.
- [[deathau]] put together a [CSS snippet for differentiating different types of tasks/checkboxes](https://github.com/deathau/obsidian-snippets/blob/main/checkbox.css) (made possible in obsidian 0.12.0). There's a [preview](https://discord.com/channels/686053708261228577/702656734631821413/836099935874056193) example.
- If you want to be able to [check off a 'parent' checkbox but not the 'child' checkboxes](https://www.reddit.com/r/ObsidianMD/comments/mqndbf/is_there_a_way_to_have_a_note_after_a_checked/gup4eiq/), `@CurioHeart` has a workaround that will allow something along these lines.
- `@Mara` was able to use the [clutter-free formatting](https://github.com/deathau/obsidian-snippets/blob/main/clutter-free-formatting.css) CSS and the [image-in-editor plugin](https://github.com/ozntel/oz-image-in-editor-obsidian) to [emulate WYSIWYG](https://discord.com/channels/686053708261228577/702656734631821413/836505456024354826) really well.
- If you want to [show specific languages in specific fonts](http://discordapp.com/channels/686053708261228577/702656734631821413/837628984580767764), you can use the Unicode range descriptor to do so.

### [[Obsidian Publish|Publish]]

- There was a discussion about [how to get a custom theme on a Publish site](https://discord.com/channels/686053708261228577/768134314864017429/835576825253986385).
- `andrioid` put together a blog post about [how to use Obsidian, Gatsby, and Nextcloud](https://andri.dk/blog/2021/blogging-with-obsidian-gatsby-and-nextcloud) to self-host a blog written in Obsidian. It's fairly technical.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- [Story Graph](https://app.thestorygraph.com/) was recommended as a goodreads alternative that isn't beholden to Amazon tracking.
- For folx who don't trust websites to stay where they are, [ArchiveBox](https://archivebox.io/) bills itself as an open source self-hosted web archiver. It takes URLs/browser history/bookmarks/Pocket/Pinboard/etc., and saves HTML, JS, PDFs, media, etc.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-05-01%20Showcases%2C%20QoL%20Improvements%2C%20%26%20Theme%20Updates.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-05-01%20Showcases%2C%20QoL%20Improvements%2C%20%26%20Theme%20Updates.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
