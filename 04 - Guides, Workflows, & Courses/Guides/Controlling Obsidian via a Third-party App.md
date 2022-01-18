---
aliases: 
- 
tags:
- seedling
publish: true
---

# Controlling Obsidian via a Third-Party App
Overview where/how you can find various obsidian-related data in a form accessible to third-party apps.

- `URI` refers to the [Obsidian URI Scheme](https://help.obsidian.md/Advanced+topics/Using+obsidian+URI#Using+Obsidian+URIs) for controlling Obsidian.
- `Adv. URI` refers to the [[obsidian-advanced-uri\|Advanced URI Plugin]] for controlling Obsidian. You can easily get the respective URI Schemes by selecting the command `Advanced URI Plugin: Copy Command URI`, select `Don't specify a file`, and then the command whose URI you would like to have. 
	- ⚠️ If you are developing something to share with others, remember to remove the vault-argument (`vault=vaultName`) from the URI or dynamically insert the proper vault name there — otherwise the URI schemes won't work
- `Hotkey Helper URI` refers to the [[hotkey-helper\|URI Scheme introduced by the Hotkey Helper Plugin]].
- URI Schemes are generally practical, since they also work on any platform, including mobile.
- [URLs must be properly encoded](https://www.w3schools.com/tags/ref_urlencode.ASP). The `Advanced URI Plugin: Copy Command URI` already applies proper URL encoding.
- In JavaScript, the functions [`encodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) and [`encodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI) are used for encoding.

| Obsidian Data                   | How to access                                                                                       | How to control                                                                                                                                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vaults                          | `~/Library/Application Support/obsidian/obsidian.json`                                              |                                                                                                                                                                                             |
| Enabled Core Plugins            | `{vaultPath}/.obsidian/core-plugins.json`                                                           |                                                                                                                                                                                             |
| Current Theme                   | `{vaultPath}/.obsidian/appearance.json`                                                             | Theme Switcher Command (via Adv. URI)                                                                                                                                                       |
| Enabled CSS Snippets            | `{vaultPath}/.obsidian/appearance.json`                                                             | Renaming a snippet located in `"{vaultPath}/.obsidian/snippets/"` basically works as a OFF-Switch, since CSS is live-reloaded by Obsidian. (renaming the file back, would be the on-switch) |
| Base Font Size                  | `{vaultPath}/.obsidian/appearance.json`                                                             |                                                                                                                                                                                             |
| Workspaces                      | `{vaultPath}/.obsidian/workspaces.json`                                                             | Open Workspace (Adv. URI)                                                                                                                                                                   |
| Tags                            | [Metadata-Extractor-Plugin](https://github.com/kometenstaub/metadata-extractor)                     | Open / Search (URI)                                                                                                                                                                         |
| Aliases                         | [Metadata-Extractor-Plugin](https://github.com/kometenstaub/metadata-extractor)                     | Open (URI)                                                                                                                                                                                  |
| Headings                        | [Metadata-Extractor-Plugin](https://github.com/kometenstaub/metadata-extractor)                     | Open Heading (Adv. URI)                                                                                                                                                                     |
| Recent Files (up to 10)         | `{vaultPath}/.obsidian/workspace` (last item)                                                       | Open (URI)                                                                                                                                                                                  |
| Starred Files                   | `{vaultPath}/.obsidian/starred.json`                                                                | Open (URI)                                                                                                                                                                                  |
| Index of Vault                  | `find "{vaultPath}" -name "*.md"` (shell)                                                           | Open (URI)                                                                                                                                                                                  |
| Plugins in Community Browser    | `https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugin.json`       | Hotkey Helper URI                                                                                                                                                                           |
| Downloads & Versions of Plugins | `https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugin-stats.json` | Hotkey Helper URI                                                                                                                                                                           |
| Themes in Community Browser     | `https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-css-themes.json`   |                                                                                                                                                                                             |
| Installed Plugins               | `ls -1 "{vaultPath}/.obsidian/plugins/"` (shell)                                                    | Hotkey Helper URI                                                                                                                                                                           |
| Installed Themes                | `ls -1 "{vaultPath}/.obsidian/themes/"` (shell)                                                     |                                                                                                                                                                                             |
| Installed CSS Snippets          | `ls -1 "{vaultPath}/.obsidian/snippets/"` (shell)                                                   |                                                                                                                                                                                             |

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Controlling%20Obsidian%20via%20a%20Third-party%20App.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Controlling%20Obsidian%20via%20a%20Third-party%20App.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
