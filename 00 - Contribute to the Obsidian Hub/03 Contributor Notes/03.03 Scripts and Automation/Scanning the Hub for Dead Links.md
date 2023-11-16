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