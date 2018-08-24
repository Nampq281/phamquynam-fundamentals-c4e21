from random import randint, choice
word_list = ["meticulous", "champion", "hexagon"]
chosen_w = choice(word_list)
chars = list(chosen_w)
for i in range(len(chars)):
    i = choice(chars)
    chars.remove(i)
    print(i, end=" ")
print()
answer = input("Your answer is: ")
if answer == chosen_w:
    print("You are correct")
else:
    print(":( try again")
