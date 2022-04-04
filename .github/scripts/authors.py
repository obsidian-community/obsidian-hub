from typing import Dict, Any

AllAuthorsStorage = Dict[str, Dict[str, Any]]


class AllAuthors(AllAuthorsStorage):
    ...


def update_author_name_for_manual_exceptions(plugin: Dict[str, str]) -> None:
    """
    If the author name would require a manual edit by hub maintainers,
    we update it here to save human time.

    A few of the notes for authors of plugins have manually-adjusted
    names, that are not represented in either the community plugins list
    or the plugin's manifest file.
    
    These automated edits used to be reverted manually, by people running
    update-releases.py. This function removes the need to know to do that.
    
    :param plugin: A dict() with the plugins properties, from both the community
                   plugins list and the plugin's own manifest.
    :return: None
    """
    # extension is a dict - either a plugin or a theme
    author = plugin['author']
    substitutions = {
        "Andrew Brown & Tim Hor": "Tim Hor",
        "Chetachi": "Chetachi E.",
        "ryanjamurphy": "Ryan J. A. Murphy"
    }
    if author in substitutions:
        plugin.update(author=substitutions[author])
