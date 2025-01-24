for i in range(20):
    print("sandro")


num1 = int(input("პირველი რიცხვი: "))
num2 = int(input("მეორე რიცხვი: "))

for i in range(num1, num2 + 1):
    print(i, "^2 =", i ** 2)


num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

for i in range(num1, num2 + 1):
    print("საიტერაციო ცვლადის კვადრატი:", i ** 2)
    print("სტ. ცვლადი + პირველი რიცხვი:", i + num1)
    print("სტ. ცვლადი + მეორე რიცხვი:", i + num2)
    print("სტ. ცვლადი * პირველი რიცხვი:", i * num1)
    print("სტ. ცვლადი * მეორე რიცხვი:", i * num2)
    

num1, num2 = 2, 3
print(num1)
print(num2)


n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print("The square of", i, "is", i ** 2)