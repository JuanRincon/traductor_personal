from random import randint
from prueba2 import eng,spa
from os import system as sys

sys('clear')

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("")
print("##### Welcome to English Vocabulary #####")
print("")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("")
print("Your app to practice your personal vocabulary")
print("")
print("")


def elige_pares():
	b = randint(1, 111)
	if b%2==0:
		a = b
		return(a)
	else:
		b -= 1
		a = b
		return(a)
	return(lang)


def select_lang():
	print("  ##  Press:  ##")
	print("")
	print("|- 1 - for vocabulary english to spanish -|")
	print("|- 2 - for vocabulary spanish to english -|\n")

	sele = int(input(""))
	if sele == 1:
		lang = eng
	else:
		lang = spa
	return(lang)

lang = select_lang()

def play_eng_esp():
	tecla = ""
	while (tecla !='x'):
		global lang
		if (tecla == 'z'):
			lang = select_lang()
		a = elige_pares()
		print("La palabra a traducir es: ")
		d = str(lang[a])
		#d = d[:-1]
		print(d, "\n")
		c = input("Ingrese la traducción: ")
		if (lang[a+1] == c):
			print("Correcto \n")
		else:
			print("Incorrecto.\nLa palabra correcta es: ", lang[a+1], "\n")
		print("Ingrese \"x\" para salir \"z\" para cambiar el lenguaje : ")
		print("o presione otra letra para continuar \n")
		tecla = input("")	


if __name__=='__main__':
	play_eng_esp()		
