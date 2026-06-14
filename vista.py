import tkinter as tk
from random import randint
import mysql.connector
from mysql.connector import errors

table_name = "" 

def connect_to_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            port="3307",
            user="root",
            database="voc"
        )
    except errors.OperationalError as e:
        print("Connection error:", e)
        return None

db = connect_to_db()

# If connection fails, you can try reconnecting in a loop or handle accordingly
if db is None:
    print("Reconnection failed.")
else:
    print("Connection successful.")

def cambio_tema():
    limpiar_ventana()
    Label_texto_ejercicio= tk.Label(ventana, text="Seleccione el tipo de ejercicio").pack()
    boton_cambio_idioms= tk.Button(ventana, text="",font=("Arial", 16))
    boton_cambio_words= tk.Button(ventana, text="",font=("Arial", 16))
    boton_cambio_verbs= tk.Button(ventana, text="",font=("Arial", 16))
    boton_cambio_reinforcement= tk.Button(ventana, text="",font=("Arial", 16))
    boton_cambio_sentences= tk.Button(ventana, text="",font=("Arial", 16))

    boton_cambio_words.configure(text="Words", command=words)
    boton_cambio_words.pack(padx=20,pady=5)
    boton_cambio_idioms.configure(text="Idioms", command=idioms)
    boton_cambio_idioms.pack(padx=20,pady=5)
    boton_cambio_verbs.configure(text="Phrasal verbs", command=verbs)
    boton_cambio_verbs.pack(padx=20,pady=5)
    boton_cambio_reinforcement.configure(text="Reinforcement", command=reinforcement)
    boton_cambio_reinforcement.pack(padx=20,pady=5)
    boton_cambio_sentences.configure(text="Sentences", command=sentences)
    boton_cambio_sentences.pack(padx=20,pady=5)
	
def ocultar_boton():
    # Oculta el botón usando el mismo gestor con el que fue creado (pack, grid o place)
    boton_again.pack_forget()
    # Pare refrescar la ventana después de ocultar el botón
    ventana.update()

def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()

def cambio_texto():
    limpiar_ventana()
    Label_texto_traduccion = tk.Label(ventana, text="Seleccione el modo de traducción").pack()
    boton_cambio_espanol = tk.Button(ventana, text="",font=("Arial", 16))
    boton_cambio_espanol.configure(text="Spanish",command=Spanish_languaje)
    boton_cambio_espanol.pack(padx=20,pady=5)
    boton_cambio_ingles = tk.Button(ventana, text="",font=("Arial", 16))
    boton_cambio_ingles.configure( text="English",command=English_languaje)
    boton_cambio_ingles.pack(padx=20,pady=5)

def words():
	global table_name
	table_name="words"
	cambio_texto()

def idioms():
	global table_name
	table_name="idioms"
	cambio_texto()

def verbs():
	global table_name
	table_name="phrasal_verbs"
	cambio_texto()

def reinforcement():
	global table_name
	table_name="reinforcement"
	cambio_texto()

def sentences():
	global table_name
	table_name="sentences"
	cambio_texto()

def English_languaje():
    y = "Eng"
    return play_eng_esp(y)

def Spanish_languaje():
    y = "Spa"
    return play_eng_esp(y)

def elige():
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    myresult = cursor.fetchone()
    cantidad = myresult[0]
    aleatorio = randint(1, cantidad)
    cursor.execute(f"SELECT * FROM {table_name} WHERE `index` = {aleatorio}")
    myresult = cursor.fetchall()
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return insertObject

def play_eng_esp(y):
    limpiar_ventana()
    palabras = elige()
    palabras = palabras[0]
    palabras = dict(palabras)
    global c
    global e
    if y == "Spa":
        d = palabras['Esp']
        c = palabras['Eng']
        texto = "La palabra a traducir es \n {}".format(d)
    elif y == "Eng":
        d = palabras['Eng']
        c = palabras['Esp']
        texto = "The word to translate is \n {}".format(d)
    Label_texto_play = tk.Label(ventana, text=texto).pack()
    e = tk.Entry(ventana, width=40)
    e.pack()
    boton_confirmar = tk.Button(ventana, text="Confirmar",font=("Arial",16), command=valor_entrada)
    boton_confirmar.pack(side=tk.BOTTOM)

def valor_entrada():
    palabra = e.get
    limpiar_ventana()
    return evalua(palabra)

def evalua(palabra):
    Label_evalua = tk.Label(ventana, text="")

    if (c == palabra):
        Label_evalua.configure(text="Correcto")
        Label_evalua.pack()
    else:
        texto = "Incorrecto \n La palabra correcta es: {}".format(c)
        Label_evalua.configure(text=texto)
        Label_evalua.pack()
    boton_again = tk.Button(ventana, text="Otra vez", command=cambio_texto)
    boton_again.pack()

c = ""

ventana = tk.Tk()

Label_texto_intro = tk.Label(ventana, text="Welcome to Englis Vocabulary \nYour app to practice your\npersonal vocabulary",font=("Arial",18),padx=20,pady=10)
Label_texto_intro.pack()
 
boton_start = tk.Button(ventana, text="Press to start",font=("Arial",16),command=cambio_tema)
boton_start.pack(padx=20,pady=5)

mensaje_label = tk.Label(ventana,text="",font=("Arial",18))
mensaje_label.pack(padx=20,pady=5)

ventana.mainloop()

