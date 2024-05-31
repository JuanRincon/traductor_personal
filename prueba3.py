from random import randint
from prueba2 import b

tecla = ""

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

print("Welcome to english vocabulary")


while (tecla !='x'):
	print("La palabra a traducir es: ")
	a = elige_pares()
	print("En este caso a es igual: ", a)
	d = str(b[a])
	#d = d[:-1]
	print(d, "\n")
	c = input("Ingrese la traducción: ")
	if (b[a+1] == c):
		print("Correcto \n")
	else:
		print("Incorrecto.\nLa palabra correcta es: ", b[a+1], "\n")
	tecla = input("Ingrese x para salir: \n")
		
