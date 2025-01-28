def is_all_uppercase(input_string):
    """
    Checks if the input string consists entirely of uppercase letters.

    Parameters:
    input_string (str): The string to check

    Returns:
    bool: True if the string is entirely uppercase, otherwise False
    """
    return input_string.isupper()

# Example usage
example_string = "HELLO WORLD"
result = is_all_uppercase(example_string)
print(f"Is the string '{example_string}' entirely uppercase? {result}")
