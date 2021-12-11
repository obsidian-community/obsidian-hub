## Potentially automatable

There are some maintenance steps that are currently done manually, and that could be run automatically, either on a cron schedule, or upon changes to the main branch.

- Updating theme download counts
  - Part of [[Updating Extensions]]
- Adding new theme, plugin and people pages
    - Part of [[Updating Extensions]]
- Generating the MOCs
  - [[Updating MOC files]]
- Sorting lists
  - [[Content: Lists]]
- Running the Python tests
  - [[Testing Python Code with Approval Tests]]
- Updating "[Structure of the Community Vault](https://publish.obsidian.md/hub/CONTRIBUTING#Structure+of+the+Community+Vault)" IN CONTRIBUTING
    - The comments in the source file show the `tree` command-line args
    - There could be a script which ran the tree command automatically, and saved the output to a file
    - That file could then be `![[]]` embedded inside the CONTRIBUTING page


## Not yet automatable

- Updating existing theme, plugin and people pages
- Publishing
