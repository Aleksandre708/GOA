def split_paragraph(paragraph):
    # Split the paragraph by periods and strip any trailing whitespace from each sentence
    sentences = [sentence.strip() for sentence in paragraph.split('.')]
    # Remove any empty sentences resulting from trailing periods
    sentences = [sentence for sentence in sentences if sentence]
    return sentences

# Example usage:
paragraph = "This is the first sentence. Here is another one. And the final one."
print(split_paragraph(paragraph))  # Output: ['This is the first sentence', 'Here is another one', 'And the final one']