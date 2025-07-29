from random import randint
from modelo import db

def elige():
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM words")
    myresult = cursor.fetchone()
    cantidad = myresult[0]
    aleatorio = randint(1, cantidad)
    cursor.execute(f"SELECT * FROM words WHERE id = {aleatorio}")
    myresult = cursor.fetchall()
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return insertObject


