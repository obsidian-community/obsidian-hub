---
aliases:
- 
tags:
-  
publish: true
---

# Checking Hub Content

The script `check_content.py` validates the content of this vault, such as checking file names, as opposed to validating the Python code and other infrastructure..

## Automation

This script is run automatically via a GitHub Action.

## Running the script manually

To run it on a fork or clone of the vault:

```bash
cd obsidian-hub/.github/scripts
python3 ./check_content.py
```

Help is available:

```bash
usage: check_content.py [-h]

Check for issues with the content of the Hub vault (such as errors in file names).

optional arguments:
  -h, --help  show this help message and exit
```
