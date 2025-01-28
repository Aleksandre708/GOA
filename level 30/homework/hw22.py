def is_all_uppercase(input_string):
    """
    Checks if all characters in a given string are uppercase.

    Parameters:
    input_string (str): The string to check

    Returns:
    bool: True if all characters are uppercase, False otherwise
    """
    return input_string.isupper()

# Prompt the user for a string
user_input = input("Please enter a string: ")

# Verify if the string contains only uppercase letters
result = is_all_uppercase(user_input)
print("The string contains only uppercase letters:", result)
