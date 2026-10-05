"""Book class - reference solution."""

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

