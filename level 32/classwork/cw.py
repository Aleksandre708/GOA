def generate_big_sentence(name, surname, age):
    return "სახელი: {}, გვარი: {}, ასაკი: {}".format(name, surname, age)

# შემოვიტანოთ მომხმარებლის მიერ შეტანილი ინფორმაცია
name = input("გთხოვთ შეიყვანეთ სახელი: ")
surname = input("გთხოვთ შეიყვანეთ გვარი: ")
age = input("გთხოვთ შეიყვანეთ ასაკი: ")

# ფუნქციის გამოძახება არგუმენტებით
result = generate_big_sentence(name, surname, age)
print(result)
