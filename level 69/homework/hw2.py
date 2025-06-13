# Take a score as input from the user
score = int(input("Enter the score: "))

# Assign grade based on the score
if score >= 90:
    grade = "Grade A"
elif score >= 80:
    grade = "Grade B"
elif score >= 70:
    grade = "Grade C"
elif score >= 60:
    grade = "Grade D"
else:
    grade = "Fail"

# Display the result
print(f"The grade is: {grade}")
