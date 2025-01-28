def convert_to_uppercase(string_list):
    """
    Converts a list of lowercase strings to uppercase.

    Parameters:
    string_list (list): A list of lowercase strings

    Returns:
    list: A list of uppercase strings
    """
    # Convert each string in the list to uppercase
    uppercase_list = [s.upper() for s in string_list]
    return uppercase_list

# Example usage
lowercase_strings = ["hello", "world", "python", "programming"]
uppercase_strings = convert_to_uppercase(lowercase_strings)
print("Uppercase Strings:", uppercase_strings)
