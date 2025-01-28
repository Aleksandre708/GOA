def append_list_of_items(lst, items):
    # Iterate through the items list and append each item to the original list
    for item in items:
        lst.append(item)
    return lst

# Example usage:
my_list = [1, 2, 3]
new_items = [4, 5, 6]
print(append_list_of_items(my_list, new_items))  # Output: [1, 2, 3, 4, 5, 6]