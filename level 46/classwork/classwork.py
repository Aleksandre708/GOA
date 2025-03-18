def manual_list(start, end, step, user_num):
    result = [num for num in range(start, end, step) if num > user_num]
    return result

print(manual_list(1, 20, 2, 10)) 
print(manual_list(5, 50, 5, 25)) 
print(manual_list(-10, 10, 3, 0)) 
