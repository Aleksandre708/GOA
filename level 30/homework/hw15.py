def count_the_occurrences(paragraph):
    """
    Counts the number of times the word 'the' appears in a given paragraph.

    Parameters:
    paragraph (str): The paragraph to search in

    Returns:
    int: The number of times 'the' appears in the paragraph
    """
    # Convert the paragraph to lowercase to ensure case-insensitive matching
    paragraph_lower = paragraph.lower()

# Split the paragraph into words
    words = paragraph_lower.split()

# Count the occurrences of 'the'
    count = words.count("the")

    return count

# Example usage
paragraph = "The quick brown fox jumps over the lazy dog. The dog was not amused."
the_count = count_the_occurrences(paragraph)
print("Number of occurrences of 'the':", the_count)
