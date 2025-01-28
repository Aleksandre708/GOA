def is_lowercase(input_string):
    """
    Checks if the input string is completely in lowercase.

    Parameters:
    input_string (str): The string to check

    Returns:
    bool: True if the string is completely in lowercase, otherwise False
    """
    return input_string.islower()

# Example usage
example_string = "hello world"
result = is_lowercase(example_string)
print(f"Is the string '{example_string}' completely in lowercase? {result} 