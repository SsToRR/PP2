from connect import connect

def view_paginated(limit, offset):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paginate_phonebook(%s, %s)", (limit, offset))
            return cur.fetchall()
