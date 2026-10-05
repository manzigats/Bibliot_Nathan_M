"""Reference solution, part 1: Book objects in a list (steps 5-8). Run: python library.py"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def show_status(self):
        if self.is_borrowed:
            print(self.title + " av " + self.author + " - lånad")
        else:
            print(self.title + " av " + self.author + " - tillgänglig")

    def borrow(self):
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    def return_book(self):
        if not self.is_borrowed:
            return False
        self.is_borrowed = False
        return True


def count_available(books):
    count = 0
    for book in books:
        if not book.is_borrowed:
            count = count + 1
    return count


def find_books(books, search_text):
    matches = []
    search_lower = search_text.lower()
    for book in books:
        if search_lower in book.title.lower():
            matches.append(book)
    return matches


books = []
books.append(Book("The Northern Light", "Alex Storm"))
books.append(Book("Midnight Harbor", "Sam Rivers"))
books.append(Book("The Quiet Forest", "Jo Lind"))

print("Alla böcker:")
for book in books:
    book.show_status()

print()
if books[0].borrow():
    print("Lånet lyckades.")
else:
    print("Boken är inte tillgänglig.")
if books[0].borrow():
    print("Lånet lyckades.")
else:
    print("Boken är inte tillgänglig.")

print()
for book in books:
    book.show_status()
print("Antal tillgängliga:", count_available(books))

if books[0].return_book():
    print("Boken lämnades tillbaka.")
else:
    print("Boken var inte lånad.")
print("Antal tillgängliga:", count_available(books))

print()
search_text = input("Sök titel: ")
matches = find_books(books, search_text)
if len(matches) == 0:
    print("Inga böcker hittades.")
else:
    for book in matches:
        book.show_status()
