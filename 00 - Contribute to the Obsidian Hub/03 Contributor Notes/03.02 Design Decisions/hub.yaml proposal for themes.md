---
publish: true
---

# `hub.yaml` proposal for theme designers

We want to propose a way for you to be able to enhance your hub note without the hassle of making PRs to the hub or having to keep things updated on two places. 

## Current workflow

As you may know, some of the hub content is populated via scripts. For themes, there are two sources of information we use:
- What you submitted to the `obsidian-releases` repo, e.g. 
  ```json
      {
        "name": "Shimmering Focus",
        "author": "pseudometa",
        "repo": "chrisgrieser/shimmering-focus",
        "screenshot": "docs/images/Promo%20Screenshot/promo-screenshot.png",
        "modes": ["dark", "light"],
        "branch": "main"
    },
   ```
- Your `obsidian.css` file to determine if you use the Style settings plugin and to see if you've listed any [compatible plugins](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/Adding+plugin+compatibility+for+themes+to+the+Obsidian+Hub).

This is covers the very basic information for most themes, but
- is not very user-friendly when trying to find themes that have X (which themes support asides? highlights?) and users have to try out the themes to find out
- limits you to a single screenshot
- requires manual edits on your side if you want to add text or other features not mentioned in style settings or list sponsorship information
    - content you add to the hub is  outside to your theme repo and will easily get out of date
    - adding or updating any content you do add to the hub requires you to go through the fork and PR workflow, which adds friction and makes it less likely that you do either
- requires manual work in the hub  repo when there are manual changes to make sure the scripts haven't removed manually added content and handling other edge cases (at least for now)

## Proposal

Our proposal is to add an optional `hub.yaml` file at the root of theme repos to add some of this information. Note that all entries are optional, so maintenance and effort can be managed by each theme designer based on their theme's complexity and requirements. We'll cover some of the basics with examples below, but you can find the full file with all the options further down in the [[#Template]] section.

### Link to the theme's documentation

The contents of the `hub.yaml` for a theme that **only** wants to add a link to the theme's documentation in its hub note would be as simple as:

```yaml
docs: https://minimal.guide/ # Link to the theme documentation
```

### Hub note contents

Similarly, if you wanted to have some control on the contents of your theme note, you can use the `hub_content` key to list which markdown documents to "import" to the hub. Generally, to avoid having to maintain two sets of docs (one for your theme and one for the hub), you could reuse a markdown file with an overview that has links to your docs.

For example, with the contents of `hub.yaml` as show below:
```yaml
hub_content: # List of markdown documents to be included as is to the hub relative to the root of the repo.
    - docs/theme_overview.md
```

And the contents of `theme_overview.md`:
```markdown

## My theme overview

This is a small description of my theme. You can find more information about the following features in the documentation:
- [Callouts](www.mytheme.com/callouts)
- [checkboxes](www.mytheme.com/checkboxes)

Report issues by clicking [here](www.github.com/octocat/mytheme/issues).
```

### Theme features

The main goal of adding a list of features is to help compare themes based on what they offer, to save one having to try them out. Keep in mind that themes (especially large ones) have many many features, and it's not our intention to make an exhaustive list of **all** the things your theme can do. Instead, ==ideally the features you list are a way to pitch to (new) users what makes your theme unique==. For that, the idea is to parse the `feature` key to identify some of the frequently sought-after features with a controlled vocabulary and automatically add links to pre-defined categories in the hub. The controlled vocabulary is based on the feature list proposed by pseudometa and extended by argentum:

| Key | Hub note | Description |
|----|-----|------|
| `color_schemes` | `[[Themes with additional color schemes]]` | Theme has additional color schemes
| `tables` | `[[Themes with special table support]]` | Dedicated cssclasses for tables
|`mobile` | `[[Themes with mobile support]]` | Does the theme provide mobile support (both phones and tablets)?
| `publish` | `[[Themes with Obsidian Publish support]]` |Does the theme have publish support?
|`print` | `[[Themes with PDF export support]]` | Adds CSS to customize the appearance of the PDF exports
|`gutter` | `[[Themes with gutter features]]` |Does the theme add custom indicators or other features to the gutter?
|`snippets` | `[[Themes with official snippets]]` | Does your theme provide additional snippets to customize parts of your theme outside of the style settings plugin?
| `images` | `[[Themes with image handling options]]` | Does your theme add any image-handling features, e.g. zooming, galleries, aligning/wrapping around text, etc.
|`highlights` | `[[Themes with custom highlights]]` | Additional colours or ways to achieve the core `==highlight==` behaviour
|`asides` | `[[Themes with side notes]]` | Any features related to the `<aside>` tag or any of its css workarounds, sometimes also called side notes or margin notes
|`checkboxes` | `[[Themes with custom checkboxes]]` |Particularly if you added custom types
| `callouts` | `[[Themes with custom callouts]]` | Does the theme add special callouts?
| `cssclass` | `[[Themes with custom css classes]]` | Does the theme add css classes that are not covered on other features? 
| `miscellaneous` | Only for certain keywords (see below)| Any other feature you'd like to mention as a markdown formatted string. Mentioning the following two will add links to the corresponding pages:

Recognised words in the `miscellaneous` features:

- `opinionated` - Will link to `[[Opinionated themes]]`. Whether the theme is opinionated (+ can you opt out of the theme's opinionatedness)
- `minimalistic` -  Will link to [Minimalistic themes](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.02+Themes+by+Category/Minimalistic+Themes) 

As an example:

```yaml
theme:
    features:
        miscellaneous:
            - A minimalistic theme perfect for focusing on writing
            - Opinionated but highly customizable

```

These two were not included in the `features` list:

- ~~has style settings~~ -> we can detect this automatically with our script, so no need to mention this manually
- ~~plugin_support - plugin compatibility list~~ -> Moved to its own section

Listing features in the `hub.yaml` should be extremely flexible. For the hub to recognize your feature, you can use:

- A boolean
  ```yaml
  theme:
      features:
          callouts: true
   ```
- A path to one or many screenshots on your repo
  ```yaml
  theme:
    features:
          callouts:
            screenshots: # Path to screenshots for this feature (from the root of the repo)
                - file: docs/all_dnd_callouts.png
                  caption: All the D&D callouts for My Theme
                - file: docs/treasure_dnd_callout.png
                  caption: Example of the treasure D&D callout
   ```
- A path to a markdown document to be included as is in the hub
  ```yaml
  theme:
      features:
          custom_callouts:
              docs:
                  file: docs/dnd_callouts_overview.md # from root of repo, to be included as is
   ```
- A link to your own documentation
  ```yaml
  theme:
      features:
          custom_callouts:
              docs:
                  links: # List of strings (can be markdown-formatted)
                      - [More information](www.mytheme.com/dnd_callouts)
   ```
- Combinations of the above options (except boolean)
  ```yaml
  theme:
      features:
          custom_callouts:
              docs:
                  file: docs/dnd_callouts_overview.md # from root of repo, to be included as is
                  links: # List of strings (can be markdown-formatted)
                      - [More information](www.mytheme.com/dnd_callouts)
              screenshots: # Path to screenshots for this feature (from the root of the repo)
                  - file: docs/all_dnd_callouts.png
                    caption: All the D&D callouts for My Theme
                  - file: docs/treasure_dnd_callout.png
                    caption: Example of the treasure D&D callout
                  
   ```

%% Note: for the implementation we'd need to know how to structure the templates so that combinations of these make sense %%

### Plugin support

This key (`plugin_support`) is essentially an alternative to parsing the [compatible plugins](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/Adding+plugin+compatibility+for+themes+to+the+Obsidian+Hub) from the `obsidian.css` file if you prefer to have the hub stuff outside of your theme file. If you don't specify this key, we'll still try to read your plugins from the css file.

```yaml
theme:
    plugin_support: [] # IDs of the plugins that have been styled by this theme (adding them here would ignore the plugin IDs on the obsidian.css file)
```

### Screenshots

If you want to add additional screenshots, or don't want to add features but prefer to just add screenshots of your theme, you can use the `screenshot` key:

```yaml
theme:
    screenshots: # Path to other screenshots from the root of the repo
        - file: 
          caption:
```

## Template

Here is a full template with all the options being proposed:

```yaml
docs: # Link to the theme documentation
hub_content: [], # List of markdown documents to be included as is to the hub relative to the root of the repo.
authors: # More than one author is possible, start a new line with - 
    - github: # GitHub user names of the people who created the plugin or theme
      websites: [] # Links to personal websites
      discord:
      twitter:
      youtube:
      sponsorships:
          buymeacoffee: # Add username to kofi or buy me a coffee here
          paypal: 
          github:
          patreon:
          others: [] # List of formatted markdown strings
maintainers: [] # GitHub user names of those maintaining the plugin (leave empty if it's the same as author)

theme:
    features:
        mobile:
            docs:
                file: # from root of repo, to be included as is
                links: [] # markdown-formatted strings
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        publish: true
            docs:
                file: # from root of repo, to be included as is
                links: [] # markdown-formatted strings
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        gutter:
            docs:
                file: # from root of repo, to be included as is
                links: [] # markdown-formatted strings
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        print:
            docs:
                file: # from root of repo, to be included as is
                links: [] # markdown-formatted strings
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        callouts:
            docs:
                file: # from root of repo, to be included as is
                links: [] # markdown-formatted strings
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        checkboxes:
          docs:
                file: # from root of repo, to be included as is
                links: [] # markdown-formatted strings
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        images:
          docs:
                file: # from root of repo, to be included as is
                links: [] # markdown-formatted strings
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        tables:
            docs:
                file: # from root of repo, to be included as is
                links: [] # markdown-formatted strings
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        asides:
            docs:
                file: # from root of repo, to be included as is
                links: [] # markdown-formatted strings
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        highlights:
            docs:
                file: # from root of repo, to be included as is
                links: [] # markdown-formatted strings
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        color_schemes:
            docs:
                file: # from root of repo, to be included as is
                links: [] # markdown-formatted strings
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        snippets:
            docs:
                file: # path to markdown file from root of repo, to be included as is
                links: [] # markdown-formatted strings, e.g. pointing to the css files for download
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        cssclass: []
            docs:
                file: # from root of repo, to be included as is
                links: [] # markdown-formatted strings
            screenshots: # Path to other screenshots from the root of the repo
                - file: 
                  caption:
        miscellaneous: [] # Other features you want to mention as markdown-formatted strings
    plugin_support: [] # IDs of the plugins that have been styled by this theme (adding them here would ignore the plugin IDs on the obsidian.css file)
    screenshots: # Path to other screenshots from the root of the repo
        - file: 
          caption:
```

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.02%20Design%20Decisions/hub.yaml%20proposal%20for%20themes.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.02%20Design%20Decisions/hub.yaml%20proposal%20for%20themes.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
