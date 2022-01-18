---
aliases:
- 
tags:
- 
---

# Updating Extensions

The script `update-releases.py` reads current data from the Obsidian Releases repo, and generates outputs for any newly-added plugins or themes.

## Running the script

To run it:

```bash
cd obsidian-hub/.github/scripts
python3 ./update-releases.py [arguments]
```

Help is available:

```bash
usage: update-releases.py [-h] [--overwrite] [-v]
                          (--all | --themes | --plugins | --update-download-counts)

Create notes based on the obsidian-releases repo

optional arguments:
  -h, --help            show this help message and exit
  --overwrite           Overwrite existing files.
  -v, --verbose
  --all                 Process plugins, themes and authors.
  --themes              Only process themes (authors won't be updated).
  --plugins             Only process plugins (authors won't be updated)
  --update-download-counts
                        Only update the download counts in existing themes. This
                        ignores the overwrite argument, and always updates.
```

## Suggested strategy for helping reviewers

**Suggestion:** To be kind to PR reviewers, put the different automated edits and the manual edits in to **separate commits**, all within a **single Pull Request**.

## Pull Request 1

### Commit 1: Update the download counts in existing theme files.

1. Run `python3 ./update-releases.py --update-download-counts`
2. Commit the changes, with a message making it clear that all changes were made by automated script (so that only minimal review is required)

### Create a pull request


## Pull Request 2

### Commit 1: Add new plugins, themes and authors

1. Run it once with: `python3 ./update-releases.py --all`
2. Commit the changes, with a message making it clear that all changes were made by automated script (so that only minimal review is required)

Note: there is no need to commit these as separate steps or separate PRs: they are the results of running a single process, and will typically only create a small number of files.

### Commit 2: Manual intervention required - with --overwrite

1. Run it again with: `python3 ./update-releases.py --all --overwrite`
2. Carefully review all the diffs, using a diff tool, and reinstate any lost text back in to the updated files
3. Commit the changes, with a message making it clear that more careful review is required

### Commit 3: Update the MOC files

By following [[Updating MOC files]].

### Create a single Pull Request, with all the changes

## Troubleshooting

### 404s

On a sample of 1 run, if you get a 404, wait about 10 minutes and run the script again, and it will probably work.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.03%20Scripts%20and%20Automation/Updating%20Extensions.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.03%20Scripts%20and%20Automation/Updating%20Extensions.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
