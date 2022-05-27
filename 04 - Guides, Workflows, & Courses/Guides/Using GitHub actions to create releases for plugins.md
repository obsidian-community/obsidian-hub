---
aliases: 
- 
tags:
- seedling
publish: true
---

# Using GitHub actions to create releases for plugins

This was originally posted by [[argenos]] in the Obsidian forum: [Using GitHub actions to release plugins - Developers & API - Obsidian Forum](https://forum.obsidian.md/t/using-github-actions-to-release-plugins/7877)

If you're like me, and you some times worry whether you have uploaded the right version of the files to a GitHub release, this might help you a little! 

I'm using [GitHub actions](https://github.com/features/actions) to automate this. My workflow looks like this:

1. Write code, fix stuff, etc. and commit my changes, pushing them to GitHub as needed.
2. When I'm ready to release a new version,
   1. Update the `manifest.json` with the right version, commit and push it.
   2. use `git tag <version number>`, e.g. `<git tag 1.0.0` using [semantic versioning](https://semver.org/).
3. Push the new tag to GitHub `git push origin --tags`
4. GitHub takes care of the rest
  - You can see the actions being run here: ![[github-actions.png]]
- This is how a normal process looks like: ![[github-actions-running.png]]
- And this is how my releases look: ![[github-plugin-release.png]]



## I want to use this, what do I do?

Here's how I'm using it in my `nldates-obsidian` plugin. To add this to your repository just copy the file and save it in the `.github/workflows/` path, i.e. your should have a `.github/workflows/releases.yml`. file. Note that the `.github` folder is a hidden one!

Note that if you are using `styles.css`, you'll need to add that file [in line 29](https://github.com/argenos/nldates-obsidian/blob/master/.github/workflows/release.yml#L29), and uncomment the last few lines.

You can grab the [release workflow here](https://github.com/argenos/nldates-obsidian/blob/master/.github/workflows/release.yml). 

## Other ways to automate

The [original post](https://forum.obsidian.md/t/using-github-actions-to-release-plugins/7877) covers other ways to automate this, including a script by [[schemar]] and using [obsidian-tools](https://github.com/obsidian-tools/obsidian-tools) 

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Using%20GitHub%20actions%20to%20create%20releases%20for%20plugins.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Using%20GitHub%20actions%20to%20create%20releases%20for%20plugins.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
