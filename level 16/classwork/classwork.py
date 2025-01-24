# საკლასო დავალება: მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში მთელი რიცხვის სახით.

# შემდეგ შექმენით დიაპაზონი 0-დან ამ რიცხვამდე და დაბეჭდეთ დიაპაზონის ყველა რიცხვის ჯამი.

# გამოიყენეთ for ციკლი

# num = int(input("Enter a number: "))
# total = 0
# for i in range(num + 1):
#     total += i
# print( "is:", total)


# საკლასო დავალება: 

# შექმენით correct_password ცვლადი და მასში შეინახეთ ნებისმიერი სთრინგი.

# სანამ მომხმარებლის შემოტანილი პაროლი არ იქნება correct_password-ის ტოლი, თავიდან შეეკითხეთ.

# საბოლოოდ, დაუბეჭდეთ access granted და ასევე რამდენჯერ მოუწია პაროლის შემოტანა.

# დაგჭირდებათ while loop, counter variable


# correct_password = 12
# me = int(input())
# if me != correct_password:
#     print("try again")
# else: 
    # print("that a correct!")


# საკლასო დავალება:

# რიცხვის გამოცნობის პროგრამა:

# შექმენით my_num ცვლადი და 1-დან 10-მდე ნებისმიერი რიცხვი მიანიჭეთ მნიშვნელობად.

# სანამ მომხმარებლის შემოტანილი რიცხვი არ იქნება my_num-ის ტოლი, ისევ შეეკითხეთ მომხმარებელს ეს რიცხვი.

# საბოლოოდ დაუბეჭდეთ "you guessed" და რამდენი ცდა დაჭირდა



my_num = 5
guess = int(input('guess my number!'))
counter = 0

while guess != my_num:
    uess = int(input('guess my number!'))
counter += 1

print("correct")
print("Your guess count:", str(counter))