# Library Inventory System (Python OOP Project)

A modular and object-oriented **Library Inventory System** implemented in Python.  
This project simulates a real-world library by allowing users to add books, register members, borrow/return books, and store all data using JSON files for persistence.

---

## Features

### Core Operations
- Add new books to the library  
- Register library members  
- Borrow books (with availability checks)  
- Return borrowed books  
- View borrowed books per member  

### Data Persistence
- Automatically saves all books and member data to JSON  
- Loads saved data automatically when the system restarts  
- Handles missing or corrupted files using try-except  

### Analytics Report
Includes:
- Most borrowed book  
- Total number of active members  
- Number of books currently borrowed  

### Interactive User Menu
Provided through `main.py`:

# Library Inventory System (Python OOP Project)

A modular and object-oriented **Library Inventory System** implemented in Python.  
This project simulates a real-world library by allowing users to add books, register members, borrow/return books, and store all data using JSON files for persistence.

---

## Features

### Core Operations
- Add new books to the library  
- Register library members  
- Borrow books (with availability checks)  
- Return borrowed books  
- View borrowed books per member  

### Data Persistence
- Automatically saves all books and member data to JSON  
- Loads saved data automatically when the system restarts  
- Handles missing or corrupted files using try-except  

### Analytics Report
Includes:
- Most borrowed book  
- Total number of active members  
- Number of books currently borrowed  

### Interactive User Menu
Provided through `main.py`:

## Project Structure

library_system/
│
├── book.py # Book class (title, author, ISBN, availability)
├── member.py # Member class (name, ID, borrowed books)
├── library.py # Core logic: add, register, lend, return, save/load
├── main.py # User menu + program entry point
│
├── books.json # Auto-generated book records storage
└── members.json # Auto-generated member records storage


