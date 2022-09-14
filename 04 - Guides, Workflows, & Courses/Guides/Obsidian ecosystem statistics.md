---
aliases: 
- 
tags:
- seedling
publish: true
---

# Obsidian statistics
*Note written by [[Fevol]]*

This note contains several stats pertaining to the Obsidian ecosystem, specifically the share of users per platform, and the downloads of plugins/themes.

All data and graphs found below have been gathered from either GitHub or Obsidian's API. 

The Python scripts to fetch, process and graph the data, alongside with all raw & processed data, can be found in this GitHub repository: [https://github.com/Fevol/obsidian-data-processing](https://github.com/Fevol/obsidian-data-processing)

Before interpreting the data found below, be aware of the following:
- All data was collected on 2022/09/11
- The amount of downloads is usually much higher than the actual amount of users who've installed a plugin/Obsidian
- Flatpak downloads are not included in the platform share, this accounts for 751k installs and updates in total, spread across all versions of Obsidian


## Platform Share

This section contains the %-share of users for every platform Obsidian is available on, excluding iOS and Android.

As of *version 0.15.9*, the share between platforms is divided as follows:
**Windows** — 53.1%
>64-bit: 98.01%
>arm:    1.19%
>32-bit: 0.79

**MacOS** — 34.4%

**Linux** — 12.1%
>AppImage: 53.92%
>Snap: 22.98%
>Debian: 17.55%
>AppImage(arm): 2.81%
>tar.gz: 2.55%
>tar.gz(arm): 0.17%

![Releases stats](https://raw.githubusercontent.com/Fevol/obsidian-data-processing/master/images/releases-platform-share.png)


## Obsidian Releases Distribution

![Releases stats](https://raw.githubusercontent.com/Fevol/obsidian-data-processing/master/images/releases-full.png)



## Plugin Downloads

This chart graphs the downloads of community plugins on the y-axis, and the relative age of a plugin on the x-axis (from oldest plugin to newest plugin)

- 21 Plugins have more than 100.000 downloads (3.24%)
- 155 Plugins have more than 10.000 downloads (23.92%)
- 449 Plugins have more than 1.000 downloads (69.29%)

![Plugin downloads](https://raw.githubusercontent.com/Fevol/obsidian-data-processing/master/images/plugins-chronological.png)



## Theme Downloads

This chart graphs the downloads of community themes on the y-axis, and the relative age of a theme on the x-axis (from oldest theme to newest theme)

- 3 Themes have more than 100.000 downloads (2.13%)
- 42 Themes have more than 10.000 downloads (29.79%)
- 135 Themes have more than 1.000 downloads (95.74%)

![Theme downloads](https://raw.githubusercontent.com/Fevol/obsidian-data-processing/master/images/themes-chronological.png)

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Obsidian%20ecosystem%20statistics.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Obsidian%20ecosystem%20statistics.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
