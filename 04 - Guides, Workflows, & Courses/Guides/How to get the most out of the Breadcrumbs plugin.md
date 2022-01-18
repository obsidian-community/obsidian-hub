
---
aliases: 
- 
tags:
- evergreen
publish: true
---

The [[breadcrumbs|Breadcrumbs]] is a very powerful plugin. As such, it seems to have a rather steep learning curve. However, after some initial set-up, you can already start reaping the benefits of arbitrary, non-exclusive hierarchies within your vault. 

*Note: this is a refined version of the post by [[lkadre]] on [this discussion](https://github.com/SkepticMystic/breadcrumbs/discussions/175) on Github.*

#### Setting your index

In the Trail/Grid settings, you can set a page to act as your Index. In my case, my Index is my homepage. It's the first page people see when they visit my Publish website and it's where they go back to. 

I honestly don't have that much use for the Trail except to gain an outsider's perspect: if someone opened my vault for the first time, how would they get to where I am right now? It's also a very nice way of cataloguing your note.

#### Setting your hierarchy note

I started using the plugin when the first Alternative Hierarchy feature launched: the [Hierarchy Note](https://github.com/SkepticMystic/breadcrumbs/wiki/Alternative-Hierarchies#hierarchy-notes). This appears in the settings under Hierarchy Notes. In my opinion it's not sustainable to exclusively use the hierarchy note as the list gets way too long, and you have to manually add things, but I think it's a good starting point, especially if you're still just testing the plugin.

#### Figuring out your hierarchies

Start with what you already have. Even if you subscribe to a flat-structure vault, your notes likely already have some sort of hierarchy. When you notice an existing hierarchy, consider adding it to the list of Hierarchies. If you follow what feels most intuitive to you, you're more likely to stick to it. It shouldn't be a chore and you probably don't need to restructure your entire vault to accommodate Breadcrumbs.

If you use Breadcrumbs, you likely already use the [[dataview|Dataview]] plugin. As of v. 1.9.0, you can use [Folder indexes](https://github.com/SkepticMystic/breadcrumbs/wiki/Alternative-Hierarchies#folder-indexes) and, as of v. 1.10.0, you can use [Tag indexes](https://github.com/SkepticMystic/breadcrumbs/wiki/Alternative-Hierarchies#tag-indexes). So you can build Breadcrumbs hierarchies from folders, notes or dataview fields – things you probably already have in some form in your vault.

(A disclaimer: when I discovered Breadcrumbs I did spend an entire afternoon, and maybe the evening and the next day too, playing with the plugin and manually adding hierarchical fields to each of my hundreds of notes. Don't be like me. Please value your time.)

#### Folders > Tags > YAML > Inline

If you're concerned about portability (I know I am), take this nifty and entirely made up hierarchy from most portable way to create breadcrumbs to least portable: Folders > Tags > YAML > Inline. 

Aside from my most top-level notes (the Homepage, the note for >> LAW <<, etc), I almost exclusively use tags and inline links. Tags are intuitive to me and very compact, and inline links are non-obstructive to the general content of the note as well as being explicit, unlike YAML. 

I personally find folders constraining but I think the big pushback has gone a bit too far: they absolutely have their uses, and the "folders are bad" narrative has made some people avoid folders when they would clearly benefit from them. Folders are also the most portable way to see your hierarchies and your files. Just check your system file explorer.

#### Hierarchy ideas

For some ideas on different hierarchies, these are the ones I currently use (some could do with better names, I know):

-   up / similar / down
-   broader / related / narrower
-   type / same-type / items
-   jurisdiction / others / of-jurisdiction
-   signatories / other-signatories / treaties
-   court / others / decisions
-   movement / peers / personalities
-   author / other-works / works

I also managed to make a hierarchy for Periodic notes through

-   ysemester / other-months / months
-   month / other-days / days

And for school I have

-   semester / others / classes

#### Example: Literature and author notes

As part of my template for my ""literature"" notes, there's a dataview inline field for the author, like this:

`- [i] Author:: {% if author %}[[{{author}}]]{% endif %}`

Note that the `- [i]` syntax is recognized by some themes as a custom checkbox.

(Well, this is in the Readwise export setting, but I believe many people have a similar set up in their literature notes, with ). Breadcrumbs picks up on this inline field and, since I have a hierarchy for "author", it reads that the author is above the literature, and all the other works by the same author are its "siblings". Basically, Breadcrumbs is magic.

I don't create notes for every author or person, but I do create them for people who are important in their field or who I keep coming across from, or who I just have something to say about. When I do, the template includes these:

`- [i] nationality:: tag civ/ `
`- [I] movement:: link to movements`

By creating a hierarchy for movement (an art movement, or a philosophy school of thought), I can check in on all the other people that I've taken notes on that also belong to that movement.

I haven't decided whether it's worth it yet, but something I've been considering is "civilisation" hierarchies to compare people from the same "civilisation" to see how thoughts have changed. It'd be especially interesting as often they critique one another. It's not that it's difficult to set up, only that I already have so many works-in-progress that I should probably hold off on that one.


%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/How%20to%20get%20the%20most%20out%20of%20the%20Breadcrumbs%20plugin.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/How%20to%20get%20the%20most%20out%20of%20the%20Breadcrumbs%20plugin.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
