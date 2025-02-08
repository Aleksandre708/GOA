
def remove_one_element(main_list, index):
    # შევამოწმოთ, არის თუ არა ინდექსი ვალიდური
    if 0 <= index < len(main_list):
        del main_list[index]  # ამოშლის შესაბამის ელემენტს
        print(main_list)  # დაბეჭდავს განახლებული სია
    else:
        print("Invalid 2")  # თუ ინდექსი არ არის ვალიდური, დაბეჭდავს შეტყობინებას