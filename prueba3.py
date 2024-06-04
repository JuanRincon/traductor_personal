from random import randint
from prueba2 import eng
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

def select_lang():
	print("  ##  Press:  ##")
	print("")
	print("|- E - for [E]nglish to spanish vocabulary -|")
	print("|- S - for [S]panish to english vocabulary -|\n")
	sele = input("")
	elige_pares(sele)
	return(sele)

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
		select_lang()
	play_eng_esp(a,b)

def play_eng_esp(a,b):
	lang = eng
	tecla = ""
	while (tecla !='x'):
		if (tecla == 'z'):
			select_lang()
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

def main():
	welcome()
	select_lang()

if __name__=='__main__':
	main()		
