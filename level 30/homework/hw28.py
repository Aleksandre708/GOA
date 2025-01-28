def swap_case(sentence):
    """
    Takes a sentence and returns it with swapped case for each letter.

    Parameters:
    sentence (str): The sentence to modify

    Returns:
    str: The modified sentence with swapped cases
    """
    return sentence.swapcase()

# Example usage
sentence = "Hello World! Python Programming is FUN."
swapped_sentence = swap_case(sentence)
print("Swapped Case Sentence:", swapped_sentence)
