---
author: ladle
aliases:
  -
tags:
  - seedling
publish: true
---

# [[Breadcrumbs]] Quickstart Guide

Breadcrumbs is a powerful plugin for Obsidian that allows you to create more complex networks between your notes. In addition to Obsidian's (powerful) linking features, Breadcrumbs allows you to explicitly name the _type_ of relationship from one note to the next.

Obsidian lets you know that certain people spend time together; Breadcrumbs tells you their family structure.

## What This is

This is intended to be a **quick-and-dirty setup**, to get you up and running with the minimal amount of investment necessary. This **is not** the "best" or even necessarily the "most efficient" way to use Breadcrumbs; instead, this is designed to get you started with setting up your hierarchy in **15 minutes or less**, as well as a bit of an explanation on what some of the settings are.

## What You'll Need

1. Obsidian
2. Breadcrumbs
3. Optional: Template core plugin
4. Optional: A (very small) understanding of YAML

# Setting Things up

For the purposes of this text, we'll be using YAML for the metadata. Breadcrumbs natively supports Dataview, which by all accounts is a **fantastic plugin**. You can find it [here](https://github.com/blacksmithgu/obsidian-dataview). Dataview allows you to use **inline fields** rather than relying on YAML (which has its own pros and cons in Obsidian), but that is outside the scope of this article.

### Yaml?

If you've never used YAML before, fear not. YAML is a recursive acronym that stands for _"YAML Ain't Markup Language"_ and is essentially used as metadata in a text file. You can find more info on Obsidian and YAML [here](https://help.obsidian.md/Advanced+topics/YAML+front+matter), and if you _really_ want to get into the weeds you can find the paper on YAML [here](https://yaml.org/spec/1.2.2/).

The upshot is that you can put data about the note that isn't content in your note, and have it be treated in a particular way that isn't shown in the Reader View of Obsidian. That's where you'll be putting our Breadcrumbs.

## Templates!

Make a template with the following at the very top of your note:

```
---
up: ""
same: ""
down: ""
next: ""
prev: ""
---
```

The order is arbitrary, but it's important to format your YAML correctly. If you are having issues use a [YAML formatter](https://jsonformatter.org/yaml-formatter) to double check. The double quotes are also generally unnecessary, but sometimes YAML can be finicky, so it can be helpful to have them.

Name this template whatever you want. Something like "general" or "basic note" or something will be fine.

## Settings!

The settings for Breadcrumbs are wonderfully complex, but they can be quite daunting. Your workflow will probably be rewarded by spending time to poke around in the menus, but you started using Obsidian to capture _ideas_, not poke around in menus, right? So for now, let's just enable some basic things that can get you up and running without too much fuss. Feel free to stop and read more, check and uncheck, etc. to your heart's content.

### General Options

Find the **"Refresh Index on Note Save"** option and **Enable** it. This can come in handy later.

### Views

This is probably where you'll spend the most time tweaking.

#### Trail/grid/juggl

Find **"Limit Trail View to only show certain fields"** and **"Select All"**

For the **"Views to show"** options you'll see four buttons. For now, **disable all of them except the 1st one.** It'll just make things a little simpler.

The **"Index note"** option is for those who use a [Nick Milo-type](https://notes.linkingyourthinking.com/_Start+Here) of Home/Index note. If you don't use that, don't worry about it. If you do:

1. Put the file name of your home note in there, using the syntax specified.
2. **Enable** the **"Shows all paths if none to index are found"** option

## Testing it Out

That's it!

To test it out, simply make a new note; let's call it `[[a]]`. Now make another note; let's call it `[[b]]`, and insert your template (the default hotkey is `ctrl/cmd + T`). In the `up: ""` field put the name of your new note `[[a]]`.

The meta data for `[[a]]` might look like this:

```yaml
---
up: ""
same: ""
down: ""
next: ""
prev: ""
----
```

and the data for `[[b]]` might look like this:

```yaml
---
up: "[[a]]"
same: ""
down: ""
next: ""
prev: ""
----
```

Save your note (default hotkey is `ctrl/cmd + S`) and go to the Reader view. (`ctrl/cmd + E`) You should see a link at the top of your note with an `a` at the top.

You can take it a step further and create a new note `[[c]]` and follow the same procedure:

```
---
up: "[[b]]"
same: ""
down: ""
next: ""
prev: ""
----
```

Opening `[[c]]` you should see a _trail_ of arrows pointing from `a → b → c`.

## Other Things

Now that you've got the basic hang of things, here are a couple other things you might find useful pretty quickly.

### Quack 🦆

"But wait!" I hear you thinking, "Does this mean I have to go back and add all of these fields into all of my notes?" While I won't give you an answer to that (there are plenty of ways to [automatically add Breadcrumbs](https://breadcrumbs-wiki.onrender.com/docs/Alternative%20Hierarchies)) I _will_ say that there's a part of Breadcrumbs that can help with that: **The Ducks view**

The Breadcrumbs Ducks view lets you see all the notes in your vault _without_ breadcrumbs in them. It has an include/exclude keyword function, and is very handy for integrating into an already existing vault, or for maintaining a vault.

### Alternative Hierarchies

**You can specify other fields** besides the default `up, same, down, next, prev ` fields that come loaded into Breadcrumbs. They will still have the same _function_ as the fields, depending on which position they're in, but they can have different values and thus be called in different situations.

Examples include having `author` in the `up` position to delineate works by a writer. Or `related` in the `same` position, to show explicit relationships. Or `next_chapter` and `prev_chapter` in the `next` and `prev` positions to show sequential chapters of a text. The sky's the limit!

### Real and Implied Relationships

By default, Breadcrumbs will imply relationships for you. If you have `[[Language]]` as a parent note to `[[English]]` and `[[German]]` it will (understandably) assume that both `[[English]]` and `[[German]]` are children of `[[Language]]`; but more than that, it'll assume that `[[English]]` and `[[German]]` are siblings, with the `same` relationship. You can check that out in the **Breadcrumbs Matrix view.**

## Conclusion

Shoutout to [[SkepticMystic]] for all their hard work on making such a fantastic resource and for being receptive to this documentation.

Thanks for reading! I hope this helps clarify some things for you, and that you continue on your journey with Breadcrumbs!

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Breadcrumbs%20Quickstart%20Guide.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Breadcrumbs%20Quickstart%20Guide.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
