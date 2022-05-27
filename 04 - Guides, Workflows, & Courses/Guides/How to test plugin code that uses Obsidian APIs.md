---
aliases: 
- 
tags:
- seedling
publish: true
---

# How to test plugin code that uses Obsidian APIs

When writing [[for Plugin Developers to Automate Tests|automated tests]] for plugins, it's common to find that your test code needs to use functions or classes in source files that use the Obsidian API.

Typically, developers find that those functions will fail to run from within test frameworks.

This note explores the available options.

## Move logic out to separate files

Use the [Extract Method refactoring](https://refactoring.guru/extract-method) to move the "business logic", that is, the code you need to test, out to separate functions that do not depend on Obsidian. Then move those functions out to files that do not depend on Obsidian.

By far the easiest way to do this is to use an automated refactoring tool, such as WebStorm, or [Abracadabra, refactor this!](https://marketplace.visualstudio.com/items?itemName=nicoespeon.abracadabra) for Visual Studio code.

This technique is demonstrated in the talk [[Plugin Testing for Developers]].

## Other people's suggestions

There are some useful discussions and links in the Obsidian API issue [Error running tests #13](https://github.com/obsidianmd/obsidian-api/issues/13).

- In [this comment](https://github.com/obsidianmd/obsidian-api/issues/13#issuecomment-819035670) [[renehernandez]] describes abstracting the usage of the filesystem capabilities from obsidian through an internal interface and depending on that interface instead of FileSystemAdapter directly. That way they can introduce a fake object during test to verify the logic they wanted in the FileDoc object.
- In [this comment](https://github.com/obsidianmd/obsidian-api/issues/13#issuecomment-880504457) `@lishid` lists some test frameworks that have attempted to help with testing Obsidian plugins:
    - [trashhalo/obsidian-plugin-e2e-test](https://github.com/trashhalo/obsidian-plugin-e2e-test): a sample repo with obsidian plugin e2e tests
    - [[obsimian-exporter#Obsimian Exporter]]: an Obsidian simulation framework for testing Obsidian plugins
    - These are both many months old, and may not be being maintained
- In [this comment](https://github.com/obsidianmd/obsidian-api/issues/13#issuecomment-1003880942) [[timhor]] reported that If anyone just needs to test editor-related functionality, he has had success substituting [CodeMirror](https://codemirror.net/doc/manual.html) as the editor on which his tests run (that's what Obsidian uses under the hood anyway). There are links showing how he did this.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/How%20to%20test%20plugin%20code%20that%20uses%20Obsidian%20APIs.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/How%20to%20test%20plugin%20code%20that%20uses%20Obsidian%20APIs.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
