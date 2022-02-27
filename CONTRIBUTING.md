---
aliases:
  - how to contribute
tags:
  - seedling
---

# CONTRIBUTING

Hi! First of all, thanks for your interest in contributing to our Obsidian community vault!
This is a big experiment on trying to create an Obsidian vault that is maintained by the community.

If you're reading this on GitHub, you might notice there are a few things that look weird.
For the best experience, we recommend [downloading the latest version](https://github.com/obsidian-community/obsidian-hub/releases/latest) of this vault or browsing it in our [publish site](https://publish.obsidian.md/hub).

## Setup & Vault Consistency

To contribute, please [download the latest version](https://github.com/obsidian-community/obsidian-hub/releases/latest) of this vault and open it in Obsidian. This is important to avoid duplicating content, and allows you to use the autocomplete when linking to other notes, searching and following our content guidelines.

Because Personal Knowledge Management is usually (as it name states) _highly_ personal, we have added a few rules about how we use Obsidian features to keep this Community vault consistent (and to preserve our sanity 🙂)

- **Tags**: We mostly use tags to indicate the status of a note. You can find more details in the [[Tag glossary]].
- **Files & Links**: Make sure that any time you add or edit a note, your settings are configured correctly. This should be set up by default. To sum up:
  - Configure `Location of new notes` to go the [[🗂️ 06 - Inbox]] folder.
  - Links should be set to `Shortest path` and wikilinks must be enabled.
  - The `Default location for new attachments` should be the folder [[🗂️ 02 Attachments]].
    ![[file-and-link-settings.png]]
- **Templates**: We have [[🗂️ 01 Templates|predefined a few templates for any new content to be added]] (more about this later). These templates include comments and instructions of when to use them.
- **Folders**: We have roughly pre-defined the structure of the vault using Johnny Decimal-ish prefixes. *Before adding new folders, please open an issue to discuss the changes you'd like to propose. *

Now that you have configured Obsidian, you are ready to do your first contribution! Have a look at the [[#Types of contributions]], and depending on what you want to contribute open the linked note for further instructions.
Once you have added or edited the note using Obsidian, come back and check out [[#Submitting your contribution]].

## Structure of the Community Vault

### Overview
This is a [tree](https://github.com/MrRaindrop/tree-cli) view of the basic folder structure of this Community Vault.

![[Hub Tree Structure]]

### The Main Folders
Lets have a brief look at the main folders:

#### [[🗂️ 00 - Contribute to the Obsidian Hub]]
This folder contains various resources for making contributions to this community vault. Other than adding your attachments here, there is most likely no real need to contribute in this folder.

#### [[🗂️ 01 - Community]]
This one contains all notes related to People, Community Events, or specific Social Media Channels belong here. Courses offered by the community, however, belong to the folder [[🗂️ 04 - Guides, Workflows, & Courses]]. You can add new pages for various persons and events here. 
%%Should we have a rule regarding the threshold for someone being "relevant enough" to get their own page?%%

#### [[🗂️ 02 - Community Expansions]]
Due to the high number of plugins, themes, snippets and auxiliary tools (third-party-tools), we have compiled [[Maps of Content (MOC)|MOCs]] to browse expansions by category. So if a user is e.g. looking for [[Status bar plugins|Status bar-related Plugins]], they can go to the respective MoC and find them there. 

Feel free to add new links to any list if they are missing! (Remember, download this vault for correct autocompletion of internal links.)

You can also create a new MoC here by using the [[T - Plugin Category|Template for Plugin Categories]] or [[T - MOCs| or MoCs in general]], but only if it is a truly new category not already covered by any of the existing lists – we want to avoid ending up with too many categories.

The sub-folder [[🗂️ 02.05 All Community Expansions]] is automatically prepopulated with notes on the all expansions of our community submitted to the community plugin browser and the community theme store respectively. The MoCs in `02.01` to `02.04` link to the individual pages found in here. 

This folder is prepopulated automatically, so you should not create any new notes in here. The only exception are Auxiliary Tools, for which you are free to create a new note with [[T - Auxiliary tool|the respective Template.]]

Each note represents exactly one tool, which (in the future) should also serve as a jumping pad for all information regarding this one tool – a bit like a Wikipedia page for each plugin, theme, snippet, or ancillary tool.

#### [[🗂️ 03 - Showcases & Templates]]
All Showcases, Examples, and Templates belong into this folder. This includes special-purpose or pre-prepared Vaults ("Starter Kits"). Note examples are pretty much the equivalent of the `#snip-a-note` channel on Discord.

In this folder, you can add new notes with the [[T - Note showcase|Template for Showcases]], the [[T - Vault showcase|Template for Vaults]], and the [[T - Templates|Template for Templates]] (Yeah, this is getting meta.)

#### [[🗂️ 04 - Guides, Workflows, & Courses]]
This is where all guides, instructions, explainers, and workflows should be placed. Courses, basically being more comprehensive paid guides, are also located here. To make it easier for everyone to find guides relevant to them, the guides should be linked to from the "for Group X" notes (which are basically MoCs) .

You can contribute here adding [[T - How to|new Guides and How Tos with the respective template]]. Remember to also link to them from any fitting "for Group X" page, so it can be found.

#### [[🗂️ 05 - Concepts]]
This folder serves as some sort of wiki or dictionary for all the technical and PKM-terms you will find when people are talking about Obsidian. Rather than explaining concepts like [[Zettelkasten]] in every guide or at the note of every plugin developed for it, you can simply refer to it's concept note.

Naturally, new notes on concepts not explained in this vault yet, are welcome. Use the [[T - New Concept|Template for new concept notes]] to add information here. Be sure to also use the [Unlinked Mentions Feature](https://help.obsidian.md/How+to/Add+aliases+to+note#Find+unlinked+mentions) to find all the notes which should be linked to the new concept. 


## On Note Location and Note Links

In general, you should create new notes **in one of the existing folders described above, instead of creating a new one**. If you are unsure in which folder a new note belongs to, use the more general [[T - New Note| New Note Template]], place it in [[🗂️ 06 - Inbox]] and let others have a look. Generally, try to search for an existing note to make additions to before creating a new one. 

If you have the feeling that your contribution belongs into two or more folders at the same time (e.g. an ancillary tool of yours, for which you also provide a guide), consider breaking up your contribution and putting smaller notes into the respective locations. Afterwards, link you contributions to each other. 

As this is indeed Obsidian, one thing pretty much always welcome is the addition of new links. Download this vault for correct autocompletion of internal links, and make use of [aliases](https://help.obsidian.md/How+to/Add+aliases+to+note#Link+with+aliases) to increase readability. Also make use of the [Unlinked Mentions Feature](https://help.obsidian.md/How+to/Add+aliases+to+note#Find+unlinked+mentions) and be sure to link to [[🗂️ 05 - Concepts|Concept Notes]] instead of explaining too much.

==**Rule of thumb for contribution**: No folders, notes for new content, and note additions for existing content, and don't be shy with new links!==

## Making your Contribution

### Writing
This has been pretty much all you need to know before making a contribution. Use the Community Vault as any other vault to write your contribution in. Obviously, you use the plugins and settings you are familiar with for writing and working with the vault.

Please turn on the spellchecking when you are writing longer bits. 🙂 (And only add  words to the dictionary if they are really common.)


### Submitting

==Before submission, remember to revert the Community Vault to its basic settings, e.g. remove installed plugins, turn on spellchecking, and change any other unusual settings back to how they previously were.== Most importantly, this concerns the [[CONTRIBUTING#Setup Vault Consistency|settings relevant to Vault consistency mentioned above]].

If you know how to use git and GitHub, go on and make a pull request. Otherwise you might be interested in reading [[How to add content through GitHub]] (we've tried to make it as friendly and assume as little background knowledge as possible!).

## Reporting broken (external) links, typos or mistakes

If you found a broken link, a typo or a mistake [please open an issue](https://github.com/obsidian-community/obsidian-hub/issues/new).


## Further Questions?
Got some question left? Check out the [[FAQ]] or drop by in the `#hub` at [the Obsidian Discord Server](https://discord.gg/veuWUTm) Wondering how a certain tag is used? Refer to the [[Tag glossary]].

Please [open a new discussion at GitHub](https://github.com/obsidian-community/obsidian-hub/discussions/new) if you have suggestions or ideas for this vault.


%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/CONTRIBUTING.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/CONTRIBUTING.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
