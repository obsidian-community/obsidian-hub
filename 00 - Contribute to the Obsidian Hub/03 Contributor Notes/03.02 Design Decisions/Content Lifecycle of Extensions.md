## Purpose

Try to capture the stages that community extensions (Plugins and Themes) go though.

## Questions on the following...

- Are the life-cycle stages correct?
- Can we decide on how to represent each of the stages in the **structure** and content on the hub?
    - Example structure:
        - `Plugins/Unlisted Plugins` ->
        - `Plugins` ->
        - `Plugins/Archived Plugins`
    - Note: There is currently `Plugins/Unlisted` - which doesn't generalise for themes: `Themes/Unlisted`
- Can we decide on how to represent each of the stages in the **content** on the hub?
    - Example content:
        - This plugin is **not yet published** in the community catalogue (???)->
        - This plugin is available in the **community catalogue** (???)->
        - This plugin is **archived** and likely no longer supported.
- Once we know that, we can script something that at least initially detects and reports inconsistencies - and maybe later actually makes edits (to update structure and/or content)
    - And run that via GitHub Actions


## Plugins

### Life-cycle of a plugin

Evolution of a plugin...

- **Unlisted**
    - Does have a release in GitHub, so could be installed via BRAT
    - ~~Not yet in community plugins~~ Not submitted to the community plugins (and it might **never** be submitted).

- **Beta**
    - Not yet in community plugins - but being tested
    - This is a difficult one - it requires manual tracking/intervention to know when a plugin enters this state. It might or not have a PR open to `obsidian-releases`
    - If we keep it as a lifecycle stage, suggest it's up to the plugin author to move it here
- **Published**
    - Is currently in community plugins file
    - This means that `update-releases.py` will create/update a hub page for the plugin
    - Repo must not be archived not archived (but we don't check that currently)
- **Archived**
    - Either: No longer listed in community plugins file
    - And/or: Plugin's GitHub repo is archived

### Plugins sources of truth

- **community-plugins.json**
    - Currently used:
        - Whether the plugin is currently there
        - Various details like repo

    - Currently not used:
        - Whether the plugin has ever been listed there in the past, and has since been removed

- **The plugin's GitHub**
    - Currently used:
        - Various details like author's name, description

    - Currently not used:
        - Whether there has ever been a release
        - Whether the repo is archived


### How the sources of truth are represented in the Hub
- **Hub structure**
    - Whether the plugin has a note in `02.05 All Community Expansions/Plugins`
    - Whether the plugin has a note in the Unlisted plugins category
        - <https://publish.obsidian.md/hub/02+-+Community+Expansions/02.01+Plugins+by+Category/Unlisted+plugins>
    - Whether the plugin has a note in the Unlisted plugins folder
        - <https://publish.obsidian.md/hub/02+-+Community+Expansions/02.05+All+Community+Expansions/Plugins/Unlisted/🗂%EF%B8%8F+Unlisted>
- Hub Content
    - Whether the plugin is listed in the 'Unlisted plugins' section of the author's note
        - e.g. <https://publish.obsidian.md/hub/01+-+Community/People/SkepticMystic>
    - Not represented in note content:
        - Whether the plugin is archived

## Themes

I think the comments above apply equally well for themes.

## Scopes for inconsistency

There are many... Here are a few.

- Plugin gets published in obsidian-releases - no one notices to check whether to remove it from 'Unlisted plugins'
    - Unlisted plugins should only contain plugins that will **NOT** be included in the `obsidian-releases` repo
- And many others