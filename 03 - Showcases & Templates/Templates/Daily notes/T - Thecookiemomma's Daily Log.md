---
date: <% tp.file.creation_date("YYYY-MM-DD")%>
week: "[[ <% tp.file.creation_date("YYYY")%>-W<% tp.file.creation_date("WW")%>]]"
month: "[[<% tp.file.creation_date("YYYY-MM MMMM")%>]]"
year: "[[<% tp.file.creation_date("YYYY")%>]]"
tags: Daily, bujo
---

```button
name Daily Log Entry 
type command
action MetaEdit: Run MetaEdit
color blue
```
^button-dailylog
# Daily Log 
#### [[<% tp.date.yesterday("YYYY-MM-DD -- dddd") %>]]-- -- [[<% tp.date.tomorrow("YYYY-MM-DD -- dddd") %>]]
%%This Template uses the following plugins extensively:  
 Dataview, Templater, Buttons, MetaEdit, Checklist, and DayPlanner. I also use Habit Tracker for the "Trackers" Section.  You may want to change the date format or habits or other pieces; just change them everywhere.%%
<% tp.web.daily_quote() %>

 What does this mean to me today?  
## Goals
### Projects Due 
#todo 
- [ ] 

### Tasks: (Add Due Date and tag for project / sphere) 
#todo
- [ ] 
- [ ] 
- [ ]   

## Trackers

Vitamins:: 
Bible Reading:: 
Prayer:: 
Duolingo:: 
Step Count:: 
[[Physical Fitness]]

## State of mind
%%I differentiate between Life Lessons and Deep Thoughts like this:  Life Lessons are things I've learned that I need to remember for the future.  Deep thoughts are often strange thoughts that stick with me that I can use for creative endeavors or discussions with others.  Revelations are related to my faith  -- the state of my faith at the moment, or what I'm learning in that area.%%
[[Life Lessons]], [[Revelations]], [[Dreams]], [[Feeling]], [[Gratitude]], [[Wellness]], [[Deep Thoughts]]

 Life Lessons:: 
 Revelations:: 
 Dreams:: 
 Feeling::  
 Gratitude:: 
Wellness:: 
Deep Thoughts:: 

***

## Rotations
[[Fanfiction]], [[Food]], [[Music]]

Read:: 
Food:: 
Music:: 

## Day Planner
- [ ] 
%% for each of the Rotation and State of Mind sections, I set up a page that uses the following Dataview query. "Bujo ", short for bullet journal, is the folder for my periodic notes. Change it to match your own. 

```dataview
TABLE <% tp.file.title %>
 FROM "Bujo" 
 WHERE <% tp.file.title %>
 SORT file.ctime
 ```
 then, on my index page, I track my habits so I see it first thing:  (Change your date format to match that of your files).
 ```tracker
searchType: dvField
searchTarget: Vitamins, Prayer, Bible-Reading, Duolingo
datasetName: Vitamins,Prayer, Bible Reading, Duolingo
folder: Bujo
dateFormat: YYYY-MM-DD -- dddd
month:
 dataset: 0,1,2,3
 color: skyblue
 todayRingColor: steelblue
```
Then, I track my steps on my "Physical Fitness" page using habit tracker.  I went with three months at a time so I could actually see them. Again, change the dates and formats to fit your setup: 

``` tracker
searchType: dvField
searchTarget: Step-Count
folder: Bujo
startDate: 2021-11-01 -- Monday
endDate: 2022-01-31 -- Monday
dateFormat: YYYY-MM-DD -- dddd
line:
    title: "Step Count Nov 21-Jan 22"
    xAxisLabel: Date
    yAxisLabel: Value
```
This is still a work in progress.  %%



%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/03%20-%20Showcases%20%26%20Templates/Templates/Daily%20notes/T%20-%20Thecookiemomma%27s%20Daily%20Log.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/03%20-%20Showcases%20%26%20Templates/Templates/Daily%20notes/T%20-%20Thecookiemomma%27s%20Daily%20Log.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
