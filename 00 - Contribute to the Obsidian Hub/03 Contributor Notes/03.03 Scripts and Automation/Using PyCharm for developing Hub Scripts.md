---
aliases: 
- 
tags:
- seedling
publish: true
---

# Using PyCharm for developing Hub Scripts

%% Add a description below this line. It doesn't need to be long: one or two sentences should be a good start. %%

## Assumptions

We assume basic knowledge of editing in PyCharm.

## Setup pycharm project.
- Open Obsidian project in PyCharm
- Trust the project
- 
- Pycharm > Preferences (macos)
- Project: Obsidian-hub
	- [pic]
	- **Setup Virtual Env**
	- Python Interpreter 
		- [pic]
		- Gear Icon > Add...
			- ![[Pasted image 20230109181702.png]]
		- Ensure Python 3.x
			- ![[Pasted image 20230109181752.png]]
		- Ok.
	- Project Structure
		- Automatically ignores the venv folder
		- Automatically recognizes .github/scripts/templates as a Template folder
		- Mark .github/scripts as a Sources folder.
		- Mark .github/scripts/test as a Test folder.
		- ![[Pasted image 20230109182440.png]]
 
### Install dependencies
  In the Project browser (left panel) navigate to the .github/scripts folder.
- Open the requirements.txt file
- Right click on the editor window for the file and run "Install All Packages"

![[Pasted image 20230109181958.png]]
![[Pasted image 20230109182010.png]]
![[Pasted image 20230109182025.png]]

### Configure the tests
- In the top right of the IDE click the "Add Configuration..." button.
- Click the plus icon ("Add new...")
	- ![[Pasted image 20230109182117.png]]
- Scroll down and select Python > pytest
	- ![[Pasted image 20230109182140.png]]
	- ![[Pasted image 20230109182206.png]]
- Set the Target folder to .github/scripts/tests
	- ![[Pasted image 20230109182303.png]]
> [!INFO] Can't see .github folder? (macos)
> In the file selector dialog press the Shift-command-. to toggle the visibility of hidden folders.
- Ok
	
## How to run the tests

###  How to run All tests?
- Play button top right.
	- ![[Pasted image 20230109182324.png]]

### How to run specific test?
- Note the play button in the test files.
- Right click on filename tab, "Run 'python tests...'" to run all the tests in this file.
	- ![[Pasted image 20230109182358.png]]
- Click the pay button in the lefthand margin next to a single test definition to run just that test.
 - [screenshot]
