# Hjälp när du fastnar

- Kör efter varje liten ändring. Läs felmeddelandets **sista rad**, sedan filnamn och radnummer.
- Prova en bok först, därefter två. Skriv ut `first.is_borrowed` och `second.is_borrowed` för att se vilket object som ändrades.
- Om du får `NameError`, kontrollera stavning, var namnet definieras och om `Book` importeras från `book.py`.
- Om du får `TypeError` när en method anropas, jämför definitionen med anropet. Har du glömt `self`?
- Om du får `AttributeError`, kontrollera att attributet verkligen skapas i `__init__` och har samma stavning som där det läses.
- Om ett andra lån lyckas trots att boken är lånad, kontrollera villkoret och att `is_borrowed` ändras på rätt object.
- Om en sökning inte hittar titeln, skriv ut både söktext och titel efter `.lower()`.
- Om en method på `Library` ger fel om `self`, kontrollera att `self` finns först i methodens parametrar och att du anropar den på ett bibliotek, till exempel `library.list_books()`.
- Inne i en `Library`-method ska du använda `self.books` för bibliotekets lista. `books` utan `self` fungerar bara om du själv har definierat en lokal variabel med det namnet.
- Kontrollera att `add_book` lägger till parametern `book` med `self.books.append(book)`. Om du råkat lägga till `book.title` eller en textsträng innehåller listan inte ett `Book`-object.
- Om du får fel när du anropar `show_status()` eller `borrow()`, kontrollera att du anropar metoden på en bok, till exempel `book.show_status()`, inte på biblioteket eller på hela listan.
- `library.books` är bibliotekets lista med böcker; `library` är inte en enskild `Book`. Skriv ut `type(library.books)` och `type(library.books[0])` när listan inte är tom.
- Kontrollera att loopen går igenom rätt lista: inne i `Library` ska den gå igenom `self.books`. I fristående kod går den igenom listvariabeln som skickas in.
- Efter steg 7 innehåller listan `Book`-object, inte dictionaries. Använd då `book.title` och `book.is_borrowed`, inte `book["title"]`.
- Om du är osäker på vad listan innehåller, skriv tillfälligt `print(type(books[0]))`: före OOP-steget är det `dict`, efteråt bör det vara `Book`.

En enkel Git-rutin efter ett fungerande steg:

```bash
git status
git add library.py REFLECTION.md
git commit -m "Describe completed step"
git push
```

Lägg även till `book.py` när du skapat den. Gör en `commit` av det som fungerar, även om du behöver hjälp med nästa steg.
