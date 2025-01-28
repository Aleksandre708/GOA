# Function to check if all characters in a string are lowercase
def is_all_lowercase(input_string):
    """
    Checks if all characters in a given string are lowercase.

    Parameters:
    input_string (str): The string to check

    Returns:
    bool: True if all characters are lowercase, False otherwise
    """
    return input_string.islower()

# Prompt the user for a string
user_input = input("Please enter a string: ")

# Verify if the string contains only lowercase letters
result = is_all_lowercase(user_input)
print("The string contains only lowercase letters:", result)