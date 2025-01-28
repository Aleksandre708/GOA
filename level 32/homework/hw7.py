def get_words(sentence):
    # Split the sentence by spaces to extract the words
    words = sentence.split()
    return words

# Example usage:
sentence = "Write a function that takes a sentence and returns a list of words."
print(get_words(sentence))  # Output: ['Write', 'a', 'function', 'that', 'takes', 'a', 'sentence', 'and', 'returns', 'a', 'list', 'of', 'words.']