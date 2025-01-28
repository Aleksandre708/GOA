def my_split(main_string, string_to_split):
    result = main_string.split(string_to_split)
    print(result)

# მომხმარებელს შემოატანინეთ მთავარი და დასაყოფი სტრინგები
main_string = input("შეიყვანეთ მთავარი სტრინგი: ")
string_to_split = input("შეიყვანეთ დასაყოფი სტრინგი: ")

# ფუნქციის გამოძახება
my_split(main_string, string_to_split)