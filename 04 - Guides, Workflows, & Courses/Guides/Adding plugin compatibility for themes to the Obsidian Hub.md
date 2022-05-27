---
aliases: 
- 
tags:
- seedling
publish: true
---

# Adding plugin compatibility for themes to the Obsidian Hub

We use some scripts to get content from a theme's GitHub repo. If your theme supports the [[obsidian-style-settings|Style Settings]] plugin, we'll automatically classify your plugin under [[Themes with Friendly Settings]], parse the contents of the settings, and add them to your theme's note.

## Plugin Compatibility

If you want to let your users know which plugins you have considered while designing your theme, you can add them to your CSS file as a comment with the following syntax:

```css
/* @plugins
core:
- <plugin-id>
- ...

community:
- <plugin-id>
- <plugin-id>
- ...
*/
```

You can get the plugin IDs for both core and community plugins from their notes here on the hub:

- Community plugins: You can browse the folder [[🗂️ Plugins|Community plugins]]
- Core plugins are listed in [[05 - Concepts/Obsidian Core Plugins]]


If you want the hub to ignore some of the settings shown by the [[obsidian-style-settings|Style Settings]] plugin, you can add an attribute `hub: ignore`. 

You can see examples of the `@plugins` block on the [shimmering focus](https://github.com/chrisgrieser/shimmering-focus/blob/1c288794b58322e923ec950c0c29cfeea5b5370c/obsidian.css#L4052) theme. An example of the usage of `hub: ignore` can be found [here](https://github.com/chrisgrieser/shimmering-focus/blob/1c288794b58322e923ec950c0c29cfeea5b5370c/obsidian.css#L4208).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Adding%20plugin%20compatibility%20for%20themes%20to%20the%20Obsidian%20Hub.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Adding%20plugin%20compatibility%20for%20themes%20to%20the%20Obsidian%20Hub.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
