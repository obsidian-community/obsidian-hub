---
aliases: 
- 
tags:
- seedling
publish: true
---

# How to Debug why Obsidian is running slowly

Obsidian prides itself on performance so if you're experiencing slowness in during normal usage in the app, don't just accept it! There's something that can be done about it.

The first thing you'll want to investigate is if the slowness is being caused by a plugin. To rule that out, try enabling "Safe Mode" from within the settings (`Settings > Community Plugins > Safe mode`).

![[safe-mode-on.png]]

While this should cause all the plugins to be unloaded from the app, it is recommended that you restart Obsidian in case any plugins didn't fully clean up after themselves (i.e. suspend any running processes and return all allocated memory).

Choose your own adventure time:
- Obsidian is fast with Safe Mode enabled
- I am still experiencing slowness

## Finding out which plugin is responsible for the slowness

If you've determined that the slowness you're experiencing is due to a plugin, the next step is finding out which one.

The simplest way to do this is to turn the plugins on one-by-one and see when the slowness gets introduced.

If you have many plugins, this process can be very tedious. To accelerate this process, you can **bisect** your plugin list using the "divide and conquer" method. This is a term stemming from computer science that simply describes the process of repeatedly splitting a problem in half until you've reached the simplest "base" problem.

So if you're trying to find the slow plugin from your list of 16 plugins, for example, you start by turning off 8 plugins. If Obsidian is still slow, then you turn off 4 of those remaining 8 plugins. If the slowness has stopped, then you know that it was caused by one of the 4 plugins you just disabled, so you repeat this process with those plugins: disable 2, check. Disable 1, check.

> This operation is faster but still a bit tedious, so luckily there's actually a [[obsidian-divide-and-conquer|Divide & Conquer]] plugin that automates some of these steps for you.

Now you have your culprit: the offending plugin that's causing slowness. Now what? You can take the opportunity to be a good citizen and file a report with the plugin author.

The best way to report plugin bugs is on the plugin's Github page.

If you want to help narrow down exactly what code from the plugin is causing the slowness, you can go the extra mile and [[#Taking a performance snapshot|take a performance snapshot]].

## Obsidian is still slow without any plugins

In the event that you're experiencing slowness _even with plugins disabled,_ then you might have found a bug. I recommend filing a bug report on the Obsidian forum with a list of steps for someone to follow to reproduce the issue. For performance-related bugs, you might be asked to [[#Taking a performance snapshot|take a performance snapshot]].

## Taking a performance snapshot

A performance snapshot will tell you exactly what operations/functions are taking up all the CPU cycles when Obsidian is being slow.

To take a performance snapshot, first open the Developer Tools (<kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>I</kbd> on Windows/Linux or <kbd>Cmd</kbd>-<kbd>Opt</kbd>-<kbd>I</kbd> on MacOS; on MacOS alternatively `View › Toggle Developer Tools`). Find the "Performance" tab.

![[performance-snapshot-step1.png]]

From the performance tab, press "Record."

While it's recording, interact with Obsidian until you experience the slowness you were observing before—a couple seconds of interaction is enough.

Next, stop the recording.

![[performance-snapshot-step2.png]]

The Performance tab will now load up an entire snapshot of with all the operations that were performed, how long they took, all along a timeline.

![[performance-snapshot.png]]

If you look at the timeline across the top of the tab, you will see a graph of CPU usage. During particular interactions, you'll see the CPU usage in the graph spiked upward. If you want to drill into what caused that spike and what the computer was doing during that time: you can drag along the timeline. Drag from the start of the spike to the end of the spike. The view will zoom into that region.

While there's a lot of useful information here, you're likely most interested in what's taking the _most_ time. For that, you can switch to the "Bottom-Up" tab. This will sort all the operations that were performed by the time it took to do them.  

![[performance-snapshot-bottom-up.png]]

> To create this example, I performed a few simple searches across the Obsidian hub vault.

In the screenshot above, you can see that two categories **Layout** and **Recalculate Style** take up 911.5 ms and 259.8 ms respectively. This means that while performing a search across the vault, most of the CPU was actually spent on rendering and displaying the search results. 

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/How%20to%20debug%20why%20Obsidian%20is%20running%20slowly.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/How%20to%20debug%20why%20Obsidian%20is%20running%20slowly.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
