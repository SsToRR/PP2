from connect import connect

def delete_by_pattern(pattern):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_by_name_or_phone(%s)", (pattern,))
    print(f"Deleted entries for: {pattern}")
