def find_hello_index(text):
    """
    Finds and prints the index of the first occurrence of the word 'hello' in a given string.

    Parameters:
    text (str): The string to search in

    Returns:
    int: The index of the first occurrence of 'hello', or -1 if not found
    """
    # Convert the text to lowercase to ensure case-insensitive matching
    text_lower = text.lower()

    # Find the index of the first occurrence of 'hello'
    index = text_lower.find("hello")

    return index

# Example usage
text = "Hello there! How are you? hello world!"
index = find_hello_index(text)
print("Index of the first occurrence of 'hello':", index)