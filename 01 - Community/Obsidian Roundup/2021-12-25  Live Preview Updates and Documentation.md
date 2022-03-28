---
link: https://www.obsidianroundup.org/2021-12-25/
author: Eleanor Konik
published: 2021-12-25T13:30:00
publish: true
---

# 2021-12-25: Live Preview Updates & Documentation
A bunch of popular themes got updated, and some discussions about productivity & workflows.

## In The Community

-   Make sure you [vote for the Gems of the year](https://forum.obsidian.md/t/obsidian-gems-of-the-year-2021-voting/28759). Checking out all the nominated stuff is a great way to see a ton of awesome new workflows and ideas!

## Obsidian Updates

versions [v0.13.11](https://forum.obsidian.md/t/obsidian-release-v0-13-11-insider-build/28809), [v0.13.12](https://forum.obsidian.md/t/obsidian-release-v0-13-12-insider-build/28813/2), [v0.13.13](https://forum.obsidian.md/t/obsidian-release-v0-13-13-insider-build/28955/1) & [v0.13.14](https://forum.obsidian.md/t/obsidian-release-v0-13-14/29006)  have been bundled up and are now available for public access, which means:

-   [Live Preview](https://help.obsidian.md/Live+preview+update) is now available for public access. Not all plugins and themes are updated to support the new editor, so please be patient and check the relevant repositories if the update leads to missing functionality you really need.
-   [[Obsidian Sync]] now has bulk restore functionality.
-   There's now RTL support, a better spellchecker, built in syntax highlighting, and several performance improvements.

## Plugin News

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). Note, though, that this is not as safe as waiting for them to go through code review._

### New

-   Here's a new [note encryption](https://github.com/LikelyLee/NoteEncryption) plugin. Please be careful with encryption. There are no take-backsies.
-   You can now [autocomplete](https://github.com/tth05/obsidian-completr) stuff from within Obsidian. It scans your vault and supports LaTeX.
-   [NLP](https://github.com/SkepticMystic/nlp) adds a _ton_ of text-extraction/manipulations features. It also lets users style words based on what part of speech they are, which is handy for editing long form writing. It also has an API, so other plugins can use it.  Here's an example of how to use it to [reproduce iA Writer's language-syntax highlighting](http://discordapp.com/channels/686053708261228577/702656734631821413/923215464912527401) using [this CSS](https://github.com/SkepticMystic/nlp/discussions/4#discussioncomment-1858644).
-   There's a new [interactive metronome](https://github.com/curtgrimes/obsidian-metronome-plugin) for Obsidian notes.
-   [Quoth](https://github.com/erykwalder/quoth/releases/tag/0.1.1) lets you embed from other Markdown documents in the vault, with more flexibility than the standard syntax with an exclamation point before a link. You can do things like inline the content you want to embed, select specific portions from one or many blocks, and add a "source" along with the embed.

### Updates

-   The new [CardBoard](https://github.com/roovo/obsidian-card-board) 0.3.2 Board Filters allow you to use file, path, and tag filters to control which tasks go on which board.
-   [Collapse All v1.4.0](https://github.com/OfficerHalf/obsidian-collapse-all/releases/tag/1.4.0) now has commands to collapse/expand both the file explorer and tag pane, and commands to collapse/expand each individually, and a new toggle to split the button into separate collapse and expand buttons, instead of having a single button that flips between the two.
-   [Embedded Note Titles 1.2.0](https://github.com/mgmeyers/obsidian-embedded-note-titles/) 1.2.0 has been updated to work with live preview.
-   The [Link Favicons plugin](https://github.com/joethei/obsidian-link-favicon) now supports overwriting Favicons with your own icons provided by the [Icon Shortcodes plugin](https://github.com/aidenlx/obsidian-icon-shortcodes), as well as defining your own icons for different URI schemes.
-   [Another Quick Switcher plugin](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher/releases/tag/3.1.0) got some breaking changes, but added a bunch of options, for example "max number of suggestions."
-   Fantasy Calendar got some quality of life updates! You can now set it so that if it finds a date in the title of a note, it will automatically add the event to the default calendar specified in settings. You can also change the date format for date strings, instead of being forced to use UTC (`YYYY-MM-DD`).
-   [Supercharged Links v0.4.0](https://github.com/mdelobelle/obsidian_supercharged_links) now supports Live Preview.
-   [Big Calendar](https://github.com/Quorafind/Obsidian-Big-Calendar/releases/tag/0.1.13) got some new CSS classes and critical bugfixes.
-   [File Tree Alternative](https://github.com/ozntel/file-tree-alternative/releases/tag/1.6.6) should use less memory now.
-   [Various Complements](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin/releases/tag/3.4.0) has better edge case handling now.

## For Developers

-   Here's a handy [guide for how to update your plugins and themes for Obsidian 0.13+](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/How+to+update+your+plugins+and+CSS+for+live+preview).
-   There's further [documentation on how to use CM6 with Obsidian](https://github.com/nothingislost/obsidian-cm6-attributes) from Obsidian October winner `@NothingIsLost`. They also wrote up some information about [the MetadataCache](https://github.com/obsidianmd/obsidian-api/issues/33).
-   `@javalent` says you can do Cmd/Ctrl-Shift-P and type `focused` then select `Emulate a focused page`, and clicking dev tools will no longer affect the actual page you're looking at.
-   Here's a neat trick today to [get a drop shadow when a container has scrolled using only CSS](https://discord.com/channels/686053708261228577/702656734631821413/921553490558459944).
-   Here's a discussion of [what theme devs think plugin devs should do when introducing elements](http://discordapp.com/channels/686053708261228577/702656734631821413/923695832690221066).
-   Here's a neat [tool for making color palettes](https://leonardocolor.io/?colorKeys=%236fa7ff&base=ffffff&ratios=3%2C4.5&mode=CAM02).

## Appearance

-   [Sanctum](https://github.com/jdanielmourao/obsidian-sanctum/releases/tag/v0.5) got a giant update with a bunch of little fixes.
-   [Minimal](https://github.com/kepano/obsidian-minimal/releases/tag/4.2.0) has a bunch of new helper classes, new layout settings available via Minimal Theme Settings, and some new hotkeys.
-   [California Coast](https://github.com/mgmeyers/obsidian-california-coast-theme) got a top-to-bottom rewrite and now supports Live Preview.
-   Shimmering Focus has been updated so all the theme's features now work in 0.13+s new editor. There were also some neat color-related updates, and it supports way more plugins now.
-   [ITS Theme](https://forum.obsidian.md/t/theme-its-dark-light-theme/12838/146) has been moved to SCSS and updated for Live Preview. There are a bunch of new Style Settings fixes and updates, and a new Nord color scheme.
-   [Sandstorm](https://github.com/jaysan0/obsidian-sandstorm) and [Nebula](https://github.com/dlccyes/obsidian-nebula/) are both new.
-   Here's a snippet that will make Obsidian look like [Apple Notes](https://discord.com/channels/686053708261228577/702656734631821413/923730545085665330). The creator is thinking about developing it out into a full-fledged theme; if that's something you'd be interested in let them know :)

## Guides

-   Here's a nifty guide on [how to design better links](https://uxdesign.cc/designing-better-links-for-websites-and-emails-a-guideline-5b8638ce675a), aimed at websites and emails but really useful for personal knowledge management.
-   Here's how you can [remap buttons on an android phone](https://discord.com/channels/686053708261228577/864046194195431425/923283744956252202) so that you can, for example, use your "volume up" button to toggle the quick switcher when using Obsidian.

## Discussions

-   Here's a nice discussion over at Hacker News about [taking daily notes in plaintext](https://news.ycombinator.com/item?id=29661167), inspired by this lovely writeup about how Jeff Huang uses a [productivity text file](https://jeffhuang.com/productivity_text_file/)
-   Here's a neat discussion [pushing back against collector's fallacy](https://discord.com/channels/686053708261228577/722584061087842365/914188614362071091).
-   Here's an example of [how to organize academic PDFs](http://discordapp.com/channels/686053708261228577/722584061087842365/923326410116980826).
-   A process for how to read/note/highlight articles and books, and how to process lit notes, plus some [tips for highlights and processing](https://forum.obsidian.md/t/how-do-you-read-process-material/29140/4?u=austin).
-   Here's [a case for using spaced repetition to enhance personal knowledge management](https://thepuranik.home.blog/2021/12/24/second-brain-obsidian-spaced-repetition-plugin/).
-   Here's an interesting discussion about [workflows to draw diagrams on the iPad with the Apple pencil](https://www.reddit.com/r/ObsidianMD/comments/rmgrt2/update_on_the_discussion_i_had_here_about_ipad/).
-   Several people chimed in to help out [someone who was overwhelmed with the possibilities of Obsidian](https://www.reddit.com/r/ObsidianMD/comments/rk1un0/need_advice_too_overwhelmed_to_start_using_the/) and having trouble starting out.

## Exemplars

-   Here's a great example of [how to use Supercharged Links](https://discord.com/channels/686053708261228577/744933215063638183/923730166444851220) and color-coding of tags to flag files as action items visually in the file tree.

-   Here's [a collection of premade TTRPG themed vaults for players and GMs](https://github.com/Rotengar/Obsidian.Character.Vaults), and, relatedly, a [really cool example of an Obsidian note recording a rpg session](https://discord.com/channels/686053708261228577/916477002909876265/923356632296075304).

-   `@benryn` put together a neat product hunt style [showcase site for published Obsidian vaults](https://www.openvaults.xyz/).
-   Here's a demo vault for [dataviews and custom views](https://github.com/kaelri/obsidian-dataview-test-vault).
-   Here's a really [beautiful example of a graph telling a story](https://www.youtube.com/watch?v=7RKNKbEYAlA).
-   Chris Wilson has a youtube video about [how he takes notes on the Bible](https://www.youtube.com/c/ChrisWilsonUK).
-   Here are some [Templates for Obsidian](https://github.com/llZektorll/OB_Template).

## Housekeeping

-   Sorry about another abbreviated edition of the Roundup, but whelp, my family celebrates Christmas and I kind of forgot I wouldn't have childcare yesterday, whups. Merry Christmas from my family to yours, I promise to do better for New Year's! If there's something cool you saw in the last three weeks and it didn't make it into the Roundup, please feel free to reach out and make sure I don't miss it.
-   Contrary to how things went for December, I expect to have some extra time in January when my son starts going half-days to daycare. If there's a burning question or topic you've been hoping I'd write an article about, reach out and I'll see about adding it to my list of projects.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-12-25%20%20Live%20Preview%20Updates%20and%20Documentation.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-12-25%20%20Live%20Preview%20Updates%20and%20Documentation.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
