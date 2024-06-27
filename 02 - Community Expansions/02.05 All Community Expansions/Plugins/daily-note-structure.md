---
plugin-id: daily-note-structure
aliases:
- Daily Note Structure
tags: 
- 
publish: true
---

%% ----- Badges ----- %%

![GitHub all releases](https://img.shields.io/github/downloads/db-developer/daily-note-structure/total?color=573E7A&logo=github&style=for-the-badge)   
![GitHub manifest version](https://img.shields.io/github/manifest-json/v/db-developer/daily-note-structure?color=573E7A&logo=github&style=for-the-badge)   
![GitHub issues by-label](https://img.shields.io/github/issues/db-developer/daily-note-structure/help%20wanted?color=573E7A&logo=github&style=for-the-badge)   
![GitHub Repo stars](https://img.shields.io/github/stars/db-developer/daily-note-structure?color=573E7A&logo=github&style=for-the-badge)

%% ----- Badges ----- %%

%% ----- Do not edit this section ----- %%

# Daily Note Structure

Plugin ID: `daily-note-structure`
Links: [GitHub repository](https://github.com/db-developer/daily-note-structure) or [<button id=HH>Open in Obsidian</button>](obsidian://show-plugin?id=daily-note-structure)
Developed by: [[db-developer]]
Mobile compatible: [[Mobile-compatible plugins|Yes]]

One-Click create a structure of multiple daily folders and files with individual names and templates.

Use the settings for creating a structure in JSON format. A click on the plugins ribbon button will create the sturcture with file data (from templates) and folder notes (filled by templates).
For best results install templater and your preferred folder note plugin.

Note:
Obsidians root object is a folder, therefore structure JSON must be of type Array '[]' and it can take any number of folders and files you like to create.
Notes of folders and file notes that already exist will be ignored, thus remain unchanged. Missing subfolders and files will be created.

Example settings file:


```json
[{
  "type": "folder",
  "namepattern": "Family",
  "template": "Other/Templater/Templates/Empty Named Folder.md",
  "children": [{
    "type": "folder",
    "namepattern": "My Name",
    "template": "Other/Templater/Templates/Empty Named Folder.md",
    "children": [{
      "type": "folder",
      "namepattern": "Diary",
      "template": "Other/Templater/Templates/Empty Named Folder.md",
      "children": [{
        "type": "folder",
        "namepattern": "{{YYYY}}",
        "template": "Other/Templater/Templates/Yearly Named Folder.md",
        "children": [{
          "type": "folder",
          "namepattern": "{{MMOW}} - {{MMMMOW}} {{YYYY}}",
          "template": "Other/Templater/Templates/Monthly Named Folder.md",
          "children": [{
            "type": "folder",
            "namepattern": "KW {{WW}} ({{MMMMOW}} {{YYYY}})",
            "template": "Other/Templater/Templates/Weekly Named Folder.md",
            "children": [{
              "type": "folder",
              "namepattern": "KW {{WW}} ({{MMMMOW}} {{YYYY}})",
              "template": "Other/Templater/Templates/Daily Named Folder.md",
              "children": []
            }, {
              "type": "folder",
              "namepattern": "Operational Planning",
              "template": "Anderes/Templater/Templates/Weekly Operational Planning Folder.md",
              "children": []
            }, {
              "type": "folder",
              "namepattern": "Resources",
              "template": "Anderes/Templater/Templates/Weekly Resources Folder.md",
              "children": []
            }]
          }]
        }]
      }]
    }]
  }]
}]
```

%% ----- Do not edit anything above this line ----- %% 

%% Does the repository or author have any sponsoring links? Uncomment the next line and add them to the author's note. If they don't, please delete the placeholder tag: #placeholder/author %%
%% ![[db-developer#Sponsor this author]] %%

%% Hub footer: Please don't edit anything below this line %%

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Plugins/daily-note-structure.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Plugins/daily-note-structure.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>