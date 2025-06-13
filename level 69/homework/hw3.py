# Take three numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest number
if num1 == num2 == num3:
    print("All three numbers are equal.")
elif num1 >= num2 and num1 >= num3:
    if num1 == num2 or num1 == num3:
        print(f"The largest number is {num1}, and it appears more than once.")
    else:
        print(f"The largest number is {num1}.")
elif num2 >= num1 and num2 >= num3:
    if num2 == num1 or num2 == num3:
        print(f"The largest number is {num2}, and it appears more than once.")
    else:
        print(f"The largest number is {num2}.")
else:
    if num3 == num1 or num3 == num2:
        print(f"The largest number is {num3}, and it appears more than once.")
    else:
        print(f"The largest number is {num3}.")
