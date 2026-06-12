import tkinter
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
	Label_texto_intro.configure(text="Seleccione el tipo de ejercicio")
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
	lan_pal.delete(0,tkinter.END)
	lan_pal.pack_forget()
	
def cambio_texto():
    Label_texto_intro.configure(text="Seleccione el modo de traducción")
    boton_cambio_espanol.configure(text="Spanish",command=Spanish_languaje)
    boton_cambio_espanol.pack(padx=20,pady=5)
    boton_cambio_ingles.configure(text="English",command=English_languaje)
    boton_cambio_ingles.pack(padx=20,pady=5)
    lan_pal.delete(0,tkinter.END)
    lan_pal.pack_forget()

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
	table_name="verbs"
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

frame1 = tkinter.Frame(ventana)

Label_texto_intro = tkinter.Label(frame1, text="Welcome to Englis Vocabulary \nYour app to practice your\npersonal vocabulary",font=("Arial",18),padx=20,pady=10)
Label_texto_intro.pack()
 
boton_cambio_espanol = tkinter.Button(frame1, text="Press to start",font=("Arial",16),command=cambio_tema)
boton_cambio_espanol.pack(padx=20,pady=5)

lan_pal = tkinter.Entry(frame1,font=("Arial",16), textvariable=palabra_var)

boton_cambio_ingles= tkinter.Button(frame1, text="",font=("Arial",16))
boton_cambio_idioms= tkinter.Button(frame1, text="",font=("Arial", 16))
boton_cambio_words= tkinter.Button(frame1, text="",font=("Arial", 16))
boton_cambio_verbs= tkinter.Button(frame1, text="",font=("Arial", 16))
boton_cambio_reinforcement= tkinter.Button(frame1, text="",font=("Arial", 16))
boton_cambio_sentences= tkinter.Button(frame1, text="",font=("Arial", 16))

mensaje_label = tkinter.Label(frame1,text="",font=("Arial",18))
mensaje_label.pack(padx=20,pady=5)
frame1.pack()

ventana.mainloop()

