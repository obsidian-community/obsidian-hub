---
aliases: 
- "Why automate tests for plugins?"
tags:
- seedling
publish: true
---

# Why automate tests for plugins?

This note describes the motivation for writing [[for Plugin Developers to Automate Tests|automated tests for software]], in the context of writing plugins for Obsidian.

## Manual Testing

### Why even test your plugin at all?

- To know it works: intended behaviour
- To know it's done/good enough
- To not break user's (and your) data

### Steps to test Obsidian Plugins

*Typically...*

1. Write your code
1. Build your plugin
1. Run it in Obsidian
1. Click and type to test it
1. Go to 1

Note:

- Yes, it's possible to streamline that
- But it's still a mental context switch out of your IDE
- And it interrupts your flow

### Testing Over Time...

It starts off easy, and gets progressively harder.

- You add a **feature**
    - You know how to test it manually and you know it works
    - The code is small and fresh in your mind
- You had **another feature**
    - Now you have two features to test
- You had another feature, and **a few more**
    - Either you test by hand all the features so far and the interactions between them, or maybe you just test the newest features
    - Now you have got more codes that could break and more features to test
    - And of course the code becomes more complicated to
- Maybe somebody comes along and submit a **pull request** to improve your plug-in
    - They didn't know all the manual tests they needed to run, so now you need to run all the manual tests
- Or maybe you spend your time writing up a **load of detailed notes** about how to test it manually, and of course those notes quickly become out of date
    - And the time that you're spending writing instructions about testing or testing manually it's not just boring time it's time when you're not adding value and not having fun
- Or maybe you wait for users to report bugs and breakages?

## Another way

- You write short snippets of code that exercise bits of your plug-in in various ways and that check that the result is what was expected
- Now you've written that code, you can run it as many times as you want - and very quickly
- You can even make it run continuously whilst you're developing
- The computer can check the behaviour far faster than you can
- And you can ask GitHub Actions to run it for you every time you or a contributor pushes code to GitHub

## Why automated tests?

- Massively quicker than manual
- Fix whilst fresh in mind
- The earlier a bug is found, the easier it is to fix it
- Helps others work on code
- Learn about your code
- Learn about other people's code

## Isn't it hard?

- It's a skill you can learn
- Gets easier with practice
- Gets easier with seeing how others test code
- When you get good at it, it saves loads of time

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Why%20automate%20tests%20for%20plugins.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Why%20automate%20tests%20for%20plugins.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
