abbr = {
    "lol" : "laugh out loud",
    "asap" : "as soon as possible",
    "mia" : "missing in action",
    "kia" : "killed in action",
    "ufo" : "unidentified flying object",
}
while True:    
    term = input("Your term: ")
    if term in abbr:
        print(term, "means", abbr[term])
    else:
        print("not a valid word")
        create = input("Do you want to add this word? Y/N ").upper()
        if create == "Y":
            new_key = term
            new_value = input("Input definition ")
            abbr[new_key] = new_value
            print("added")
        else:
            print()
    print()

    
