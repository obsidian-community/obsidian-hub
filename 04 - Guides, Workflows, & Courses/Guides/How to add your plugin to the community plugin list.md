---
aliases:
- Submit plugin
tags:
- seedling
publish: true
---

# How to add your plugin to the community plugin list

This note is based on the instructions of the [obsidian sample plugin readme](https://github.com/obsidianmd/obsidian-sample-plugin#adding-your-plugin-to-the-community-plugin-list).

## Preparing your repository

1.   [[How to release a new version of your plugin|Publish an initial version]] of your plugin.
2.   Make sure you have a `README.md` file in the root of your repo, clearly describing the plugins purpose and providing clear usage instructions.
3.  Add a license to your repository. You can use [Choose a License](https://choosealicense.com/) if you don't know which one to pick.
4.  Check that your `manifest.json` is at the root of your repo.

## Submitting your plugin

1.  Fork the [obsidian-releases](https://github.com/obsidianmd/obsidian-releases#community-plugins) repo and edit the `community-plugins.json` file. If you prefer to do it from GitHub's web interface, you can follow this instructions, but submit your changes as described in [[How to add content through GitHub]] or [[How to add your plugin to the community plugin list#Submitting your plugin]].
2.  Add the information of your plugin at the end of the list (Don't forget to add a comma after the last plugin!). For your convenience you can copy this template and paste it at the end of the list:
```json
  {
    "id": "",
    "name": "",
    "author": "",
    "description": "",
    "repo": "<github username>/<repository>"
  }
```
3. Fill out the information of your plugin. Below you can find the description of each field (taken from the [obsidian-releases](https://github.com/obsidianmd/obsidian-releases#community-plugins) repo):
	-   `id`: A unique ID for your plugin. Make sure this is the same one you have in your `manifest.json`.
	-   `name`: The name of your plugin. This will be used to search for your plugin.
	-   `author`: The author's name.
	-   `description`: A short description of what your plugin does.
	-   `repo`: The GitHub repository identifier, in the form of `user-name/repo-name`, if your GitHub repo is located at `https://github.com/user-name/repo-name`.
4.  Make a pull request at [https://github.com/obsidianmd/obsidian-releases](https://github.com/obsidianmd/obsidian-releases) to add your plugin.
5. Once you've opened the PR, you'll be prompted to use the pull request template. Complete everything in it and submit.
	![[plugin-submission-PR-template.png]]
6. Your plugin will go through a small review process. Once your plugin is approved, the PR will be merged and users will be able to install it from the community plugin list.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/How%20to%20add%20your%20plugin%20to%20the%20community%20plugin%20list.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/How%20to%20add%20your%20plugin%20to%20the%20community%20plugin%20list.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
