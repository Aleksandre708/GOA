try:
    user_input = input("გთხოვთ შეიყვანოთ რიცხვი: ")
    number = float(user_input)  # ვცდილობთ გადავაქციოთ რიცხვად (float ან int)
    print("თქვენი რიცხვია:", number)

except ValueError:
    print("შეცდომა: გთხოვთ შეიყვანოთ მხოლოდ რიცხვი!")