def insert_word(sentence, word, index):
    # Splitting the sentence into two parts
    before_index = sentence[:index]
    after_index = sentence[index:]

# Inserting the word in the given index
    new_sentence = before_index + word + after_index

    return new_sentence

# Example usage
result = insert_word("Hello, world!", "beautiful ", 7)
print(result)  # Output: "Hello, beautiful world!"
