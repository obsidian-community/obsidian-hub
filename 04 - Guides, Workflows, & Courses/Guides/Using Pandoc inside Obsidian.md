---
author: SkepticMystic
aliases: 
- Using Pandoc inside Obsidian
tags:
- seedling
publish: true
---

# Using Pandoc inside Obsidian

%% Add a description below this line. It doesn't need to be long: one or two sentences should be a good start. %%

The markdown slides from my [[Obsidian Community Talks|community talk]] on [[YT - Pandoc and Obsidian - Create slideshows, PDFs and Word documents]].
You can convert these to a [[revealjs]] slideshow using pandoc.

By [[SkepticMystic]]

# Command line tools

Let's you give commands directly to the computer using text.

- Usually we would click on things, but now we can **type** our commands
- Basic example: `echo`

## Structure of cmds

`function args --options`

- Options are like arguments, but optional
    - They come with a default.

## Perspective

You always run cmds **from** some folder/path

- `C:\Users\SkepticMystic`

## Paths

---

### Absolute

Starting from the "root" folder of your **computer**, a slash-separated list of folders to where you want to go.

Here:

```sh
C:\Users\SkepticMystic\Obsidian\CommunityTalks\Pandoc.md
```

---

Absolute paths don't care about where you currently are.

- They refer to the same place on your computer no matter which perspective you look from.

---

#### `cd`

<center>💡</center>

- From `C:\Users\SkepticMystic`

- To `C:\Users\SkepticMystic\Music\iTunes`

---

### Relative

Starting from the **folder you are currently in**, a slash-separated list of folders to where you want to go.

- The path to your file _relative_ to where you are right now.

- If you are running your cmd from `C:\Users\SkepticMystic`
- And you want to get to `C:\Users\SkepticMystic\Music\iTunes`...

# Pandoc

A command line tool to convert between document types

- **Pan**- (Greek) meaning "all", "of everything", or "involving all members" of a group.

---

Pandoc takes your document, converts it to a common type (AST), and then converts _that_ to your desired output type.

- Don't worry too much about this, just know you can convert from any one type, to most other types.

## First Conversions

Basic structure:

```sh
pandoc "file.md" -o "file.ext"
```

- ⚠️ if `file.ext` already exists, pandoc will **overwrite** it

---

### `md` → `docx`

```sh
pandoc "C:\Users\SkepticMystic\Pandoc\Example files\pandoc CT.md" -o "C:\Users\SkepticMystic\Pandoc\Conversions\pandoc CT.docx"
```

---

### `md` → `pdf`

```sh
pandoc "C:\Users\SkepticMystic\Pandoc\Example Files\pandoc CT.md" -o "C:\Users\SkepticMystic\Pandoc\Conversions\pandoc.pdf"
```

. . .

- ℹ️ You may need to install a pdf conversion engine, but pandoc will tell you how

# Citations

---

## Overview

1. Insert **citations** into your note
2. Tell pandoc where to find your **reference library**
3. Tell pandoc how to **style** your references

## 1. Pandoc Citations

All your references have a **citekey**.

- A unique identifier for that source
- Mine look like: `authorTitle(3)Year`
- `ajzenTheoryPlannedBehaviour2011`

---

Pandoc can insert a citation for you if you give it the citekey for that source in this form:

- `[@citekey]`
- `[@ajzenTheoryPlannedBehaviour2011]`

---

Citations plugin 💯

- Does this for you `Insert Markdown Citation`

## 2. Reference Library

You have to give your reference library to pandoc in a format it understands (`.bib` or `.json`).

- Example with Zotero
- Better Bibtex

## 3. Reference styles

There are _1000's_ of ways to style a reference

[Official library of styles](https://github.com/citation-style-language/styles)

- Find your style, and just copy the URL
- Example style: <https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl>

## Telling Pandoc to cite for you

We need to tell Pandoc:

1. Where to get the reference data from:

```sh
--bibliography "C:\Users\SkepticMystic\OneDrive\1D Personal\Zotero Exports\My Library.json"
```

---

2. Which reference style to use:

```sh
--citeproc --csl "https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl"
```

---

All together:

```sh
pandoc "C:\Users\SkepticMystic\Pandoc\Example files\reference-example.md" --bibliography "C:\Users\SkepticMystic\OneDrive\1D Personal\Zotero Exports\My Library.json" --citeproc --csl "https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl" -o "C:\Users\SkepticMystic\Pandoc\Conversions\reference-example.docx"
```

# Templates 🖌️

The default outputs for pandoc aren't winning any awards.

We can use templates to style them for us, though!

---

## Templates

Super powerful:

- Variables!
- Layout
- Styling

... Not gonna talk about them

## Reference Docs

Word doesn't let you use regular templates, but it does allow what are called "reference documents".

- _Some_ layout
- Styling

---

Let's make our own reference doc.

1. First get a copy of the default `reference.docx`

```sh
pandoc -o "C:\Users\SkepticMystic\Pandoc\Templates\custom-reference.docx" --print-default-data-file reference.docx
```

---

2. Open `custom-reference.docx` in Word, modify the styles, and save.

> The contents of the reference docx are ignored, but it's stylesheets and document properties (including margins, page size, header, and footer) are used in the new docx.
> [Pandoc Documentation](https://pandoc.org/MANUAL.html)

---

3. Apply it to a conversion

```sh
pandoc "C:\Users\SkepticMystic\Pandoc\Example files\pandoc CT.md" --reference-doc="C:\Users\SkepticMystic\Pandoc\Templates\custom-reference.docx" -o "C:\Users\SkepticMystic\Pandoc\Conversions\pandoc CT.docx"
```

# Snippets plugin

Allows you to run cmd line commands inside Obsidian!

- Just put your command inside a `sh` codeblock, and use the Snippets command `Run`

```sh
echo 'Hello Obsidian!'
```

```output
'Hello Obsidian!'

```

```sh
echo %date%
```

```output
2021/06/13

```

```sh
echo %date:/=-%
```

```output
2021-06-13

```

## `&`

Used to chain multiple commands together.

```sh
oneFunc & another
```

---

So far, we've been using absolute paths the whole time:

```sh
pandoc "C:/Users/SkepticMystic/OneDrive/1D Personal/git-Vault 1D/1. Projects/Obsidian/Community Talks/Using Pandoc to keep your workflow inside Obsidian.Community Talk.md"
--reference-doc="C:\Users\SkepticMystic\Pandoc\Templates\APA7.docx"
-o "C:\Users\SkepticMystic\Pandoc\Conversions\Using Pandoc to keep your workflow inside Obsidian.Community Talk %date:/=-%.docx"
```

---

But using `&`, we can first change drive into the closest folder with everything we need, then run the command from there:

```sh
cd "C:/Users/SkepticMystic/OneDrive/1D Personal" & pandoc "git-Vault 1D/1. Projects/Obsidian/Community Talks/Using Pandoc to keep your workflow inside Obsidian.Community Talk.md" --reference-doc="Pandoc\Templates\APA7.docx" -o "Pandoc\Conversions\Using Pandoc to keep your workflow inside Obsidian.Community Talk Live %date:/=-%.docx"
```

---

### `start`

Add `& start "" "output\file.docx"` to the end of the command to open the converted file immediately.

```sh
cd "C:/Users/SkepticMystic/OneDrive/1D Personal" & pandoc -s "git-Vault 1D/1. Projects/Obsidian/Community Talks/Using Pandoc to keep your workflow inside Obsidian.Community Talk.md" -o "Pandoc\Conversions\pandoc.Community Talk %date:/=-%.docx" & start "" "Pandoc\Conversions\pandoc.Community Talk %date:/=-%.docx"
```

## Using Templater

With Templater, we can create a template to insert into a file which fills in everything we need for us!

- `<% tp.file.title %>` - title of current file
- `<% tp.file.path(relative=true) %>` - relative path to current file
- `<% tp.system.suggester(["A", "B"], ["A", "B"]) %>` - asks the user for a choice between A and B, and returns the result

---

```sh
cd "C:/Users/SkepticMystic/OneDrive/1D Personal" & pandoc -s "git-Vault 1D/<% tp.file.path(relative=true) %>" --citeproc --csl "https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl" --bibliography "Zotero Exports\My Library.json" --reference-doc="Pandoc\Templates\<% tp.system.suggester(["APA7", "Thesis"], ["APA7", "Thesis"]) %>.docx" -o "Pandoc\Conversions\<% tp.file.title %> %date:/=-%.docx" & start "" "Pandoc\Conversions\<% tp.file.title %> %date:/=-%.docx"
```

# Revealjs

We can also make [revealjs](https://revealjs.com) slide shows.

We just need to tell pandoc to convert our markdown **to** `-t` revealjs.

---

```sh
cd "C:/Users/SkepticMystic/OneDrive/1D Personal" & pandoc -t revealjs --slide-level=2 -s "git-Vault 1D/3. Resources/Field/reveal test.md" -o "Pandoc\Conversions\reveal test %date:/=-%.html" & start "" "Pandoc\Conversions\reveal test %date:/=-%.html"
```

## Other options

- Themes: `-V theme={themeName}`
- Slide-level: `--slide-level={number}`
- Custom styling: `--css="path\to\stylesheet.css"`
- And you can also use references like we've covered already

---

```sh
cd "C:/Users/SkepticMystic/OneDrive/1D Personal" & pandoc -t revealjs -V theme=beige --slide-level=2 -s "git-Vault 1D/3. Resources/Field/reveal test.md" --citeproc --csl "https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl" --bibliography "Zotero Exports\My Library.json" -H "C:\Users\SkepticMystic\Pandoc\Stylesheets\reveal-js-styles.css" -o "Pandoc\Conversions\reveal test %date:/=-%.html" & start "" "Pandoc\Conversions\reveal test %date:/=-%.html"
```

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Using%20Pandoc%20inside%20Obsidian.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Using%20Pandoc%20inside%20Obsidian.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
