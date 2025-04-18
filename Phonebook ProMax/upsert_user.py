from connect import connect

def upsert_user(name, phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    print(f"Upserted: {name} -> {phone}")
