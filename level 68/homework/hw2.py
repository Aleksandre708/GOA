# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check voting eligibility
if age >= 18:
    print("You can vote!")
else:
    print("You are not eligible to vote.")
