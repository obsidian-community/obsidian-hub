---
aliases: 
- Submit theme
- publish a theme
tags:
- seedling
publish: true
---

# How to add your theme to the community theme store

The TL;DR is that you have to add the information of your theme to the to the [`community-css-themes.json` file](https://github.com/obsidianmd/obsidian-releases/blob/master/community-css-themes.json) in the [obsidian-releases](https://github.com/obsidianmd/obsidian-releases/) repo. 

## Preparing your repository

Your theme must be hosted on GitHub on a public repository. Before submitting your theme, make sure that your repository contains the following:
1. A `README.md` file in the root of your repo
2. A screenshot of your theme to be displayed in the community theme store. We recommend using an image of 1920×1080px.
3. Your `.css` file must be named `obsidian.css` and be at the root of your repository.
4. It is highly recommended that you add a license to your theme. You can use [Choose a License](https://choosealicense.com/) if you don't know which one to pick.
5. To submit your theme, you can go ahead and make a [pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) if you are familiar with git. Otherwise keep reading for instructions on how to submit your theme through GitHub's web interface.

## Submitting your theme

1. Click [here](https://github.com/obsidianmd/obsidian-releases/edit/master/community-css-themes.json) to edit the `community-css-themes.json` in GitHub's web interface. 
2. Scroll all the way to the bottom to add your theme at the end of the file, and add a `,` after the last theme: 
	![[theme-submission-add-comma.png]]
3. Copy this template and paste it in the last few lines:
	```json
    {
        "name": "<theme name>",
        "author": "<author name, pseudonim or username>",
        "repo": "<github username>/<repository>",
        "screenshot": "example.png",
        "modes": ["dark", "light"],
		"branch": "master"
    }
	```
4. Fill out the information of your theme. Make sure to only select the `modes` (dark, light, or both) that are compatible with your theme and that the `branch` you are using is correct (e.g. `master` vs `main`)
	![[theme-submission-add-info.png]]
5.  Describe your changes (e.g. "Add Hitchhiker's theme") and click on "Propose changes":
	![[theme-submission-propose-changes.png]]
5. You'll be prompted to use the pull request template. Complete everything in it and submit.
	![[theme-submission-PR-template.png]]

