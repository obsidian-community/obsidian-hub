---
link: https://www.obsidianroundup.org/2021-11-13-wysiwyg-called-live-preview-is-here/
author: Eleanor Konik
published: 2021-11-13T13:11:00
publish: true
---

# 2021-11-13: WYSIWYG (called "Live Preview") is HERE!
Beta test a new Scrivener corkboard alternative, "CorkBoard." Manage your recipes in Obsidian with CookLang. 9 themes updated!

## Obsidian Updates

-   WYSIWYG Mode is here! Known as "Live Preview" because "WYSIWYG" means different things to different people, Insiders can enable this _experimental_ feature. It does _not_ work identically to what you might expect from the Codemirror Options plugin, because it uses the Codemirror6 editor, not Codemirror5.

### Release Notes

**Live Preview (also known as “WYSIWYG” mode) is [now available](https://forum.obsidian.md/t/obsidian-release-v0-13-0-insider-build/26919) for insider testing.** To enable it, go to `Settings > Editor > Experimental Live Preview`. Changing this option requires a restart to take effect. The list of known bugs can be found [in Discord](https://discord.com/channels/686053708261228577/716028884885307432/908079085257908234). Please report bugs in the `Live Preview bug reports` thread in Discord.

Current features:

-   Hide markdown formatting syntax.
-   Embedded notes, images, audio, video, PDFs and notes using the wikilink syntax will show a preview in the editor.
-   Embedded images using the markdown syntax from external sources will show previewed.
-   Block `($)` LaTeX will show a preview. Inline LaTeX will be implemented in a future release.
-   Checklists will be replaced with a checkbox. Clicking on it will toggle the check status. Checkboxes have a `data-task` attribute added.
-   Separators (---) are now implemented.
-   Headings will now always show the # characters when the cursor is on that line.
-   Added external link icon.

Some notes:

-   "Source mode" is not the same as the old CM5 editor mode. Currently, "source mode" is bare bones CM6 with Live Preview mode disabled.

### FAQ

#### What will happen to the "old" editor?

-   via `@Licat` [CM5 will eventually be deprecated into a "legacy" mode](http://discordapp.com/channels/686053708261228577/716028884885307432/908117730006269962), and maybe in a few years we will stop shipping with it.

#### What about VIM?

-   Vim in Obsidian core depends on the vim features in Codemirror 5, which have yet to be ported to Codemirror 6. Here's [the discussion about why not](https://github.com/codemirror/codemirror.next/issues/79).
-   Here is a forum [discussion about some possible alternative ways to support vim](https://forum.obsidian.md/t/vim-support-for-the-new-editor-codemirror-6-neovim-libvim-or-something-else/21803) mode in the new editor.
-   Windows users may be able to use this [vim emoulation](https://github.com/pit-ray/win-vind) that works on top of windows controls.

## Plugin News

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

### New

-   [CookLang plugin](https://github.com/deathau/cooklang-obsidian) adds support for the recipe markup language cooklang in Obsidian.
-   [Sentence Navigator](https://github.com/timhor/obsidian-sentence-navigator) lets you manipulate sentences as a unit of movement. Select, move and delete by whole sentences.
-   [Obsidian Chevereto Image Uploader](https://github.com/kkzzhizhou/obsidian-chevereto-image-uploader) can resize and upload the image in your clipboard to chevereto (Self-hosted Image Hosting Software) when pasting.
-   [Obsidian Structure](https://github.com/dobrovolsky/obsidain-structure) allows users to create dendron-like hierarchy using `.` based structure, i.e. `aws` and `aws.ec2`
-   [Obsidian Bible Reference](https://github.com/tim-hub/obsidian-bible-reference) automatically inputs text from the bible when you input chapter & verse information.
-   [Downfile](https://github.com/WHG555/obsidian-downfile) is designed to help users in mainland China to download third-party themes and plugins when there are some connection problems.

### Updates

-   [0.5.7 Beta of BRAT](https://github.com/TfTHacker/obsidian42-brat/discussions/16) lets users beta test themes, update beta themes, install themes from the command palette, switch to different installed theme from the command palette (making it easy to test bugs on the default theme), update logging, and more. There is also a new "All commands" command, which should be useful on mobile.
-   [Readwise Official 2.0](https://twitter.com/readwiseio/status/1457776445015552008) supports mobile sync, customizable folder & file names, individual file resyncing, improved templating, and "quieter" sync notifications. There were also some bugfixes, so if you were having trouble, check out the update.
-   [Graph Analysis](https://github.com/SkepticMystic/graph-analysis) can now add links to any file type to its index; images, Word docx, PDFs, etc. You can also filter out specific notes in Graph Analysis
-   [Obsidian Trello v1.6.0](https://github.com/OfficerHalf/obsidian-trello/releases/tag/1.6.0) allows markdown in trello comments, card descriptions, and checklists to be rendered
-   CodeMirror Options 0.8.x supports rendering embeds in edit mode.
-   [Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/1.3.0) v1.3.0 supports searching by tags.

### Betas

-   [CorkBoard](https://github.com/jmilldotdev/obsidian-corkboard) is a visual canvas for your notes that lets you mimic the Scrivener corkboard. You can add a pile of random cards, either from your whole vault or from a search, replace cards by typing paths or with new random cards, drag and drop cards, & make visual links between cards on the board. I have not yet personally tried it out, but only because I'm buckled down for national novel writing month. v0.2.0 got some bugfixes and fancy tag styling, improved integrations with the daily notes & periodic notes plugins, and improvements to the tag board.
-   [Auto Class v1.3.0](https://github.com/OfficerHalf/obsidian-auto-class) now supports for linked panes
-   [Exclidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.4.8-beta) support for the Live Preview (available to Insiders) is available as a beta via BRAT.

### Under The Radar

-   You can [add a button for mobile that opens the quick switcher](https://github.com/kometenstaub/quick-switcher-button).

### For Developers

-   There was a [forum discussion about how plugin developers could make their plugins more secure](https://forum.obsidian.md/t/community-plugin-security-hint-and-quality-gate/26227/5) which included a section on how [users can review their plugins for security vulnerabilities](https://snyk.io/test/).
-   There's a [new bash script](https://github.com/selfire1/obsidian-plugin-quickcreator) designed to help automate some of the more finnicky parts of plugin development, like forking the sample plugin and creating release files.
-   via `@Licat` — Plugin devs should absolutely [start migrating to Editor](http://discordapp.com/channels/686053708261228577/716028884885307432/908117908255834122) if possible, if they were using CM5's editor directly.
-   There is now an append function for both the `Vault` and the `Adapter` APIs.
-   There is now a function to sanitize HTML called `sanitizeHTMLToDom` which returns a `DocumentFragment` of the sanitized HTML content.
-   You can now `setInstructions` for an `EditorSuggest`.
-   There is now a `wordAt` function on the Editor interface.

## Feature Requests

-   Some folks would really like a [critic markup plugin](https://forum.obsidian.md/t/critic-markup/18485).
-   [note inheritance inspired by object oriented programming](https://forum.obsidian.md/t/note-inheritance-and-making-notes-into-nodes/26844)
-   [allow users to set custom default settings for all new vaults](https://forum.obsidian.md/t/custom-default-vault-settings/6613).
-   There were some requests for [improvements to the Publish UI](https://forum.obsidian.md/t/publish-ui-collapse-expand-folders/25668/3).

## Appearance

### Snippets

-   It is now possible to [hide your metadata container in preview](https://discord.com/channels/686053708261228577/702656734631821413/908197190638374912) with a small button that can be toggled.
-   Here's the [Live Preview Companion](https://github.com/Mara-Li/Obsidian-Snippet-collection/blob/main/CM6_LivePreview.css) designed to clean up tags and reduce some visual clutter.
-   Here's [another snippet](http://discordapp.com/channels/686053708261228577/716028884885307432/908080331905728583) to add more visual noise reduction to Live Preview.

### Theme Updates

-   [Sanctum v0.3.1](https://github.com/jdanielmourao/obsidian-sanctum/releases) got a bunch of small updates, and some new cssclasses, including support for list-only kanbans and custom checkbox admonitions. There are a bunch of new task/checkbox options, the option to color-code headers, and improved support for [[Obsidian Publish]]. Here's the [roadmap kanban](https://github.com/jdanielmourao/obsidian-sanctum/projects/1).
-   The [ebullientworks theme](https://github.com/ebullient/obsidian-theme-ebullientworks) now supports floating frontmatter via stylesettings, small tweaks, and a change to checkboxes so that they color the border & contents instead of filling them. There are also two dropdowns in style settings to choose primary/secondary accent color. Header fonts are now in style settings, admonitions should be easier to style/color in CSS (vs. the panels).
-   [Primary v0.1.1](https://github.com/ceciliamay/obsidianmd-theme-primary/releases/tag/v0.1.1) & [Primary v0.2.0](https://github.com/ceciliamay/obsidianmd-theme-primary/releases/tag/v0.2.0) has a bunch of fixes & features intended to improve the experience on mobile.
-   [Minimal 4.0.8](https://github.com/kepano/obsidian-minimal) now has improved support for Dictionary, Git, Excalidraw, Dataview & Outliner plugins.
-   [Spectrum Version 1.0.0](https://github.com/Braweria/Spectrum) got a _bunch_ of features, including fancy list stylings, image floats, table styling, and new checkbox types.
-   [ITS](https://forum.obsidian.md/t/theme-its-dark-light-theme/12838/138) has a bunch of small improvements, new Style Settings toggles, support for Alternate Checkboxes & Codemirro Options pluins, and more.
-   [Bubble Space Theme v0.1.1](https://github.com/Emrie-Candera/Bubble-Space-Theme/releases/tag/v0.1.1) comes with new css features and styling, explained on the [wiki](https://github.com/Emrie-Candera/Bubble-Space-Theme/wiki).
-   [Obsidian You](https://github.com/selfire1/obsidian-you-theme/releases/) is now up to v0.1.2, with German language support and some other small fixes.
-   Blue Topaz now supports the Style Settings plugin.

## Ancillary Code

-   A new [tool](https://github.com/elchead/blog-cli) to publish blog posts to Github pages from inside Obsidian.
-   Here's a [Python3 script](https://github.com/dannberg/kindle-clippings-to-obsidian) to format all your Kindle Highlights for import.

## Guides

-   Bryan Jenks put together [a bunch of short videos](https://twitter.com/tallguyjenks/status/1457861276701364227?t=P-NvNUSvIxqulA5OsfRWcw) explaining what different "common terms" in the community mean, like "pkm" (personal knowledge management).
-   Here's how to [automate the uploading process](https://publish.obsidian.md/bramses/Quick+Action+(Mac)+Cloudflare+Image+Upload) of using Cloudflare Images to store images on Obsidian with Automator.

## Showcases

-   `@Sharfaroz` shared an incredible [loom video](https://www.loom.com/share/cfedb027ba7e4d819784145075f82eff) about how he uses the dataview and kanban plugins to view the same data: one example was a reading list, the other was plugins to check out, but both were really impressive examples.
-   I pushed a reasonably big update to my [public vault](https://publish.obsidian.md/eleanorkonik/). There's a slight modification of my folder structure, mostly because I merged "my education" and "teaching" folders and added a genealogy section. There are also a bunch of new notes about the usual stuff, like [axolotls](https://publish.obsidian.md/eleanorkonik/40+Slipbox/42+Zettels/axolotl) & the difference between a [thing and a folkmoot](https://publish.obsidian.md/eleanorkonik/40+Slipbox/42+Zettels/Thing+vs.+Folkmoot), but also a lot of worldbuilding notes about weird creatures like the [tulpi](https://publish.obsidian.md/eleanorkonik/50+Worldbuilding/51+Verraine/tulpi): "winged whale-like goats that eat pine pollen that drifts on the wind..."
-   Here's an article about [journaling in Obsidian](https://astobbe.me/posts/building-a-journaling-habit-with-obsidian/).
-   `@TFTHacker` shared [a collection of beautiful graphs from the community](https://twitter.com/TfTHacker/status/1458885283420721157).

## Discussions

-   [How to build a second brain as a software developer](https://aseemthakar.com/how-to-build-a-second-brain-as-a-software-developer/) did pretty well over at [Hacker News](https://news.ycombinator.com/item?id=29188418).
-   Here's a discussion about a [shared class vault](https://discord.com/channels/686053708261228577/722584061087842365/906626100648632381).
-   The pros/cons of [nested vaults](https://forum.obsidian.md/t/nested-vaults-usage-and-risks/6360) came up again.
-   Here's a neat way to use [manual ids to reference paper notes in notebooks](http://discordapp.com/channels/686053708261228577/710585052769157141/908697269048578118).
-   Here was a discussion about how different people [use obsidian on mobile](http://discordapp.com/channels/686053708261228577/864046194195431425/907698273412874241).
-   Here was a discussion about the [safety & security of various sync methods](https://www.reddit.com/r/ObsidianMD/comments/qqcp08/security_question_sync/).
-   Here was a discussion about [how to use Obsidian as a planner](https://www.reddit.com/r/ObsidianMD/comments/qp9ffe/do_you_use_obsidian_for_your_dayweekmonthly/).

## In The Wild

-   Here's a lovely article about [using Obsidian and the Journey plugin in writing poetry](https://birrellwalsh.medium.com/obsidian-as-a-companion-on-a-poems-journey-b2378517e56?sk=e4e1d84c4c83d6e216f514af183f1563).
-   Here's `@curtismchale` looking at Obsidian's [Longform plugin as a potential Scrivener replacement](https://www.youtube.com/watch?v=vhWwTE26-u4).

## Ancillary Tools

-   Community member `@sashinexists` created a fast, minimal typing practice app called [infintytype](https://infinitype.io/).
-   Bryan Jenks put together a video about how [Research Rabbit integrates with Zotero](https://youtu.be/6vVcqwdpfK0), which may be of interest to academics and researchers.
-   [https://morss.it/](https://morss.it/) will grab the full text for you if an RSS feed is truncated
-   [Tarsnap](https://www.tarsnap.com/) got resurfaced again as a great tool for making backups.
-   Here is a [color gradient generator](https://cssgradient.io/)

## Housekeeping

-   I shared a [pretty wholesome thread](https://twitter.com/EleanorKonik/status/1458774483569893379) about the impact Obsidian has had on me personally, and why I believe that tools _do_ matter and that "tweaking settings instead of writing" _can_ be "productive." Check it out!

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-11-13%20WYSIWYG%20%28called%20Live%20Preview%29%20is%20HERE.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-11-13%20WYSIWYG%20%28called%20Live%20Preview%29%20is%20HERE.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
