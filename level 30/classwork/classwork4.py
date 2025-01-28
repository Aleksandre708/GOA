#მომხმარებლისგან შემოტანა
main_str = input("შეიტანეთ მთავარი სთრინგი: ")
str_to_count = input("შეიტანეთ დასათვლელი სთრინგი: ")

#სთრინგის დათვლა
count = main_str.count(str_to_count)

#შედეგის დაბეჭდვა
print(f"'{str_to_count}' სთრინგი შეგხვდა {count} ჯერ '{main_str}' სთრინგში")