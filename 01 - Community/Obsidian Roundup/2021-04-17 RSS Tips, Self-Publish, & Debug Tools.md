---
link: https://www.obsidianroundup.org/2021-04-17/
author: Eleanor Konik
published: 2021-04-17
publish: true
---

# 2021-04-17: RSS Tips, Self-Publish, & Debug Tools
The Dataview plugin is getting a lot of attention. Plugin developers got some nifty debugging features for mobile. We discussed resonance calendars and task management, and surfaced some useful RSS tricks for keeping up with Obsidian news if this newsletter is too infrequent for you.

## Community Events

- The second half of the [community talk for how to leverage the Dataview plugin](https://youtu.be/jW5pD4SioFM) is now available on [[YouTube]]. You can vote for which upcoming community talks you're interested in [on the forum](https://forum.obsidian.md/t/obsidian-talks-which-talks-do-you-want-to-hear/15705/).
- `@nickmilo` & [[SkepticMystic]] are hosting [[blacksmithgu]] , the creator of the [[dataview|Dataview]] plugin, on a community Zoom meeting. Details are [here](https://discord.com/channels/686053708261228577/710585052769157141/832070319136833546) in the Discord. [[eleanorkonik|Eleanor Konik]] has agreed to do a share and showcase.
- Wanna join a fancy book club? [[ryanjamurphy]] and `@bri (they/m)` are hosting the first book club session for [Knowledge Architectures by Denise Bradford](https://www.routledge.com/Knowledge-Architectures-Structures-and-Semantics/Bedford/p/book/9780367219444) on April 25th 11-12ish PST, more info here: https://discord.com/channels/686053708261228577/744933215063638183/830888490433904641

## Plugin News

- The [[obsidian-outliner|Outliner]] plugin now lets you click on bullets to zoom in!
- The [music notation plugin](https://github.com/TilBlechschmidt/obsidian-plugin-abcjs) renders music sheets from code blocks using the `music-abc` language.
- There was a nice [discussion](https://discord.com/channels/686053708261228577/710585052769157141/832070319136833546) initiated by `@pjeby` about some under-loved plugins that blend so well into the UI that you might not even known you need them, for example [[tag-wrangler|Tag Wrangler]], [[hotkey-helper|Hotkey Helper]], and [[pane-relief|Pane Relief]]
- `@alex.dinu` published [an initial version of a plugin that performs table sorting](https://github.com/alexandru-dinu/obsidian-sortable/releases/tag/0.1.0); it works with [[dataview|Dataview]] but is not yet in the community plugins list.
- From a plugin security perspective, this discussion about how [Obsidian has the ability to blacklist / disable plugins that are identified to have issues or vulnerabilities](http://discordapp.com/channels/686053708261228577/707816848615407697/832445992808218635) was very reassuring.
- [[mgmeyers]] updated the [[obsidian-style-settings|Style Settings]] plugin to give [better error reports](http://discordapp.com/channels/686053708261228577/707816848615407697/832315933842079784), which is always useful. The repo also has [This CSS Snippet](https://github.com/mgmeyers/obsidian-style-settings/blob/main/obsidian-default-theme.css) can be used to adjust every CSS variable of the default Obsidian theme.

### For Developers

- [[liamcain]] shared his [approach to mobile debugging on iOS](https://discord.com/channels/686053708261228577/817515900349448202/826416602911211535). It uses a [script for the plugin](https://gist.github.com/liamcain/3f21f1ee820cb30f18050d2f3ad85f3f).
- There is a now [a method for developers to write test cases that interact with a running obsidian instance](https://forum.obsidian.md/t/for-plugin-developers-write-test-cases-that-interact-with-a-running-obsidian-instance/16574).

## Feature Requests

- `@Murf` requested a [search operator similar to YAML similar to the line section](https://forum.obsidian.md/t/search-operator-for-yaml-similar-to-line-section/16565). As [[dataview|Dataview]] becomes more popular and better-understood, this will probably become more valuable, so if you have a use-case or want to advocate for this feature, please reply to the forum thread.

## Workflow Stuff

- For folks using MacOS, `@benhamilton` figured out a workflow for using [[icalBuddy]], a script, and a keyboard macro to [list events from a ical into a daily note](https://discord.com/channels/686053708261228577/694233507500916796/832463345952620554).

## Tips & Tricks

- PDF tip via [[cotemaxime]]: you can embed a specific page of a pdf with `![[My File.pdf#page=number]]`
- If you're using a sync service that doesn't let you opt out of syncing a particular folder, there is a setting in Obsidian that will let you override where that particular instance of Obsidian pulls its configurations from: in About -> Advanced -> Override config folder. This is also helpful if you've got access to the mobile beta and want to differentiate settings from your desktop config.
- `u/aviranco` on Reddit asked [how to restyle checklists to _not_ change the display of subitems under a completed task](https://www.reddit.com/r/ObsidianMD/comments/mqndbf/is_there_a_way_to_have_a_note_after_a_checked/gup4eiq); the community came through with [a CSS snippet](https://discord.com/channels/686053708261228577/702656734631821413/832507883925143552).
- If you like the idea of being able to zoom in and out to various tiles on your Obsidian workspace, `@Licat` put together [a CLI snippet](http://discordapp.com/channels/686053708261228577/744933215063638183/832420779378343937) that could be extended into a nifty plugin by an enterprising developer!
- In base Obsidian, footnotes screw with the line height and make paragraphs look not-quite-right from a spacing perspective. But `@Klaas` has a fix on their [GitHub snippet repository](https://forum.obsidian.md/t/how-to-achieve-css-code-snippets/8474).
- There's a mobile emulation flag in the desktop app that will let you check your CSS before moving it over to mobile, if you're a Supporter or VIP with access.

## PKM Tips

- We had a discussion about how to [adapt the concept of a Resonance calendar from Notion to Obsidian](http://discordapp.com/channels/686053708261228577/744933215063638183/832611785903308871) in order to help bridge the gap between "collector's fallacy" and "forgetting where you read something and not being able to find the reference again."
- There was an insightful discussion of [when to use a "task in a page" vs "tasks in a list" structure](http://discordapp.com/channels/686053708261228577/694233507500916796/832507555783770202) in the discord.

## [[🗂️ 02.04 Auxiliary Tools by Category|Ancillary tools]]

- We had another [discussion](https://discord.com/channels/686053708261228577/744933215063638183/832294628752752701) of the [[Onyx Boox]] and how nice it is to have Obsidian mobile open on one half of the screen, with a PDF or epub on the other half, and take notes directly into Obsidian with either handwriting, voice, or keyboard inputs.
- It's possible to get the raw list github merges for [plugins & themes as an RSS feed](https://github.com/obsidianmd/obsidian-releases/commits/master.atom) if you don't want to wait for the weekly newsletter but also don't want to hang out in the Discord.
- You can also get a direct [RSS feed from the discourse forum](https://meta.discourse.org/t/rss-feed-for-category-latest/37192) from a tag or a category, for example if you just wanted to follow the [community talks RSS](https://forum.obsidian.md/tag/community-talks.rss).
- For [[Static Site Generators]], there was some [discussion](http://discordapp.com/channels/686053708261228577/694233507500916796/832502926555086908) about [[Hugo]] vs. [[Jekyll]], along with a [forum post](https://forum.obsidian.md/t/notenote-link-publish-your-obsidian-notes-with-jekyll-for-free/7951) about how to self-host your obsidian notes as a [[Digital garden]]. We also talked about [how to get a newsletter](http://discordapp.com/channels/686053708261228577/694233507500916796/832332146194251816) with [[Hugo]] if you're more comfortable with the technical side of things.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/01%20-%20Community/Obsidian%20Roundup/2021-04-17%20RSS%20Tips%2C%20Self-Publish%2C%20%26%20Debug%20Tools.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/01%20-%20Community/Obsidian%20Roundup/2021-04-17%20RSS%20Tips%2C%20Self-Publish%2C%20%26%20Debug%20Tools.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
