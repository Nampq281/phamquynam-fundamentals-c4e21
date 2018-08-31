# person = ["Quan", 20, "Hanoi","Thang Long"]
# print(person)
# person = {

# }
# print(person)

# person = {
#     "name": "Quan"
# }
# print(person)

person = {
    "name":"Quan",
    "age":20,
    "city":"Hanoi",
}

# person["status"] = "complicated"
# print(person)
# del person["age"]
# print (person)

# for k in person.keys():
#     print(x)
# for v in person.values():
#     print(v)

for k, v in person.items():
    print(k, ":", v)