import tkinter

ventana = tkinter.Tk()

nombre_var = tkinter.StringVar()

def cambio_texto():
    texto_intro.configure(text="Seleccione el modo de traducción")
    boton_cambio.configure(text="English")
    boton_cambio_espanol= tkinter.Button(ventana, text="Spanish")

texto_intro = tkinter.Label(ventana, text="Welcome to Englis Vocabulary \nYour app to practice your personal vocabulary",font=("Arial",18),padx=20,pady=10)
texto_intro.pack()

boton_cambio = tkinter.Button(ventana, text="Precione para iniciar",font=("Arial",16),command=cambio_texto)
boton_cambio.pack(padx=20,pady=10)

ventana.mainloop()
