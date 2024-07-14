#!/bin/bash
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"'{title}' not found in the library.")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"'{title}' not found in the library.")
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")

if __name__ == "__main__":
    # Example usage
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))
    library.list_available_books()
    library.check_out_book("1984")
    library.list_available_books()
    library.return_book("1984")
    library.list_available_books()
