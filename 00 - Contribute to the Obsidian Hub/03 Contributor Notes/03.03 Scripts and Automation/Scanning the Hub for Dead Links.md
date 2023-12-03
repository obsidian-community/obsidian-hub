---
aliases: 
tags:
  - seedling
publish: true
---

# Scanning the Hub for Dead Links

%% Add a description below this line. It doesn't need to be long: one or two sentences should be a good start. %%

This is a guide on how to check the Hub for dead links, aka links that no longer work.

For scanning links [[mProjectsCode|I]] used [this tool](https://github.com/tcort/markdown-link-check) that [[chrisgrieser|pseudometa]] suggested.

To run the tool you can use this Linux command in the hub root folder, which scans for all markdown files, then passes them to the link check tool and finally writes the output to then `linkcheck.txt` file.

```bash
find . -name \*.md -print0 | xargs -0 -n1 markdown-link-check > linkcheck.txt
```

This will will contain information on all links in all files, but we are only interested in the dead links.
To filter this file you can run this TypeScript file with [Bun](https://bun.sh/).

```ts
// options on what to filter
const FILTER_COMMUNITY_EXPANSIONS = true;
const FILTER_COMMUNITY_PEOPLE = true;
const FILTER_OBSIDIAN_ROUNDUP = true;

class ActiveFile {
    name: string
    links: string[];

    constructor(name: string, links: string[]) {
        this.name = name;
        this.links = links;
    }

    toString(): string {
        return `${this.name}\n${this.links.join('\n')}\n\n`
    }

    addLink(str: string): void {
        this.links.push(str);
    }
}

// read in the full file
const inFile = Bun.file('./linkcheck.txt');
const linkcheck = await inFile.text();

let out: ActiveFile[] = []

let activeFile: undefined | ActiveFile = undefined;

// iterate through all the lines creating an array of ActiveFile instances which contain all broken links for that file
for (const line of linkcheck.split('\n')) {
    if (line.startsWith('FILE:')) {
        if (activeFile) {
            out.push(activeFile);
        }

        activeFile = new ActiveFile(line, []);
    }

    // only add broken links to the ActiveFile
    if (line.includes(' → Status:')) {
        activeFile?.addLink(line);
    }
}

if (activeFile) {
    out.push(activeFile);
}

// write the content to the filtered file
const outFile = Bun.file('./filtered_linkcheck.txt');
await Bun.write(
    outFile, 
    out
        // only include files that have failed links
        .filter(x => x.links.length > 0)
        // filter by options
        .filter(x => !(FILTER_COMMUNITY_EXPANSIONS && x.name.includes('02 - Community Expansions/02.05 All Community Expansions')))
        .filter(x => !(FILTER_COMMUNITY_PEOPLE && x.name.includes('01 - Community/People')))
        .filter(x => !(FILTER_OBSIDIAN_ROUNDUP && x.name.includes('01 - Community/Obsidian Roundup')))
        // sort by file name
        .sort((a, b) => a.name.localeCompare(b.name))
        .map(x => x.toString())
        .join('')
);
```

The script can be configured to filter out specific folders via the three constants at the top of the file.

After running the script you are left with a `filtered_linkcheck.txt` file that only contains dead links and their files.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.03%20Scripts%20and%20Automation/Scanning%20the%20Hub%20for%20Dead%20Links.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.03%20Scripts%20and%20Automation/Scanning%20the%20Hub%20for%20Dead%20Links.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
