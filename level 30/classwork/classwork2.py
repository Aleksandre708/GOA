def manual_find(main_string, str_to_find):
    for i in range(len(main_string) - len(str_to_find) + 1):
        if main_string[i:i+len(str_to_find)] == str_to_find:
            return i
    return -1

# მაგალითი გამოყენება:
main_string = "გამარჯობა, ეს არის სატესტო სტრინგი"
str_to_find = "სატესტო"
print(manual_find(main_string, str_to_find))  # დააბრუნებს 17

str_to_find = "არარსებული"
print(manual_find(main_string, str_to_find))  # დააბრუნებს -1