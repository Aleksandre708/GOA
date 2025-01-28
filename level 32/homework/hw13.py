def insert_at_index(lst, index, item):
    # Use the insert method to add the item at the specified index
    lst.insert(index, item)
    return lst

# Example usage:
my_list = [1, 2, 3, 5]
index = 3
new_item = 4
print(insert_at_index(my_list, index, new_item))  # Output: [1, 2, 3, 4, 5]