from random import randint
from prueba2 import eng
from os import system as sys

sys('clear')

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

def main():
#	welcome()
	select_lang()

if __name__=='__main__':
	main()		
