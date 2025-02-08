def find_maximum(numbers):
    if not numbers:
        return None  

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num