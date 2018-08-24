print("Hi there, here are your fav things so far")
print("*"*50)
fav_items = ["deathnote", "Netflix", "teaching"]
for index, item in enumerate(fav_items):
    print(index+1,". ", item, sep= "")
print("*"*50)

delete = input("Favorite item to get rid of? ")
if delete in fav_items:
    fav_items.remove(delete)
else:
    print("invalid")
print("*"*50)

for index, item in enumerate(fav_items):
    print(index+1,". ", item, sep= "")