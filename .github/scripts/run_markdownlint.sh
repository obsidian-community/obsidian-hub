#!/usr/bin/env bash

cd ../..

MARKDOWN_COMMAND=".github/scripts/node_modules/.bin/markdownlint --fix"

${MARKDOWN_COMMAND} 00\ -\ Contribute\ to\ the\ Obsidian\ Hub
${MARKDOWN_COMMAND}  "04 - Guides, Workflows, & Courses"
