# Name: Harsh Singh
# Date: 2025-11-30
# Assignment: Library Inventory System - Book Class

class Book:
    def __init__(self, title, author, isbn, available=True, borrow_count=0):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.borrow_count = borrow_count  # for analytics

    def borrow(self):
        if self.available:
            self.available = False
            self.borrow_count += 1
            return True
        return False

    def return_book(self):
        self.available = True

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available,
            "borrow_count": self.borrow_count
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["author"],
            data["isbn"],
            data["available"],
            data.get("borrow_count", 0)
        )
