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
total = 0
total_price = {}
for pr in item_list:
    price = price_list[pr]
    stock = stock_list[pr]
    total_price[pr] = price * stock
    total += total_price[pr]
    
print(total_price)
print(total)