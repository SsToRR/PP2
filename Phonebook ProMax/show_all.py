from connect import connect

def show_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook_2 ORDER BY id")
            return cur.fetchall()
