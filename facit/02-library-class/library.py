"""Reference solution, final version: Library class. Run: python library.py"""

from book import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            book.show_status()

    def count_available(self):
        count = 0
        for book in self.books:
            if not book.is_borrowed:
                count = count + 1
        return count

    def find_books(self, search_text):
        matches = []
        search_lower = search_text.lower()
        for book in self.books:
            if search_lower in book.title.lower():
                matches.append(book)
        return matches


library = Library()
first = Book("The Northern Light", "Alex Storm")
second = Book("Midnight Harbor", "Sam Rivers")
third = Book("The Quiet Forest", "Jo Lind")
library.add_book(first)
library.add_book(second)
library.add_book(third)

print("Alla böcker:")
library.list_books()

print()
if first.borrow():
    print("Lånet lyckades.")
else:
    print("Boken är inte tillgänglig.")
if first.borrow():
    print("Lånet lyckades.")
else:
    print("Boken är inte tillgänglig.")
library.list_books()
print("Antal tillgängliga:", library.count_available())

if first.return_book():
    print("Boken lämnades tillbaka.")
else:
    print("Boken var inte lånad.")
print("Antal tillgängliga:", library.count_available())

print()
search_text = input("Sök titel: ")
matches = library.find_books(search_text)
if len(matches) == 0:
    print("Inga böcker hittades.")
else:
    for book in matches:
        book.show_status()
