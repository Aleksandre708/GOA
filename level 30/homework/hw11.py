def find_substring_index(main_string, substring):
    """
    Finds the starting index of a user-specified substring in a provided string.

    Parameters:
    main_string (str): The string to search in
    substring (str): The substring to search for

    Returns:
    int: The starting index of the substring, or -1 if not found
    """
    return main_string.find(substring)

# Example usage
main_string = "I love learning Python programming!"
substring = "Python"
index = find_substring_index(main_string, substring)
print(f"Starting index of '{substring}':", index)
