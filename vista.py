import tkinter
import prueba3 
from random import randint
from prueba2 import eng
from os import system as sys
from prueba3 import elige_pares

sys('clear')

def cambio_texto():
    Label_texto_intro.configure(text="Seleccione el modo de traducción")
    boton_cambio_espanol.configure(text="English",command=English_languaje)
    boton_cambio_espanol.pack(padx=20,pady=5)
    boton_cambio.configure(text="Spanish",command=Spanish_languaje)

def English_languaje():
    Label_texto_intro.configure(text="La palabra a traducir es: ")
    y = "Eng"
    eleccion = elige_pares(y)
    eleccion = list(eleccion)
    c = eleccion[0]
    b = eleccion[1]
    play_eng_esp(c,b,y)

def Spanish_languaje():
    mensaje_label.configure(text="Has elegido Spanish")
    y = "Spa"
    eleccion = elige_pares(y)
    eleccion = list(eleccion)
    c = eleccion[0]
    b = eleccion[1]
    play_eng_esp(c,b,y)


def play_eng_esp(c,b,y):
    lang = eng
    tecla = ""
    #print("La palabra a traducir es: ")
    d = str(lang[b])
    texto = "La palabra a traducir es \n {}".format(d)
    Label_texto_intro.configure(text=texto)
    #print(d, "\n")
    #e = input("Ingrese la traducción: ")
    
    palabra = tkinter.StringVar()
    lan_pal = tkinter.Entry(ventana,font=("Arial",16), textvariable=palabra)
    lan_pal.pack(padx=20,pady=5)
    boton_cambio.configure(text="Confirmar")
    mensaje_label.pack_forget()
    boton_cambio_espanol.pack_forget()
    boton_cambio.pack(side=tkinter.BOTTOM)

    if (lang[c] == palabra):
        #print("Correcto \n")
        pass
    else:
        print("Incorrecto.\nLa palabra correcta es: ", lang[c], "\n")
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
		cambio_texto()

ventana = tkinter.Tk()

nombre_var = tkinter.StringVar()

Label_texto_intro = tkinter.Label(ventana, text="Welcome to Englis Vocabulary \nYour app to practice your personal vocabulary",font=("Arial",18),padx=20,pady=10)
Label_texto_intro.pack()
    
boton_cambio = tkinter.Button(ventana, text="Precione para iniciar",font=("Arial",16),command=cambio_texto)
boton_cambio.pack(padx=20,pady=5)

boton_cambio_espanol= tkinter.Button(ventana, text="",font=("Arial",16))

mensaje_label = tkinter.Label(ventana,text="",font=("Arial",18))
mensaje_label.pack(padx=20,pady=5)

ventana.mainloop()
