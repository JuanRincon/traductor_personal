import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import errors, Error

ventana = tk.Tk()

table_name = "" 
history_back = []
history_forward = []
current_page = None
bandera = ""

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port="3307",
            user="root",
            database="voc",
        )
        return conn

    except Exception as e:
        print("ERROR MYSQL:", repr(e))
        input("Presiona Enter para cerrar...")
        return None

def menu():
    ventana.title("Menu Demo")

    # Create the menubar
    menubar = tk.Menu(ventana)
    ventana.config(menu=menubar)

    # Create a File menu
    file_menu = tk.Menu(menubar, tearoff=False)
    file_menu.add_command(label="Start", command=lambda: navegar(inicio))
    file_menu.add_command(label="Exit", command=ventana.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    # Create a navigate menu
    navi_menu = tk.Menu(menubar, tearoff=False)
    navi_menu.add_command(label="Back", command=backward)
    navi_menu.add_command(label="Forward", command=forward)
    menubar.add_cascade(label="Navigate", menu=navi_menu)

def navegar(funcion_destino, *args, **kwargs):
    global current_page

    if current_page is not None:
        history_back.append(current_page)

    history_forward.clear()

    current_page = {
        "func": funcion_destino,
        "args": args,
        "kwargs": kwargs
    }

    funcion_destino(*args, **kwargs)

def backward():
    global current_page

    if not history_back:
        return

    history_forward.append(current_page)

    current_page = history_back.pop()

    limpiar_ventana()

    current_page["func"](
        *current_page["args"],
        **current_page["kwargs"]
    )


def forward():
    global current_page

    if not history_forward:
        return

    history_back.append(current_page)

    current_page = history_forward.pop()

    limpiar_ventana()

    current_page["func"](
        *current_page["args"],
        **current_page["kwargs"]
    )

def datos_entrenamiento():
    def limpiar_campos():
        entry_index.delete(0, tk.END)
        entry_eng.delete(0, tk.END)
        entry_esp.delete(0, tk.END)

    def insertar():
        conexion = connect_to_db()
        cursor = conexion.cursor()
        sql = f"INSERT IGNORE INTO {table_name} (Eng, Esp) VALUES (%s, %s)"
        check_query = f"SELECT * FROM {table_name} WHERE Eng = %s OR Esp = %s"
        valores = entry_eng.get(), entry_esp.get()
        try:
			# 1. Check if the word already exists
            cursor.execute(check_query, valores)

            if cursor.fetchone():
                print(f"Word '{valores}' already exists. Skipping insert.")
                return False

            cursor.execute(sql, valores)
            conexion.commit()
            messagebox.showinfo('Información', 'Registro insertado con éxito')
            limpiar_campos()
        except Error as e:
            messagebox.showerror('Error', str(e))
        finally:
            conexion.close()

    def editar():
        conexion = connect_to_db()
        cursor = conexion.cursor()
        sql = f"UPDATE {table_name} SET Eng=%s,Esp=%s WHERE `index`=%s"
        valores = (entry_eng.get(), entry_esp.get(), entry_index.get())
        try:
            cursor.execute(sql, valores)
            conexion.commit()
            messagebox.showinfo('Información', 'Registro actualizado con éxito')
            limpiar_campos()
        except Error as e:
            messagebox.showerror('Error', str(e))
        finally:
            conexion.close()

    def eliminar():
        conexion =  connect_to_db()
        cursor = conexion.cursor()
        sql =f"DELETE FROM {table_name} WHERE `index`=%s"
        try:
            cursor.execute(sql,(entry_index.get(),))
            conexion.commit()
            messagebox.showinfo('Información', 'Registro eliminado con éxito')
            limpiar_campos()
        except Error as e:
            messagebox.showerror('Error', str(e))
        finally:
            conexion.close()

    def buscar():
        conexion =   connect_to_db()
        cursor = conexion.cursor()

        if entry_index.get():
            sql = f"SELECT * FROM {table_name} WHERE `index`=%s"
            variable = (entry_index.get(),)
        elif entry_eng.get():
            sql = f"SELECT * FROM {table_name} WHERE Eng=%s"
            variable = (entry_eng.get(),)
        elif entry_esp.get():
            sql = f"SELECT * FROM {table_name} WHERE Esp=%s"
            variable = (entry_esp.get(),)
        try:
            cursor.execute(sql,variable)
            registro = cursor.fetchone()
            if registro and entry_index.get():
                entry_eng.insert(0, registro[1])
                entry_esp.insert(0, registro[2])
            elif registro and entry_eng.get():
                entry_index.insert(0, registro[0])
                entry_esp.insert(0, registro[2])
            elif registro and entry_esp.get():
                entry_index.insert(0, registro[0])
                entry_eng.insert(0, registro[1])
            else:
                messagebox.showinfo('Información', 'No se encontró el registro solicitado')
        except Error as e:
            messagebox.showerror('Error', str(e))
        finally:
            conexion.close()
    
    def mostrar_todo():
        limpiar_ventana()
        conexion = connect_to_db()
        if not conexion:
            return
        tabla = ttk.Treeview(ventana, show="headings")
        tabla.pack(fill="both", expand=True)
        boton_inicio = tk.Button(ventana, text="Inicio", command=inicio)
        boton_inicio.pack()
        try:
            cursor = conexion.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")

            columnas = [col[0] for col in cursor.description]

            tabla.delete(*tabla.get_children())
            tabla["columns"] = columnas

            for col in columnas:
                tabla.heading(col, text=col)
                tabla.column(col, width=120)

            for fila in cursor.fetchall():
                tabla.insert("", tk.END, values=fila)

        except mysql.connector.Error as e:
            messagebox.showerror("Error", str(e))

        finally:
            conexion.close()
    limpiar_ventana()
    menu()
    tk.Label(ventana,text="Index").grid(column=0,row=0)
    entry_index= tk.Entry(ventana)
    entry_index.grid(column=0,row=1)

    tk.Label(ventana,text="Eng").grid(column=1,row=0)
    entry_eng= tk.Entry(ventana)
    entry_eng.grid(column=1,row=1)

    tk.Label(ventana,text="Esp").grid(column=2,row=0)
    entry_esp= tk.Entry(ventana)
    entry_esp.grid(column=2,row=1)

    tk.Button(ventana,text="Insertar", command=insertar).grid(column=0, row=2)
    tk.Button(ventana,text="Buscar", command=buscar).grid(column=1, row=2)
    tk.Button(ventana,text="Editar", command=editar).grid(column=2, row=2)
    tk.Button(ventana,text="Eliminar", command=eliminar).grid(column=3, row=2)
    tk.Button(ventana,text="Limpiar", command=limpiar_campos).grid(column=3, row=1)
    tk.Button(ventana,text="Mostrar todo", command=mostrar_todo).grid(column=3, row=0)

def cambio_tema(define):
    limpiar_ventana()
    menu()
    global bandera
    bandera = define
    Label_texto_ejercicio= tk.Label(ventana, text="Seleccione el tipo de ejercicio\n ",font=("Arial",16)).pack()
    boton_cambio_idioms= tk.Button(ventana, text="",font=("Arial", 16))
    boton_cambio_words= tk.Button(ventana, text="",font=("Arial", 16))
    boton_cambio_verbs= tk.Button(ventana, text="",font=("Arial", 16))
    boton_cambio_reinforcement= tk.Button(ventana, text="",font=("Arial", 16))
    boton_cambio_sentences= tk.Button(ventana, text="",font=("Arial", 16))

    boton_cambio_words.configure(text="Words", command=lambda: navegar(words))
    boton_cambio_words.pack(padx=20,pady=5)
    boton_cambio_idioms.configure(text="Idioms", command=lambda: navegar(idioms))
    boton_cambio_idioms.pack(padx=20,pady=5)
    boton_cambio_verbs.configure(text="Phrasal verbs", command=lambda: navegar(verbs))
    boton_cambio_verbs.pack(padx=20,pady=5)
    boton_cambio_reinforcement.configure(text="Reinforcement", command=lambda: navegar(reinforcement))
    boton_cambio_reinforcement.pack(padx=20,pady=5)
    boton_cambio_sentences.configure(text="Sentences", command=lambda: navegar(sentences))
    boton_cambio_sentences.pack(padx=20,pady=5)
	
def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()

def cambio_texto():
    limpiar_ventana()
    menu()
    Label_texto_traduccion = tk.Label(ventana, text="Seleccione el modo de traducción\n ",font=("Arial",16)).pack()
    boton_cambio_espanol = tk.Button(ventana, text="",font=("Arial", 16))
    boton_cambio_espanol.configure(text="Spanish",command=lambda: navegar(play_eng_esp,"Spa"))
    boton_cambio_espanol.pack(padx=20,pady=5)
    boton_cambio_ingles = tk.Button(ventana, text="",font=("Arial", 16))
    boton_cambio_ingles.configure( text="English",command=lambda: navegar(play_eng_esp,"Eng"))
    boton_cambio_ingles.pack(padx=20,pady=5)

def words():
    global table_name
    table_name="words"
    if bandera == "datos":
        datos_entrenamiento()
    else:
        cambio_texto()

def idioms():
    global table_name
    table_name="idioms"
    if bandera == "datos":
        datos_entrenamiento()
    else:
        cambio_texto()

def verbs():
    global table_name
    table_name="phrasal_verbs"
    if bandera == "datos":
        datos_entrenamiento()
    else:
        cambio_texto()

def reinforcement():
    global table_name
    table_name="reinforcement"
    if bandera == "datos":
        datos_entrenamiento()
    else:
        cambio_texto()

def sentences():
    global table_name
    table_name="sentences"
    if bandera == "datos":
        datos_entrenamiento()
    else:
        cambio_texto()

def elige():
    try:
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {table_name} ORDER BY RAND() LIMIT 1")
        myresult = cursor.fetchone()
        if myresult is None:
            return []
        cursor.close()
        db.close()
        return myresult
    except Exception as ex:
        print("ERROR:", ex)
        return[]

def play_eng_esp(y, palabras=None):
    limpiar_ventana()
    menu()

    # Si no tenemos una palabra guardada,
    # seleccionamos una nueva.
    if palabras is None:

        palabras = elige()

        if not palabras:
            messagebox.showwarning(
                "Aviso",
                "No existen registros en la tabla."
            )
            navegar(inicio)
            return

        palabras = {
            "Eng": palabras[1],
            "Esp": palabras[2]
        }

        # Guardamos la palabra seleccionada en la página actual
        current_page["args"] = (y, palabras)

    global c
    global e

    if y == "Spa":
        d = palabras["Esp"]
        c = palabras["Eng"]
        texto = "La palabra a traducir es: \n\n{}\n ".format(d)

    elif y == "Eng":
        d = palabras["Eng"]
        c = palabras["Esp"]
        texto = "The word to translate is: \n\n{}\n ".format(d)

    Label_texto_play = tk.Label(
        ventana,
        text=texto,
        font=("Arial", 16)
    )
    Label_texto_play.pack()

    e = tk.Entry(
        ventana,
        width=40
    )
    e.pack()

    boton_confirmar = tk.Button(
        ventana,
        text="Confirmar",
        font=("Arial", 16),
        command=valor_entrada
    )
    boton_confirmar.pack(side=tk.BOTTOM)

def valor_entrada():
    palabra = e.get()
    limpiar_ventana()
    return evalua(palabra)

def evalua(palabra):
    menu()
    Label_evalua = tk.Label(ventana, text="")
    if (c == palabra):
        Label_evalua.configure(text="Correcto",font=("Arial",16))
        Label_evalua.pack()
    else:
        texto = "Incorrecto \n La palabra correcta es: \n {} \n ".format(c)
        Label_evalua.configure(text=texto,font=("Arial",16))
        Label_evalua.pack()
    boton_again = tk.Button(ventana, text="Otra vez",font=("Arial",16), command=lambda: navegar(cambio_texto))
    boton_again.pack()

def inicio():
    limpiar_ventana()
    c = ""

    Label_texto_intro = tk.Label(ventana, text="Welcome to Englis Vocabulary \nYour app to practice your\npersonal vocabulary\n ",font=("Arial",18),padx=20,pady=10)
    Label_texto_intro.pack()
     
    boton_start = tk.Button(ventana, text="Press to start",font=("Arial",16),command=lambda: navegar(cambio_tema, "juego"))
    boton_start.pack(padx=20,pady=5)
    boton_datos = tk.Button(ventana, text="Ingresa nuevos datos",font=("Arial",16),command=lambda: navegar(cambio_tema, "datos"))
    boton_datos.pack(padx=20,pady=5)

    mensaje_label = tk.Label(ventana,text="",font=("Arial",18))
    mensaje_label.pack(padx=20,pady=5)

#ventana.title("Your app to study languages")

if __name__=='__main__':
    inicio()

ventana.mainloop()
