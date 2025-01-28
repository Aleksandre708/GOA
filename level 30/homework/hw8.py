def to_lowercase(mixed_case_string):
    """
    Converts a mixed-case string to all lowercase letters.

    Parameters:
    mixed_case_string (str): The string with mixed case letters

    Returns:
    str: The string in all lowercase letters
    """
    return mixed_case_string.lower()

# Example usage
mixed_case_string = "Hello WoRLd! PyTHon ProGRamMinG."
lowercase_string = to_lowercase(mixed_case_string)
print("Lowercase String:", lowercase_string)
