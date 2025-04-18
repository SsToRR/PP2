from insert_user import insert_user
from insert_by_csv import insert_csv
from upsert_user import upsert_user
from search import search_by_pattern
from paginate import view_paginated
from delete_user import delete_by_pattern
from show_all import show_all

def menu():
    while True:
        print("\n=== PHONEBOOK MENU ===")
        print("1. Insert single user")
        print("2. Insert users from CSV")
        print("3. Upsert user (update if exists)")
        print("4. Search by pattern")
        print("5. View paginated")
        print("6. Delete by name or phone")
        print("7. Show all entries")
        print("8. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            insert_user(input("Name: "), input("Phone: "))
        elif choice == '2':
            insert_csv(input("CSV file path: "))
        elif choice == '3':
            upsert_user(input("Name: "), input("Phone: "))
        elif choice == '4':
            for row in search_by_pattern(input("Search pattern: ")):
                print(row)
        elif choice == '5':
            limit = int(input("Limit: "))
            offset = int(input("Offset: "))
            for row in view_paginated(limit, offset):
                print(row)
        elif choice == '6':
            delete_by_pattern(input("Name or phone to delete: "))
        elif choice == '7':
            for row in show_all():
                print(row)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
