text = str(input("Input a sentence: ")).lower()
text = text.replace(" ","")
letter_counts = {}

for letter in list(text):
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

for (i, j) in sorted(letter_counts.items()):
    print(i, j)
    

