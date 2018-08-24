print ("Hi there, favorite things so far")
print("*"*50)
fav_items = ["death note", "Netflix", "teaching"]
# fav_index = len(fav_items)+1
for index, item in enumerate(fav_items):
    print(index+1,". ", item, sep="")
print("*"*50)

item_no = int(input("Position you want to update? "))
if 1>item_no>3:
    item_r = input("Your replacing favorite ")
    print("*"*50)

    fav_items[item_no-1] = item_r
    for index, item in enumerate(fav_items):
        print(index+1,". ", item, sep="")
    print("*"*50)
else:
    print("invalid")
