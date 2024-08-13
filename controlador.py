from random import randint
from modelo import eng

def elige_pares(x):
    b = randint(0, (len(eng)-1))
    a = 0
    if ((b%2==0) and (x == 'Eng')):
        a = b + 1
    elif ((b%2!=0) and (x == 'Eng')):
        b -= 1
        a = b + 1
    elif ((b%2==0) and (x == 'Spa')):
        b -= 1
        a = b - 1
    elif ((b%2!=0) and (x == 'Spa')):
        a = b - 1
    else:
        print("error")
    return(a,b,x)

