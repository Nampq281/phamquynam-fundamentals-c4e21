from random import *
from calc import caculate

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 9)
    y = randint(0, 9)
    op = choice(['+','-','*','/'])
    r = caculate(x, y, op)
    z = randint(-1, 1)
    result = r+z
    return [x, y, op, result]
    
def check_answer(x, y, op, z, user_choice):
    if z == 0:
        if user_choice == True:
            return True
        if user_choice == False:
            return False
    else:
        if user_choice == True:
            return False
        if user_choice == False:
            return True

