import tkinter
from prueba3 import *

ventana = tkinter.Tk()

nombre_var = tkinter.StringVar()

def English_languaje():
    mensaje_label.configure(text="Has elegido English")
    a = "Eng"
    select_lang(a)

def Spanish_languaje():
    mensaje_label.configure(text="Has elegido Spanish")
    a = "Spa"
    select_lang(a)

def cambio_texto():
    texto_intro.configure(text="Seleccione el modo de traducción")
    boton_cambio_espanol.configure(text="English",command=English_languaje)
    boton_cambio.configure(text="Spanish",command=Spanish_languaje)

texto_intro = tkinter.Label(ventana, text="Welcome to Englis Vocabulary \nYour app to practice your personal vocabulary",font=("Arial",18),padx=20,pady=10)
texto_intro.pack()

boton_cambio = tkinter.Button(ventana, text="Precione para iniciar",font=("Arial",16),command=cambio_texto)
boton_cambio.pack(padx=20,pady=10)

boton_cambio_espanol= tkinter.Button(ventana, text="",font=("Arial",16))
boton_cambio_espanol.pack(padx=20,pady=10)

mensaje_label = tkinter.Label(ventana,text="",font=("Arial",18))
mensaje_label.pack(padx=20,pady=5)

ventana.mainloop()
