---
aliases: 
- 
tags:
- seedling
publish: true
---

# Plugin Testing for Developers

By [[claremacrae|Clare Macrae]]

This [[Obsidian Community Talks|talk]] is an introduction to [[for Plugin Developers to Automate Tests|automated testing of Obsidian plugins]] for developers, and to automated testing of software in general.
The [[YouTube|video]] of this talk can be found below, followed by a summary of [[#The plugins reviewed|the plugins reviewed]]:

<iframe width="100%" height="400px" src="https://www.youtube.com/embed/OviNyXnvi-o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## The plugins reviewed

Much of the talk used 4 Obsidian plugins that already had automated tests to explore how to test, and what makes good tests.

These are the plugins reviewed.

### Note Refactor

- [[note-refactor-obsidian|Note Refactor]]
- Uses **mocha**
- Nice break-up of tests
- Nice test descriptions
- Mock of date
- Sample data file

### Dataview

- [[dataview|Dataview]]
- Uses **Jest**
- Takes noticeable amount of time - lots of tests
- Demonstration:Can run individual tests
- Demonstration:Can explore behaviour of the code

### Linked Data Helper

- [[linked-data-helper|Linked Data Helper]]
- Uses **Jest**
- Test data stored in repo
- Nice helper functions so tests are readable
- Uses Jest snapshot testing to capture complex output

> I have to say, it is really a good feeling that I can just run the tests and see that I get the same output instead of needing to run the commands inside Obsidian.
> 
> @koala/@kometenstaub

### Tasks

- [[obsidian-tasks-plugin|Tasks]]
- Uses **Jest**
- Nice data-driven tests
- Nice integration with GitHub Actions
- Nice integration with git: [lefthook.yml](https://github.com/obsidian-tasks-group/obsidian-tasks/blob/3210fffba1afba3520366531f084adab268f0622/lefthook.yml)
- Shows mocking of dates in Jest
- General comment: quite a lot of repetition of code in the tests, at the time of the talk
- Demonstration: using 'extract method' refactoring

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Community%20Talks/Plugin%20Testing%20for%20Developers.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Community%20Talks/Plugin%20Testing%20for%20Developers.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
