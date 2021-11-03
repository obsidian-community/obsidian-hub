#!/usr/bin/env python3

import csv
from utils import get_template, write_file, get_json_from_github, PLUGINS_JSON_FILE

CATEGORY_FILE = "Categories_2021-09-21.csv"
PLUGINS_FILE = "Plugins-Categorized_2021-09-21.csv"


def create_categories_from_csv():
    template = get_template("category")

    released_plugins = get_json_from_github(PLUGINS_JSON_FILE)
    plugin_dict = {p.get("name"): p for p in released_plugins}

    with open(CATEGORY_FILE, "r") as csv_file:
        reader = csv.reader(csv_file)

        # Skip headers
        next(reader)

        for row in reader:
            cat, desc, plugins, _, _ = row
            if not desc:
                desc = "#placeholder/description"

            plugin_list = list()
            for plugin in plugins.split(","):
                plugin_info = plugin_dict.get(plugin)
                plugin_list.append(dict(id=plugin_info.get("id"), name=plugin))

            write_file(
                template,
                cat,
                name=cat,
                description=desc,
                related=True,
                plugins=plugin_list,
            )


def main():
    create_categories_from_csv()


if __name__ == "__main__":
    main()
