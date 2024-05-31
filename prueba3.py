from random import randint
from prueba2 import b

def elige_pares():
	a = 0
	a = randint(1, 111)
	if a%2!=0:
	    return(a)	
	else:
	    elige_pares()	
	return(a)

print("Welcome to english vocabulary")

tecla = ""

a = elige_pares()

while (tecla !='x'):
	print("La palabra a traducir es: ")
	print("a es igual a: ", a)
	d = str(b[a])
	#d = d[:-1]
	print(d, "\n")
	c = input("Ingrese la traducción: ")
	if (b[a+1] == (c+',')) | (b[a+2] == (c+',')) | (b[a+3] == (c+',')):
		print("Correcto \n")
	else:
		print("Incorrecto.\nLa palabra correcta es: ", b[a+1], "\n")
	tecla = input("Ingrese x para salir: \n")
		
