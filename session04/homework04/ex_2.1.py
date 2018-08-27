#1
price_list = {"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
stock_list = {"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
item_list = list(price_list)
details = {}
for fruit in item_list:
    price = price_list[fruit]
    stock = stock_list[fruit]
    details[fruit] = {'price: ': price, 'stock: ': stock}

for x in details:
    print(x)
    for y in details[x]:
        print (y, ':', details[x][y])

