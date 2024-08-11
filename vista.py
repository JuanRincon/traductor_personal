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
    y = "Eng"
    eleccion = elige_pares(y)
    eleccion = list(eleccion)
    c = eleccion[0]
    b = eleccion[1]
    play_eng_esp(c,b,y)

def Spanish_languaje():
    global c
    global b
    y = "Spa"
    eleccion = elige_pares(y)
    eleccion = list(eleccion)
    c = eleccion[0]
    b = eleccion[1]
    play_eng_esp(c,b,y)

def play_eng_esp(c,b,y):
    #global palabra
    lang = eng
    d = str(lang[b])
    texto = "La palabra a traducir es \n {}".format(d)
    Label_texto_intro.configure(text=texto)
    mensaje_label.pack_forget()
    boton_cambio_espanol.pack_forget()
    boton_cambio.configure(text="Confirmar", command=evalua)
    boton_cambio.pack(side=tkinter.BOTTOM)
    lan_pal = tkinter.Entry(ventana,font=("Arial",16), textvariable=palabra_var)
    lan_pal.pack(padx=20,pady=5)

def evalua():
    lang = eng
    nombre = nombre_var.get()
    palabra = palabra_var.get()

    if (lang[c] == palabra):
        Label_texto_intro.configure(text="Correcto")
        Label_texto_intro.pack()
    else:
        texto = "Incorrecto \n La palabra correcta es: {}".format(lang[c])
        Label_texto_intro.configure(text=texto)
        Label_texto_intro.pack()

ventana = tkinter.Tk()

nombre_var = tkinter.StringVar()
palabra_var = tkinter.StringVar()

Label_texto_intro = tkinter.Label(ventana, text="Welcome to Englis Vocabulary \nYour app to practice your personal vocabulary",font=("Arial",18),padx=20,pady=10)
Label_texto_intro.pack()
    
boton_cambio = tkinter.Button(ventana, text="Precione para iniciar",font=("Arial",16),command=cambio_texto)
boton_cambio.pack(padx=20,pady=5)

boton_cambio_espanol= tkinter.Button(ventana, text="",font=("Arial",16))

mensaje_label = tkinter.Label(ventana,text="",font=("Arial",18))
mensaje_label.pack(padx=20,pady=5)

ventana.mainloop()
