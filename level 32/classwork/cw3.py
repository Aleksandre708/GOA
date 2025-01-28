def manual_append(main_list, item_to_insert):
    main_list.insert(len(main_list), item_to_insert)

# მაგალითი გამოყენების
my_list = [1, 2, 3, 4]
manual_append(my_list, 5)
print(my_list)  # შედეგი: [1, 2, 3, 4, 5]
