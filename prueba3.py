from random import randint
from prueba2 import eng
from os import system as sys

sys('clear')

"""
def select_lang():
	print("  ##  Press:  ##")
	print("")
	print("|- E - for [E]nglish to spanish vocabulary -|")
	print("|- S - for [S]panish to english vocabulary -|\n")
	sele = input("")
	elige_pares(sele)
"""

def select_lang(o):
    if o == "Eng":
        print("English")
    elif o == "Spa":
        print("Spanish")
    else:
        print("Error")
    elige_pares(o)

def elige_pares(x):
	b = randint(0, (len(eng)-1))
	a = 0
	if ((b%2==0) and (x == 'e' or x == 'E')):
		a = b + 1
	elif ((b%2!=0) and (x == 'e' or x == 'E')):
		b -= 1
		a = b + 1
	elif ((b%2==0) and (x == 's' or x == 'S')):
		b -= 1
		a = b - 1
	elif ((b%2!=0) and (x == 's' or x == 'S')):
		a = b - 1
	else:
		print("error")
	play_eng_esp(a,b,x)

def play_eng_esp(a,b,y):
	lang = eng
	tecla = ""
	print("La palabra a traducir es: ")
	d = str(lang[b])
	print(d, "\n")
	c = input("Ingrese la traducción: ")
	if (lang[a] == c):
		print("Correcto \n")
	else:
		print("Incorrecto.\nLa palabra correcta es: ", lang[a], "\n")
	print("Ingrese \"x\" para salir \"z\" para cambiar el lenguaje : ")
	print("o presione otra letra para continuar \n")
	tecla = input("")	
	opciones(tecla)

def opciones(m):
	if (m == 'z'):
		select_lang()
	#elif(m == 'x'):
		#despedida()
	else:
		elige_pares(y)


def main():
#	welcome()
	select_lang()

if __name__=='__main__':
	main()		
