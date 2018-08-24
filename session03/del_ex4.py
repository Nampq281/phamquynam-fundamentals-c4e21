print("Hi there, here are your fav things so far")
print("*"*50)
fav_items = ["deathnote", "Netflix", "teaching"]
for index, item in enumerate(fav_items):
    print(index+1,". ",item, sep="")
print("*"*50)

delete = int(input("Favorite position you want to get rid of?"))
fav_items.pop(delete-1)
for index, item in enumerate(fav_items):
    print(index+1,". ",item, sep="")
