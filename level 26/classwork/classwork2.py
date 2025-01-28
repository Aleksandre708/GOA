def manual_range(start, end, step):
    range_list = []
    current = start
    while current <= end:
        range_list.append(current)
        current += step

    for num in range_list:
        if num % 2 == 0:
            print(num)

# ფუნქციის გამოძახება რამდენიმე არგუმენტით
manual_range(1, 20, 2)
manual_range(2, 15, 3)
manual_range(10, 50, 5)
manual_range(0, 30, 4)
manual_range(5, 25, 1)