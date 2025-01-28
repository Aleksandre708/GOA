def insert_at_end(lst, item):
    # Insert the item at the end using the length of the list as the index
    lst.insert(len(lst), item)
    return lst

# Example usage:
my_list = [1, 2, 3]
new_item = 4
print(insert_at_end(my_list, new_item))  # Output: [1, 2, 3, 4]