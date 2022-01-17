# How to Style Obsidian
By [[ryanjamurphy|Ryan J. A. Murphy]]

---

Ancient proverb:
> Give a person some CSS, style them for a day. Teach them CSS, and they'll procrastinate for a lifetime.

So you've downloaded that sleek new theme everyone's talking about. Your notes have never looked better. You sit at your desk, coffee steaming, hands hovering over your keyboard, and the most important thought you'll ever have is—wait, no, that header is the wrong shade of [Pantone's 2015 colour of the year, marsala!](https://www.diamondvogel.com/architectural/blog/2015-pantone-color-of-the-year)

EVERYTHING IS RUINED.

Don't despair. We've updated the help docs so that you can become your own CSS stylist. Read the below, style Obsidian to your [heart's delight/content/desire](https://www.thetelegram.com/news/local/in-hearts-delight-hearts-desire-hearts-content-and-cupids-love-is-in-the-air-every-day-284274/), and then add "Front-end developer" to your resumé!

## The tutorial

~~Hypertext Markup Language (HTML) was created in 1989 by Tim Berners-Lee as ...~~

We kid. There's a lot to learn about how apps like Obsidian are constructed and represented on your computer, but there's better resources than this one on learning those things. We're going to try to focus only on what you need to know to style parts of the app. At the end, we point to some of those resources should you wish to learn more.

## About CSS

Obsidian uses Cascading Style Sheets (CSS) to describe what all of the parts of your vault should look like. This means that virtually every aspect of Obsidian can be customized to suit your tastes and preferences—but if you haven't used CSS before, it may be intimidating.

Here are the basics to help you fine-tune Obsidian.

CSS is a kind of programming language. When editing Obsidian's CSS, there's only two things you really need to think about:

1.  How do I target the right parts of Obsidian? (e.g., sidebar buttons, quotes in the edit view, links in hover-preview); and
2.  How do I tell Obsidian what it should look like?

Choosing what to style in CSS means using **selectors**. A selector is a way of identifying which part of the app you want to style. For specificity, selectors are usually nested: for example, if you want to target the typeface of quotes in the editor view, you need to select exactly that—if you select quotes in general, you'll change how blockquotes look _everywhere in the app._

Styling what you've selected means using **properties**. There are many properties to use in CSS. Telling the app how you want a given thing to look simply means identifying which properties you want to edit and giving those properties the values you want.

You give these instructions with a **declaration**. A declaration includes a selector (what to style), the properties you want to style (what parts of the thing you want to change), and the properties' new values (how you want them to look). E.g., if you want to declare that all text in the editor become blue, you are essentially saying "Obsidian, look for all text in the Editor view, and tell it to become blue."

In real CSS, that declaration looks like:

```css
.markdown-source-view {
	color: blue;	
}
```

`.markdown-source-view` is the selector. The properties we want to style are contained within a `{}` set of brackets. `color:` is the property we want to style. `blue` is the value we want to give this property. All property–value relationships are indicated with a property, then a colon `:`, then the value, and then a semicolon to indicate the end of a line. Properties are typically indented one indent from the selector to make it easy to differentiate them.

CSS is interpreted sequentially. The last declaration rules over any that came before it. So, if you were to make the following declarations:

```css
.markdown-source-view {
	color: blue;
}

.markdown-source-view {
	color: black;
}
```

The text colour would be black, not blue. I.e., the app would layer what comes last in the document over whatever came before it.

However, if you want to insist, you can write `!important`, like so:
```css
.markdown-source-view {
	color: blue !important;
}

.markdown-source-view {
	color: black;
}
```

And the `!important` statement overrules others—the result would be blue, not black.

Most often, you'll select the things you want to style via their **classes**. Classes are an attribute added to the underlying structure of the app so that they may be targeted with selectors. `.markdown-source-view` is a class identifying any content in the app open to the Editor view. Classes are denoted with a preceding `.`.

Depending on what you style, you may also want to target **elements**. Elements are the structural parts of the app. For instance, every paragraph can be identified with a `p` element selector. Elements are described without preceding punctuation.

To increase specificity, you can use logic in your selectors.

A space `  ` increases specificity by selecting descendants: `grandparent parent child` will select only the child of a parent who is a child of grandparent. Example: `.markdown-source-view blockquote` will select only blockquotes that exist somewhere inside edit mode panes.

A period `.` between classes indicates an "and" relationship. `.programmer.designer` selects only elements that have both `programmer` and `designer` as a class. Example: `.nav-file.is-active` allows you to style only the active (e.g., currently focused-on) file in the File Explorer list of files.

A comma `,` simply allows you to use the same declaration for comma-separated groups. Example: `blockquote, pre` will target both `blockquote` elements and `pre` elements.

For more on selectors, see https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors

## Where do I put my stylin' declarations?

If you're making a comprehensive theme, you can put it under `VAULT/.obsidian/themes`. Give it a cool name like `Best theme ever.css` and it will show up under Settings → Appearance → Theme in Obsidian. You might need to hit the `Reload themes` button if it's not being detected.

If you're making small tweaks to an existing theme, put them under `VAULT/.obsidian/snippets` instead.

## Finding components in Obsidian

You can identify what you want to style using Obsidian's developer tools. This is activated via `Ctrl+Shift+I` on Windows/Linux or `Cmd+Opt+I` on macOS. Pressing these commands opens a bunch of technical information in a new sidebar. The Elements tab of the developer tools sidebar is all you really need to worry about. It describes the underlying structure of Obsidian (and your notes!)

Notice that if you hover over the elements, the window highlights what you're looking at. For some elements, it may show nothing—these are parts of the application (currently) hidden from view. For others it may highlight the whole window or major parts of the window—all of these parts are stylable with CSS!

Notice, too, that some of the elements can be unfolded. By default, the whole structure is collapsed to be more compact. Unfold those parts to explore more detailed parts of the structure.

This unfolding is important. The structure is composed of parent-child-sibling relationships. Consider the following:

```html
<div class="markdown-source-view">
	<div class="CodeMirror cm-s-obsidian CodeMirror-wrap CodeMirror-focused">
		<pre class=" CodeMirror-line " role="presentation">
			<span role="presentation" style="">Notice, too, that some of the elements can be unfolded. By default, the whole structure is collapsed to be more compact. Unfold those parts to explore more detailed parts of the structure.
			</span>
		</pre>
		<pre class=" CodeMirror-line " role="presentation">
			<span role="presentation" style="">This unfolding is important. The structure is composed of parent-child-sibling relationships. Consider the following:</span>
		</pre>
	</div>
</div>---
publish: false
---

<iframe width="100%" height="400px" src="https://www.youtube.com/embed/gYK3VDQsZJo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

Look at the indentations. The two `pre` elements are _siblings_ of one another: they sit at the same level in the hierarchy. They are _children_ of the `div` with classes `CodeMirror cm-s-obsidian CodeMirror-wrap CodeMirror-focused`; that div is their _parent_.

Do you need to worry about anything else about this code right now? Thank the gods, no. Just keep that parent-child-sibling structure in mind for the next section.

## Identifying parts of Obsidian for styling

There are two ways of exploring Obsidian's underlying structure in the developer tools sidebar in order to identify the parts you want to change.

The hard way is to unfold elements, hovering over them as you go, in order to "zoom in" on the details you want. This is sometimes handy as it helps you understand the overall architecture of the app, and it may give you more ideas about what you want to style.

The easy way is to use the developer tools's "Select an element on the page to inspect it" tool. It looks like this, and is usually found in the upper-left corner of the developer tools sidebar:

![[Select to inspect element.png]]

Click that button, then move your pointer over the app. Now, pieces of the app become highlighted as you hover over them, and the corresponding part of the structure also unfolds and becomes highlighted in the developer tools pane.

From this inspection mode, click the thing you want to style. Make sure the whole object you want to style is highlighted before you click, and nothing else. Remember: selectors are very specific!

Now, look at the part of the structure unfolded and selected in the developer tools pane. Some investigation is necessary now: use your pointer to hover over it, then the parts around it. Recall the parent-child-sibling relationship. This gives you a sense of which parts of the structure correspond to which parts of the app.

Look at the parts that are most senior while still capturing everything you want to style and nothing else. This part's classes (and sometimes its element) are what you will want to use to choose a selector.

In the example above, I may want to edit only the colour of the text on my currently focused pane.

Should I choose `.CodeMirror-line` as my class? No! That will style _all_ elements with `.CodeMirror-line` as a class.

What about `.markdown-source-view`? No! That will style all Editor panes.

With a bit more exploration and some intuition, we can see that there's a component just junior to `.markdown-source-view` with the class `CodeMirror-focused`. Interesting, eh? Do other panes have this class? Open some and see.

The answer is no. Only the currently-active pane contains a component with class `CodeMirror-focused`. Therefore, our selector for our declaration is `CodeMirror-focused`

... isn't it?

No! In a declaration, classes are indicated with a leading `.`, remember? So, the declaration will look like:

```css
.CodeMirror-focused {}
```

## Choosing and setting properties and values

Now that we know how to select what we want to target, how do we know what to style?

This can be tricky. There are many CSS properties, and most of them can apply to almost anything on your page.

To start, think of what you want to change. Typeface? Font size? Background colour?

Scan through this list: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference

Do you see anything that might be relevant? Click through to it to read the details of how to choose values for that property. Then, try it out.

## A few final notes

### The necessity of experimentation

Ultimately, like most graphic design work, editing CSS is a matter of trial and error. Experiment, iterate, and you'll get better. The next time you go to make a change it'll be easier to know how to do it, and you'll be able to do more things.

### Edit and Preview panes

`obsidian-source-view` is an editor pane. `obsidian-preview-view` is a preview pane. If you include either in a selector, your changes will not apply to the other.

### Colours and variables

Colours are typically described as an RGB hexadecimal value. Don't worry, you don't need to care about what that means. Just know that colours are often described like `#123456`. To precisely indicate a colour, you'll want to use a colour tool to identify that code for use in your declarations.

However! Many themes in Obsidian use _variables_. For choosing colours, this means you can have a palette of colours used in many places in your theme without needing to change the colour in every single place every time you decide you want a new hue of blue. Read about colour variables here: https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties

### Learning by taking themes apart

One of the best ways to learn is to open the `obsidian.css` file of your favourite theme and explore it. Try changing some values and watching what happens in Obsidian.

### Lookin' good, Frankenstein's Monster

Do you see something in another theme that looks slick, but complicated? The flexibility of CSS means that you can probably copy and paste the code used to make that change into your theme and it will work. Again, though, see "The necessity of experimentation" above! Trial and error may be necessary to help you make it fit within your theme.

### Going further

Want to learn more about CSS in general? The Mozilla Developer Network docs are one of the best resources: https://developer.mozilla.org/en-US/docs/Web

CSS Tricks is a fantastic resource for finding neat ways of working with CSS (and HTML and JavaScript) to achieve fantastic results: https://css-tricks.com

---
Topics: [[Obsidian community themes]] [[Obsidian CSS]]

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/How%20to%20Style%20Obsidian.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/How%20to%20Style%20Obsidian.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
