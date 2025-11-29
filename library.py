# Name: Harsh Singh
# Date: 2025-11-30
# Assignment: Library Inventory System - Library Logic

import json
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    # ---------------------------
    # ADDING BOOKS AND MEMBERS
    # ---------------------------

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_data()

    def register_member(self, name, member_id):
        self.members.append(Member(name, member_id))
        self.save_data()

    # ---------------------------
    # FINDERS
    # ---------------------------

    def find_book(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def find_member(self, member_id):
        return next((m for m in self.members if m.member_id == member_id), None)

    # ---------------------------
    # BORROW AND RETURN
    # ---------------------------

    def lend_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            return False, "Invalid member or book."

        if member.borrow_book(book):
            self.save_data()
            return True, "Book borrowed successfully."
        return False, "Book is not available."

    def take_return(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            return False, "Invalid member or book."

        if member.return_book(book):
            self.save_data()
            return True, "Book returned."
        return False, "Book was not borrowed by this member."

    # ---------------------------
    # FILE HANDLING
    # ---------------------------

    def save_data(self):
        try:
            with open("books.json", "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)

            with open("members.json", "w") as f:
                json.dump([m.to_dict() for m in self.members], f, indent=4)

        except:
            print("Error saving data.")

    def load_data(self):
        try:
            with open("books.json", "r") as f:
                books_data = json.load(f)
                self.books = [Book.from_dict(b) for b in books_data]
        except:
            self.books = []

        try:
            with open("members.json", "r") as f:
                members_data = json.load(f)
                self.members = [Member.from_dict(m) for m in members_data]
        except:
            self.members = []

    # ---------------------------
    # ANALYTICS FEATURE
    # ---------------------------

    def most_borrowed_book(self):
        if not self.books:
            return None
        mb = max(self.books, key=lambda b: b.borrow_count)
        return mb.title, mb.borrow_count

    def count_active_members(self):
        return len(self.members)

    def borrowed_books_count(self):
        return sum(1 for b in self.books if not b.available)
