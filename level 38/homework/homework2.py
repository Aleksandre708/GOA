my_tuple = (1, 2, 3, 4, 5)
try:
    my_tuple[1] = 10 
except TypeError as e:
    print("Error:", e)