## Concepts
This template will detect modify behaviors and help you to record which notes that you modified today, automatically inserting these notes to any place of your daily notes. 
![image](https://github.com/user-attachments/assets/58e1ac58-acf6-498e-8832-dfe3fa0677fe)

The template is modular that: 
1. You don't have to modify your current daily notes templates at all.(But you can also customize a place for recording)
2. You can either insert the note to an existing place like the end of daily note, or modify your daily note template to add a place for inserting.
3. You can customize the query to collect the code. The query is the same as `Dataview Query`. 

## How to use this template?
1. You need to install the Templater plugin and Dataview plugin
2. In setting of Templater plugin, ensure that the folder template is enabled to auto-enforce daily note template to new created daily notes![image](https://github.com/user-attachments/assets/5edefd02-e065-46c6-b170-6f3c81eeb055)

3. You need to specify a folder to store your templates in the setting of Templater plugin
4. Create a new `.md` file in your template folder
5. Copy the template below and paste it into your `.md` file that just created
6. Modify the `Constants`:`RECORD_NOTE_FOLDER`,`QUERY_STRING`,`START_POSITION`,`END_POSITION`
7. In the setting of Templater plugin, add this template as "start-up template"![image](https://github.com/user-attachments/assets/4448ea44-9cc3-4ae8-b86e-f21381e67868)


### The Record Note Folder
By default, the record folder is "Logs/Daily Notes". You should adjust it to your daily note folder. 

### The Query String
You can seamlessly move your dataview query here but deleting the line-breaks. 
By default, will use the data in this dataview query:
```dataview
table WITHOUT ID
file.link as "Modified Notes", file.mtime as "Edit Time"
from !"MyTestFolder"
where file.mday = date(today)
sort file.mtime asc
limit 32
```

### Start Position and End Position
This string defines where to insert the data. Not only the admonition plugin is supported, but for all other plugins. 
By default, this will insert a table of data to an admonition-callout:
```ad-note
title: Modified Notes on this day
collapse: close
```
Effect:
![image](https://github.com/user-attachments/assets/58e1ac58-acf6-498e-8832-dfe3fa0677fe)

It's also recommended to place it under a title(Require this title exist in your daily note template):
```
START_POSITION = "#### Dataview Query";
END_POSITION = "#### Dataview JS";
```
Effect:
![image](https://github.com/user-attachments/assets/57aa7556-265d-4d5d-b739-4ea9863b1dea)

If you want to insert to the end of your daily note, just leave `END_POSITION` blank. 

## Template
```
<%*
// Configuration Constants
const RECORD_NOTE_FOLDER = "Logs/Daily Notes";
const QUERY_STRING = `table WITHOUT ID file.link as "Modified Notes", file.mtime as "Edit Time" from !"MyTestFolder" where file.mday = date(today) sort file.mtime asc limit 32`;
const START_POSITION = "title: Modified Notes on this day\ncollapse: close"; 
const END_POSITION = "````"; 
const dv = app.plugins.plugins["dataview"].api;

// Get today's date in ISO format
let today = moment().format("YYYY-MM-DD");
let DailyNote = moment(today).format("YYYY-MM-DD");
let recordNote = DailyNote; 
let note = app.vault.getAbstractFileByPath(`${RECORD_NOTE_FOLDER}/${recordNote}.md`);

// Delay function
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

new Notice("Autoupdate scripts are running! ", 3000);
console.log("Autoupdate scripts are running! ");

// Function to create a new note
async function createNewNote() {
    await tp.file.create_new("", recordNote, false, RECORD_NOTE_FOLDER);
    new Notice(`Created new note ${recordNote} in folder ${RECORD_NOTE_FOLDER}.`, 5000);
    console.log(`Created new note ${recordNote} in folder ${RECORD_NOTE_FOLDER}.`);
    await delay(500);
}

// Function to fetch query output
async function fetchQueryOutput() {
    try {
        return await dv.queryMarkdown(QUERY_STRING);
    } catch (error) {
        new Notice("⚠️ ERROR querying data: " + error.message, 5000);
        console.log(`⚠️ ERROR: ${error}`);
        throw error; // Rethrow to handle in the calling function
    }
}

// Function to process query output
function processQueryOutput(queryOutput) {
    const lines = queryOutput.split('\n');
    return lines.length > 3 ? queryOutput.trimEnd() : "No note is modified today! ";
}

// Function to read note content
async function readDailyNoteContent() {
    return await app.vault.read(note);
}

// Function to update the note
async function updateNoteContent(content, recordData) {
    const regex = new RegExp(`${START_POSITION}[\\s\\S]*?(?=${END_POSITION})`);
    if (regex.test(content)) {
        const newContent = content.replace(regex, `${START_POSITION}\n${recordData}\n`);
        await app.vault.modify(note, newContent);
        new Notice("Daily note auto updated! ", 2000);
        console.log("Daily note auto updated! ");
    } else {
        new Notice("⚠️ ERROR updating note: " + recordNote + "! Check console log.", 5000);
        console.log(`⚠️ ERROR: The given pattern "${START_POSITION} ... ${END_POSITION}" is not found in ${recordNote}! `);
    }
}

// Main function to update daily notes
async function updateDailyNotes() {
    try {
        if (!tp.file.find_tfile(recordNote)) {
            await createNewNote();
        }

        const dvqueryOutput = await fetchQueryOutput();
        const recordData = processQueryOutput(dvqueryOutput.value);
        const content = await readDailyNoteContent();
        await updateNoteContent(content, recordData);
    } catch (error) {
        new Notice("⚠️ An unexpected error occurred: " + error.message, 5000);
        console.log(`⚠️ ERROR: ${error}`);
    }
}

// Debounce function to limit the rate at which a function can fire
function debounce(func, wait) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

// Set up event listener to run the update function on every file save with debounce
app.vault.on('modify', debounce(async (file) => {
    console.log(`Detected File Change: ${file.name}`);
    if (file.name === `${recordNote}.md`) {
        await delay(200);
    } else {
        await updateDailyNotes();
        console.log(`Try updating ${recordNote}.md`);
    }
}, 60000)); // 60 seconds debounce

%>
```

You can also subscribe to latest update/improvement here: https://github.com/LeCheenaX/Obsidian-useful-scripts/tree/main/Templates
