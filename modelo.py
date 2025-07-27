import mysql.connector
from mysql.connector import errors

def connect_to_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            port="33062",
            user="root",
            password="Socrates123*",
            database="voc"
        )
    except errors.OperationalError as e:
        print("Connection error:", e)
        return None

voc = connect_to_db()

# If connection fails, you can try reconnecting in a loop or handle accordingly
if voc is None:
    print("Reconnection failed.")
else:
    print("Connection successful.")
