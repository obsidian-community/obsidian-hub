#!/usr/bin/env python3

import sys
import argparse
from typing import Sequence, Dict, List, Any

from github3api import GitHubAPI

from obsidian_releases import get_community_plugins
from utils import (
    get_template,
    print_progress_bar,
    write_template_file,
)

from plugins import Plugin

PluginIssue = Dict[str, str]


def process_issues_for_plugin(gh_client: GitHubAPI, plugin: Plugin, label: str) -> List[PluginIssue]:
    issues = list()
    repo_issues = gh_client.get(f'/repos/{plugin.repo()}/issues?labels={label}', _get="all")
    for issue in repo_issues:
        # pull requests are also an issue according to the gh api
        if "pull_request" not in issue:
            issues.append(
                {"title": issue['title'], "url": issue['html_url'], "pluginID": plugin.id(), "plugin": plugin.name()})
    return issues


def process_issues(api_key: str, overwrite: bool = True, verbose: bool = False) -> None:
    plugin_list = get_community_plugins()
    client = GitHubAPI(bearer_token=api_key)
    rate_limit = client.get('/rate_limit')['resources']['core']['remaining']
    if rate_limit < len(plugin_list) * 3:
        print("will hit the rate limit: aborting")
        quit(1)
        return
    print("-----\nProcessing plugin issues....\n")
    template = get_template("plugin_issues")

    documentation = list()
    help_wanted = list()
    good_first_issue = list()
    print_progress_bar(
        0, len(plugin_list),
    )
    for plugin in plugin_list:
        documentation.extend(process_issues_for_plugin(client, plugin, "documentation"))
        help_wanted.extend(process_issues_for_plugin(client, plugin, "help wanted"))
        good_first_issue.extend(process_issues_for_plugin(client, plugin, "good first issue"))

        print_progress_bar(
            plugin_list.index(plugin) + 1, len(plugin_list),
        )
    sorted_help_wanted = sorted(help_wanted, key=lambda issue: issue['plugin'])
    sorted_documentation = sorted(documentation, key=lambda issue: issue['plugin'])
    sorted_good_first_issue = sorted(good_first_issue, key=lambda issue: issue['plugin'])
    args = {
        "help_wanted": sorted_help_wanted,
        "documentation": sorted_documentation,
        "good_first_issue": sorted_good_first_issue
    }
    write_template_file(template, "Plugins seeking help", overwrite=overwrite, verbose=verbose, **args)


def main(argv: Sequence[str] = sys.argv[1:]) -> None:
    parser = argparse.ArgumentParser(
        description="Update Plugin Issues"
    )
    parser.add_argument("--apikey", action="store", default=False, required=True)

    args = parser.parse_args(argv)
    process_issues(args.apikey)


if __name__ == "__main__":
    main()
