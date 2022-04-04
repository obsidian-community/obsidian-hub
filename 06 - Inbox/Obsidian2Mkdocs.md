---
aliases: 
- Mkdocs Publish
- Material Publish
tags:
- seedling
- mkdocs
- publish
publish: true
---

# Obsidian to Mkdocs

Official website: 
- [Template Website](https://mara-li.github.io/mkdocs_obsidian_template/)
- [My french website](https://www.mara-li.fr/)

[Documentation](https://github.com/Mara-Li/mkdocs_obsidian_publish)
[FAQ](https://github.com/Mara-Li/mkdocs_obsidian_template/wiki/Q&A/)

Cost: 0 (Free)

Available for: [[Windows Tools|Windows]], [[MacOS Tools|MacOS]], [[Linux Tools|Linux]], [[Android Apps|Android]], [[iOS Apps|iOS]], [[iPadOS Apps]] (It only needs Git and python)

Obsidian2Mkdocs is a [python](https://www.python.org/) is a workflow that rely on a python script to publish a notes using mkdocs. It exists other alternative, but it's is thinked around a partial publishing and vault : you choose which note will be shared and publish by metadata. 

It supports a lot of Obsidian things, as :
- [[obsidian-admonition|Admonition]]
- Custom Attribute : [[markdown-attributes|Markdown Attributes]], [[obsidian-contextual-typography|Contextual Typography]]
- Wikilinks and relative links
- Obsidian markdown : Highlight, tilde
- Transclusion and embeding files
- Image Flags CSS
- Latex, Mermaid… 

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

# Showcase
![](https://github.com/Mara-Li/mkdocs_embed_file_plugins/raw/main/docs/demo.gif)
![](https://github.com/Mara-Li/mkdocs_embed_file_plugins/raw/main/docs/note3.png)

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/06%20-%20Inbox/Obsidian2Mkdocs.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/06%20-%20Inbox/Obsidian2Mkdocs.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
