---
aliases: [how to contribute]
tags: [seedling]
---

# CONTRIBUTING

Hi! First, thanks for your interest in contributing to our Obsidian community vault!  
This is a big experiment in creating an Obsidian vault maintained by the community.

You might notice some weird things if you're reading this on GitHub.  
For the best experience, we recommend [downloading the current version](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip) of this vault or browsing it on our Obsidian Publish hosted [website](https://publish.obsidian.md/hub).

## Setup & Vault Consistency

To contribute, please [download the current version](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip) of this vault and open it in Obsidian. This is important to avoid duplicating content and allows you to use autocomplete when linking to other notes, searching, and following our content guidelines.

Because Personal Knowledge Management is usually (as its name states) _highly_ personal, we have added a few rules about using Obsidian features to keep this Community vault consistent (and to preserve our sanity 🙂).

- **Tags**: We primarily use tags to indicate the status of a note (the #seedling → #evergreen lifecycle). You can find more details in the [[Tag glossary]]. Note that the `#placeholder/*` tags documented there are deprecated for new content. They existed to scaffold bot-assisted stub filling, which the Hub no longer does.
- **Frontmatter.** Keep using the existing `aliases`, `tags`, and `publish` fields. When you materially edit or verify an existing note, also set (or update) a `reviewed: YYYY-MM-DD` frontmatter field to today's date. This is now the Hub's staleness signal, since automated bots no longer flag out-of-date content. Don't backfill `reviewed` onto notes you haven't actually reviewed just to add the field.
- **Files & Links**: Ensure your settings are configured correctly whenever you add or edit a note. This should be set up by default. To sum up:
  - Configure the `Default location for new notes` to `In the folder specified below`.
  - In the new `Folder to create new notes in` option, select the [[🗂️ Inbox]] folder.
  - Set the `New link format` setting to the `Shortest path when possible`.
  - Set the `Use [[Wikilinks]]` setting to `Enabled`
  - The `Default location for new attachments` should be folder Contribute/[[🗂️ 02 Attachments]].

![[file-and-link-settings.png]]

- **Templates**: We have [[🗂️ 01 Templates|predefined a few templates for adding new content]] (more about this later). These templates include comments and instructions on when to use them. To enable Obsidian to use this folder:
  - Under `Core plugins`, locate `Templates` and `Enable` this plugin.
  - Scroll to the `Templates` settings under the `PLUGIN OPTIONS` header and set the `Template folder location` option to `Contribute/01 Templates`.
- **Folders**: We have roughly pre-defined the vault structure into a handful of top-level folders (see below). _Before adding new folders, please open an issue to discuss the changes you'd like to propose._

Now that you have configured Obsidian, you can make your first contribution! Look at the [[#The Main Folders|types of contributions]], and depending on what you want to contribute, open the linked note for further instructions.

Once you have added or edited the note using Obsidian, check out [[#Submitting|Submitting your contribution]].

## Structure of the Community Vault

### Overview

This is a [tree](https://github.com/MrRaindrop/tree-cli) view of the basic folder structure of this Community Vault.

![[Hub Tree Structure]]

### The Main Folders

Let's have a brief look at the main folders:

#### [[🗂️ Contribute]]

This folder contains various resources for making contributions to this community vault. Other than adding your attachments here, there is likely no need to contribute to this folder.

#### [[🗂️ Showcases & Templates]]

All Showcases, Examples, and Templates belong to this folder. This includes special-purpose or pre-prepared Vaults ("Starter Kits"). Note examples are the equivalent of the `#snip-a-note` channel on Discord.

In this folder, you can add new notes with the [[T - Note showcase|Template for Showcases]], the [[T - Vault showcase|Template for Vaults]], and the [[T - Templates|Template for Templates]]. (Yeah, this is getting meta.)

#### [[🗂️ Guides & Courses]]

All guides, instructions, explainers, and workflows should be placed here. Courses, more comprehensive paid guides, are also located here, along with Community Talks, Events, and Video Channels notes. To make it easier for everyone to find guides relevant to them, the guides should be linked to the "for Group X" notes (which are MoCs).

You can contribute here by adding [[T - How to|new Guides and How-Tos with the respective template]]. Remember to also link to them from any fitting "for Group X" page so it can be found.

#### [[🗂️ Concepts]]

This folder serves as some wiki or dictionary for all the technical and PKM terms you will find when people talk about Obsidian. Rather than explaining concepts like [[Zettelkasten]] in every guide or at the note of every plugin developed for it, you can refer to its concept note.

Naturally, new notes on concepts not explained in this vault are welcome. Use the [[T - New Concept|Template for new concept notes]] to add information here. Be sure to use the [Unlinked Mentions Feature](https://help.obsidian.md/How+to/Add+aliases+to+note#Find+unlinked+mentions) to find all the notes that should be linked to the new concept.

#### [[🗂️ Obsidian Roundup|Archive]]

This folder holds the discontinued Obsidian Roundup newsletter archive. It is read-only history, please don't add new notes here.

## Out of Scope

The Hub used to maintain a bot-synced directory of plugins, themes, CSS snippets, auxiliary tools, and contributor/author pages, plus a weekly community-roundup digest. All of that was removed. It duplicated data that [community.obsidian.md](https://obsidian.md/plugins), Obsidian's in-app plugin/theme browser, and each project's own repository already maintain far more reliably than a hand-edited vault ever could.

Please do not submit:

- Per-plugin, per-theme, per-CSS-snippet, or per-auxiliary-tool pages.
- Per-author/per-contributor "profile" pages.
- Roundup-style periodic digests or changelogs.
- Any other "directory of X" content that is really just a sync of an external list (plugin browser, theme store, GitHub topic search, etc).

If you want to showcase how you personally use a plugin, theme, or workflow, that's still welcome as a guide, showcase, or template under [[🗂️ Guides & Courses]] or [[🗂️ Showcases & Templates]]. Just don't try to catalogue the whole ecosystem here.

## On Note Location and Note Links

In general, create new notes **in one of the existing folders described above instead of creating a new one**. If you are unsure in which folder a new note belongs, use the more general [[T - New Note|New Note Template]], place it in [[🗂️ Inbox]], and let others look. Generally, try to search for an existing note to add before creating a new one.

If you feel your contribution belongs to two or more folders simultaneously (e.g., an ancillary tool for which you also provide a guide), consider breaking up your contribution and putting smaller notes into the respective locations. Afterwards, link your contributions to each other.

As this is indeed Obsidian, one thing always welcome is the addition of new links. Download this vault for correct autocompletion of internal links, and use [aliases](https://help.obsidian.md/How+to/Add+aliases+to+note#Link+with+aliases) to increase readability. Also, use the [Unlinked Mentions Feature](https://help.obsidian.md/How+to/Add+aliases+to+note#Find+unlinked+mentions) and link to [[🗂️ Concepts|Concept Notes]] instead of explaining too much.

==**Rule of thumb for contribution**: No folders, notes for new content, and note additions for existing content, and don't be shy with new links!==

## Making Your Contribution

### Writing

This is all you need to know before contributing. Use the Community Vault as any other vault to write your contribution in. You use the plugins and settings you are familiar with for writing and working with the vault.

Please turn on the spellchecking when you are writing longer bits. 🙂 (And only add words to the dictionary if they are common.)

### Submitting

==Before submission, remember to revert the Community Vault to its basic settings, e.g., remove installed plugins, turn on spellchecking, and change any other unusual settings back to how they previously were.== This concerns the [[CONTRIBUTING#Setup Vault Consistency|settings relevant to the Vault consistency mentioned above]].

If you know how to use Git and GitHub, make a pull request. Otherwise, you might be interested in reading [[How to add content through GitHub]] (we've tried to make it as friendly and assume as little background knowledge as possible!).

## Reporting Broken (external) Links, Typos or Mistakes

If you found a broken link, a typo, or an error, [please open an issue](https://github.com/obsidian-community/obsidian-hub/issues/new).

## Further Questions?

Do you have some questions left? Check out the [[FAQ]] or drop by the `#hub` at [the Obsidian Discord Server](https://discord.gg/veuWUTm). How is a specific tag used? Refer to the [[Tag glossary]].

Please [open a new discussion at GitHub](https://github.com/obsidian-community/obsidian-hub/discussions/new) if you have suggestions or ideas for this vault.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/CONTRIBUTING.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/CONTRIBUTING.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
