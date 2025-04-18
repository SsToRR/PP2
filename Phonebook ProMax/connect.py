import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="phonebook_2",
            user="postgres",
            password="MirasPP2"
        )
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print("Connection failed:", error)
