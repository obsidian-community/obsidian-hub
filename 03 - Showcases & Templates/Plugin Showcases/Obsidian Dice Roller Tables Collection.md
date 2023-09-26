---
aliases: 
- 
tags:
- seedling
---

# Obsidian Dice Roller Tables Collection

I made a collection of [Dice Roller](https://github.com/valentine195/obsidian-dice-roller) Tables that I use to run my DND campaigns! You can find them at my [Github Repository](https://github.com/WychWitch/Obsidian-Dice-Roller-Tables). Download or clone it, and add it to your vault!

Before using, **Please make update/install to the latest version of the [Dice Roller](https://github.com/valentine195/obsidian-dice-roller) and [Buttons](https://github.com/shabegom/buttons) plugins to be able to use these pages!**

It's also recommended that you turn off the following settings within Dice Roller for maximum compatibility: 
- *Display formula with results*
- *Display Lookup Table Roll*
- *Show Dice Button*

## Example of NPC Generator
![2hDw43Oiub](https://user-images.githubusercontent.com/1291820/142545127-0690300d-1f55-4563-a523-0a2e715d483f.gif)

## Customization
There are a few pages that should be edited to fit your vault's set up and/or your campaign!
- Race Dice Tables
	- This is the one that probably requires the most editing, as the races I have included are *specific* to my campaign. All you need to do is replace the race names with ones that better fit your campaign!
- NPC Dice tables: 
	- Connections-outgoing
		- This table and the ones below all require you to change the tags to match your tag from \#dnd/npc, \#dnd/pc, etc formatting! 
	- Connections-incoming
	- npc or faction

## Overview of Generators 
Here are the generators I have created:
- \_Example Generators
	- This contains links to specific generators, and a Magic Item Name generator and an Encounter generator!
- NPC Generator
	- This is an NPC generator, containing personality, quirks, and even some tarot cards with meanings
- Angel Generator 
	- This is an  Angel/Celestial generator using one of my favorite perchances as a source!
- Deity Generator
	- An (admittedly barebones) Deity generator!


## Optional Scripts

### txt2dice
If you're interested, I also wrote a small script called txt2dice to convert any txt file list (with each item on a newline) in python3! Save the below code and run it as `py path/to/txt2dice.py path/to/file-name.txt`

Some options include `-o outputName` changes the output name, `-t titleName` adds the title to the table, and adds the table-name as the block-id!

```python
import argparse


parser = argparse.ArgumentParser(description='Converts a list into a diceroller-formatted md table', prog='txt2dice')
parser.add_argument('input', help='The file to convert to markdown!')

parser.add_argument('--output', '-o', help='The name of the file to write to! Warning: This WILL overwrite any file that exists already.Default is txt2dice-output.md', default='txt2dice-output.md', required=False)
parser.add_argument('--title', '-t', help='The name of the table you will generate! It will also add it as a block id.', default='Table', required=False)

args = parser.parse_args()

listOfLines = []

mdTableBody = ""

mdTable = ""  

try:
  with open(f'{args.input}') as afile:
    listOfLines = afile.read().splitlines() 
except FileNotFoundError:
  print(f"Could not find {args.input}")

num = 1
for item in listOfLines:
  mdTableBody += f"\n|{num}|{item}|"
  num +=1

mdTableBody += f"\n^{args.title}\n"
mdtableHeader = f"""| dice: 1d{num-1} | {args.title}|
| --------- | ------------------- |"""

mdTable = mdtableHeader + mdTableBody

if args.output.endswith('.md'):
  text_file = open(f"tables/{args.output}", "w")
  text_file.write(mdTable)
  text_file.close()
else:
  text_file = open(f"table/{args.output}.md", "w")
  text_file.write(mdTable)
  text_file.close()

print(f"Converted and saved to {args.output}!")

```

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/03%20-%20Showcases%20%26%20Templates/Plugin%20Showcases/Obsidian%20Dice%20Roller%20Tables%20Collection.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/03%20-%20Showcases%20%26%20Templates/Plugin%20Showcases/Obsidian%20Dice%20Roller%20Tables%20Collection.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
