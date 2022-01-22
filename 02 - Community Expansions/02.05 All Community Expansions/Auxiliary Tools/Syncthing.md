---
aliases:
  -
tags:
  - seedling
publish: true
---

# Syncthing

Official website: https://syncthing.net/
Documentation: https://docs.syncthing.net/
Cost: free, open source
Available for: [[Windows Tools|Windows]], [[MacOS Tools|MacOS]], [[Linux Tools|Linux]], [[Android Apps|Android]]

A peer-to-peer file synchronisation application, which can be used to keep your Obsidian vault synchronised across multiple devices almost instantaneously.

## Configuration for Obsidian
You'll probably want the following files to be excluded from synchronisation in your `.stignore`. If you're not using the [[metadata-extractor|Metadata Extractor]] plugin, you'll only need to exclude `workspace`.
```
// most important one. this keeps track of your open panes and files in the app
.obsidian/workspace
// Metadata Extractor generates these automatically, so you shouldn't sync them
.obsidian/plugins/metadata-extractor/allExceptMd.json
.obsidian/plugins/metadata-extractor/metadata.json
.obsidian/plugins/metadata-extractor/tags.json
```
You *can* exclude your entire `.obsidian` directory instead for simplicity, but in that case your plugins and configuration will not be synchronised at all.

Note that Syncthing does *not* synchronise the `.stignore` itself, so you will need to set up your ignore patterns on each device separately. If you save a copy of your `.stignore` elsewhere in your Obsidian vault, it can simply be copied to set up a new device smoothly.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Auxiliary%20Tools/Syncthing.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Auxiliary%20Tools/Syncthing.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
