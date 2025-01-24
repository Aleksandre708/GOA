a = 10
b = 5
c = 15
d = True
e = False

print((a > b) and (c > a))  # True და True -> True
print((a < b) or (d and (c == 15)))  # False ან (True და True) -> True
print((a == 10) and not e)  # True და არა False -> True
print((b != 5) or (d and (c > b)))  # False ან (True და True) -> True
print(not (a > c) or (b < c))  # True ან True -> True
print((d or e) and (b <= a))  # True და True -> True
print((c - a == b) and (a * 2 > c))  # True და False -> False
print((a / b > 1) or (e and d))  # True ან (False და True) -> True
print((a == 10) and (not (c < 15)))  # True და False -> False
print(((b * 3) == c) and (e or (d == True)))  # True და (False ან True) -> True