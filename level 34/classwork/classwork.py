# საკლასო დავალება:

# შექმენით ფუნქცია რომელიც მიიღებს ორ პარამეტრს - main_list, indexes_list.

# თქვენი დავალებაა, რომ indexes_list სიაში რა ინდექსებიც
# იქნება მოცემული, მთავარ სიაში, მაგ ინდექსებზე წაშალოთ ელემენტები

def remove_elements_by_indexes(main_list, indexes_list):
    # პირველ რიგში, სიის ინდექსები უნდა დავყოთ პრდობით
    indexes_list.sort(reverse=True)  # რიცხვები კლებადობით იმისთვის, რომ ჩვენ მიერ წაშლილი ელემენტები არ გადაფარონ ერთმეორეს
    for index in indexes_list:
        if 0 <= index < len(main_list):  # დავამოწმოთ რომ ინდექსი არ იყოს არასაკმარისი
            del main_list[index]  # წაშლას დავაპირებთ
    return main_list 