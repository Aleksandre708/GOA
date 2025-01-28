def reverse_and_format(sentence):
    # Reversing the provided string
    reversed_string = sentence[::-1]

# Formatting into a sentence
    return f"The reversed string is: {reversed_string}"

# Example usage
result = reverse_and_format("Hello, world!")
print(result)  # Output: "The reversed string is: !dlrow ,olleH"