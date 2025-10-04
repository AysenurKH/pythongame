"""A small `pdoc` example."""

print("Hello there")


def get_random_ingredients3(kind: str = "No cheese at all") -> list[str]:
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    return ["shells", "gorgonzola", "parsley", kind]
