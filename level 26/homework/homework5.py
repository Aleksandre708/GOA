def find_maximum(numbers):
    # ინიციალიზაცია პირველ ელემენტზე
    max_value = numbers[0]

# for ციკლის გამოყენება სიის შემოწმებისათვის
    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value

# ფუნქციის გამოძახება და შედეგის დაბეჭდვა
my_list = [12, 45, 67, 23, 89, 4]
max_value = find_maximum(my_list)
print(f"მაქსიმალური მნიშვნელობა სიაა: {max_value}")
