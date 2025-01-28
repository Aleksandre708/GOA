def find_python_position(sentence):
    """
    Finds the position of the first occurrence of the word 'Python' in a sentence.

    Parameters:
    sentence (str): The sentence to search in

    Returns:
    int: The position of the first occurrence of 'Python', or -1 if not found
    """
    return sentence.find("Python")

# Example usage
sentence = "I love learning Python programming!"
position = find_python_position(sentence)
print("Position of 'Python':", position)
