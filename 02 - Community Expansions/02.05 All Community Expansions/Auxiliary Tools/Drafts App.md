---
aliases:
  - Drafts
tags:
  - seedling
publish: true
---

# Drafts
Official website: https://getdrafts.com/
Documentation: https://docs.getdrafts.com/
Cost: Free / 1,99$ per month for [Drafts Pro](https://docs.getdrafts.com/draftspro)
Available for: [[MacOS Tools|MacOS]], [[iOS Apps|iOS]], [[iPadOS Apps|iPad]]

Drafts is a markdown-based note-taking app that is focussed on good mobile experience, tight integration with the Apple ecosystem, and a frictionless process of adding content. It also has great extensibility through its [actions](https://actions.getdrafts.com/), which work very similar to [[templater-obsidian|Templater]] scripts. 

Due to the focus on mobile and quickly adding content, Drafts complements Obsidian well for iOS and Mac users.

## Readings
- [Getting Started - Drafts User Guide](https://docs.getdrafts.com/gettingstarted/)
- [Guide: Integrating Obsidian with Drafts](https://forums.getdrafts.com/t/using-obsidian-with-drafts/11221)
- [Discussion in the Drafts Forum on working with Drafts & Obsidian](https://forums.getdrafts.com/t/drafts-and-obsidian-why/10968)

## Moving content from Drafts to Obsidian
There are about a dozen different Drafts Actions to do that, many of them relying on the [Advanced URI plugin](https://github.com/Vinzent03/obsidian-advanced-uri). ("Actions" is how plugins are called in the Drafts ecosystem.)

[All Drafts Actions related to Obsidian](https://actions.getdrafts.com/search?utf8=%E2%9C%93&q=obsidian)

## Moving content from Obsidian to Drafts
There is no dedicated plugin for Obsidian that does that, *but* you can use the [URI commands plugin](https://github.com/kzhovn/uri-commands-obsidian) to send content from Obsidian to Drafts. Simply add the URL Scheme to the plugin: 

```url
drafts://x-callback-url/create?text=%23%20{{fileName}}%0A{{fileText}}&tags=via%20Obsidian
```

Refer to the README of the URI commands plugin and the [Drafts documentation of URL Schemes](https://docs.getdrafts.com/docs/automation/urlschemes) for further customizations.

## Other Resources
- [Obsidian Markdown Syntax](https://actions.getdrafts.com/s/1r1) (made by [[chrisgrieser|pseudometa]]): Makes Drafts use the same Markdown Syntax as Obsidian (e.g., `#tags` or `%%comments%%`)

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Auxiliary%20Tools/Drafts%20App.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Auxiliary%20Tools/Drafts%20App.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
