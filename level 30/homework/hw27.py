def swap_case(input_string):
    """
    Converts a string such that uppercase letters become lowercase and vice versa.

    Parameters:
    input_string (str): The string to modify

    Returns:
    str: The modified string with swapped cases
    """
    return input_string.swapcase()

# Example usage
example_string = "Hello World! Python Programming is FUN."
swapped_string = swap_case(example_string)
print("Swapped Case String:", swapped_string)
