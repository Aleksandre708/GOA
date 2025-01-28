def replace_spaces_with_underscores(input_string):
    """
    Replaces all spaces in a given string with underscores.

    Parameters:
    input_string (str): The string to modify

    Returns:
    str: The modified string with spaces replaced by underscores
    """
    return inputstring.replace(" ", "")

# Example usage
example_string = "Hello world! Python programming is fun."
modified_string = replace_spaces_with_underscores(example_string)
print("Modified String:", modified_string)
