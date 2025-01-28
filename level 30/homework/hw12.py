def find_char_index(main_string, char):
    """
    Finds the index of a specified character in a given string.

    Parameters:
    main_string (str): The string to search in
    char (str): The character to search for

    Returns:
    int: The index of the specified character, or -1 if not found
    """
    return main_string.find(char)

# Example usage
main_string = "Hello World!"
char = "W"
index = find_char_index(main_string, char)
print(f"Index of '{char}':", index)
