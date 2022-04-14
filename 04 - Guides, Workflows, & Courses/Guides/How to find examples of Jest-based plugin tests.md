---
aliases: 
- 
tags:
- seedling
publish: true
---

# How to find examples of Jest-based plugin tests

When first writing [[for Plugin Developers to Automate Tests|automated tests]], it can be useful to review existing test code for ideas.

For the popular [Jest](https://jestjs.io) framework, there are already many community plugins to review.

## Obsidian Plugins Depending on Jest

As of 2022-04-07.

*Note: No guarantee that there are any tests written or run!*

- FHachez/[obsidian-convert-url-to-iframe](https://github.com/FHachez/obsidian-convert-url-to-iframe)
- JeppeKlitgaard/[ObsidianAnkiBridge](https://github.com/JeppeKlitgaard/ObsidianAnkiBridge)
- MSzturc/[obsidian-advanced-slides](https://github.com/MSzturc/obsidian-advanced-slides)
- aidenlx/[marginnote-companion](https://github.com/aidenlx/marginnote-companion)
- aidurber/[obsidian-plugin-dynamic-toc](https://github.com/aidurber/obsidian-plugin-dynamic-toc)
- arnau/[obsidian-metatable](https://github.com/arnau/obsidian-metatable)
- beaussan/[update-time-on-edit-obsidian](https://github.com/beaussan/update-time-on-edit-obsidian)
- blacksmithgu/[obsidian-dataview](https://github.com/blacksmithgu/obsidian-dataview)
- charliecm/[obsidian-tidy-footnotes](https://github.com/charliecm/obsidian-tidy-footnotes)
- chhoumann/[MetaEdit](https://github.com/chhoumann/MetaEdit)
- chhoumann/[quickadd](https://github.com/chhoumann/quickadd)
- coddingtonbear/[obsidian-csv-table](https://github.com/coddingtonbear/obsidian-csv-table)
- coddingtonbear/[obsidian-itinerary](https://github.com/coddingtonbear/obsidian-itinerary)
- coddingtonbear/[obsidian-local-rest-api](https://github.com/coddingtonbear/obsidian-local-rest-api)
- darlal/[obsidian-switcher-plus](https://github.com/darlal/obsidian-switcher-plus)
- denisoed/[obsidian-orthography](https://github.com/denisoed/obsidian-orthography)
- ebullient/[obsidian-snippetor](https://github.com/ebullient/obsidian-snippetor)
- ebullient/[obsidian-task-collector](https://github.com/ebullient/obsidian-task-collector)
- elias/[sundqvist-obsidian-annotator](https://github.com/elias/sundqvist-obsidian-annotator)
- erykwalder/[quoth](https://github.com/erykwalder/quoth)
- fantasycalendar/[obsidian-fantasy-calendar](https://github.com/fantasycalendar/obsidian-fantasy-calendar)
- hadynz/[obsidian-kindle-plugin](https://github.com/hadynz/obsidian-kindle-plugin)
- ivan/[lednev-obsidian-task-archiver](https://github.com/ivan/lednev-obsidian-task-archiver)
- jglev/[obsidian-paste-to-current-indentation](https://github.com/jglev/obsidian-paste-to-current-indentation)
- joethei/[obsidian-rss](https://github.com/joethei/obsidian-rss)
- kometenstaub/[linked-data-helper](https://github.com/kometenstaub/linked-data-helper)
- kometenstaub/[metadata-extractor](https://github.com/kometenstaub/metadata-extractor)
- kometenstaub/[obsidian-version-history-diff](https://github.com/kometenstaub/obsidian-version-history-diff)
- larslockefeer/[obsidian-plugin-todo](https://github.com/larslockefeer/obsidian-plugin-todo)
- mcndt/[obsidian-toggl-integration](https://github.com/mcndt/obsidian-toggl-integration)
- motif/[software-obsimian](https://github.com/motif/software-obsimian)
- mrjackphil/[obsidian-text-expand](https://github.com/mrjackphil/obsidian-text-expand)
- platers/[obsidian-linter](https://github.com/platers/obsidian-linter)
- pmorim/[obsidian-chess](https://github.com/pmorim/obsidian-chess)
- raineszm/[obsidian-export-to-tex](https://github.com/raineszm/obsidian-export-to-tex)
- raineszm/[obsidian-latex-environments](https://github.com/raineszm/obsidian-latex-environments)
- samwarnick/[obsidian-simple-embeds](https://github.com/samwarnick/obsidian-simple-embeds)
- schemar/[obsidian-tasks](https://github.com/schemar/obsidian-tasks)
- st3v3nmw/[obsidian-spaced-repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition)
- tgrosinger/[ledger-obsidian](https://github.com/tgrosinger/ledger-obsidian)
- tgrosinger/[slated-obsidian](https://github.com/tgrosinger/slated-obsidian)
- tgrosinger/[tq-obsidian](https://github.com/tgrosinger/tq-obsidian)
- timhor/[obsidian-editor-shortcuts](https://github.com/timhor/obsidian-editor-shortcuts)
- timhor/[obsidian-sentence-navigator](https://github.com/timhor/obsidian-sentence-navigator)
- valentine195/[obsidian-fantasy-calendar](https://github.com/valentine195/obsidian-fantasy-calendar)
- vslinko/[obsidian-outliner](https://github.com/vslinko/obsidian-outliner)
- vslinko/[obsidian-zoom](https://github.com/vslinko/obsidian-zoom)

## Updating the list of plugins

```bash
git clone https://github.com/claremacrae/obsidian-repos-downloader.git

cd obsidian-repos-downloader
python3 obsidian-repos-downloader.py

cd plugins
find . -name jest.config.\* | grep -v node_modules | sort
```

<!--

Converting the console output to the links above

https:\/\/github\.com\/([^\/]+)\/([^ ]+) 

| [$1](https://github.com/$1) | [$2](https://github.com/$1/$2) |

| $1 | [$2](https://github.com/$1/$2) |

[$1/**$2**](https://github.com/$1/$2)

-->
