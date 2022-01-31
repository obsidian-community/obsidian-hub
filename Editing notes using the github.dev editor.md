---
aliases: 
- 
tags:
- seedling
publish: true
---

# Editing notes using the github.dev editor

%% Add a description below this line. It doesn't need to be long: one or two sentences should be a good start. %%

This guide will cover the basics of using the github.dev editor for the [[Obsidian Hub]]. This editor is great when you are making quick edits that don't need any Obsidian-specific functionality.

In particular, if you are browsing the Hub and you see a note that you would like to improve, this guide shows you how to make the edit, using the "Edit in GitHub" button at the bottom of the note.

## Opening the github.dev editor

To open the editor you'll usually have two options: 
1. On the Hub's [publish site](https://publish.obsidian.md/hub/00+-+Start+here), each note has an "Edit in GitHub" button in its footer.
2. When you are in the Hub's [GitHub repository](https://github.com/obsidian-community/obsidian-hub), pressing <kbd>.</kbd> will take you to the editor. 

Note that you will need a GitHub account to make edits, and if you aren't logged in to it, launching the github.dev editor will prompt you for your GitHub login details.

## Making changes to the notes

1. To make changes, you can select files from the file explorer (1), and make edits to the note (2) as you would on any text editor or paste any changes made in Obsidian to existing notes. To add new files, you can also drag from your system's file explorer to the file explorer in the editor (1).
	![[github.dev editor.png]]
2. Once you are ready to submit your changes, switch to the version control tab. You'll see the names of the files you've modified under the "Changes" section:
    ![[github.dev editor version control.png|300]]
3. Add the files you want to submit by pressing the <kbd>+</kbd> sign (2), and write a message describing the changes you've made(1): 
	![[github.dev editor stage changes.png|300]]
4. To submit your files, you have to press the <kbd>✓</kbd> button at the top. 
	The first time you make an edit to the hub, you'll get a message explaining that GitHub will create a copy of the repository on your account. This is called a **Fork**.
	![[github.dev editor commit changes.png]]
5. Next, it will ask you to give a name to the *branch* where you want to save your changes. You can choose a new name for it, or just press enter. ^8cdfd9
	![[github.dev editor create branch.png]] 
6. GitHub will let you know it will switch now to the copy of the repository in your account. And once it reloads you'll see that your changes have been saved.
	![[github.dev switch to fork.png|300]]
	![[github.dev fork view.png]]

At this stage, your edits are in your fork of the Hub.

## Submitting changes to the Hub

Now you need to submit the changes in Fork to the original Hub repository.

This is called creating a **Pull Request**.

1. Clicking on [this](https://github.com/obsidian-community/obsidian-hub/compare) link is equivalent to going to the Hub repository, clicking on the Pull Requests tab and choosing New. Click on compare across forks, and choose yours on head repository. For the branch, switch to the one you chose on [[#^8cdfd9|step 6]] on the previous section:
	![[github compare forks.png]]
2. Once you have selected your fork and branch, you can choose <kbd>Create pull request</kbd>
	![[github create pull request.png]] 
3. Fill out the template and when you are done, press on <kbd>Create pull request</kbd>.  
	![[github fill out PR template.png]]

## What happens next?

Your Pull Request will be added to the [list of Pull Requests](https://github.com/obsidian-community/obsidian-hub/pulls) in the original Hub repository.

Your edits will later be reviewed by a volunteer of the Hub project, and then merged in to the latest version of the Hub.
Reviewers may request changes before merging. 

When the Publish site is next updated, your improvement will be visible to all. Thank you!

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/Editing%20notes%20using%20the%20github.dev%20editor.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/Editing%20notes%20using%20the%20github.dev%20editor.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
