# Function to count the occurrences of a character in a string
def count_char_occurrences(main_string, char):
    """
    Counts the occurrences of a specified character in a given string.

    Parameters:
    main_string (str): The string to search in
    char (str): The character to count

    Returns:
    int: The number of times the character appears in the string
    """
    return main_string.count(char)

# Example usage
# Ask the user for a character
user_char = input("Please enter a character: ")

# Provide a sample string
sample_string = "The quick brown fox jumps over the lazy dog."

# Count the occurrences of the user-specified character
occurrences = count_char_occurrences(sample_string, user_char)
print(f"Number of occurrences of '{user_char}' in the string:", occurrences)
