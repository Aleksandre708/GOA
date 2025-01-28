def insert_at_beginning(lst, item):
    # Insert the item at the beginning, which is index 0
    lst.insert(0, item)
    return lst

# Example usage:
my_list = [2, 3, 4]
new_item = 1
print(insert_at_beginning(my_list, new_item))  # Output: [1, 2, 3, 4]