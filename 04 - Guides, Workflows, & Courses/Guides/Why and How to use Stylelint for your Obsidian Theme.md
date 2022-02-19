---
aliases: 
- stylelint
- linter
tags:
- 
publish: true
---

# Why and How to use Stylelint for your Obsidian Theme
*written by [[chrisgrieser|pseudometa]]*

This guide explains why it is beneficial for theme designers to use a linter and how to get started with [Stylelint](https://stylelint.io/), the most popular linter for CSS.

## What is Linting, and what is its purpose?
[Linters](https://www.wikiwand.com/en/Lint_(software)) are tools that analyze code to report bugs and stylistic problems. There are linters for pretty much every programming language,[^1] and [Stylelint](https://stylelint.io/) is regarded as the state-of-the-art linter for CSS.

__Using linters has several advantages:__
1. They point out *invalid code*, e.g., using `//comments` which are invalid in CSS.
2. Linters also encourage best practices in your code, like avoiding duplicate selectors.
3. They enforce *consistent* styling, which increases the readability of your code, e.g., to always have exactly one line break after between two blocks.
4. For the simpler rules, linters usually offer an option to *auto-fix* the code, saving you a lot of time.

As the rules regarding styling are quite subjective, they are all opt-in and configurable. Error reports, however, are unambiguous and, in my view, the reason why *everyone* should use a linter, regardless of the value one puts on nicely formatted code.

## Getting Started

### Requirements
`stylelint`, as most linters, is installed via `npm`. To check whether you have `npm` installed, you can run this command in your Terminal:

```shell
# Check whether npm is installed
npm -v
```

If the command returns a version number, you are good to go. If it doesn't, you need to [install Node on your machine](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm). (Homebrew users on Mac can do that via `brew install node`.)

### Installing Stylelint
After installing `npm`, you can run the following code in your Terminal to install `stylelint` and its dependency, `postcss`. 

```shell
# Install stylelint & dependency
npm install -g stylelint postcss
```

### Stylelint Configuration File
In contrast to most other linters, `stylelint` will not work without a configuration file. This means you have to create such a configuration file (`.stylelintrc.json`) before you can use `stylelint`.

```shell
# Create a stylelint configuration file in your home directory
touch ${HOME}/.stylelintrc.json
```

By default, all `stylelint` rules are turned off, meaning you have to add some basic configuration before you can use `stylelint`. Luckily, there is the `npm` package `stylelint-config-recommended` which activates all linting rules regarding ["possible errors"](https://stylelint.io/user-guide/rules/list/#possible-errors). You can install it via:

```shell
# Install recommended configurations
npm install -g stylelint-config-recommended
```

Then, open the `.stylelintrc.json` in your home directory. 

Note that files beginning with `.` (so-called "dotfiles") are hidden by default on macOS. So if you are on macOS, you either have to make hidden files visible by pressing `cmd + shift + .` in Finder, or you can open the configuration file via this Terminal command:

```bash
# open config file via Terminal
open ${HOME}/.stylelintrc.json
```

To keep things simple, __I recommend you simply copy-paste the following basic configuration__ into that file. This will activate `stylelint-config-recommended`, but disable two rules that mostly create false positives in the specific context of Obsidian theme development.

```json
{
	"extends": ["stylelint-config-recommended"],
	"rules": {
		"font-family-no-missing-generic-family-keyword": null,
		"no-descending-specificity": null
	}
}
```

While there are far more things `stylelint` can do, this should suffice to get started. (At the end of this guide, I explain how to do further configurations.)

## Usage

### In the Terminal
The most basic usage is done via the command line. The two most common commands are the one to report all issues and the one to auto-fix issues (and report those that cannot be auto-fixed).[^2]

```shell
# Report all issues
stylelint "/path/to/my/css/file/theme.css"

# Auto-fix issues and report the remaining non-fixable issues
stylelint --fix "/path/to/my/css/file/theme.css"
```

### In the Code Editor
More convenient than using `stylelint` in the Terminal is to install an integration for your code editor. With those editor integrations, you can get live feedback on rule violations as soon as you type them.

There is a plugin for [Sublime Text](https://packagecontrol.io/packages/SublimeLinter-stylelint), a plugin for [VS Code](https://marketplace.visualstudio.com/items?itemName=stylelint.vscode-stylelint), and various plugins for [other common code editors](https://stylelint.io/user-guide/integrations/editor/).

## Further Configuration

### Rules for Best Practices and Code Formatting
With the current configuration, `stylelint` will only report clear and likely errors in your CSS. You can, however, also set up `stylelint` to check consistency, best practices, and increased readability.

The `stylelint` documentation [lists a total of 170 rules](https://stylelint.io/user-guide/rules/list/) from which you can choose. (Remember that all rules under the section "Possible Errors" are already enabled by `stylelint-config-recommended`, so you do not need to add them.)

To include more rules, open the `.stylelintrc.json` again and simply add any rules in plain text. The configuration file is formatted as `json`, meaning you have to follow the [JSON Syntax](https://www.w3schools.com/js/js_json_syntax.asp). (If you cannot find the error in your configuration, you can use a [JSON validator](https://jsonformatter.curiousconcept.com/) to locate your syntax error.)

### Plugins for Stylelint
On top of all that, there are [dozens and dozens of plugins for stylelint](https://github.com/hudochenkov/stylelint-order), too. The most important one is [stylelint-order](https://github.com/hudochenkov/stylelint-order), which enables `styelint` to automatically order declarations inside blocks. I personally also like [a small plugin that reports ignored properties](https://www.npmjs.com/package/stylelint-declaration-block-no-ignored-properties). You install the plugins as you did install everything else before:

```shell
# Install plugins
npm install -g stylelint-order 
npm install -g stylelint-declaration-block-no-ignored-properties
```

Plugins and their rules *both* need to be activated in your `.stylelintrc.json`. The details on how to do that can be found in the READMEs of the respective plugin.

### Example Configuration
You can take a look at the [stylelint configuration of the theme *Shimmering Focus*](https://github.com/chrisgrieser/shimmering-focus/blob/main/.stylelintrc.json) as an example of a very extensive configuration.

[^1]: There is also a [[obsidian-linter|Linter specifically for Obsidian]].
[^2]: You can find out which rules can be auto-fixed by checking the [documentation of the specific rules](https://stylelint.io/user-guide/rules/list/#possible-errors).

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Why%20and%20How%20to%20use%20Stylelint%20for%20your%20Obsidian%20Theme.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Why%20and%20How%20to%20use%20Stylelint%20for%20your%20Obsidian%20Theme.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
