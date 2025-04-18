from connect import connect

def insert_user(name, phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook_2(name, phone) VALUES (%s, %s)", (name, phone))
    print(f"Inserted: {name} -> {phone}")
