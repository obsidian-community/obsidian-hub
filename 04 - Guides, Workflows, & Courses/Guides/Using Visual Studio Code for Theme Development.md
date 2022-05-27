---
aliases: 
- vscode
- visual studio code
tags:
- seedling
publish: true
---

# Using Visual Studio Code for Theme Development
*written by [[damiankorcz|Damian Korcz]]*

## 📝 Prerequisites
This guide points out the most useful features of VSCode which will help you with Theme Development.

If you are brand new to Theme Development in Obsidian, you might want to visit the [[for Theme Designers]] section of the Hub to familiarise yourself with a few basics.

If you don't already use Visual Studio Code (often abbreviated as VSCode), you can download it from here: **https://code.visualstudio.com/**

VSCode is available for Windows, Linux and MacOS.

To help you get up to speed with VSCode, the [**Documentation**](https://code.visualstudio.com/docs) from the VSCode team is a good place to start; specifically the [**Introductory Videos**](https://code.visualstudio.com/docs/getstarted/introvideos) and the section describing useful features for [**CSS, SCSS and Less**](https://code.visualstudio.com/docs/languages/css).

## 💻 Workspaces
The Workspaces function in VSCode allows you to have an independent 'profile' for your project allowing it to have it's own set of specific settings, and Extensions that are enable/disabled for it, etc. 

**To create a Workspace in VSCode:**
1. Open your Project's folder by going to `File` and selecting `Open Folder...`.
2. Save it by going to `File` and selecting `Save Workspace As...`.

You can now use the newly created `.code-workspace` file as a shortcut to your Project's workspace instead of launching VSCode directly. Keep in mind that the `.code-workspace` file stores the workspace specific settings so keep it somewhere safe. I keep mine in the root folder that stores all of my project repositories. You can always make a shortcut of it on your desktop for more convenient access.

I personally like to disable most Extensions globally in VSCode and only enable the ones that are relevant to each Workspace. This helps to reduce the load VSCode puts on your system if you use a lot of different Extensions across your projects.

**To Manage Enabled/Disabled Extensions in VSCode:**

1. Open the Extensions window:

	`Ctrl+Shift+X` (Windows/Linux)
	`Cmd+Shift+X` (MacOS)

2. Enable/Disable Extension globally:

	`Right Click` on the Extension and select `Enable` / `Disable`.

3. Enable/Disable Extension for the current Workspace:

	`Right Click` on the Extension and select `Enable (Workspace)` / `Disable (Workspace)`.

**More Info: [Workspaces](https://code.visualstudio.com/docs/editor/workspaces)**

## 🗃️ Folding and Regions

Region Markers allow you to setup custom `Regions` which can help you with organising your code and as an additional way to fold your code.

**You can add custom Region Markers for CSS/Less/SCSS using:**

- `/*#region*/` at the Start of the Region.
- `/*#endregion*/` at the End of the Region.

**Fold All Regions Marker:**

`Ctrl+K` followed by `Ctrl+8` (Windows/Linux)
`Cmd+K` followed by `Cmd+8` (MacOS)

**Unfold All Regions Marker:**

`Ctrl+K` followed by `Ctrl+9` (Windows/Linux)
`Cmd+K` followed by `Cmd+9` (MacOS)

> 💡 **EXAMPLE**
> ![[VSCode Guide - Folding and Regions.gif]]
> You can organise different sections of your CSS/SCSS and make it easy to fold them away for easier navigation.
 
**More Info: [Folding and Regions](https://code.visualstudio.com/docs/editor/codebasics#_folding)**

## ⌨️ Useful Shortcuts
To see the full list of available shortcuts inside VSCode use:

`Ctrl+K` followed by `Ctrl+S` (Windows/Linux)
`Cmd+K` followed by `Cmd+S` (MacOS)

Here are per OS Shortcut References in PDF format: [**Windows**](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf), [**Linux**](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf) and [**MacOS**](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf).

If you are coming from another IDE/Text Editor you might be able to use an extension to replace VSCode Shortcuts/Keymaps with the ones found in the IDE/Text Editor you used. There is a section of the [**VSCode Extension Marketplace dedicated to Keymaps**](https://marketplace.visualstudio.com/search?target=VSCode&category=Keymaps&sortBy=Installs).

Here are a few Shortcuts to handy functions of VSCode:

 ### Command Palette
 
 `Ctrl+Shift+P` (Windows/Linux)
 `Cmd+Shift+P` (MacOS)

> 💡 **EXAMPLE**
> ![[VSCode Guide - Command Palette.gif]]
> Open the Command Palette and search for the function you are looking for. You have access to all of the functionality of VS Code, including keyboard shortcuts for the most common operations. Handy for figuring out shortcuts for frequently used functions.

**More info: [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)**

### Quick File Navigation

`Ctrl+P` (Windows/Linux)
`Cmd+P` (MacOS)

> 💡 **EXAMPLE**
> ![[VSCode Guide - Quick File Navigation.gif]]
> Use the Quick File Navigation to get to any file in your project with ease. Just start typing out the name of the file and select it in the list for it to open in the editor.

**More Info: [Quick File Navigation](https://code.visualstudio.com/docs/editor/editingevolved#_quick-file-navigation)**

### Search

`Ctrl+Shift+F` (Windows/Linux)
`Cmd+Shift+F` (MacOS)

> 💡 **EXAMPLE**
> ![[VSCode Guide - Search.gif]]
> Search for a phrase across **all files in the Workspace**. You can replace that phrase with a new text. Click on any result to have it open up in the editor at the specific search result. 

**More info: [Search](https://code.visualstudio.com/docs/editor/codebasics#_search-across-files)**

### Find and Replace

`Ctrl+F` (Windows/Linux)
`Cmd+F` (MacOS)

> 💡 **EXAMPLE**
> ![[VSCode Guide - Find and Replace.gif]]
> Search for a phrase across the **current file**. You can replace that phrase with a new text.

**More info: [Find and Replace](https://code.visualstudio.com/docs/editor/codebasics#_find-and-replace)**

### Multiple Selection (multi-cursor)

`Alt+Click` **OR** `Ctrl+Alt+Up` / `Ctrl+Alt+Down` (Windows/Linux)
`Alt+Click` **OR** `Cmd+Alt+Up` / `Cmd+Alt+Down` (MacOS)

> 💡 **EXAMPLE**
> ![[VSCode Guide - Multiple Selection-Multi-Cursor.gif]]
> Place the cursor where you click or add an additional one directly above or below the current one.

You can also `Click`  to select a word, and press:

`Ctrl+D` (Windows/Linux)
`Cmd+D` (MacOS)

This adds the next occurrence of the currently selected text to the selected text.

> 💡 **EXAMPLE**
> ![[VSCode Guide - Multiple Selection-Next-Occurrence.gif]]
> You can quickly select the same word in your file without needing to individually place the next cursor by clicking. Handy when the word is in a different place on each line.

**More Info: [Multiple Selection (multi-cursor)](https://code.visualstudio.com/docs/editor/codebasics#_multiple-selections-multicursor)**

### Column (Box) Selection

`Click` where you want to start a Column (Box) Selection, press and hold `Shift+Alt` while `Click` selecting to the opposite corner and release once the selection is complete. (Windows/Linux/MacOS)

> 💡 **EXAMPLE**
> ![[VSCode Guide - Column-Box Selection.gif]]
> Use the Column (Box) Selection if you need to change some text/values that are horizontally aligned.

**More Info: [Column (Box) Selection](https://code.visualstudio.com/docs/editor/codebasics#_column-box-selection)**

### Toggle Wrapping in Current File

`Alt+Z` (Windows/Linux/MacOS)

> 💡 **EXAMPLE**
> ![[VSCode Guide - Toggle Wrapping.gif]]
> If your file includes long lines of text e.g. Base64 embedded fonts/SVGs toggling Wrapping will make them remain on one line no matter the length or wrap the text around to the next line depending on the width of the File's window.

**More Info: [Toggle Wrapping in Current File](https://code.visualstudio.com/docs/editor/codebasics#_how-do-i-turn-on-word-wrap)**

### Rename Symbol

Click on what you want to rename and press `F2` (Windows/Linux/MacOS)

> 💡 **EXAMPLE**
> ![[VSCode Guide - Rename Symbol.gif]]
> To rename any text/variable instances, click on one of them and press `F2`. Change the name to what you want and it will rename all of the instances of the selected text/variable to what you typed.

**More Info: [Rename Symbol](https://code.visualstudio.com/docs/editor/editingevolved#_rename-symbol)**

## ⚙️Settings 
You can access the Settings by pressing:

`Ctrl+,` (Windows/Linux)
`Cmd+,` (MacOS)

The Settings can be changed independently for:

- User (Global)
- Current Workspace
- Currently Open Folder

For generic settings I would recommend setting them in the User and for specific settings to the workflow of the project setting them in the Workspace.

Here is a list of useful Settings (You can search for them using the Search Bar at the top of the Settings window):

### Files: Auto Save
Using the `After Delay` option the files save after a set delay once any change is made to the file. You can adjust the delay time in the `Files: Auto Save Delay` setting to whatever you want. I have it set to `1000` milliseconds (1 second).

### Editor: Font Family
This will change the font used in the editor area of VSCode. The fonts are sourced from the ones installed on your Operating System. Use the name of the system font to set it. You can also adjust the size of the font using the `Editor: Font Size` setting.

### Files: Exclude
If there are any files or folders you don't want to show up in the File Explorer you can hide them by adding a new pattern.

**More Info: [Settings](https://code.visualstudio.com/docs/getstarted/settings)**

## 💾 Settings Sync
If you happen to be working with VSCode across multiple devices it is a good idea to setup Settings Sync. It will synchronise settings, key bindings and installed extensions across your machines. You will need to use a Microsoft account or a GitHub account to sync.

Simply click on the `Cog` icon in the bottom left corner and select `Turn On Settings Sync...`. You will be presented with the options for data to be synchronised. 

**More Info: [Settings Sync](https://code.visualstudio.com/docs/editor/settings-sync)**

## 🔌 Extensions
Here is a list of useful Extensions:

### General
- [**Color Highlight**](https://marketplace.visualstudio.com/items?itemName=naumovs.color-highlight) - Adds a background of the color corresponding to the color value in the code. 
- [**Code Spell Checker**](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) - Spell checking for VSCode. By Default it's set to US English and comes with GB English as well. Other languages are available as additional Extensions.
- [Change Color Format](https://marketplace.visualstudio.com/items?itemName=bbugh.change-color-format) - enables you to quickly convert colors into different color formats.

### Sass/SCSS
- [**Sass**](https://marketplace.visualstudio.com/items?itemName=Syler.sass-indented) - Indented Sass syntax highlighting, autocomplete & Formatter for VSCode.
- [**SCSS IntelliSense**](https://marketplace.visualstudio.com/items?itemName=mrmlnc.vscode-scss) - SCSS IntelliSense (Variables, Mixins and Functions) for all files in the workspace.
- [**Stylelint**](https://marketplace.visualstudio.com/items?itemName=stylelint.vscode-stylelint) - A mighty, modern linter that helps you avoid errors and enforce conventions in your styles.

### Themes/Icons
Here are my personal favourites I'm currently using:
- [**Lucy Theme**](https://marketplace.visualstudio.com/items?itemName=juliettepretot.lucy-vscode) - Easy on the eyes and nice looking theme. I use the `lucy-evening` variant.
- [**File Icons**](https://marketplace.visualstudio.com/items?itemName=file-icons.file-icons) - Icon set for files in the File Explorer.
- [**Fluent Icons**](https://marketplace.visualstudio.com/items?itemName=miguelsolorio.fluent-icons) - Changes the icons in the Left Sidebar to more rounded ones.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Using%20Visual%20Studio%20Code%20for%20Theme%20Development.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Using%20Visual%20Studio%20Code%20for%20Theme%20Development.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
