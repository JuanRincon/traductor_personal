import tkinter
from controlador import elige

def cambio_texto():
    Label_texto_intro.configure(text="Seleccione el modo de traducción")
    boton_cambio_espanol.configure(text="Spanish",command=Spanish_languaje)
    boton_cambio_espanol.pack(padx=20,pady=5)
    boton_cambio_ingles.configure(text="English",command=English_languaje)
    boton_cambio_ingles.pack(padx=20,pady=5)
    lan_pal.delete(0,tkinter.END)
    lan_pal.pack_forget()

def English_languaje():
    y = "Eng"
    return play_eng_esp(y)

def Spanish_languaje():
    y = "Spa"
    return play_eng_esp(y)

def play_eng_esp(y):
    palabras = elige()
    palabras = palabras[0]
    palabras = dict(palabras)
    global c
    if y == "Spa":
        d = palabras['Esp']
        c = palabras['Eng']
        texto = "La palabra a traducir es \n {}".format(d)
    elif y == "Eng":
        d = palabras['Eng']
        c = palabras['Esp']
        texto = "La palabra a traducir es \n {}".format(d)
    Label_texto_intro.configure(text=texto)
    mensaje_label.pack_forget()
    boton_cambio_ingles.pack_forget()
    boton_cambio_espanol.configure(text="Confirmar", command=evalua)
    boton_cambio_espanol.pack(side=tkinter.BOTTOM)
    lan_pal.pack(padx=20,pady=5)

def evalua():
    global c

    nombre = nombre_var.get()
    palabra = palabra_var.get()

    if (c == palabra):
        Label_texto_intro.configure(text="Correcto")
        Label_texto_intro.pack()
    else:
        texto = "Incorrecto \n La palabra correcta es: {}".format(c)
        Label_texto_intro.configure(text=texto)
        Label_texto_intro.pack()
    boton_cambio_espanol.configure(text="Otra vez", command=cambio_texto)

c = ""

ventana = tkinter.Tk()

nombre_var = tkinter.StringVar()
palabra_var = tkinter.StringVar()

Label_texto_intro = tkinter.Label(ventana, text="Welcome to Englis Vocabulary \nYour app to practice your\npersonal vocabulary",font=("Arial",18),padx=20,pady=10)
Label_texto_intro.pack()
    
boton_cambio_espanol = tkinter.Button(ventana, text="Press to start",font=("Arial",16),command=cambio_texto)
boton_cambio_espanol.pack(padx=20,pady=5)

lan_pal = tkinter.Entry(ventana,font=("Arial",16), textvariable=palabra_var)

boton_cambio_ingles= tkinter.Button(ventana, text="",font=("Arial",16))

mensaje_label = tkinter.Label(ventana,text="",font=("Arial",18))
mensaje_label.pack(padx=20,pady=5)

ventana.mainloop()

