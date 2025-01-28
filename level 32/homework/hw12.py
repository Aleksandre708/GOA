def extend_list(list1, list2):
    # Use the extend method to append all elements of list2 to list1
    list1.extend(list2)
    return list1

# Example usage:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(extend_list(list1, list2))  # Output: [1, 2, 3, 4, 5, 6]
