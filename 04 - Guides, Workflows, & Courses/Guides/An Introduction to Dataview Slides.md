---
author: SkepticMystic
aliases: 
- 
tags:
- seedling
publish: true
---

# An Introduction to [[dataview|Dataview]] (Slides)

%% Add a description below this line. It doesn't need to be long: one or two sentences should be a good start. %%

These are the original markdown slides from my [[Obsidian Community Talks|Community Talk]] on [[YT - An Introduction to Dataview|An Introduction to Dataview]].

You can convert these slides to [[revealjs]] by [[Using Pandoc inside Obsidian|using Pandoc]].

For a better reading experience on the web version of the hub, these notes have been reformatted and provided in [[An Introduction to Dataview|condensed form]].

By [[SkepticMystic]]

# Overview

---

1.  Broad Intro to Dataview

. . .

2.  Metadata

::: incremental

3.  Dataview Queries
    - `List`
    - `From`
    - `Where`
    - `Task`
    - `Table`
    - `Sort`
    - `Flatten`
    - `Group by`

:::

# Introduction

## {data-background-iframe="https://blacksmithgu.github.io/obsidian-dataview/#/README"}

# Metadata

## What is it?

Metadata provides information _about_ your data.

. . .

It is _extra_ info that is either already _inherent_ in your data, or info that you **manually add**.

## Examples of Metadata 💡

---

### Photographs

::: incremental

- Date & time ⏰
- Location 🌍
- People 🧑‍🤝‍🧑

:::

---

My display picture has the following _inherent_ metadata:

:::::::::::::: {.columns}
::: {.column width="60%"}
![|SkepticMystic Mandala dp](https://i.imgur.com/UrwAWzI.jpg)
:::
::: {.column width="40%"}
![|Image metadata](https://i.imgur.com/dWmowLU.png)
:::
::::::::::::::

---

But it could also be given other properties:

![|Edit image metadata](https://i.imgur.com/YPT6Gzb.png){ height=400px }

---

### Markdown Notes

We can also add metadata to **Markdown notes** using a language called <abbr title="Yaml Ain't Markup Language"><em>YAML</em></abbr>.

- YAML is a **structured** way of adding _arbitrary_ metadata to a file.

---

#### Adding YAML Metadata

1.  At the **top** of your note, add 3 dashes `---`
2.  Underneath that, you can start adding key-value pairs in the form `key: value`
    - In the photo example, this would look as follows:

```yaml
---
dimensions: 1200x1200
bit depth: 24
title: "Mandala Display Picture"
rating: 5
---
```

3.  To finish the metadata block, close it off with 3 dashes again `---`.

---

```yaml
---
dimensions: 1200x1200
bit depth: 24
title: "Mandala Display Picture"
rating: 5
---
```

## YAML Lists

You can add more than one `value` to each `key` using _lists_.

There are two notations you can use:

##### 1. Inline

```yaml
foods: [apples, pears, oranges]
```

---

##### 2. Indented

```yaml
foods:
  - apples
  - pears
  - oranges
```

==Note the spacing==

## Types of Metadata

You can find this information on the [Dataview reference page](https://blacksmithgu.github.io/obsidian-dataview/#/README)

```yaml
number: 3.6
string: "Foo all the bars"
list:
  - 1
  - -2
  - 3.5
  - 1.61803

date:
  - 2021-04
  - "2021-04-09"
  - 2021-04-09T12:12:54

link: [[2021-04-09 Daily Note]]
```

---

### Implicit Metadata in all notes

| Property     | Value                                    | Type     |
| ------------ | ---------------------------------------- | -------- |
| `file.name`  | File **title**                           | `string` |
| `file.path`  | Full file **path**                       | `string` |
| `file.link`  | **Link** to the file                     | `link`   |
| `file.size`  | **Size** (in bytes) of the file          | `number` |
| `file.ctime` | Date that the file was **created**       | `date`   |
| `file.mtime` | Date that the file was last **modified** | `date`   |
| `file.day`   | The **date** contained in the note title | `date`   |

---

`file.tags` - An `array` of all **tags** in the note.

. . .

- Subtags are broken down by each level, so `#Tag/1/A` will be stored in the array as

<br>

`[#Tag, #Tag/1, #Tag/1/A]`

# Dataview Queries

## `List`

Creates a _list_ of the specified notes

```dataview
list
```

## `From`

Determines **where** to get notes _from_.

---

### From \#Tag

You can get all notes _from_ a specified **tag**:

```dataview
list
from #MOC
```

---

### From "Folder"

All notes from a **folder**:

```dataview
list
from "1. Projects"
```

---

### From \[\[Links\]\]

And even all notes with links coming _into_ a note:

```dataview
list
from [[Yoga MOC]]
```

Or going _out of_ a note:

```dataview
list
from outgoing([[yoga MOC]])
```

- This syntax may change in an upcoming release.

---

### Combining Sources

You can use the 3 basic logical operators to create more complex `from` queries:

::: incremental

- `list from #A and #B`
- `list from "University" or "Work"`
- `list from -#Personal`
- `list from [[CSS]] and -#HTML`

:::

---

### String Concatenation

In the results of a `list`, you can include metadata fields joined with strings

```dataview
list "File Path: " + file.path + " :)"
from #SN
```

---

### Lists of lists

A `list` can also display indented sublists of metadata:

```dataview
list authors
from #SN/Blog
```

## `Task`

`Task` searches for all checkboxes `- [ ] ` in your vault.

It returns a list of all tasks, grouped by their parent note

```dataview
task from #MOC
```

# `Where`

---

After choosing _which_ notes to use, you can narrow down the list further using a `where` block.

. . .

This lets you use the various _comparison operators_ on the metadata fields in your notes.

`>`, `>=`, `<`, `<=`, `=`, `!=`

. . .

<center>`where {condition}`</center>

## Examples

::: incremental

- `where file.size > 1000`

- `where file.name != "2021-04-09 Daily Note"`

- `where file.mtime >= date(today) - dur(1 day)`

- `where !complete`

:::

# `Table`

---

`Table` can show you a _table_ of various metadata fields linked to each note.

`Table {field 1}, {field 2}, ...`

## Examples

```dataview
table intensity
from #Uni/2021/Asg
```

![|Dataview table](https://i.imgur.com/OnEoP7J.png)

---

```dataview
table title, type
from #SN
```

---

```dataview
table file.tags
from Kw/Yoga
```

## `Sort`

You can use `sort` to define which order to list the results in, and which `field` to sort by:

`sort field asc/desc`

. . .

Give multiple fields to decide ties

`sort field1 asc/desc, field2 asc/desc, ...`

## `Flatten`

Use `flatten` to "unroll" lists into their own rows.

```dataview
table authors from #SN
```

Versus

```dataview
table authors from #SN
flatten authors
```

## `Group by`

`Group by` lets do gather together results based on the value of a field.

Examples:

- Group tasks by `completed`
- Group games by `rating`
- Group assignments by `intensity`

---

First, gather all the assignments:

<center>`from #Uni/2021/Asg `</center>

Then, group by `intensity`:

<center>`group by intensity`</center>

---

### `rows` Object

By grouping the notes, we've created a **new object**.

This is a **nested list** of all the assignments grouped by intensity.

. . .

Something like:

```js
[
	[A1, A2, A6], // Green
	[A3, A4], // Yellow
	[A5, A7], // Red
];
```

---

To access this new list, we use the `rows` object.

- Get the file name of every note in the array: `rows.file.name`
- Get the due date of every note: `rows.dueDate`

---

```dataview
table intensity, rows.title
from #Uni/2021/Asg
group by intensity
```

## Group by tags

```dataview
table rows.file.tags, rows.file.link
from #Fi/Yoga
group by file.tags
```

. . .

### Limitations

It will only consider two notes to be in the same group if they have **exactly the same tags**.

- So even if two notes have `#Note/Author`, if the one has a tag that the other doesn't, they won't be grouped together.

# Functions

## `Contains()`

Used to see if:

- a `string` _contains_ a substring
- a `list` _contains_ a value

. . .

`where contains(file.name, "Daily Note")`

. . .

`where contains(authors, "Robert Lamb")`

## `Length()`

Returns the _length_ of a `string` or `list`

. . .

`where length(file.name) > 10`

## `Sum()`

Returns the _sum_ of the numbers in a `list`

. . .

`where sum(minutesStudied) < 60`

## Many other Functions

[Further reading](https://blacksmithgu.github.io/obsidian-dataview/#/functions)

# Neat Examples

## [Snippet Showcase](https://forum.obsidian.md/t/dataview-plugin-snippet-showcase/13673) {data-background-iframe="https://forum.obsidian.md/t/dataview-plugin-snippet-showcase/13673"}

## Untagged Notes

<center>`list where length(file.tags) = 0`</center>

## Birthdays

```dataview
list from #People
where Dates.Birthday = "<% tp.date.now(format = "YYYY-MM-DD") %>"
```

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/An%20Introduction%20to%20Dataview%20Slides.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/An%20Introduction%20to%20Dataview%20Slides.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
