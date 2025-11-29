# Library Inventory System (Python OOP Project)

A modular and object-oriented Library Inventory System implemented in Python.
This project simulates a real-world library by allowing users to add books, register members, borrow/return books, and store all data using JSON files for persistence.

# Features
Core Operations

Add new books to the library

Register library members

Borrow books (with availability checks)

Return borrowed books

View borrowed books per member

Data Persistence

Automatically saves all books and member data to JSON

Data is reloaded every time the program restarts

Error handling for missing/corrupted files

Analytics Report

Includes simple insights such as:

Most borrowed book

Total number of active members

Number of books currently borrowed

Interactive User Menu

The main.py file provides a command-line menu for easy interaction:

1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. View Library Report
6. Exit

📁 Project Structure
library_system/
│
├── book.py           # Book class (title, author, ISBN, availability)
├── member.py         # Member class (name, ID, borrowed books)
├── library.py        # Core logic: add, register, lend, return, save/load
├── main.py           # User interface (interactive menu)
│
├── books.json        # Auto-generated book records
└── members.json      # Auto-generated member records

🧩 File Overview
book.py

Defines the Book class

Tracks:

Title

Author

ISBN

Availability

Borrow count (for analytics)

member.py

Defines the Member class

Stores:

Member name

Member ID

List of borrowed book ISBNs

library.py

Handles all core processing:

Add books

Register members

Borrow/return operations

JSON file save/load

Analytics generation

main.py

Runs an interactive loop menu for user operations.
