---
aliases: 
- 
tags:
- seedling
publish: true
---

# How to get started developing plugins?

This is the quick start guide from the [obsidian sample plugin readme](https://github.com/obsidianmd/obsidian-sample-plugin):

1.   Make a copy of this repo as a template with the "Use this template" button (login to GitHub if you don't see it).
	  ![[github-use-template-repo.png]]
2.   Clone your repo to a local development folder. For convenience, you can place this folder in your `.obsidian/plugins/your-plugin-name` folder.
3.   Install NodeJS, then run `npm i` in the command line under your repo folder.
4.   Run `npm run dev` to compile your plugin from `main.ts` to `main.js`.
5.   Make changes to `main.ts` (or create new `.ts` files). Those changes should be automatically compiled into `main.js`.
6.   Reload Obsidian to load the new version of your plugin.
7.   Enable plugin in settings window.
8.   For updates to the Obsidian API run `npm update` in the command line under your repo folder.
