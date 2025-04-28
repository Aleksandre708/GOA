# 1. შევქმნათ ცვლადი სადაც ინახება ინტეჯერი
number = 10

# 2. ვცადოთ ისეთი ოპერაცია, რომელიც გამოიწვევს TypeError-ს
try:
    result = number + "5"  # ეს გამოიწვევს TypeError-ს, რადგან int და str არ შეგიძლიათ დაამატოთ
except TypeError as e:
    print("მოხდა TypeError:", e)