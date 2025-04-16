# file: phonebook_app.py

import psycopg2
import csv

DB_CONFIG = {
    'host': "localhost",
    'dbname': "phonebook_2",
    'user': "postgres",
    'password': "MirasPP2"
}

def connect():
    return psycopg2.connect(**DB_CONFIG)

# 1. Function: search by partial pattern (name, surname, phone)
def search_pattern(pattern: str):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
            return cur.fetchall()

# 2. Procedure: upsert user by name/phone
def upsert_user(name: str, phone: str):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    print(f"Upserted user: {name} -> {phone}")

# 3. Procedure: bulk insert users with validation
def bulk_insert(names: list[str], phones: list[str]):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL bulk_insert_users(%s, %s)", (names, phones))
    print("Bulk insert complete. Invalid phones (if any) logged in DB.")

# 4. Function: paginated view with limit/offset
def paginated_view(limit: int, offset: int):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paginate_phonebook(%s, %s)", (limit, offset))
            return cur.fetchall()

# 5. Procedure: delete by name or phone
def delete_by_name_or_phone(pattern: str):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_by_name_or_phone(%s)", (pattern,))
    print(f"Deleted records matching: {pattern}")

# Additional helpers (console/csv interaction)
def insert_from_console():
    name = input("Name: ")
    phone = input("Phone: ")
    upsert_user(name, phone)

def insert_from_csv(path: str):
    names, phones = [], []
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                names.append(row[0])
                phones.append(row[1])
    bulk_insert(names, phones)

def query_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook_2 ORDER BY id")
            return cur.fetchall()

def query_by_name(name: str):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook_2 WHERE name = %s", (name,))
            return cur.fetchall()

def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Insert single user (console)")
        print("2. Bulk insert from CSV")
        print("3. Upsert user")
        print("4. Search by pattern")
        print("5. View paginated")
        print("6. Delete by name or phone")
        print("7. Show all")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv(input("CSV file path: "))
        elif choice == '3':
            upsert_user(input("Name: "), input("Phone: "))
        elif choice == '4':
            for row in search_pattern(input("Pattern: ")):
                print(row)
        elif choice == '5':
            try:
                limit = int(input("Limit: "))
                offset = int(input("Offset: "))
                for row in paginated_view(limit, offset):
                    print(row)
            except ValueError:
                print("Invalid input for limit/offset")
        elif choice == '6':
            delete_by_name_or_phone(input("Name or phone to delete: "))
        elif choice == '7':
            for row in query_all():
                print(row)
        elif choice == '8':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
