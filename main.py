# Name: Harsh Singh
# Date: 2025-11-30
# Assignment: Library Inventory System - Main Menu

from library import Library

lib = Library()

print("\n=== Welcome to the Library Inventory System ===")

while True:
    print("""
1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. View Library Report
6. Exit
    """)

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Book Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        lib.add_book(title, author, isbn)
        print("Book added successfully.")

    elif choice == "2":
        name = input("Member Name: ")
        member_id = input("Member ID: ")
        lib.register_member(name, member_id)
        print("Member registered successfully.")

    elif choice == "3":
        mem = input("Member ID: ")
        book_isbn = input("Book ISBN: ")
        ok, msg = lib.lend_book(mem, book_isbn)
        print(msg)

    elif choice == "4":
        mem = input("Member ID: ")
        book_isbn = input("Book ISBN: ")
        ok, msg = lib.take_return(mem, book_isbn)
        print(msg)

    elif choice == "5":
        print("\n=== Library Report ===")
        mb = lib.most_borrowed_book()
        if mb:
            print(f"Most borrowed book: {mb[0]} ({mb[1]} times)")
        print(f"Total members: {lib.count_active_members()}")
        print(f"Books currently borrowed: {lib.borrowed_books_count()}")

    elif choice == "6":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")
