def manual_index(main_string, search_string):
    main_len = len(main_string)
    search_len = len(search_string)

    for i in range(main_len - search_len + 1):
        if main_string[i:i + search_len] == search_string:
            return i
    return -1