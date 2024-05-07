---
aliases: 
- 
tags:
- seedling
publish: true
---

# Project Cards
![[project-cards-screenshot.png]]

This template uses the [[dataview|Dataview]] plugin to create a live-updating view of projects or tasks. Its goal is to make Obsidian a friendlier place for genuine task management.

To use this template, you’ll need to:

1. Create the view template files.
2. Create a project note.
3. Add the view to a note.

---

## 1. Create the View

> This applies Dataview’s `dv.view()` method, which lets you create reusable code blocks and embed them in other notes. [See the Dataview documentation](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/#dvviewpath-input) for more technical detail.

Start by creating a folder in your vault to contain the template. We’ll refer to it as `project-cards` in this walkthrough, but any unique name will do.

Inside this folder, create two files to contain the code at the bottom of this page:

- [view.js](#view.js) contains the JavaScript code that generates the HTML for your list of project cards. 
- [view.css](#view.css) contains the CSS styling to make your cards look pretty.

You may want to place your Dataview templates inside a folder for better organization. Example folder structure:

```
├── Views
│   └── project-cards
│       ├── view.js
│       └── view.css
```

Once these files are created, copy the code below into each one. You may want to use an external code editor for this part, such as [Visual Studio Code](https://code.visualstudio.com/).

---

## 2. Create Projects

Back in Obsidian, make a new note to serve as your first project. Any note with the following [[YAML frontmatter]] format will work:

```yaml
---
tags:     project
title:    Some Neat Project
subtitle: PROJECT-0001
status:   todo
dates:
  '2021-12-21 14:00': In progress.
links:
  'A Useful Link': https://www.google.com
---
```


- `title`: The card will show this as the name of your project.
- `subtitle`: This will appear below the title. Can be used for (e.g.) a short description of the project or a reference code.
- `status`: The card will show a colored icon to indicate the status of the project. Supported status codes: `todo`, `today`, `cont` (continuing or standing), `wait` (waiting or pending), `important`, and `done`. (Use `view.css` to add more codes and colors!)
- `dates`:  Keep track of deadlines, milestones, or the latest activity. If the project has at least one date, that date will be used to sort projects. You can add any number of additional dates here, but they won’t affect [sorting](#sorting).
- `links`:  Add any number of useful links here, e.g. to a Google Doc, a Wikipedia article, or the project website. These will show on the project card as clickable buttons.
- `priority`: Optional [sort](#sorting) priority, `1` thru `9`. Defaults to `9` if none is set.
- `tags`: Optional. Tagging your note as `#project` is just one convenient way for Dataview to query your project notes.

---

## 3. Embed View

Now that we have the template and a project, we can put them together. Add the following code block to a new or existing note:

```dataviewjs
dv.view( 'project-cards', {
  projects: dv.pages('#project')
});
```

This tells Dataview to select all notes with the `#project` tag, sort them in ascending order—earlier dates followed by later dates—and display them as project cards.

You can use additional Dataview queries to narrow down the results. For example, to show only projects with a status of `todo`:

```dataviewjs
dv.view( 'project-cards', {
  projects: dv.pages('#project').where( p => p.status == 'wait' )
});
```

### Sorting

Projects are sorted by the following parameters, in order of precedence:

- **Date:** Earliest to latest. The first item in the project’s `dates` list. If the project has no dates, it’s treated as the current date and time.
- **Priority:** The project’s `priority` number. Defaults to `9`.
- **Title:** The project’s `title`.

The list can be reversed by passing an `order` value of `desc`:

```dataviewjs
dv.view( 'project-cards', {
  projects: dv.pages('#project'),
  order: 'desc'
});
```

---

## Code Reference

### view.js

```js
let projects = input.projects;
let order    = input.order || 'asc';

// SORT
projects = projects.sort( project => {

    // DATE
    let date = moment( ( project.dates && Object.keys(project.dates).length ) ? Object.keys(project.dates)[0] : null ).unix();
    
    // PRIORITY
    let priority = project.priority || 9;

    // TITLE
    let title = project.title || project.file.name;
    
    return `${date}-${priority}-${title}`; // default
    
}, order);

// RENDER
let html = `<section class="project-cards">`;

for (let i = 0; i < projects.length; i++) {

    const project = projects[i];

    // Jump ahead to get the most relevant date.
    let now = moment();

    if ( project.status == 'todo' && project.dates && Object.keys(project.dates).length ) {
        projectTimestamp = Object.keys(project.dates)[0];
        let projectDate  = moment( projectTimestamp );

        if ( projectDate.format('YYYY MM DD') == now.format('YYYY MM DD') || projectDate.unix() <= now.unix() ) {
            project.status = 'today';
        }
    }
    
    html += `<article class="project-card">`;
        
    // ICON
    if ( project.status ) html += `<span class="project-card-status" data-status="${project.status}">&nbsp;</span>`;

    // TITLE
    let title = project.title || project.file.name;
    html += `<h1 class="project-card-title"><a href="${project.file.name}" data-href="${project.file.name}" class="internal-link">${title}</a></h1>`;

    // SUBTITLE
    html += `<div class="project-card-meta">`;

    if ( project.subtitle ) html += `<span class="project-card-subtitle">${project.subtitle}</span>`;

    html += '</div>';

    // DATES
    if ( project.dates && Object.keys(project.dates).length ) { for (let l = 0; l < Object.keys(project.dates).length; l++) {
        const itemTimestamp = Object.keys(project.dates)[l];
        const itemText      = project.dates[ itemTimestamp ];

        let itemDate        = moment( itemTimestamp );
        let itemHasTime     = ( itemTimestamp.split(' ').length > 1 );

        
        let sameYear        = ( now.format('YYYY') == itemDate.format('YYYY') );

        let displayDate     = itemDate.calendar(null, {
            sameDay: '[Today]',
            nextDay: '[Tomorrow]',
            nextWeek: 'dddd',
            lastDay: '[Yesterday]',
            lastWeek: '[Last] dddd',
            sameElse: ( sameYear ? 'D MMMM' : 'D MMMM YYYY' ),
        });

        if ( itemHasTime ) {
            displayDate += ' <span class="project-card-sep">•</span> ' + itemDate.format( 'h:mm a' );
        }

        html += `<div class="project-card-date">
            <span class="project-card-date-prefix" title="${itemDate}">${displayDate}</span>
            <span class="project-card-date-text" title="${itemDate}">${itemText}</span>
        </div>`;
            
    }}

    // LINKS
    html += `<div class="project-card-meta">`;

    if ( project.links && Object.keys(project.links).length ) { for (let l = 0; l < Object.keys(project.links).length; l++) {
        let linkText = Object.keys(project.links)[l];
        let linkURL  = project.links[ linkText ];
        html += `<a class="project-card-link" href="${linkURL}">${linkText}</a>`;
            
    }}

    html += '</div>';

    html += '</div>';

    html += '</article>';

}

html += `</section>`;

return html;
```

### view.css

> These styles were written for the [Minimal](https://github.com/kepano/obsidian-minimal) theme, but they should look decent as-is with any dark theme.

```css
.project-cards {
    margin: 2em 0;
}

.markdown-preview-view .project-card .internal-link,
.markdown-preview-view .project-card .internal-link:hover {
    text-decoration: none;
}

.project-card {
    margin: .5em 0;
    /* border: 1px solid #444; */
    background: hsla(0, 0%, 0%, .1);
    padding: .5em .5em .5em 2em;
    position: relative;
    /* max-width: 40em; */
    border-radius: .25rem;
}

/* Display priority tags as colored circle badges instead of text. */
.project-card-status {
	display: block;
    position: absolute;
    top: .75em;
    left: .5em;
    color: transparent;
	content: '';
    width: 1em;
    height: 1em;
    border-radius: 50%;
    margin-right: .25em;
}

.project-card-status[data-status="today"] {
	background: #d9534f;
}

.project-card-status[data-status="todo"] {
    background: #0275d8;
}

.project-card-status[data-status="done"] {
    background: #5cb85c;
}

.project-card-status[data-status="cont"] {
    background: #5bc0de;
}

.project-card-status[data-status="wait"] {
    background: #444;
}

.project-card-status[data-status="important"] {
    background: #ffd946;
}

.project-card .project-card-title {
    margin: 0;
    font-size: 1rem;
}

.project-card-title a {
    color: inherit;
    text-decoration: none;
}

.project-card-meta,
.project-card-date {
    font-size: smaller;
    color: #999;
    line-height: 1.5;
    margin-top: .25em;
}

.project-card-link {
    display: inline-block;
    color: inherit;
    line-height: 1;
    padding: 4px;
    margin-right: .5em;
    margin-bottom: .5em;
    border: 1px solid #444;
    text-decoration: none;
}

.project-card-date-prefix {
    margin-right: .5em;
    color: white;
}

.project-card-date-text {
    color: #999;
}

.project-card-sep {
    color: #666;
}
```

---

For more templates and examples, check out the original demo on [GitHub](https://github.com/kaelri/obsidian-dataview-test-vault). However, note that the Project Cards view files hosted on GitHub are not fully compatible with this guide.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/03%20-%20Showcases%20%26%20Templates/Templates/Plugin-specific%20templates/Dataview%20templates/Project%20Cards.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/03%20-%20Showcases%20%26%20Templates/Templates/Plugin-specific%20templates/Dataview%20templates/Project%20Cards.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
