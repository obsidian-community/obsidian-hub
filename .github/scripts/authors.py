def adjust_author(extension):
    """
    
    :param extension: 
    :return: 
    """
    # extension is a dict - either a plugin or a theme
    author = extension['author']
    substitutions = {
        "Andrew Brown & Tim Hor": "Tim Hor",
        "Chetachi": "Chetachi E.",
        "ryanjamurphy": "Ryan J. A. Murphy"
    }
    if author in substitutions:
        extension.update(author=substitutions[author])
