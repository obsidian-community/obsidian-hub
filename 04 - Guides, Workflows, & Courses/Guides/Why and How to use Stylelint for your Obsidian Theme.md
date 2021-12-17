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

This guide explains why it is beneficial for theme designers to use a linter and how to get started with [Stylelint](https://stylelint.io/) , the most popular linter for CSS.

## What is Linting, and what is its purpose?
[Linters](https://www.wikiwand.com/en/Lint_(software)) are basically tools that analyze code and report bugs as well as stylistic problems. There are linters for every programming language,[^1] and [Stylelint](https://stylelint.io/) is regarded as the state-of-the-art linter for CSS code.

__Using a linter has several advantages:__
1. They report *errors* and best-practice-violations in your code, e.g., using `//comments` which are invalid in CSS.
2. They enforce *consistent* styling, which increases the readability of your code, e.g., to always have exactly one line break after between two blocks.
3. For the simpler rules, linters usually also offer an option to *autofix* the code, *saving you tons of time* to clean your code.

As styling rules are of course subjective, they are opt-in and configurable. Error reports, however, are mostly unambiguous and in my view the reason *everyone* should use a linter, regardless of the value one puts on code consistency.

## Getting Started

### Requirements
Stylelint, as most linters, are installed via `npm`. To check whether you have `npm` installed, you can run this command in your Terminal:

```shell
# Check whether npm is installed
npm -v
```

If the command returns a version number, you are good to go. If it doesn't, you need to [install Node on your machine](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm). (Homebrew users on Mac can easily do that via `brew install node`.)

### Installing Stylelint
When you have `npm` installed, you just need to run the following code in your Terminal to install `stylelint` and its dependency, `postcss`. 

```shell
# Install stylelint & dependency
npm install -g stylelint postcss
```

### Stylelint Configuration File
In contrast to other linters, `stylelint` will not work without a configuration file. So you have to create a configuration file (`.styelintrc.json`) before you are able to use `styelint`.

```shell
# Create a stylelint configuration file in your home directory
touch ${HOME}/.stylelintrc.json
```

Now creating the configuration isn't enough, since `stylelint` has *turned off all rules by default*. This means you have to set up some basic configuration, too, before you can use stylelint. Luckily, there is the `npm` package `stylelint-config-recommended` which activates all linting rules regarding ["possible errors"](https://stylelint.io/user-guide/rules/list/#possible-errors).

```shell
# Install recommended configurations
npm install -g stylelint-config-recommended
```

Then, you open the `.stylelintrc.json` in your home directory. Note that files that begin with `.` (so-called "dot files") are hidden by default on macOS. So you either have to make hidden files visible (by pressing `cmd + shift + .` in Finder) or you by using this command in the Terminal:

```bash
# open config file via Terminal
open ${HOME}/.stylelintrc.json
```

For getting started more easily, __I recommend to simply copypaste the following basic configuration__. This will activate `stylelint-config-recommended`, but disable two rules that mostly create false positives in the specific context of Obsidian theme development.

```json
{
	"extends": ["stylelint-config-recommended"],
	"rules": {
		"font-family-no-missing-generic-family-keyword": null,
		"no-descending-specificity": null
	}
}
```

While there are far more things stylelint can do, this should suffice as a basic setup to get started. (At the end of this guide, I explain how to do further configurations.)

## Usage

### In the Terminal
The most basic usage is done via the command line. The two most common commands are the one to report all issues and the one to autofix issues (and report the ones that cannot be autofixed).[^2]

```shell
# Report all issues
stylelint "/path/to/my/css/file/theme.css"

# Autofix issues and report the non-fixable issues remaining
stylelint --fix "/path/to/my/css/file/theme.css"
```

### In the Code Editor
More convenient than using `stylelint` in the Terminal is to install an integration for your code editor. With those editor integrations, you can get live feedback on linting rule violations as soon as you type them.

There is a plugin for [Sublime Text](https://packagecontrol.io/packages/SublimeLinter-stylelint) (also requires the [SublimeLinter Plugin](https://packagecontrol.io/packages/SublimeLinter)), a plugin for [VS Code](https://marketplace.visualstudio.com/items?itemName=stylelint.vscode-stylelint), and a bunch of plugins for [other common code editors](https://stylelint.io/user-guide/integrations/editor/).

## Further Configuration

### Rules for Styling and Best Practices
The configuration set up in the sections before only covers linting rules *reporting errors in CSS*. However, you can also set up rules for consistent code, best practices, and increased readability of code.

You can take a look at the [list of all stylelint rules](https://stylelint.io/user-guide/rules/list/) featuring a total of 170 rules and add choose any of them as you like. Remember that all rules under the section "Possible Errors" are already enabled by `stylelint-config-recommended`, so you not need to add them.[^3]

To add the custom rules, open the `.stylelintrc.json` again and simply add any rules in plain text. If you are not familiar with it, the configuration file is formatted as `json`, and you need to follow the [JSON Syntax](https://www.w3schools.com/js/js_json_syntax.asp), otherwise `styelint` won't work. (If you cannot find the error in your configuration, you can use a [JSON validator](https://jsonformatter.curiousconcept.com/) to locate your syntax error.)

### Plugins for Stylelint
On top of all that, there are even [dozens of plugins for stylelint](https://github.com/hudochenkov/stylelint-order), too. The most relevant one should be [stylelint-order](https://github.com/hudochenkov/stylelint-order), which automatically orders declarations inside blocks, I personally also like [a small plugin that reports ignored properties](https://www.npmjs.com/package/stylelint-declaration-block-no-ignored-properties). You install the plugins as you did install everything else before:

```shell
# Install plugins
npm install -g stylelint-order 
npm install -g stylelint-declaration-block-no-ignored-properties
```

Plugins and their rules *both* need to be activated in your `.stylelintrc.json`. The details on to do that what the plugins do exactly can be found in the READMEs of the respective plugin.

### Example Configuration
You can take a look at the [stylelint configuration of *Shimmering Focus*](https://github.com/chrisgrieser/shimmering-focus/blob/main/.stylelintrc.json) for an example of how far you can fine-tune stylelint.

[^1]: There is also [[obsidian-linter|Linter specifically for Obsidian]].
[^2]: You can find out which rules can be autofixed by checking the [documentation of the specific rules](https://stylelint.io/user-guide/rules/list/#possible-errors).
[^3]: You can, however, add them to apply some manual changes, like [changing the severity of a rule](https://stylelint.io/user-guide/configure#severity) from `error` to `warning`.
