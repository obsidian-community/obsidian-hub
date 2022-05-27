---
link: https://www.obsidianroundup.org/2021-01-01/
author: Eleanor Konik
published: 2022-01-01T13:30:00
publish: true
---

# 2022-01-01: Recipe Importing, Linking to Aliases, & Semantic Search
New daily notes templates, personal knowledge management guides, and new sync alternatives.

## In The Community

-   Here's a reflection on the difference between using [Obsidian vs. Roam for book clubs](https://www.maggiedelano.com/garden/obsidian-vs-roam-for-running-book-clubs).

## Obsidian Updates

Insider builds [v0.13.15](https://forum.obsidian.md/t/obsidian-release-v0-13-15-insider-build/29155), [v0.13.16](https://forum.obsidian.md/t/obsidian-release-v0-13-16-insider-build/29215) & [v0.13.17](https://forum.obsidian.md/t/obsidian-release-v0-13-17-insider-build/29522) added fun features like:

-   Edit mode now supports headings in lists (which allows better interoperability with programs like Logseq).
-   Switching between files will now keep the undo/redo history for the last 20 files, unless the file was changed externally. Not available for the legacy editor.
-   Improved behavior when pressing Enter in lists and blockquotes.

along with a bunch of bug fixes!

## Plugin News

### New in the Community List

-   [Advanced Slides](https://github.com/MSzturc/obsidian-advanced-slides) by `@MSzturc`  lets users create markdown-based presentations in Obsidian. They can be printed, have justified content, and more! If you installed this previously, make sure to check out the `1.2.0` update, which has a bunch of bugfixes.
-   [TagFolder](https://github.com/vrtmrz/obsidian-tagfolder) by `@vrtmrz`  will show tags in a folder-like manner.
-   [Obsidian Graphviz](https://github.com/QAMichaelPeng/obsidian-graphviz) by `@QAMichaelPeng`   lets uses render Graphviz Diagrams.

### Pending (as of Friday morning)

_Note: Most of these plugins are not yet available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool (BRAT)](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

-   [Rant-Lang](https://github.com/lanice/obsidian-rant) by `@lanice`  lets users use a code block with the rant type, in which you can enter a Rant program. The program is then compiled and executed with Rant, and the result shown in the Obsidian preview mode.
-   [Import Foundry VTT journal entries](https://github.com/farling42/obsidian-import-foundry) by `@farling42`  imports your journal entries from your selected Foundry virtual table-top.
-   [Tomorrow's Daily Note](https://github.com/frankolson/obsidian-tomorrows-daily-note) by `@frankolson`   is an obsidian plugin that creates tomorrow's daily note for preemptive planning.
-   [Indentation Guides](https://github.com/mgmeyers/obsidian-indentation-guides) by `@mgmeyers`   adds vertical lines to the editor denoting indentation level of lists and other content.
-   [TimeStamper](https://github.com/Gru80/obsidian-timestamper) by `@Gru80`  lets users insert customized time/date stamp, similar to the natural language dates plugin's functionality.
-   [Wrap with shortcuts](https://github.com/manic/obsidian-wrap-with-shortcuts) by `@manic`  will wrap let users create a hotkey to wrap selected text in custom tags, for example `<u>` or `<aside>`.
-   [Native Scrollbars](https://github.com/mgmeyers/obsidian-native-scrollbars) by `@mgmeyers`  enables native OS scrollbars throughout obsidian
-   [Plaintext](https://github.com/dbarenholz/obsidian-plaintext) by `@dbarenholz`  lets users open specified files as plaintext (RAW mode).
-   [Text-to-Speech Plugin](https://github.com/brainoverflow98/obsidian-text-to-speech-plugin) by `@brainoverflow98`  is a simple text-to-speech plugin which uses the Chromium's SpeechSynthesis API.

### Beta

_Note: these plugins have not yet been submitted for code review, and are being made available primarily for testing purposes._

-   The [cooklang importer](https://github.com/nothingislost/obsidian-cooklang-importer) brings us one step closer to Obsidian becoming a fully featured recipe manager. The developer hopes to one day improve the parser and merge the functionality into the "main" [cooklang plugin](https://github.com/deathau/cooklang-obsidian), but I've been using it. It's definitely an improvement over importing manually. I look forward to our community & the cooklang community one day sharing recipes between us in an open protocol sort of way. I _personally_ feel that there's huge potential here to compete with more expensive recipe (& shopping list) databases like plan2eat and paprika.
-   You can also do plain text accounting thanks to the [Ledger plugin](https://github.com/tgrosinger/ledger-obsidian), which just entered early beta.
-   You can now [import a JSON file and handlebars template](https://github.com/farling42/obsidian-import-json) to create a series of notes inside a named folder in your vault.
-   [Coalescer](https://github.com/geoffreysflaminglasersword/Coalescer) allows you to easily merge files, links, and tags with each other to better organize your vault.
-   [Remotely Save](https://github.com/fyears/remotely-save) supports mobile (especially iOS) to share notes between local device and S3, Dropbox, webdav, (OneDrive coming soon).
-   You can combine [Templater](https://discord.com/channels/686053708261228577/875720842443649045/926258548650942565)  and the new [Auto Linker](https://github.com/nothingislost/obsidian-auto-linker) plugin to have all of your filenames be prefixed with timestamps but all of your wikilinks be formatted with just the `[[words from the title]]` because it will link directly to the alias (which templater can create). I just started using it so that I can link to `[[2021.02.01 Bugs are cool]]` using a programmatically created alias, `[[Bugs are cool newsletter]]` for example, and there are other similar uses-cases folks might find handy as long as you don't tend to use the same alias for multiple files. I'm personally finding this _very_ useful when I'm annotating things in non-obsidian programs and don't have access to the quick switcher but do want to "link" to a particular file I remember the name of but not the number of... but am relying on numbers in the filename for sorting. Here's a [demo](http://discordapp.com/channels/686053708261228577/707816848615407697/920527336904986625) and further discussion about this.

### Updates

-   The [outliner plugin](https://github.com/vslinko/obsidian-outliner/releases/tag/2.0.0), [link favicons plugin](https://github.com/joethei/obsidian-link-favicon), [Image in Editor](https://github.com/ozntel/oz-image-in-editor-obsidian/releases/tag/2.0.1) and [LanguageTool](https://github.com/Clemens-E/obsidian-languagetool-plugin/issues) plugins now support Live Preview and the new editor.
-   [AnkiBridge 0.4.0](https://github.com/JeppeKlitgaard/ObsidianAnkiBridge) got better handling of multiple note types and allows for configuration of cloze deletion.
-   [Reading Time](https://github.com/avr/obsidian-reading-time/releases/tag/1.1.0) added a command to get the reading time of selected text.
-   The [Longform](https://github.com/kevboh/longform/issues/35) developer checked in; they're working on updates for Compile and are working on a big refactor to set up some future projects.
-   Dice Roller can now replace the note content with the result for all roller types, including section, table and tag rollers.
-   [Big calendar](https://github.com/Quorafind/Obsidian-Big-Calendar/releases/tag/0.2.1) supports adding event ✉️  in Calendar View now.
-   [Copy Publish URL](https://github.com/kometenstaub/copy-publish-url) now  supports opening the current note's Git commit history on GitHub, which enables convenient way for everyone who uses git for backups to access the full version history of a note.

### Under The Radar

-   Here's a discussion of [using a button to update a YAML value](https://www.reddit.com/r/ObsidianMD/comments/rre6wk/button_to_add_or_substract_from_yaml_or_dataview/) with [MetaEdit](https://github.com/chhoumann/MetaEdit).
-   The [Markmind](https://github.com/MarkMindCkm/obsidian-markmind) plugin has a neat outliner mode.
-   Don't forget that the [link converter](https://github.com/ozntel/obsidian-link-converter) can easily swap between `[markdown](links)` and `[[wikilinks]]` for a whole vault conversion.

## For Developers

-   `getSectionInfo()` is now implemented for custom code blocks in Live Preview.
-   Heads up to theme developers: the `.list-bullet` CSS has been reworked. It will now keep the original character and superimpose the dot using the `:after` pseudo-element.
-   Debugging Tip via `@pseudometa`: Name your fonts differently than the font you have installed on your system.
-   Consider adding your thoughts to the pending [Best Practices and Tips for Theme Development](https://github.com/obsidian-community/obsidian-hub/pull/191) hub note. Here's a guide for [how to do that via github](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/How+to+add+content+through+GitHub).
-   Here's a discussion about potential API changes [caching links and other content](https://github.com/obsidianmd/obsidian-api/issues/33) that is way too high level for me to understand, but developers should probably be aware of because `Modifying the persistent cache is hard but a simple interface for adding custom graph node relationships might be fairly painless to expose.`

## Appearance

-   [Obsidian Nord Enhanced](https://github.com/AidanGlickman/obsidian-nord-enhanced) by `@AidanGlickman`  and [Sandstorm](https://github.com/jaysan0/obsidian-sandstorm) by `@jaysan0`  are new :)
-   Shimmering Focus Version 1.479 has a new preset color scheme (Nord-ish), heading level indicators, built-in css classes, support for the [newly updated custom checkboxes snippet](https://github.com/SlRvb/Obsidian--ITS-Theme/blob/main/S%20-%20Checkboxes.css), and more.
-   [Minimal 4.3](https://github.com/kepano/obsidian-minimal/releases/tag/4.3.0) comes with settings for text labels for primary navigation, dataview column trimming, and a maximum width for dataview columns (along with other fixes and improvements). `@kepano` is looking for [translation help](https://discord.com/channels/686053708261228577/771575014382108672/926328555204403250), by the way.
-   [Sanctum](https://github.com/jdanielmourao/obsidian-sanctum/releases) got like four separate updates. It now a new "true black" mode, improved relationship lines in reading & editing views, heading level indicators, some font tweaks, and some bug fixes. Here's the [roadmap](https://github.com/users/jdanielmourao/projects/1/views/4).
-   [Sodalite](https://github.com/tomzorz/Sodalite/releases/tag/0.6.4) now supports Live Preview mode.
-   [Wyrd 0.3.0](https://github.com/curio-heart/obsidian-wyrd/releases/tag/v0.3.0) supports live preview and has its own print style now.
-   [ITS Theme](https://forum.obsidian.md/t/theme-its-dark-light-theme/12838/146) has a bunch of new style settings and toggles, a new color scheme (Nord), and live preview updates.
-   Here's a list of the code for the [default obsidian theme colors](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/Default+Obsidian+Theme+Colors), for folks who like the regular theme but just want to change the color from purple to, say, green ;).

## Feature Requests

-   Here's a feature request from the Sanctum theme developer to [add classes to navigation folders and list items](https://forum.obsidian.md/t/add-has-children-class-to-navigation-folders-and-list-items/29360).
-   Here's a discussion about [how search could be improved](https://www.reddit.com/r/ObsidianMD/comments/rr0478/poor_search_results_in_obsidian/).
-   An [improved tag-styling plugin](https://discord.com/channels/686053708261228577/702656734631821413/880750672906170408) would be awesome, and `@argentum` is happy to explain why.
-   Wouldn't it be neat if we could [search for plugins by author](https://forum.obsidian.md/t/search-for-plugins-by-author/29623)?
-   I would love it if the parser [let markdown syntax work inside more html tags so people don't keep creating non-standard workarounds](https://forum.obsidian.md/t/parse-markdown-inside-details-summary-tags/23764/2?u=argentum). Currently, people use `<s class>` tags instead of `<aside>` (which is more correct from an HTML standards perspective) because `<s class=aside>this is a **statement** okay</s>` parses correctly.

## Ancillary Code

-   Here's a templater script to turn all instances of `- [ ]`  in a selection to `- [>]` to indicate that [the task has been deferred](https://discord.com/channels/686053708261228577/875720842443649045/924023303537057812). Note that this works best with themes that have [alternate checkboxes](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.05+All+Community+Expansions/CSS+Snippets/Alternate+Checkboxes+(SlRvb)), like ITS and Sanctum.
-   Here's [a script to move things to a specific folder](https://gist.github.com/TfTHacker/79898dc50416e37a6b0e9542b042cc2e) (i.e. an archive folder), along with [documentation](https://forum.obsidian.md/t/quick-capture-mac-ios-and-inbox-processing/21808) for the workflow.
-   The new [Wordcount Dashboard](https://gist.github.com/chrisgrieser/ac16a80cdd9e8e0e84606cc24e35ad99#file-word-count-dashboard-md) uses accurate wordcounts instead of just estimates and will inherit the ordering of scenes from the longform plugin. Thanks to dataview's live-refreshing, the order even updates live.

## Guides

-   Here's a [collection of guides for personal knowledge management](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/for+Knowledge+Management). If you know of any other good ones, please consider [submitting them to the hub](https://publish.obsidian.md/hub/00+-+Contribute+to+the+Obsidian+Hub/%F0%9F%97%82%EF%B8%8F+00+-+Contribute+to+the+Obsidian+Hub).
-   Small tip: don't forget that you can [pin notes into the left and right sidebars](https://www.reddit.com/r/ObsidianMD/comments/rouvu5/notsopro_tip_pin_mocs_on_the_lefthand_side_to/), too, they aren't limited to just the panes!
-   Here's an [in-depth introduction into personal knowledge management and academic workflows](https://www.youtube.com/watch?v=kCOrqKrocCM) with Matthew Strother and Maggie Delano.
-   Here's a fun little tip for how to use `q` to [mark useful files](https://www.kungfugrippe.com/post/453204090/q-trick).

## Discussions

-   Someone on Twitter mentioned that they don't think it's possible for obsidian to have "as big a year as 2021."  [My take](https://twitter.com/EleanorKonik/status/1476889586194333707) was that there's still a lot of exciting ground to break in the notetaking app space that could revolutionize obsidian the same way that live preview and mobile (and dataview and templater and javalent's plugin suite) were such exciting moments. I invite you all to share what ideas _you_ have for exciting, revolutionary changes Obsidian could bring in 2022, either in [Discord](https://discord.com/channels/686053708261228577/694233507500916796/926447177281179699) or in the Twitter thread (or wherever, really, but I'll be monitoring those two places).
-   There was an interesting [twitter thread](https://twitter.com/syncretizm/status/1474586679646195712) about the drawbacks of outliners and how the breadcrumbs plugin + atomic notes (or, my contribution, [sections](https://twitter.com/EleanorKonik/status/1474739970178961412)) might be more suitable for zettelkasten-style hierarchies.
-   There was a very insightful discussion in Discord about [the pros and cons of different workflows for different purposes](https://discord.com/channels/686053708261228577/771575014382108672/926074710058471444).
-   [Daily Notes templates](https://www.reddit.com/r/ObsidianMD/comments/rpy21o/what_template_do_you_use_for_your_daily_notes/) have been a big discussion topic lately. Here's [mediapathic's daily notes template](https://gist.github.com/mediapathic/de12c8cd3e56633234cc2e426c6f3604).
-   Here's a nice [article about why a user moved away from UUIDs and aggressive automations](https://jamierubin.net/2021/12/08/de-automating-my-reading-notes-a-new-and-better-way-for-capturing-my-reading-notes-in-obsidian/) with their personal knowledge management in order to engage with the subjects they were reading more. Commenter `Clemens` pointed out that "requiring some manual interaction with information enhances your ability to draw valuable conclusions from it. It’s called disfluency."
-   Here's a good discussion about [one vault vs. multiple vaults](https://www.reddit.com/r/ObsidianMD/comments/rpqya5/1_vault_vs_multiple_vaults/) that I  plan to link to every time it comes up in Discord ;)
-   Here's why you might want to [create a knowledge base if you're moving to a new job](https://offbyone.us/posts/new-job-knowledge-base/).
-   There was a wonderful discussion about [different ways to structure notes](http://discordapp.com/channels/686053708261228577/710585052769157141/925739231635206194) that touches on some insightful reasons (and ways) to "file" notes next to relevant notes, [[Zettelkasten]] style.
-   Here's a discussion (complete with nice infographics) about [how to get information from various formats](http://discordapp.com/channels/686053708261228577/710585052769157141/924193628325306418) (i.e. books, ebooks, pdfs, articles) into Obsidian without duplicating content.

## Ancillary Tools

-   Here's a [script to use MKDocs with Obsidian vault for publishing](https://github.com/Mara-Li/mkdocs_obsidian_template), and another [free lightweight obsidian publisher](https://github.com/PabloLION/free-lightweight-obsidian-publisher) for Mac/zsh users.
-   MarkText might be a viable alternative to Typora if folks were looking for a markdown editor with "wysiwyg" mode for their second screen. Here's the [Hacker News discussion](https://news.ycombinator.com/item?id=29687061) and here's the [Obsidian Discord discussion](http://discordapp.com/channels/686053708261228577/700466324840775831/924632180146188288).
-   [OpenAI Embeddings](https://github.com/bramses/openai-embeddings-ts) is a program that basically indexes your obsidian files into a database and lets you use "smart" plain-language search to find stuff in your vault (or other plaintext files). It is currently under active development, and if you've ever been curious about the kind of work I do to translate what the devs are doing into plain English to share with you, [this was a particularly good example](https://discord.com/channels/686053708261228577/840286264964022302/926469843790757920).
-   [Mega.nz](https://mega.nz/)  is a New Zealand based cloud service that gives 20GB of storage to a free user, and the files are encrypted while they’re on their servers. Folks [confirmed that it works with Windows/Android](https://forum.obsidian.md/t/meta-post-syncing-between-devices/20983/23?u=eleanorkonik).
-   [Scholarcy](https://twitter.com/scholarcy/status/1471444464975728647) distills research papers into interactive flashcards and lets users get key findings & citation links. It allows for reading, sharing, and annotation — and has a PDF to Markdown feature. They recently  added image extraction to the markdown output, along with the key concepts, findings, pull quotes and linked references.
-   Here's a cool trick for the cross-platform text expander [espanso](https://espanso.org/) that lets users [keep line breaks from automatically sending the message](http://discordapp.com/channels/686053708261228577/694233507500916796/920753193355452557).

## Personal

Thanks to how many of you guys were interested in [Refind](https://refind.com/?utm_source=newsletter&utm_medium=barter&utm_campaign=Mn6vY1aQFu5DtmSrH9P7sg) ("The essence of the web, every morning in your inbox") when it got mentioned because it syncs to Readwise (which syncs to Obsidian), the developer invited me to curate a deep dive into [the history of food](https://refind.com/EleanorKonik/the-history-of-food). I'm pretty stoked about it, and the developer was impressed at how fast I was able to get it written, thanks to my Obsidian notes ;)

Refind's thing is that they try to summarize and offer overviews of things you might be interested in. It's mostly focused on getting machine learning algorithms to find you articles you're likely to enjoy, but there are also hand-curated lists and some interesting database features. I mostly use it for the ability to search a database that's limited to interesting longform articles (i.e. not the SEO dreck I get from most search engines).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-01-01%20%20Recipe%20Importing%2C%20Linking%20to%20Aliases%2C%20and%20Semantic%20Search.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-01-01%20%20Recipe%20Importing%2C%20Linking%20to%20Aliases%2C%20and%20Semantic%20Search.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
