def is_uppercase(input_string):
    """
    Checks if the input string is in uppercase.

    Parameters:
    input_string (str): The string to check

    Returns:
    bool: True if the string is in uppercase, otherwise False
    """
    return input_string.isupper()

# Prompt the user for a string
user_input = input("Please enter a string: ")

# Check if the string is in uppercase and display the result
if is_uppercase(user_input):
    print("The string is in uppercase.")
else:
    print("The string is not in uppercase.")
