def get_string_lengths(string_list):
    """
    Returns the lengths of each string in the provided list.

    Parameters:
    string_list (list): A list of strings

    Returns:
    list: A list of lengths corresponding to each string in the input list
    """
    # Get the length of each string in the list
    lengths = [len(string) for string in string_list]
    return lengths

# Example usage
strings = ["hello", "world", "python", "programming"]
lengths = get_string_lengths(strings)
print("Lengths of strings:", lengths)
