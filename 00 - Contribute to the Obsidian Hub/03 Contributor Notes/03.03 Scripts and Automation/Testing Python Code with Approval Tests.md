---
aliases:
- 
tags:
- 
---

# Testing Python Code with Approval Tests


About the Python tests in [.github/scripts](https://github.com/obsidian-community/obsidian-hub/tree/main/.github/scripts)

## TL;DR

TODO Add a TL;DR as a quick-start...

## Approval Tests in general

The traditional approach for writing automated tests for code is to call a function that tests that the result of an operation matches the expectation.

In pseudo code:

```
assert actual_value = expected_value
```

Approval Tests instead allow us to verify a chunk of output (such as a string or a file) in one operation as opposed to writing test assertions for each element.

Complex results can be saved in a file, rather than having to do something like:

- write a large number of separate asserts, for each part of the output
- paste a large string of "expected" value in the test source code.

There are Approval Tests library implementations in many different languages: [approvaltests.com](https://approvaltests.com).

## Python Approval Tests

[ApprovalTests.Python](https://github.com/approvals/ApprovalTests.Python)

## How Approval Tests work

### Approval Tests Process

The simplest use of Approval Tests is to call a `verify()` method, that:

1. writes out the text or object it is given to some output file (called "received")
2. then compares the file content with previously-accepted output (called "approved").
3. if these are equivalent, then the test passes
4. if the received differs from the approved, or if the approved does not exist yet,
   then the framework searches for a diff-tool on your machine,
   and uses it to show you the differences - with:
     - received on the left
     - approved on the right

## Dealing with test failures

The diff tool allows you to easily inspect the changes between received and approved.

You can then either:

1. Fix the code, if the differences show an unwanted change
2. Use the diff tool to copy the changes over from received to approved, if the changes are intentional. This is called "approving" the output.

### Scenario: First run of a new test

The test always fails, and loads a diff tool showing the received file, and an empty approved file, for you to decide whether to approve the output.

### Scenario: Test passes

No diff tool is launched, as no action is required.

### Scenario: Reviewing the output to spot the changes

TODO Add screenshot and description

### Scenario: Unwanted/unexpected difference

TODO Add screenshot and description

### Scenario: You changed the code and want to update the approved files

TODO Add screenshot and description

### Diff Tools (a.k.a. "Reporters")

**Note**: to be used effectively, Approval Tests require you to have a diff tool installed.

For the Python library, the supported tool names are listed in:

- https://github.com/approvals/ApprovalTests.Python/blob/master/approvaltests/reporters/reporters.json

But note that this links to the latest file, and we may be using a pinned version: see requirements.txt.

## Reference material

1. Clare's talks on Approval Tests:
      - https://claremacrae.co.uk/conferences/presentations_by_topic.html#testing-legacy-c-code-with-approval-tests
      - The start of the 2019-02-05 video is probably the best introduction.
2. Python ApprovalTests library:
      - https://github.com/approvals/ApprovalTests.Python

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.03%20Scripts%20and%20Automation/Testing%20Python%20Code%20with%20Approval%20Tests.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/00%20-%20Contribute%20to%20the%20Obsidian%20Hub/03%20Contributor%20Notes/03.03%20Scripts%20and%20Automation/Testing%20Python%20Code%20with%20Approval%20Tests.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
