import csv
from connect import connect

def insert_csv(path):
    names, phones = [], []
    with open(path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            names.append(row[0])
            phones.append(row[1])
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL bulk_insert_users(%s, %s)", (names, phones))
    print("Bulk insert complete.")
