# 8) Prompt the user to enter a password. Keep asking until they enter the correct password.

password = "ბესო_შავია"

input1 = "dfj9idsaj9idjs9iadujs9i8d9jeai"

while input1 != password:
    input1 = input("შემეიყვანე პაროლი> ")
    if input1 == password:
        print("სწორია!")
    else:
        print("არასწორია!")