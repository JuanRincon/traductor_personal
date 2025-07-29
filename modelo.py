import mysql.connector
from mysql.connector import errors

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
