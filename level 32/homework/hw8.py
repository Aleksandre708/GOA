def parse_csv(csv_string):
    # Split the CSV string by commas
    items = csv_string.split(',')
    # Remove any leading or trailing whitespace from each item
    items = [item.strip() for item in items]
    return items

# Example usage:
csv_string = "apple, banana, cherry, date"
print(parse_csv(csv_string))  # Output: ['apple', 'banana', 'cherry', 'date']