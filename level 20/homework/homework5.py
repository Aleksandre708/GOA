number = int(input("Enter a number: "))
if number <= 1:
    print("number is not a prime number.")
else:
    for i in range(2, number):
        if number % i == 0:
            print("number is not a prime number.")
    else:
        print("number is a prime number.")