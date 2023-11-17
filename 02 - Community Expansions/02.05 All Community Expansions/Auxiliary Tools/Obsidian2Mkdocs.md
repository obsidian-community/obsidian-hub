---
aliases: 
- Mkdocs Publisher
tags:
- seedling
publish: true
---

# Obsidian to Mkdocs

Author: [[obsidianMkdocs|Mara-Li]]
Cost: 0 (Free)

Available for: [[Windows Tools|Windows]], [[MacOS Tools|MacOS]], [[Linux Tools|Linux]], [[Android Apps|Android]], [[iOS Apps|iOS]], [[iPadOS Apps]]

Obsidian2Mkdocs was a workflow that relied on a Python script to publish your notes using Mkdocs. It existed as an alternative to the official [[Obsidian Publish]] service. It has since been replaced by a variety of tools maintained by the [[ObsidianPublisher]] community.

It supported:
- Obsidian's Markdown flavour
- [[obsidian-admonition|Admonitions]]
- Custom Attributes: 
	- [[markdown-attributes|Markdown Attributes]],
	- [[obsidian-contextual-typography|Contextual Typography]]
- Wikilinks and relative links
- Transclusion and embeding files
- Image Flags CSS
- Latex, Mermaid

The script has since been archived but is still [available on GitHub](https://github.com/ObsidianPublisher/obsidian-mkdocs-publisher-python).

## Quick tutorial

- Clone the [template](https://github.com/Mara-Li/mkdocs_obsidian_template#readme)
- Install all requirements with `pip install -r requirements`
- Customize the `mkdocs.yml` : `site_name`, `site_description`, `site_url`, logo and favicons
 - Run `obs2mk` to start the configuration, and share (and push) your files !

### Script usage
```sh
usage: obs2mk [-h] [--git | --mobile] [--meta] [--keep] [--config] [--force] [--filepath FILEPATH | --ignore]

Create file in docs and relative folder, move image in assets, convert admonition code_blocks, add links and push.

options:
  -h, --help            show this help message and exit
  --git, --g, --G       No commit and no push to git
  --mobile, --shortcuts, --s, --S
                        Use mobile shortcuts fonction without push.
  --meta, --m, --M      Update the frontmatter with link
  --keep, --k, --K      Keep deleted file from vault and removed shared file
  --config, --c, --C    Edit the config file
  --force, --d, --D     Force conversion - only work if path not specified
  --filepath FILEPATH, --f FILEPATH
                        Filepath of the file you want to convert
  --ignore, --ignore-share, --no-share, --i, --vault
                        Convert the entire vault without relying on share state.
```

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/06%20-%20Inbox/Obsidian2Mkdocs.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/06%20-%20Inbox/Obsidian2Mkdocs.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
