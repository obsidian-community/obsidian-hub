---
aliases: 
- 
tags:
- seedling
publish: true
---

# Markdown Syntax

## Introductory Readings
- [Introduction to Basic Markdown Syntax](https://www.markdownguide.org/basic-syntax/)
- [John Gruber's Original Documentation](https://daringfireball.net/projects/markdown/)

## Lesser known Markdown Syntax
- Indenting text with a preceding blank lines is rendered as ==code block== (which is why it changes color, which gets asked quite often).
- A dash (`-`) or equal sign (`=`) below some text turns it into a heading, due to the older (but still supported) *setext-syntax* for Markdown headings. Continuing to write some non-dash-non-equal-sign-character fixes this already.
- When using the `Strict Line Breaks` setting, a single line break can be created by placing two spaces at the end of a line (["Two Space Rule"](https://daringfireball.net/projects/markdown/syntax#p)) 
	- Since `Strict Line Breaks` makes Obsidian ignore single line breaks, they can be used for  [Semantic Line Breaks](https://sembr.org/)
- To write special characters like `*` or `$` without them triggering some markup like *italics* or Mathjax, they need to be escaped by putting a backlash in front of it: `\*` or `\$`.
- Lists that have single blank lines in between the list items are considered =="loose lists"== and which get extra spacing between each list item. To remove that spacing, simply remove the blank lines between list items. (Note that some themes already disable loose lists by default.)
- To get a line break in a Markdown table, use `<br>`.
- To get a code block in a code block, you can use four backticks. (To have a code block in a code block in a code block, you would use five, etc.)
	
`````md
````md
	```md
	fsfsfsf
	```
````
`````
