# შექმენით სია 10 ელემენტით
items = ["გიტარა", "ფლეიტა", "დრამი", "საქსოფონი", "ვიოლინო", "ბასი", "ჩელო", "თრუმპეტი", "კლავირი", "მანდოლინი"]

# შემოატანინეთ num1 და num2 მომხმარებლებს
num1 = int(input("შეიყვანეთ num1 ინდექსი: "))
num2 = int(input("შეიყვანეთ num2 ინდექსი: "))

# შეამოწმეთ პირობები და სიის slices
if num1 > num2:
    sliced_list = items[num2:num1+1]
elif num2 > num1:
    sliced_list = items[num1:num2+1]
else:
    sliced_list = []

# დაბეჭდეთ ახალი სია
print("ახალი სია:", sliced_list)
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
