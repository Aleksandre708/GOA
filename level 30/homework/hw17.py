def count_word_occurrences(text, word):
    """
    Counts the occurrences of a specified word in a given text.

    Parameters:
    text (str): The text to search in
    word (str): The word to count

    Returns:
    int: The number of times the word appears in the text
    """
    # Convert the text to lowercase to ensure case-insensitive matching
    text_lower = text.lower()

    # Split the text into words
    words = text_lower.split()

    # Count the occurrences of the specified word
    count = words.count(word.lower())

    return count

# Example usage
text = "The quick brown fox jumps over the lazy dog. The dog was not amused by the fox."
word = "the"
occurrences = count_word_occurrences(text, word)
print(f"Number of occurrences of '{word}':", occurrences)