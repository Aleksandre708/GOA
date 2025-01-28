def format_name(first_name, last_name):
    # Capitalizing the first and last names
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()

# Formatting into a single string
    return f"{first_name} {last_name}"

# Example usage
name = format_name("john", "doe")
print(name)  # Output: "John Doe"