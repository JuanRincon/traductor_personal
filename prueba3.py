from random import randint
from prueba2 import eng,spa


print("Welcome to english vocabulary")

def elige_pares():
	b = randint(1, 111)
	if b%2==0:
		a = b
		return(a)
	else:
		print("b es igual: ", b)
		b -= 1
		a = b
		print("a es igual: ", a)
		return(a)


def select_lang():
	print("1. for vocabulary english to spanish")
	print("2. for vocabulary spanish to english")
	sele = int(input(""))
	if sele == 1:
		lang = eng
	else:
		lang = spa
	return(lang)


def play_eng_esp():
	tecla = ""
	while (tecla !='x'):
		lang = select_lang()
		a = elige_pares()
		print("La palabra a traducir es: ")
		print("En este caso a es igual: ", a)
		d = str(lang[a])
		#d = d[:-1]
		print(d, "\n")
		c = input("Ingrese la traducción: ")
		if (lang[a+1] == c):
			print("Correcto \n")
		else:
			print("Incorrecto.\nLa palabra correcta es: ", lang[a+1], "\n")
		tecla = input("Ingrese x para salir: \n")
		

if __name__=='__main__':
	play_eng_esp()		
