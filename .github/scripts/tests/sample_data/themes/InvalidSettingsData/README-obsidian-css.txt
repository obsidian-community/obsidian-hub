The obsidian.css in this folder has an error on line 24, due
the indentation being done with a tab character, instead of 2 spaces.

This was original reported in this issue:
https://github.com/whyt-byte/Blue-Topaz_Obsidian-css/issues/217

It's preserved here so that we can have a test case, to
confirm that the Hub code gracefully detects errors parsing
themes, instead of just falling over.