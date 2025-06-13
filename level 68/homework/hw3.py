# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Compare the two numbers
if num1 > num2:
    print("The first number is larger.")
elif num2 > num1:
    print("The second number is larger.")
else:
    print("Both numbers are equal.")
