from random import randint, choice
from calc import caculate

while True:
# generate the math
    x = randint(0, 9)
    y = randint(0, 9)
    op = choice(['+', '-', '*', '/'])
    z = randint(-1, 1)
    r = caculate(x, y, op)      
    print(x, op, y, '=', r+z)
# compare user_answer to solution
    user_answer = input('Y/N ').lower()
    if caculate(x, y, op) ==r:
        if user_answer == 'y':
            print('+1 point')
        elif user_answer == 'n':
            print('0 point')
        else:
            print('invalid')
    else:
        if user_answer == 'y':
            print('0 point')
        elif user_answer == 'n':
            print('+1 point')
        else:
            print('invalid')
