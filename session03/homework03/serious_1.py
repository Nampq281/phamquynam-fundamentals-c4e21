items = ["T-shirt", "Sweater"]
while True:
    command = input("Welcome to our shop, what do you want (C, R, U, D)? ").upper()
    if command =="R":
        print("Our items: ", ", ".join(items))

    elif command =="C":
        new_item = input("Enter new item ")
        items.append(new_item)
        print("Our items: ", ", ".join(items))

    elif command =="U":
        position = int(input("Update position? "))
        if 1 <=position <= len(items):
            new_item = input("New item? ")
            items[position-1] = new_item
            print("Our items: ", ", ".join(items))
        else:
            print("invalid")

    elif command =="D":
        delete = int(input("Delete position?"))
        if 1 <= delete <= len(items):
            items.pop(delete-1)
            print("Our items: ", ", ".join(items))
        else:
            print("invalid")

    else:
        print("invalid")
        