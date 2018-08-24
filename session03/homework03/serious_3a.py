from random import randint, choice
word = "champion"
chars = list(word)
for i in range(len(chars)):
    i = choice(chars)
    print(i, end= " " )
    chars.remove(i)
print()
answer = input("Your answer: ")
if answer == word:
    print("Congratulation, you are correct")
else:
    print("Try again :(")




