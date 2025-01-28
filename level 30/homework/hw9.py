def capitalize_first_letter(input_string):
    """
    Capitalizes the first letter of a given string.

    Parameters:
    input_string (str): The string to be capitalized

    Returns:
    str: The string with the first letter capitalized
    """
    return input_string.capitalize()

# Example usage
input_string = "hello world! python programming."
capitalized_string = capitalize_first_letter(input_string)
print("Capitalized String:", capitalized_string)
