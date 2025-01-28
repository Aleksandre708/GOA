name = input("შეიყვანეთ სახელი: ")
choice = input("შეიყვანეთ არჩევანი ('u' ან 'l'): ")

if choice == 'u':
    print(name.upper())
elif choice == 'l':
    print(name.lower())
else:
    print("wrong information")