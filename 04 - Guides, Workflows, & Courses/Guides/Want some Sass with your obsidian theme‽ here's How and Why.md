---
aliases:
- sass
- scss
tags:
- 
publish: true
---
# Want some Sass with your obsidian theme? Here's How and Why
*written by [[jdanielmourao]]*

## What is Sass and Scss?
Sass, aka **S**yntactically **A**wesome **S**tyle**S**heet, is a CSS pre-processor. It has features such as nesting, mixins, and more, which allow you to make cleaner CSS code and reduce repetitions, resulting in smaller files, and making the CSS file easier to maintain. Do keep in mind, though, that using a pre-processor is only advisable **after** you've learned the basics of CSS, and are familiar with general good practices for CSS.

What is a pre-processor exactly? Well, to put it simply, it's a program that processes an input file to produce an output that is used for other programs. In this case, it takes a `.sass`/`.scss` file, and outputs it as `.css`.

### What's the difference between the two?
Both Sass and Scss are two different syntaxes that achieve the same thing. One is an extension of the CSS syntax (SCSS), while the other, older syntax, is a simpler way of writing (Indented Syntax, commonly known as Sass). Note that the old indented syntax is often referred to as Sass because it was the first to exist, but nowadays, when referring to Sass, people mean the pre-processor (and even Scss), and not the indented syntax.

Here's a simple example:

SCSS:
```
.nav-action-button {
    color: grey;
    height: 4px;
    
    &.is-active {
        background-color: black;
        color: white;
    }
    &:hover {
        color: unset;
        background-color: blue;
    }
}
```
Indented syntax (Sass):
```
.nav-action-button
    color: grey
    height: 4px
    
    &.is-active
        background-color: black
        color: white

    &:hover
        color: unset
        background-color: blue
```

As you can see, one clearly inherits the syntax from CSS, whilst the other one is a very simplified syntax, with barely any punctuation.

### Which one should I choose?
Although that is a personal choice, this guide will be focusing on **SCSS**, for a couple of reasons:
1. It's an extension of the CSS syntax, meaning it will be more familiar for anyone coming from CSS, but most importantly, it means that every valid CSS stylesheet is automatically a valid SCSS file. This is very useful if you already have snippets or a theme in development, and don't want to rewrite it in its entirety. You can simply copy paste the code into the scss file, and it will work!
2. It is the most popular of the two (for a good reason), which makes it easier to find tutorials/documentation. Popularity shouldn't be the main reason you end up choosing one from the other, but it sure makes it easier to follow along tutorials, etc.

 ## Why would you want to use it for theming?

Having read the beginning of this guide, you can probably guess why Scss can be useful for theming. It allows you to separate your code into modules, which can be edited separately, and compiled into one file. This improves organization (no more need for relying on that search function!), and makes finding code faster. It also allows you to do things such as indentation, which greatly reduce repetition, making pieces of individual code easier to spot, and makes it so you don't have to type as much code. More on that later!

## Getting started
Browsers (and electron/obsidian), do not understand sass code. Thus, you'll need to convert a sass/scss file into a normal css file. For the curious amongst you, that process is called *transpiling*.

For that, you'll need a **Sass pre-compiler**. 

There are a few ways you can install the Sass pre-compiler, which you can check out [here](https://sass-lang.com/install). This guide will go through how to install it using npm. For that, naturally, you'll first need to have `npm` installed on your system. To check if you have `npm` installed, you can run the following command in the terminal:
```
npm -v
```
If you have it installed, it should return a version number. If that's not the case, you'll need to [install Node](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

### Installation
Now, having installed npm, you can simply input the following command in the terminal:
```
npm install -g sass
```
Now in order to check if sass is installed, run the following command:
```
sass --version
```
It should return a version number, which confirms you now have Sass installed!

### Setup
Now that you can use the Sass pre-compiler, you can go ahead and create a `.scss` file, say, `input.scss`.
In order to convert `input.scss` into a css file using the terminal/command-line, you'll either have to first be inside the file's directory, or specify the file path.
(skip this part if you just want to know how to do it automatically)

---
For the former, you'll need to use the `cd` (change directory) command. For Example:
```
cd c:\directorypath
```
If you are on Windows, and saved the file inside another disk other than `c:`, simply type:
```
d:

cd d:\directorypath
```
You can then run the following command in the terminal:
```
sass input.scss output.css
```
This will compile the `input.scss` file and output a `output.css` file in the same location. It can also output a `output.css.map` file, which you can ignore.

Alternatively, you can just run a single command:
```
sass input-file-path.scss output-file-path.css
```
This enables you to compile a file and output a css file wherever you want in your system.

---
Now, what happens if you want to keep editing a `scss` file, would you need to keep running that command? 

If you want to automatically update the output file, whenever you edit and save the `.scss` file, there's an easier, cleaner way of doing this.
First, for the sake of organization, create 2 folders: one called "scss", and another called "css", for example. This isn't totally necessary, as you can keep them in the same place, but is recommended to make it easier to find the scss file and its modules (which will be covered down below).
You'll be placing your `.scss` files in the "scss" folder, and the `.css` file in the "css" folder. Simple enough.
Now, in order to automatically update, you can run the following command (note that you either need to already be inside the directory that contains both folders, or specify the paths in quotation marks):
```
sass --watch scss:css
```
or
```
sass --watch "input-scss-folder-path":"output-css-folder-path"
```
That should tell Sass to keep looking at those folders for updates, and when an edit is detected, it will automatically start compiling! 
This will be the command you'll need to remember and always run in the terminal whenever you want to start working on the `scss` file. Keep in mind that any changes you make to the compiled `css` file will be overwritten when you compile again. To avoid this, **always edit on the `scss` file**.

Note: If there happens to be an error, it will be detected by the pre-compiler, and shown in the terminal, along with its location, to facilitate correction.

If you want to learn more about the command-line interface of Sass, click [here](https://sass-lang.com/documentation/cli/dart-sass).

### Some useful features
So now that you're all setup, there are a few useful features you might want to take a look at first. Those being:
- **Nesting** - rather than repeating the same selectors, you can simply write one inside the other. Here's a simple example that just skims the surface:

SCSS:
```
.markdown-preview-view {
	strong {
		font-weight: bold;
	}
	em {
		font-style: italic;
	}
}
```

Compiled CSS:
```
.markdown-preview-view strong {
	font-weight: bold;
}
.markdown-preview-view em {
	font-style: italic;
}
```
---
- **Variables** - not to be confused with [custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties), since they both have their uses, and can even be combined. One of the differences of sass variables is that they don't show up in the final css file, as they get replaced by their values. More info on that [here](https://sass-lang.com/documentation/variables). Example:

SCSS
```
$color-primary: black;
$border-primary: rgba($color-primary, 0.7);

button {
	border: 1px solid $border-primary;
}
```

CSS
```
button {
	border: 1px solid rgba(black, 0.7);
}
```
---
- **Modules** - You can organise your code into smaller files, by creating modules, and load them in a single scss file to compile. This means you can have your variables, snippets of code, etc, in different files and simply have a file dedicated to assembling the final input.css file. Always name those files with an underscore at the beginning, so Sass can identify them as modules. Here's an example from [sass's website](https://sass-lang.com/):

SCSS
```
//_base.scss
$font-stack: Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
```
```
// styles.scss
@use 'base';

.inverse {
  background-color: base.$primary-color;
  color: white;
}

```

CSS
```
body {
  font: 100% Helvetica, sans-serif;
  color: #333;
}

.inverse {
  background-color: #333;
  color: white;
}
```

Note that variables that are contained in a module that's imported need to have that module's name before the variable's name, as shown above.

TIP: You can keep your variables in a `_var.scss` file, and then whenever you use a variable from that module, write `@use 'var';` at the beginning of the file, and `var.$variable-name` as the variable name. This makes it somewhat similar to CSS custom properties syntax, so it's easier to remember.

These are just a few SCSS features you can use in order to make writing CSS easier for you. You can read up on the [SASS Documentation](https://sass-lang.com/documentation) to get a better grasp of its rules and capabilities.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Want%20some%20Sass%20with%20your%20obsidian%20theme%E2%80%BD%20here%27s%20How%20and%20Why.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Want%20some%20Sass%20with%20your%20obsidian%20theme%E2%80%BD%20here%27s%20How%20and%20Why.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
