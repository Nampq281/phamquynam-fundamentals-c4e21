#phần hàm
def caculate(x, y ,op):  
    result = 0
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        if y == 0:
            pass
        else:
            result = x / y

    return result #đưa result ra ngoài scope của def

# #phần test   
# a = int(input('a= '))
# op = input("(+, -, *, /): ")
# b = int(input('b= '))
# r = caculate(a, b, op) #cho result lưu lại vào r
# print(r)
