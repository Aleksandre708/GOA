def factorial(n):
    # 0-ის და 1-ის ფაქტორიალი არის 1
    if n == 0 or n == 1:
        return 1
    else:
        # რეგურსიული გამოძახება
        return n * factorial(n - 1)

# ფუნქციის გამოძახება და შედეგის დაბეჭდვა
result = factorial(5)
print(f"რიცხვის 5 ფაქტორიალი არის: {result}")