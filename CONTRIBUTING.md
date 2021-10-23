---
aliases:
  - how to contribute
tags:
  - seedling
---

# Contributing to the Obsidian community vault

Hi! First of all, thanks for your interest in contributing to our Obsidian community vault!
This is a big experiment on trying to create an Obsidian vault that is maintained by the community.
If you're reading this on GitHub, you might notice there are a few things that look weird.
For the best experience, we recommend [downloading the latest version][download vault] of this vault or browsing it in our [publish site][published vault].

## Setup

To contribute, please [download the latest version][download vault] of this vault and open it in Obsidian. This is important to avoid duplicating content, and allows you to use the autocomplete when linking to other notes, searching and following our content guidelines.

Because PKM is usually (as it name states) _highly_ personal, we have added a few rules about how we use Obsidian features to preserve our sanity:

- **Tags**: We mostly use tags to indicate the status of a note. You can find more details in the [[Tag glossary]].
- **Files & Links**: Make sure that any time you add or edit a note, your settings are configured correctly. This should be set up by default. To sum up:
  - Configure `Location of new notes` to go the [[🗂️ 06 - Inbox]] folder.
  - Links should be set to `Shortest path` and wikilinks must be enabled.
  - The `Default location for new attachments` should be the folder [[🗂️ 03 Attachments]].
    ![[file-and-link-settings.png]]
- **Templates**: We have predefined a few templates for any new content to be added (more about this later). These templates include comments and instructions of when to use them.
- **Folders**: We have roughly pre-defined the structure of the vault using Johnny Decimal-ish prefixes. Before adding new folders, please open an issue to discuss the changes you'd like to propose.

Now that you have configured Obsidian, you are ready to do your first contribution! Have a look at the [[#Types of contributions]], and depending on what you want to contribute open the linked note for further instructions.
Once you have added or edited the note using Obsidian, come back and check out [[#Submitting your contribution]]

## Types of contributions

To try and make it easy for folks to navigate this vault and find content they're interested in we have added a little bit of structure to the vault. If you can, try to file any new notes in one of the folders described in [[#Adding or editing notes]], but don't worry too much about it! If you don't think it fits any of those folders, or are unsure/don't have time to think about this, just do the following:

1. Create a new note (if you followed the steps in [[#Setup]] it should be created under [[🗂️ 06 - Inbox]])
2. Apply the [[T - New Note]] template and write!
3. [[How to add content through GitHub|Submit your changes to GitHub]]

### Adding or editing notes

#### [[03 - Community Tools For Obsidian/Plugins/🗂️ Plugins|Plugins]]

- [[03 - Community Tools For Obsidian/Plugins/🗂️ Plugins]] - This folder is pre-populated with information from the [obsidian-releases]() repository. Here you can add more information about the plugin itself. For [[09.02 - How To|how to]] do something with a plugin keep reading.
- [[02 - Categories/Plugins/🗂️ Plugins]] - Help us categorize community plugins!

#### [[🗂️ Templates]]

Here you can contribute the templates you use for Obsidian. Examples of those include:

- [[🗂️ 03.01 - Daily notes|Daily note templates]]
- [[🗂️ 03.02 - Weekly notes|Weekly note templates]]
- [[🗂️ 03.03 - Monthly notes|Monthly note templates]]
- [[🗂️ 03.04 - Yearly notes|Yearly note templates]]
- [[🗂️ 03.05 - Projects|Project management templates]]
- [[🗂️ 03.06 - Literature notes|Literature note templates]]

[[🗂️ 03.10 - Plugin-specific templates|Plugin-specific templates]]:

- [[🗂️ Dataview templates]]
- [[🗂️ Templater templates]]

#### [[03 - Community Tools For Obsidian/Themes/🗂️ Themes|Themes]]

Similar to the community plugins, this folder is pre-populated with information from the [obsidian-releases](https://github.com/obsidianmd/obsidian-releases/) repository. You can add information about the theme itself or add links to support the author of your favourite theme. See [[#04 - CSS Snippets]] for more.

#### [[🗂️ CSS Snippets]]

There are different ways to contribute CSS snippets:

- Links to snippets hosted on GitHub or as Gists (recommended)
- Snippets hosted in this community vault.

#### [[🗂️ 04 - Examples & Showcases]]

- Note examples are the equivalent of the `#snip-a-note` channel on Discord.
- Vault examples are notes that describe how you organize your note. They can be as simple as screenshots of your folder structure or as complicated as a starter vault.

#### [[09 - Digital Garden]]

##### [[09.02 - How To]]

Do you want to share how you do _X_ with Obsidian, a community plugin or an ancilliary tool? This is the right place! They can be as atomic or as comprehensive as you'd like.
We added a few folders with topics we have forseen, but don't worry too much about where your note belongs -- just add it at the root of this folder if it's ambiguous.

- [[Workflows]]
- [[Plugin Tips and Tricks]]
- [[🗂️ Guides]]
- [[Publishing]]

#### [[10 - Resources]]

In addition to storing all the note attachments in this folder, here we collect all Obsidian-related resources. These are mostly links to external websites. Examples include:

- [[YouTube| YouTube Videos, Channels and Playlists]]
- [[T - Blog posts]] or [[Websites]]
- [[02 - Categories/Auxiliary Tools/🗂️ Auxiliary Tools]]
- [[Publish sites]] and other [[Digital garden]]

#### [[🗂️ Events]]

For regularly or publicly held events, you can add a note describing the event and any other important information or links.

### Adding suggestions or ideas for this vault

Please [click here](https://github.com/obsidian-community/obsidian-hub/discussions/new) if you have suggestions or ideas for this vault.

### Reporting broken (external) links, typos or mistakes

If you found a broken link, a typo or a mistake [please open an issue](https://github.com/obsidian-community/obsidian-hub/issues/new).

## Submitting your contribution

If you know how to use git and GitHub, go on and make a pull request. Otherwise you might be interested in reading [[How to add content through GitHub]] (we've tried to make it as friendly and assume as little background knowledge as possible!)

[download vault]: https://github.com/obsidian-community/obsidian-hub/releases/latest
[publish site]: https://publish.obsidian.md/hub
