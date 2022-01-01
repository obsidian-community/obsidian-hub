from typing import Dict


def adjust_author(plugin: Dict[str, str]) -> None:
    """
    
    :param plugin: 
    :return: 
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
