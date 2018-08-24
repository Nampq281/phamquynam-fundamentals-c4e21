favs = ['netflix','teaching', 'swimming']
for i, item in enumerate(favs):
    print(i+1, item)


while True: 
    command  = input("What do you want (C, R, U, D)? ").upper()
    if command == "C":
        add = input("You want to add: ")
        favs.append(add)
        for i, item in enumerate(favs):
            print(i+1, item)

    elif command == "R":
        for i, item in enumerate(favs):
            print(i+1, item)

    elif command == "U":
        item_no = int(input("Position to update"))
        if 1>item_no>3:
            update = input("Replacing item")
            favs[item_no-1] = update
            for i, item in enumerate(favs):
                print(i+1, item)   
        else:
            print("invalid")

    elif command == "D":
        delete = int(input("Favorite position to delete?"))
        if 1>item_no>3:
            favs.pop(delete-1)
            for i, item in enumerate(favs):
                print(i+1, item)  
        else:
            print("invalid")


    else:
        print("invalid")

