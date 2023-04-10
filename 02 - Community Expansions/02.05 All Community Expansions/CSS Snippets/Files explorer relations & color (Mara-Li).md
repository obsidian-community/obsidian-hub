---
aliases: 
- Folder Color
- Coloured Folder
- Relations line explorer
tags:
- Folder
- Nested Folder
- Explorer
publish: true
---

# File explorer relations : Lines & Color

*You can find more snippets in [My github repository : Obsidian Snippet Collection](https://github.com/Mara-Li/Obsidian-Snippet-collection)*

Folder relation allows to :
- Add color for each folder, numbered from 00 to 100
- Add lines for children files of a folder

You can adjust color and line with [[obsidian-style-settings|Style Settings]]. 

- [Folder Relations [Relation line & background color]](https://raw.githubusercontent.com/Mara-Li/Obsidian-Snippet-collection/main/folder-color_bg.css)
- [Folder Color [Font color]](https://github.com/Mara-Li/Obsidian-Snippet-collection/blob/HEAD/folder-color_font.css)

![[Mara_FolderColor.png]]![[Mara_FolderColor2.png]]

*Note : The files and folder icons is from [[obsidian-icon-folder|Icon Folder]]*

<u>Credit</u>: 
- [Lithou](https://forum.obsidian.md/t/adding-color-to-obsidian-a-rainbow-of-possibility/12805/11)
- [Javalent](https://github.com/valentine195/Obsidian-Vault/blob/HEAD/.obsidian/snippets/colors.folders.css)

```css
/* 
=========================================================================================================   
                                          COLOURED NESTED FOLDER 
        credit : Lithou ; Jeremy Valentine ; Mara-Li
        You need to change the data-path to corresponding to your folder.
        This will allow the colouring of the top level folders into sections that "drop down" when opened. 
        The Color can be changed using Style Settings.
========================================================================================================= */

/* @settings
name: Nested Folder — Background Color
id: nested
settings:
    -
        id: adjust-line 
        format: heading
        collapsed: true
        title: Adjust Line
        level: 2
    -
        id: adjust-pc
        format: em
        title: Line PC
        description: Adjust line with icon (in em) (ON PC)
        default: 1.2
        type: variable-number
    -
        id: adjust-mobile
        format: em
        title: Line MOBILE
        description: Adjust line with icon (in em) (ON MOBILE)
        default: 0.8
        type: variable-number
    -
        id: color
        collapsed: false
        title: Color choose
        type: heading
        level: 2
    -
        id: bg00
        format: hex
        opacity: true
        type: variable-themed-color
        title: 00. Folder
        default-light: "#3131312c"
        default-dark: "#6e6e6e2c"
    -
        id: bg10
        format: hex
        opacity: true
        type: variable-themed-color
        title: 10. Folder
        default-light: "#6867ad2c"
        default-dark: "#bb77622c"
    - 
        id: bg20
        format: hex
        opacity: true
        type: variable-themed-color
        title: 20. Folder
        default-light: "#85adad2c"
        default-dark: "#77664e2c"
    -
        id: bg30
        format: hex
        opacity: true
        type: variable-themed-color
        title: 30. Folder
        default-light: "#50A6862c"
        default-dark: "#798c642c"
    - 
        id: bg40
        format: hex
        opacity: true
        type: variable-themed-color
        title: 40. Folder
        default-light: "#4765AB2C"
        default-dark: "#4765AB2c"
    -
        id: bg50
        format: hex
        opacity: true
        type: variable-themed-color
        title: 50. Folder
        default-light: "#8FA1CC2c"
        default-dark: "#8FA1CC2c"    
	-
        id: bg60
        format: hex
        opacity: true
        type: variable-themed-color
        title: 60. Folder
        default-light: "#8FA1CC2c"
        default-dark: "#8FA1CC2c"    
	-
        id: bg70
        format: hex
        opacity: true
        type: variable-themed-color
        title: 70. Folder
        default-light: "#ffffff00"
        default-dark: "#ffffff00"
    -
        id: bg80
        format: hex
        opacity: true
        type: variable-themed-color
        title: 80. Folder
        default-light: "#ad8c332c"
        default-dark: "#ad8c332c"
	-
        id: bg90
        format: hex
        opacity: true
        type: variable-themed-color
        title: 90. Folder
        default-light: "#ffffff00"
        default-dark: "#ffffff00"
    -
        id: bg100
        format: hex
        opacity: true
        type: variable-themed-color
        title: 100. Folder
        default-light: "#ffffff00"
        default-dark: "#ffffff00"
    -
        id: bgZZ
        format: hex
        opacity: true
        type: variable-themed-color
        title: ZZ. Folder
        default-light: "#B69D912c"
        default-dark: "#617e8c2c"
*/

:root {
  /* folder colours */
  /* line styles for nesting indicators */
  --nestlinesize1: solid;
  --nestlinestyle1: 2px;
  --nestlinesize2: groove;
  --nestlinestyle2: 2px;
  --nestlinecolor2: rgb(255, 255, 255);
  --nestlinesize3: dashed;
  --nestlinestyle3: 2px;
  --FolderRadius: 5px;
  --FoldText: white;
  --FoldTextMaster: var(--FoldText);
  --inbox-font: 0, 18, 25;
  --adjust-pc: 1.2em;
  --adjust-mobile: 0.8em;
}

.theme-dark {
  --root-file-color: white;
  --FoldText: rgba(255, 255, 255, 0.267);
  --nestlinecolor1: rgba(255, 255, 255, 0.267);
  --nestlinecolor3: rgba(255, 255, 255, 0.267);
  --nestlinecolor3: rgba(255, 255, 255, 0.267);
  --bg00: #6e6e6e2c;
  --bg10: #bb77622c;
  --bg20: #77664e2c;
  --bg30: #798c642c;
  --bg40: #4765ab2c;
  --bg50: #8fa1cc2c;
  --bg60: #ffffff00;
  --bg70: #ffffff00;
  --bg80: #ad8c332c;
  --bg90: #ffffff00;
  --bg100: #ffffff00;
  --bgZZ: #617e8c2c;
  --normal-folder: white;
}

.theme-light {
  --root-file-color: var(--text-normal);
  --FoldText: rgba(0, 0, 0, 0.171);
  --nestlinecolor1: rgba(0, 0, 0, 0.144);
  --nestlinecolor3: rgba(0, 0, 0, 0.144);
  --bg00: #3131312c;
  --bg10: #bb77622c;
  --bg20: #85adad2c;
  --bg30: #50a6862c;
  --bg40: #4765ab2c;
  --bg50: #8fa1cc2c;
  --bg60: #ffffff00;
  --bg70: #ffffff00;
  --bg80: #ad8c332c;
  --bg90: #ffffff00;
  --bg100: #b69d912c;
  --bgZZ: #b69d912c;
  --normal-folder: black;
}

.nav-file-title,
.nav-folder-title {
  color: var(--normal-folder);
}

/* Sanctum adjust */

.nav-folder-title-content,
.nav-file-title-content {
  color: revert !important;
}

/* SR Plugins adjust */

div:not(.is-mobile)
  > .workspace-leaf-content
  > .view-content
  .nav-folder-title {
  color: var(--text-accent) !important;
}

div:not(.is-mobile)
  > .workspace-leaf-content
  > .view-content
  > .nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title {
  color: var(--text-normal) !important;
}

div:not(.is-mobile)
  > .workspace-leaf-content
  > .view-content
  .nav-file-title-content {
  color: var(--text-normal) !important;
}

div:not(.is-mobile)
  > .workspace-leaf-content
  .view-content
  .nav-file-title-content:hover,
div:not(.is-mobile)
  > .workspace-leaf-content
  > .view-content
  > .nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title:hover {
  color: var(--text-accent) !important;
}

div:not(.is-mobile)
  > .workspace-leaf-content
  .view-content
  .nav-folder-children
  .nav-file-title-content:first-child::before {
  top: -1px !important;
}

/* Minimal Theme overrides */

.nav-file {
  margin-left: 0;
  padding: 0;
}

.nav-file-title {
  margin: 0;
  padding-left: 0;
}

/* Set up explorer container margins */

.nav-files-container {
  margin: 0px 5px;
}

.nav-file-title,
.nav-folder-title {
  border-radius: 0px;
}

.nav-folder-title {
  margin: 0;
  width: 100% !important;
}

/* Uncomment this for adjusting line with icon */

.nav-folder:not(.mod-root) > .nav-folder-children .nav-file-title {
  margin-left: -5px;
}

/* Top Level Folder Titles */

.nav-folder.mod-root > .nav-folder-children > .nav-folder > .nav-folder-title {
  font-family: var(--default-font);
  font-size: calc(var(--augmente) + 3px) !important;
  color: var(--FoldText);
  padding-left: 5px;
  margin-top: 7px;
  /* space between top level sections */
  border-radius: var(--FolderRadius) var(--FolderRadius) 0px 0px;
}

/* Rounded borders */

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder.is-collapsed
  > .nav-folder-title {
  border-radius: var(--FolderRadius);
}

/* General Nav Folder Children (this is the part that expands from each top level folder) */

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-children {
  padding-left: 0px;
  border-top: var(--FoldText) 1px solid;
  border-radius: 0px 0px var(--FolderRadius) var(--FolderRadius);
  color: var(--FoldText);
  /* padding-bottom: 12px; */
}

/* active file increase font size and removes normal highlight marker */

.nav-file-title.is-active {
  font-size: 105%;
}

/* Adds hemisphere marker to active file instead */

/* .nav-file-title.is-active {
    
} */

/* 16 Top level Folders By Starting Digit (0-F)
These are set for me by leading number/letter which also ensures they are in the correct order when sorted alphabetically
You can change these to match your use case. */

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="00."],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="00."]
  + .nav-folder-children {
  background-color: var(--bg00);
}

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="10."],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="10."]
  + .nav-folder-children {
  background-color: var(--bg10);
}

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="20."],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="20."]
  + .nav-folder-children {
  background-color: var(--bg20);
}

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="30."],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="30."]
  + .nav-folder-children {
  background-color: var(--bg30);
}

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="40."],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="40."]
  + .nav-folder-children {
  background-color: var(--bg40);
}

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="50."],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="50."]
  + .nav-folder-children {
  background-color: var(--bg50);
}

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="60."],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="60."]
  + .nav-folder-children {
  background-color: var(--bg60);
}

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="80."],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="80."]
  + .nav-folder-children {
  background-color: var(--bg80);
}

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="90."],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="90."]
  + .nav-folder-children {
  background-color: var(--bg90);
}

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="70."],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="70."]
  + .nav-folder-children {
  background-color: var(--bg70);
}

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="100."],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="100."]
  + .nav-folder-children {
  background-color: var(--bg100);
}

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="ZZ."],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="ZZ."]
  + .nav-folder-children {
  background-color: var(--bgZZ);
}

.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="Ressource"],
.nav-folder.mod-root
  > .nav-folder-children
  > .nav-folder
  > .nav-folder-title[data-path^="Ressource"]
  + .nav-folder-children {
  background-color: var(--bgZZ);
}

/* Scrollbars eliminated */

::-webkit-scrollbar {
  width: 0px;
  height: 0px;
}

/* Relationship lines for 2nd, 3rd, and 4th level folders */

@media only screen and (max-device-width: 1024px) {
  .is-mobile .nav-folder.mod-root {
    overflow: hidden !important;
  }
  .nav-folder.mod-root
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-file {
    border-left: var(--nestlinestyle1) var(--nestlinesize1)
      var(--nestlinecolor1);
    margin-left: var(--adjust-mobile);
  }
  .nav-folder.mod-root
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder {
    border-left: var(--nestlinestyle1) var(--nestlinesize1)
      var(--nestlinecolor1);
    margin-left: var(--adjust-mobile);
  }
  .nav-folder.mod-root
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-file {
    border-left: var(--nestlinestyle2) var(--nestlinesize2)
      var(--nestlinecolor2);
    margin-left: var(--adjust-mobile);
  }
  .nav-folder.mod-root
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder {
    border-left: var(--nestlinestyle2) var(--nestlinesize2)
      var(--nestlinecolor2);
    margin-left: var(--adjust-mobile);
  }
  .nav-folder.mod-root
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-file {
    border-left: var(--nestlinestyle3) var(--nestlinesize3)
      var(--nestlinecolor3);
    margin-left: var(--adjust-mobile);
  }
  .nav-folder.mod-root
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder {
    border-left: var(--nestlinestyle3) var(--nestlinesize3)
      var(--nestlinecolor3);
    margin-left: var(--adjust-mobile);
  }
}

@media only screen and (min-device-width: 1024px) {
  .nav-folder.mod-root
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-file {
    border-left: var(--nestlinestyle1) var(--nestlinesize1)
      var(--nestlinecolor1);
    margin-left: var(--adjust-pc);
  }
  .nav-folder.mod-root
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder {
    border-left: var(--nestlinestyle1) var(--nestlinesize1)
      var(--nestlinecolor1);
    margin-left: var(--adjust-pc);
  }
  .nav-folder.mod-root
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-file {
    border-left: var(--nestlinestyle2) var(--nestlinesize2)
      var(--nestlinecolor2);
    margin-left: var(--adjust-pc);
  }
  .nav-folder.mod-root
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder {
    border-left: var(--nestlinestyle2) var(--nestlinesize2)
      var(--nestlinecolor2);
    margin-left: var(--adjust-pc);
  }
  .nav-folder.mod-root
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-file {
    border-left: var(--nestlinestyle3) var(--nestlinesize3)
      var(--nestlinecolor3);
    margin-left: calc(var(--adjust-pc));
  }
  .nav-folder.mod-root
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder
    > .nav-folder-children
    > .nav-folder {
    border-left: var(--nestlinestyle3) var(--nestlinesize3)
      var(--nestlinecolor3);
    margin-left: calc(var(--adjust-pc));
  }
}

/* == File Explorer - animation for active file as per Obuntu === */

.nav-folder.mod-root > .nav-folder-title {
  padding-left: 6px;
  font-size: 14px;
  font-weight: normal !important;
  top: -6px;
  cursor: default;
}

.nav-file.is-active > .nav-file-title,
.nav-file.is-active > .nav-file-title:hover {
  border-radius: 6px;
  font-weight: normal !important;
  border-left: 2px solid var(--text-accent);
  transition: all 0.5s ease;
}

.nav-file.is-active > .nav-file-title {
  padding-left: 5px;
}

.nav-file-title.is-active,
body:not(.is-grabbing) .nav-file-title:hover,
body:not(.is-grabbing) .nav-folder-title:hover {
  /* border-radius: 2px; */
  transition: all 0.2s ease;
}

body:not(.is-grabbing) .nav-folder-title:hover {
  border-radius: 0px;
}

.nav-file-title.is-active::before {
  margin-top: 2px;
  width: 22px;
  height: 20px;
}

.nav-file-tag {
  top: -1px;
}

.nav-folder-children {
  padding-left: 1.9em;
}
```

```css
/* 
==============================================================================  
                    FOLDER FONT COLOR 
    credit : Mara-Li
    You need to change the data-path to corresponding to your folder.
============================================================================== */

/* @settings
name: "Nested Folder — Font Color"
id: icons color
settings:
    -
        id: settings-font
        level: 1
        collapsed: true
        type: heading
        title: General settings
        description: font and files settings
    -
		id: files
		title: Files icon
		type: class-toggle
    -
        id: size
        type: variable-number
        format: px
        default: 18
        title: Icon Size
    -
        id: augmente
        title: Augmente font size nav
        default: 14
        max: 30
        min: 14
        format: px
        step: 1
        type: variable-number-slider
    -
        id: color-h
        title: Color
        type: heading
        level: 1
        collapsed: false
    -
        id: F00
        title: 00. Folder
        type: variable-themed-color
        default-light: "#001219"
        default-dark: "#8d8d8d"
        format: hex
		opacity: false
    -
        id: F10
        title: 10. Folder
        type: variable-themed-color
		opacity: false
        default-light: "#4765AB"
        default-dark: "#bb7762"
        format: hex
    -
        id: F20
        title: 20. Folder
        type: variable-themed-color
		opacity: false
        default-light: "#3E9C9D"
        default-dark: "#b7822f"
        format: hex
    -
        id: F30
        title: 30. Folder
        type: variable-themed-color
        default-light: "#50A686"
        default-dark: "#798c64"
        format: hex
		opacity: false
    -
        id: F40
        title: 40. Folder
        type: variable-themed-color
        format: hex
        default-light: "#4765AB"
        default-dark: "#4765AB"
		opacity: false
    -
        id: F50
        title: 50. Folder
        type: variable-themed-color
        format: hex
        default-dark: "#8FA1CC"
        default-light: "#8FA1CC"
        opacity: false
    -
        id: F60
        title: 60. Folder
        type: variable-themed-color
        format: hex
        default-dark: "#8FA1CC"
        default-light: "#8FA1CC"
        opacity: false
    -
        id: F70
        title: 70. Folder
        type: variable-themed-color
        format: hex
        default-dark: "#ffffff00"
        default-light: "#ffffff00"
        opacity: false
	-
        id: F80
        title: 80. Folder
        type: variable-themed-color
        format: hex
        default-light: "#ad8c33"
        default-dark: "#ad8c33"
        opacity: false
	-
        id: F90
        title: 90. Folder
        type: variable-themed-color
        format: hex
        default-light: "#ad8c33"
        default-dark: "#ad8c33"
        opacity: false
	-
        id: F100
        title: 100. Folder
        type: variable-themed-color
        format: hex
        default-light: "#ffffff00"
        default-dark: "#ffffff00"
        opacity: false
	-
        id: FZZ
        title: ZZ. Folder
        type: variable-themed-color
        format: hex
        default-light: "#B69D91"
        default-dark : "#617e8c"
		opacity: false
*/

.theme-dark {
  --F00: #8d8d8d;
  --F10: #bb7762;
  --F20: #b7822f;
  --F30: #798c64;
  --F40: #4765ab;
  --F50: #8fa1cc;
  --F60: #8fa1cc;
  --F70: #ffffff00;
  --F80: #ad8c33;
  --F90: #ad8c33;
  --F100: #ffffff00;
  --FZZ: #617e8c;
}

.theme-light {
  --F00: #00121a;
  --F10: #bb7762;
  --F20: #3e9c9d;
  --F30: #50a686;
  --F50: #4765ab;
  --F40: #8fa1cc;
  --F60: #8fa1cc;
  --F70: #ffffff00;
  --F80: #ad8c33;
  --F90: #ad8c33;
  --F100: #ffffff00;
  --FZZ: #b69d91;
}

:root {
  --size: 18px;
  --augmente: 14px;
}

/* 
======================================================================================  
                                      COLOR
====================================================================================== 
*/

/* ======================== FILES =================== */


.nav-file-title,
.nav-folder-title {
  font-size: var(--augmente) !important;
}

.nav-file-title.is-being-dragged,
.nav-folder-title.is-being-dragged {
  background-color: #8e939349 !important;
}

body:not(.is-grabbing) .nav-file-title:hover .nav-folder-collapse-indicator,
body:not(.is-grabbing) .nav-folder-title:hover .nav-folder-collapse-indicator {
  background-color: transparent !important;
}

.nav-folder-title[data-path^="/"] {
  display: none;
}

.fx-icons .nav-folder:not(.nav-folder.mod-root) {
  margin-left: 0;
}

.nav-file-title-content:hover,
.nav-folder-title-content:hover,
.collapse-icon:hover {
  background-color: transparent !important;
  filter: saturate(150%);
  color: currentColor !important;
}

.nav-folder-title.is-being-dragged-over {
  background-color: transparent !important;
  color: currentColor !important;
  filter: saturate(500%) !important;
}

.CodeMirror-foldgutter-folded,
.is-collapsed .nav-folder-collapse-indicator,
.nav-folder-collapse-indicator {
  color: currentColor !important;
}

.nav-file-tag {
  display: none;
}

.nav-file-title.is-active:not(.nav-file-title.is-active:hover) {
  background-color: rgba(255, 255, 255, 0.075) !important;
  filter: saturate(150%);
}

.nav-folder-children .nav-file-title-content:first-child::before {
  font-size: 18px !important;
}

.nav-folder-children .nav-file-title-content:first-child::before {
  font-size: var(--size) !important;
  padding-left: 3px !important;
}

/* ======================== FOLDER 00 =================== */

.nav-folder-title[data-path^="00."],
.nav-file-title[data-path*="00."] {
  color: var(--F00) !important;
}

/* ======================== FOLDER 10 =================== */


.nav-folder-title[data-path^="10."],
.nav-file-title[data-path*="10."] {
  color: var(--F10) !important;
}

/* ======================== FOLDER 20 - 23 =================== */


.nav-folder-title[data-path^="20."],
.nav-file-title[data-path^="20."],
.nav-file-title[data-path^="20."][data-path*="21."],
.nav-file-title[data-path^="20."][data-path*="22."],
.nav-file-title[data-path^="20."][data-path*="23."] {
  color: var(--F20) !important;
}

/* ======================== FOLDER 30 =================== */

.nav-folder-title[data-path^="30"],
.nav-file-title[data-path*="30."] {
  color: var(--F30) !important;
}

/* ======================== FOLDER 40 =================== */

.nav-folder-title[data-path^="40"],
.nav-file-title[data-path*="40."] {
  color: var(--F40) !important;
}

/* ======================== FOLDER 50 =================== */

.nav-folder-title[data-path^="50."],
.nav-file-title[data-path*="50."] {
  color: var(--F50) !important;
}

/* ======================== FOLDER 60 =================== */

.nav-folder-title[data-path^="60."],
.nav-file-title[data-path*="60."] {
  color: var(--F60) !important;
}

/* ======================== FOLDER 70 =================== */

.nav-folder-title[data-path^="70"],
.nav-file-title[data-path*="70."] {
  color: var(--F70) !important;
}

/* ======================== FOLDER 80 =================== */

.nav-folder-title[data-path^="80."],
.nav-file-title[data-path^="80."] {
  color: var(--F80) !important;
}

/* ======================== FOLDER 90 =================== */

.nav-folder-title[data-path^="90."],
.nav-file-title[data-path*="90."] {
  color: var(--F90) !important;
}

/* ======================== FOLDER 100 =================== */

.nav-folder-title[data-path^="100."],
.nav-file-title[data-path*="100."] {
  color: var(--F100) !important;
}

/* ======================== RESSOURCE - ZZ =================== */

.nav-folder-title[data-path^="ZZ."],
.nav-file-title[data-path*="ZZ."] {
  color: var(--FZZ) !important;
}

.nav-folder-title[data-path^="Ressource"],
.nav-file-title[data-path*="Ressource"] {
  color: var(--FZZ) !important;
}


/* 
======================================================================================  
                                      HOVER
====================================================================================== 
*/

.nav-folder-title[data-path^="00."]:hover {
  background-color: var(--bg00) !important;
  filter: invert(50%) sepia(100%) saturate(0%) hue-rotate(250deg) brightness(0%);
  color: var(--F00) !important;
}

.nav-file-title[data-path^="00."]:hover,
.nav-folder-title[data-path*="01."]:hover,
.nav-folder-title[data-path*="02."]:hover,
.nav-folder-title[data-path*="03."]:hover {
  color: var(--F00) !important;
  background-color: var(--bg00) !important;
  filter: invert(50%) sepia(100%) saturate(0%) hue-rotate(250deg) brightness(0%);
}

.nav-folder-title[data-path^="10."]:hover,
.nav-file-title[data-path^="10."]:hover {
  color: var(--F10) !important;
  background-color: var(--bg10) !important;
  filter: saturate(150%);
}

.nav-folder-title[data-path^="20."]:hover,
.nav-file-title[data-path^="20."]:hover,
.nav-file-title[data-path^="20."][data-path*="30."]:hover,
.nav-file-title[data-path^="20."][data-path*="10."]:hover,
.nav-file-title[data-path^="20."][data-path*="20."]:hover {
  color: var(--F20) !important;
  background-color: var(--bg20) !important;
  filter: saturate(150%);
}

.nav-folder-title[data-path^="30"]:hover,
.nav-file-title[data-path*="30."]:hover {
  color: var(--F30) !important;
  background-color: var(--bg30) !important;
  filter: saturate(150%);
}

.nav-folder-title[data-path^="40"]:hover,
.nav-file-title[data-path*="40."]:hover {
  color: var(--F40) !important;
  background-color: var(--bg40) !important;
  filter: saturate(150%);
}

.nav-folder-title[data-path^="50"]:hover,
.nav-file-title[data-path*="50."]:hover {
  color: var(--F50) !important;
  background-color: var(--bg50) !important;
  filter: saturate(150%);
}

.nav-folder-title[data-path^="60."]:hover,
.nav-file-title[data-path*="60."]:hover {
  color: var(--F60) !important;
  filter: saturate(150%);
  background-color: var(--bg60) !important;
}

.nav-folder-title[data-path^="ZZ."]:hover,
.nav-file-title[data-path*="ZZ."]:hover {
  color: var(--FZZ) !important;
  filter: saturate(150%);
  background-color: var(--bgZZ) !important;
}

.nav-folder-title[data-path^="Ressource"]:hover,
.nav-file-title[data-path*="Ressource"]:hover {
  color: var(--FZZ) !important;
  filter: saturate(150%);
  background-color: var(--bgZZ) !important;
}
```

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/CSS%20Snippets/Files%20explorer%20relations%20%26%20color%20%28Mara-Li%29.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/CSS%20Snippets/Files%20explorer%20relations%20%26%20color%20%28Mara-Li%29.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
