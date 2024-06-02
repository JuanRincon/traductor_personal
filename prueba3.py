from random import randint
from prueba2 import eng,spa
from os import system as sys

sys('clear')


def welcome():
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
	return(cosa)

def select_lang():
	print("  ##  Press:  ##")
	print("")
	print("|- E - for vocabulary english to spanish -|")
	print("|- S - for vocabulary spanish to english -|\n")
	sele = input("")
	#return(sele)
	if (sele == 'e'):
		lang = eng
	elif (sele == 'E'):
		lang = eng
	elif (sele == 's'):
		lang = spa
	elif (sele == 'S'):
		lang = spa
	else:
		select_lang()
	return(lang)

def play_eng_esp():
	lang = select_lang()
	tecla = ""
	while (tecla !='x'):
		if (tecla == 'z'):
			lang = select_lang()
		a = elige_pares()
		print("La palabra a traducir es: ")
		d = str(lang[a])
		print(d, "\n")
		c = input("Ingrese la traducción: ")
		if (lang[a+1] == c):
			print("Correcto \n")
		else:
			print("Incorrecto.\nLa palabra correcta es: ", lang[a+1], "\n")
		print("Ingrese \"x\" para salir \"z\" para cambiar el lenguaje : ")
		print("o presione otra letra para continuar \n")
		tecla = input("")	

def main():
	welcome()
	play_eng_esp()

if __name__=='__main__':
	main()		
