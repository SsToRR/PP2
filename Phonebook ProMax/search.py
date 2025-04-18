from connect import connect

def search_by_pattern(pattern):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
            return cur.fetchall()
