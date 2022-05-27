The Obsidian [backlinks panel](https://help.obsidian.md/Plugins/Backlinks) uses the following HTML structure. If your plugin attempts to recreate a similar structure, like the [[graph-analysis|Graph Analysis]] Co-Citations view does, it is useful to use the same classes that Obsidian uses natively. That way, themes will more easily apply to your plugin's custom view.

```svelte
<script lang="ts">
  const buttons: any[] = []
  const d =
    'M94.9,20.8c-1.4-2.5-4.1-4.1-7.1-4.1H12.2c-3,0-5.7,1.6-7.1,4.1c-1.3,2.4-1.2,5.2,0.2,7.6L43.1,88c1.5,2.3,4,3.7,6.9,3.7 s5.4-1.4,6.9-3.7l37.8-59.6C96.1,26,96.2,23.2,94.9,20.8L94.9,20.8z'
</script>

<!-- Header with buttons -->
<div class="view-content">
  <div class="nav-header">
    <div class="nav-buttons-container">
      {#each buttons as button}
        <div class="nav-action-button"><svg /></div>
      {/each}
    </div>
  </div>

  <!--- Everything under the buttons -->
  <div class="backlinks-pane">
    <!-- The "Linked Mentions" dropdown -->
    <div class="tree-item-self is-clickable">
      <!-- The arrow to open/close the dropdown -->
      <span class="tree-item-icon">
        <svg><path fill="currentColor" stroke="currentColor" {d} /></svg>
      </span>
      <div class="tree-item-inner">Linked Mentions</div>
      <!-- Measure container -->
      <div class="tree-item-flair-outer">
        <span class="tree-item-flair">Measure</span>
      </div>
    </div>
    <!-- The items under the "Linked Mentions" dropdown -->
    <div class="search-result-container">
      <!-- Not sure why it is double wrapped, given it has no sibling? -->
      <div class="search-results-children">
        <div style="width: 1px; height: 0.1px; margin-bottom: 0px;" />
        <!-- The entire second-level dropdown & inner results -->
        <div class="tree-item search-result" draggable="true">
          <!-- The second-level dropdown -->
          <div class="tree-item-self search-result-file-title is-clickable">
            <!-- The dropdown arrow -->
            <div class="tree-item-icon collapse-icon">
              <svg><path fill="currentColor" stroke="currentColor" {d} /></svg>
            </div>
            <!-- The actual clickable link to the second-level file -->
            <div class="tree-item-inner">Note Name</div>
            <!-- Measure container -->
            <div class="tree-item-flair-outer">
              <span class="tree-item-flair">Measure</span>
            </div>
          </div>
          <!-- Container of the actual note content containing the backlink -->
          <div class="search-result-file-matches">
            <div style="width: 1px; height: 0.1px; margin-bottom: 0px;" />
            <div class="search-result-file-match">
              <span>Text before highlight</span>
              <span class="search-result-file-matched-text">
                [[Highlighted Note Name]]
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/06%20-%20Inbox/Backlinks%20Panel%20HTML%20Svelte%20Component.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/06%20-%20Inbox/Backlinks%20Panel%20HTML%20Svelte%20Component.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
