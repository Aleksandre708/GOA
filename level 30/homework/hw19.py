def find_char_index(main_string, char):
    """
    Returns the index of a specified character in a given string.

    Parameters:
    main_string (str): The string to search in
    char (str): The character to find

    Returns:
    int: The index of the specified character, or -1 if not found
    """
    return main_string.find(char)

# Example usage
main_string = "The quick brown fox jumps over the lazy dog."

# Ask the user for a character
user_char = input("Please enter a character: ")

# Find the index of the user-specified character
index = find_char_index(main_string, user_char)
print(f"Index of '{user_char}' in the string:", index)
