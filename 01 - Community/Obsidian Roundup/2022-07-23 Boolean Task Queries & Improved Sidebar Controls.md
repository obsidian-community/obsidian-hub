---
link: https://www.obsidianroundup.org/2022-07-23/
author: Eleanor Konik
published: 2022-07-23T12:30:00
publish: true
---

# 2022-07-23: Boolean Task Queries & Improved Sidebar Controls
Plugin settings design tips & productivity book recommendations.

## In The Community

-   The subreddit has [new flairs](https://www.reddit.com/r/ObsidianMD/comments/w4bpun/robsidianmd_mod_update_20220721/) for plugins and themes, and encourages people who want to post memes to use the new [meme subreddit](https://www.reddit.com/r/ObsidianMDMemes/).

## Tips

-   It's a good habit to restart Obsidian after you disable or update plugins and themes, just in case there's been dependency updates or issues with unloading old settings.

## Obsidian Updates

-   Silver and Licat, the duo who developed Obsidian solo before recently bringing Liam onto the team, just had a baby — their second together since launching Obsidian 🥰. They all got home from the hospital on Sunday and seem to be doing well.
-   [Insider 0.15.7](https://forum.obsidian.md/t/obsidian-release-v0-15-7-insider-build/40543) had a bunch of fixes and added support for `.mov` and `.mkv` files (although the precise support may vary by platform). You can also get the `Inter` font from the top of the font list now — it's the old default font. You can switch back to Inter by going to `Settings > Appearance` in Obsidian, which will make `->` turn back into a "proper arrow" if you're into that. But really you should consider a more font agnostic method, like those described [in Discord](https://discord.com/channels/686053708261228577/702656734631821413/998649374118785087).

## Plugin News

### New in Community Plugins

-   [Ninja Cursor](https://github.com/vrtmrz/ninja-cursor) by `@vrtmrz`  enhances cursor visibility, [Commander](https://github.com/phibr0/obsidian-commander) by `@phibr0`  lets you add more commands to your work space, and you can now more simply [trim unnecessary whitespace](https://github.com/zlovatt/obsidian-trim-whitespace). Here's a Discord demo of [Commander](https://discord.com/channels/686053708261228577/855181471643861002/999763489579077632)

### Pending (as of Friday morning)

_Note: Not all new plugins are available in the community list yet, as they need to go through code review first. You can manually install plugins that aren't in the community list yet by using the [Beta Reviewer's Auto-update Tool](https://github.com/TfTHacker/obsidian42-brat). This is **not as safe** as waiting for them to go through code review._

-   [Hide Sidebars on Window Resize](https://github.com/NomarCub/obsidian-hide-sidebars-on-window-resize) by `@NomarCub`  automatically hides the sidebars when your window is resized to be narrower. There's also the similar beta plugin [Sidebar Toggler](https://github.com/chrisgrieser/obsidian-sidebar-toggler) that lets you control them from a third party window manager using a URI scheme.
-   [Tagged Documents Viewer](https://github.com/mgeduld/obsidian-tagged-documents-viewer) by `@mgeduld`  opens a modal with scrollable content of all documents that contain a specific tag or tags.
-   [Hard Breaks](https://github.com/bkis/obsidian-hard-breaks) by `@bkis`  turn soft line breaks in Markdown into hard line breaks automatically.

### Updates

_If you want a more comprehensive list of what plugins updated this week, check out this [plugin updates index](https://obsidian-plugin-stats.vercel.app/updates) by Ganessh Kumar._

-   [Dataview](https://github.com/blacksmithgu/obsidian-dataview/issues/729) now supports inline queries for live preview.
-   [Hover Editor 0.11.2](https://github.com/nothingislost/obsidian-hover-editor/releases/tag/0.11.2) is now in general release; you should update if you're using Obsidian 0.15.6+
-   [Obsidian Checklist Plugin 2.2.2](https://github.com/delashum/obsidian-checklist-plugin/releases) should work better on mobile now.
-   The Dataview API now supports publishing notes containing codeblocks with dataview queries; they'll render as contents instead of code. [Version 2.14.0 of Digital Garden](https://github.com/oleeskild/obsidian-digital-garden/releases/tag/2.14.0) and [Obsidian Github Publisher](https://github.com/obsidianMkdocs/obsidian-github-publisher) both now support this API.
-   [Obsidian RTL](https://github.com/esm7/obsidian-rtl) got a big round of bugfixes and now works on mobile.
-   [Task Completer](https://github.com/GamerGirlandCo/obsidian-auto-checkbox/releases/tag/1.1.0) makes it so that, when you complete a task, all subtasks will also be marked as done.
-   [Tasks 1.9.0](https://github.com/obsidian-tasks-group/obsidian-tasks/releases/tag/1.9.0) now has support for [Boolean expressions to combine queries](https://obsidian-tasks-group.github.io/obsidian-tasks/queries/combining-filters/) (AND, OR, NOT), [auto-suggest](https://obsidian-tasks-group.github.io/obsidian-tasks/getting-started/auto-suggest/), and [task components and tags in any order](https://obsidian-tasks-group.github.io/obsidian-tasks/getting-started/auto-suggest/#what-do-i-need-to-now-about-the-order-of-items-in-a-task). [1.10.0](https://github.com/obsidian-tasks-group/obsidian-tasks/releases/tag/1.10.0) lets users group by tags.
-   [Pane Relief 0.2.2](https://github.com/pjeby/pane-relief/releases/tag/0.2.2) now supports the Style Settings plugin, with two frequently-requested options: adding pane numbers, and disabling history counts.
-   [Metadata Menu](https://github.com/mdelobelle/metadatamenu/releases/tag/0.1.0) now has an API.

### For Developers

-   In Discord there was some [guidance on plugin settings design](https://discord.com/channels/686053708261228577/840286264964022302/999733142845915246).
-   SilentVoid is looking for a new maintainer for [Templater](https://github.com/SilentVoid13/Templater). Based on things others have said in Discord, I suspect that _even if you're not a coder,_ just helping consolidate and categorize issues helps developers save a lot of time.
-   Rob Smith is looking to hire a developer to build a [column folder and file sidebar](https://discord.com/channels/686053708261228577/840286264964022302/999725468230111242) (details in Discord).

## Feature Requests

-   An LSP client for Obsidian would make it easier to use things like Grammarly, Vale, advanced linting or autocompletion in code blocks and stuff. Also YAML validation and YAML autocomplete. There are [more details on Discord](https://discord.com/channels/686053708261228577/700466324840775831/997559190191079514).
-   Here's a nice write-up about [how to leverage unlinked mentions](https://forum.obsidian.md/t/expanding-the-usefulness-of-unlinked-mentions/40633), that comes complete with ideas for improvements.
-   If it would be useful for you, add your support to the feature request for [editing transclusions in place](https://forum.obsidian.md/t/enable-editing-of-transclusion-in-place/15342?u=synchronicity).

## Appearance

-   [Sanctum](https://github.com/jdanielmourao/obsidian-sanctum) now allows for more scrollbar customizations, got some fixes, and some subtle tweaks to make it feel cleaner.
-   [Minimal](https://github.com/kepano/obsidian-minimal) now supports a new setting in Style Settings under Minimal > Text  to adjust paragraph spacing, which helps with aligning reading and edit modes.

## Guides

-   Here's how to use the Dropbox API for [automatically publishing a website from your Obsidian files](https://chaseignited.com/posts/publishing-my-website-from-obsidian-files/).
-   Here's a nice writeup for how Rishikesh Sreehari uses [Obsidian for curating a newsletter](https://rishikeshs.com/how-i-curate-my-newsletter/).
-   Here's how Richard Carter used Obsidian to [research and outline a book about Darwin](http://richardcarter.com/sidelines/converting-my-notes-into-a-chapter/).

## Discussions

-   Discord played host to a nice discussion about [different types of notes and how they relate to methods for folder use](https://discord.com/channels/686053708261228577/710585052769157141/997694236969410571).
-   Here was a [great discussion about common conventions in Obsidian usage](https://www.reddit.com/r/ObsidianMD/comments/w4ww5g/questions_on_obsidian_conventions/).
-   Here's a nice roundup of [books about productivity and knowledge management](https://www.reddit.com/r/ObsidianMD/comments/w2ncrh/what_are_the_books_or_any_ressources_about/). Some of the mentioned books were ones I hadn't ever heard of.

## Showcases

-   [The Quantum Well](https://publish.obsidian.md/myquantumwell/) is a public publish site (digital garden) focused on mathematics and physics.
-   Here's a [handcrafted SVG version of the Workflow Diagram](https://gist.github.com/azaol-aegnor/f9b548b8e864c570b2a3e0c9bf1e045d) from David Allen's `Getting Things Done`.
-   Here's a new [daily notes template](https://discord.com/channels/686053708261228577/744933215063638183/997882220222107699) shared in Discord.
-   Here are some examples of [using tags as status markers](https://www.reddit.com/r/ObsidianMD/comments/w06qun/to_the_few_fellows_who_use_tags_as_status_id_like/).

## Housekeeping

I'm going to be out of town with just an iPad for two weeks in August, which will impact the Roundup to various degrees. Although editions will still come out, they may be limited to priority updates. Also, if I'm slower to respond to emails, that's a big reason for why.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2022-07-23%20Boolean%20Task%20Queries%20%26%20Improved%20Sidebar%20Controls.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2022-07-23%20Boolean%20Task%20Queries%20%26%20Improved%20Sidebar%20Controls.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
