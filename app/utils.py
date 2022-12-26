def camelize(string: str) -> str:
    """
    Convert a string from snake_case to camelCase
    """
    words = string.split("_")
    return words[0] + "".join([word.title() for word in words[1:]])
