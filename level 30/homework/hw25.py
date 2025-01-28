def replace_dog_with_cat(sentence):
    """
    Replaces all occurrences of the word 'dog' with 'cat' in the given sentence.

    Parameters:
    sentence (str): The sentence to modify

    Returns:
    str: The modified sentence with 'dog' replaced by 'cat'
    """
    return sentence.replace("dog", "cat")

# Example usage
sentence = "The quick brown dog jumps over the lazy dog."
modified_sentence = replace_dog_with_cat(sentence)
print("Modified Sentence:", modified_sentence)