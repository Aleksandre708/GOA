try:
    name = input("გთხოვთ შეიყვანოთ თქვენი სახელი: ")
    
    # მარტივი შემოწმება, რომ არ იყოს ცარიელი
    if not name.strip():
        raise ValueError("სახელი არ შეიძლება იყოს ცარიელი!")

    print("მოგესალმებით,", name)

except ValueError as ve:
    print("შეცდომა:", ve)

except Exception as e:
    print("დაფიქსირდა გაუთვალისწინებელი შეცდომა:", e)