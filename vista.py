import tkinter

ventana = tkinter.Tk()

nombre_var = tkinter.StringVar()

def traducir():
    mensaje_label.configure(text="Vamos mejorando")

def cambio_texto():
    texto_intro.configure(text="Seleccione el modo de traducción")
    boton_cambio.configure(text="English",command=traducir)
    boton_cambio_espanol= tkinter.Button(ventana, text="Spanish",font=("Arial",16),command=traducir)
    boton_cambio_espanol.pack(padx=20,pady=10)

texto_intro = tkinter.Label(ventana, text="Welcome to Englis Vocabulary \nYour app to practice your personal vocabulary",font=("Arial",18),padx=20,pady=10)
texto_intro.pack()

boton_cambio = tkinter.Button(ventana, text="Precione para iniciar",font=("Arial",16),command=cambio_texto)
boton_cambio.pack(padx=20,pady=10)

mensaje_label = tkinter.Label(ventana,text="",font=("Arial",18))
mensaje_label.pack(padx=20,pady=5)

ventana.mainloop()
