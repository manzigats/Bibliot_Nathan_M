# Biblioteket – Pythonrepetition och grundläggande OOP

Du bygger ett litet terminalprogram där böcker kan lånas och lämnas tillbaka. Du börjar med variabler, `if`, listor och funktioner. När det fungerar bygger du om **boken** från en `dict` till ett `Book`-object. Sedan skapar du en `Library` som håller reda på flera `Book`-object och kan arbeta med dem.

Det här är en övning, **inte en examination**. Arbeta i ordning. Gör en `commit` efter varje fungerande steg; om du inte hinner allt är det viktigare att du förstår de första stegen. Du behöver Python och Git, men inga externa paket. Vänta med arv, `@property` och avancerad felhantering.

## Kom igång

1. Öppna lärarens publika GitHub-template och välj **Use this template → Create a new repository**. Skapa ditt eget **private** repo.
2. Klona ditt eget repo och öppna mappen i VS Code.
3. Öppna `library.py`. Börja med den filen och kör `python library.py` (eller `python3`/`py` beroende på dator).
4. Läs ett steg i taget. Prova varje kontrollpunkt innan du gör en `commit` och går vidare. Använd [HJALP.md](HJALP.md) när du fastnar.

## Steg 1 – En bok

Skapa variablerna `title = "The Northern Light"`, `author = "Alex Storm"` och `is_borrowed = False` i `library.py`. Skriv ut titel, författare och om boken är tillgänglig. Använd ett `if`/`else` för statusen, så att du skriver **tillgänglig** när `is_borrowed` är `False`.

**Kontroll:** Ändra tillfälligt `is_borrowed` till `True`; statusen ska ändras utan att du ändrar ditt `if`/`else`. Återställ sedan till `False`.

**Commit:** `Add first book and availability`

## Steg 2 – Låna och lämna tillbaka

Använd `if` för att låna boken: om den är tillgänglig, sätt `is_borrowed = True` och skriv att lånet lyckades. Om den redan är lånad, skriv att den inte är tillgänglig. Lägg därefter till ett liknande villkor för att lämna tillbaka den. Prova även att låna den två gånger i rad och att lämna tillbaka den två gånger i rad. Beskriv i reflektionen vad som bör hända vid det andra försöket.

**Kontroll:** Efter ett lyckat lån ska statusen vara lånad; efter återlämning ska den vara tillgänglig. Ett misslyckat andra lån ska inte ändra statusen.

**Commit:** `Handle borrowing and returns`

## Steg 3 – Flera böcker

Byt från fristående variabler till en `list` med tre `dict`. Varje dictionary ska ha nycklarna `title`, `author` och `is_borrowed`. Använd första boken och hitta på två till. Gör en `for`-loop som visar titel och om varje bok är ledig. Ta bort eller kommentera bort gamla körningar från steg 2 som annars lånar och återlämnar samma bok automatiskt varje gång programmet körs.

**Kontroll:** Tre olika böcker visas. Om du ändrar `is_borrowed` för en bok ska bara den bokens status ändras. Lägg till en fjärde bok för att se att loopen hittar den.

**Commit:** `List books with dictionaries`

## Steg 4 – Funktioner med parameters

Skriv `show_book(book)` som får en dictionary och skriver ut titel och status. Skriv `borrow_book(book)` och `return_book(book)` som ändrar dictionaryn bara när ändringen är tillåten. Använd funktionerna på olika böcker i listan. Låt `borrow_book` och `return_book` returnera `True` när status ändrades och `False` annars; använd gärna returvärdet för ett meddelande utanför funktionen.

**Kontroll:** Låna den första boken två gånger. Returvärdena blir `True` och `False`. Den andra boken påverkas inte. Återlämna första boken och kontrollera att den går att låna igen.

**Commit:** `Extract book functions`

## Steg 5 – Skapa class Book

Skapa `class Book` i `library.py`. Skriv `__init__(self, title, author)` som sätter `self.title`, `self.author` och `self.is_borrowed = False`. Skapa först `first = Book("The Northern Light", "Alex Storm")` och skriv ut dess attribut. Skapa sedan `second` med annan titel och författare. På detta steg behöver du ännu inte flytta lånefunktionerna.

**Kontroll:** Båda böckerna börjar som tillgängliga och har olika titel. Skriv tillfälligt `first.is_borrowed = True` och kontrollera att `second.is_borrowed` fortfarande är `False`. Återställ sedan första boken eller skapa den på nytt.

**Commit:** `Add Book class and constructor`

## Steg 6 – Flytta beteendet till methods

Flytta logiken från `show_book`, `borrow_book` och `return_book` till methods på `Book`: `show_status(self)`, `borrow(self)` och `return_book(self)`. `borrow` och `return_book` ska returnera `True` vid en ändring och `False` annars. Välj om `show_status` skriver ut texten eller returnerar en sträng, men använd samma val konsekvent. Ta bort eller kommentera bort de gamla procedurala funktionerna när de nya fungerar.

**Kontroll:** `first.borrow()` lyckas första gången och misslyckas andra gången. Efter `first.return_book()` är den tillgänglig. `second` ska hela tiden ha sin egen status.

**Commit:** `Move book behavior into methods`

## Steg 7 – En lista med Book-object

Skapa minst tre `Book`-object och lägg dem i en `list` som heter `books`. Använd en loop för att visa varje boks status. Låna den första boken och skriv sedan ut alla statusar igen. Förklara för dig själv vad variabeln `self` syftar på när du anropar `books[0].borrow()` respektive `books[1].borrow()`.

**Kontroll:** Lånet av `books[0]` ändrar bara den första boken. Din lista ska innehålla `Book`-object, inte de gamla dictionaries. Efter detta steg ska programmets normala körning använda OOP-versionen.

**Commit:** `Use independent Book objects`

## Steg 8 – Sök och räkna i listan

Låt användaren skriva en del av en titel med `input()`. Gå igenom listan och skriv ut matchande böcker, oavsett stora och små bokstäver. Om inget matchar, skriv ett tydligt meddelande. Räkna också hur många böcker som är tillgängliga och visa antalet. Skriv en fristående funktion `count_available(books)` som får listan och returnerar ett tal. Nu arbetar du med hela listan, inte med bara en `Book`.

**Kontroll:** Sökningen `nOrTh` hittar `The Northern Light`. Sökning utan träffar ger ett meddelande. Om en av tre böcker är lånad ska antalet tillgängliga vara 2. Prova också en tom lista och se att antalet blir 0.

**Commit:** `Search books and count available titles`

## Steg 9 – Skapa class Library

Skapa `class Library` i `library.py`:

```python
class Library:
    def __init__(self):
        self.books = []
```

Skapa ett `Library`-object. `library` är ett object och `library.books` är en lista. Senare ska listan innehålla referenser till `Book`-object. Skapa gärna två `Library`-object och jämför deras listor: varje bibliotek ska börja med sin egen tomma lista. Lägg ännu inte till några metoder.

**Kontroll:** Skriv ut `library.books` och kontrollera att den är tom. Lägg tillfälligt till något i det ena bibliotekets lista och kontrollera att det andra bibliotekets lista fortfarande är tom. Ta sedan bort testvärdet igen innan du fortsätter.

**Commit:** `Add Library class`

## Steg 10 – Lägg till Book-object i Library

Lägg till en method på `Library` som tar emot ett object och lägger det i listan:

```python
def add_book(self, book):
    self.books.append(book)
```

Skapa minst två `Book`-object och lägg till dem med `library.add_book(first)` och `library.add_book(second)`. Tänk efter: vad syftar `self` på i methoden, och vad syftar parametern `book` på? Skapas en kopia av `Book`-objectet, eller vad innehåller `library.books`?

**Kontroll:** Listan innehåller båda böckerna. Låna `first` och kontrollera att samma bok i bibliotekets lista nu är lånad.

**Commit:** `Add books to library`

## Steg 11 – Visa böcker genom Library

Lägg till en method `list_books(self)` i `Library`. Använd en `for`-loop som går igenom `self.books` och anropar `show_status()` på varje bok, till exempel:

```python
def list_books(self):
    for book in self.books:
        book.show_status()
```

Låt metoden själv visa böckerna; den behöver inte returnera en ny lista.

**Kontroll:** När du anropar `library.list_books()` visas status för flera olika `Book`-object. Kontrollera att en lånad bok visas som lånad och att de andra fortfarande har sina egna statusar.

**Commit:** `List library books`

## Steg 12 – Räkna genom Library

Du har redan provat den fristående funktionen `count_available(books)`. Nu när `Library` äger boklistan kan du prova att flytta räknandet till en method `count_available(self)` i `Library`, som använder `self.books`. Jämför anropen `count_available(books)` och `library.count_available()`. Förklara varför båda sätten kan fungera och varför det kan kännas tydligare att låta `Library` räkna när den äger samlingen. Det är ett val, inte en absolut regel. Du kan också prova att flytta titelsökningen till en `find_books(self, search_text)`-method, men det är frivilligt.

**Kontroll:** Med en lånad bok av tre ska båda varianterna räkna två tillgängliga böcker. Prova också en tom lista i den fristående funktionen eller ett tomt bibliotek.

**Commit:** `Count available books in Library`

## Steg 13 – Modules och felsökning

Flytta `class Book` till en ny fil `book.py` och importera den i `library.py` med `from book import Book`. Låt `Library` ligga kvar i `library.py`; båda klasserna kan vara i samma mapp utan att skapa en paketstruktur. Kör programmet igen; output ska vara densamma. Prova därefter **tillfälligt** att skriva `def borrow():` utan `self` i `Book`. Anropa `first.borrow()`, läs felmeddelandet och återställ methoden. Skriv i reflektionen vad Python skickar in när du anropar en method på ett object.

**Kontroll:** Huvudprogrammet fungerar när `book.py` och `library.py` ligger i samma mapp. Den tillfälliga ändringen med saknat `self` ska vara borttagen innan din `commit`.

**Commit:** `Move Book class to module`

## Avsluta

Svara på [REFLECTION.md](REFLECTION.md), kör programmet, kontrollera `git status` och gör en sista `commit`. Gör sedan `push`. Om du inte hann allt, skriv vilka steg som fungerar. Det är användbar information inför nästa lektion.

**Commit:** `Reflect on library OOP practice`

### Om du blir klar tidigare

Lägg till ett `release_year` i `__init__` och visa utgivningsåret i status. Prova två olika år. Gör ett separat `commit`. Vänta med arv, privata attribut, `@property` och databaser.

## Facit (referenslösningar)

Mappen `facit/` innehåller referenslösningar som du kan köra med `python library.py` inifrån respektive mapp.

- `facit/01-book-objects` är en referenslösning för första delen av övningen (steg 5–8): `Book`-object i en lista, sök och räkna, före `Library`.
- `facit/02-library-class` är den slutliga referenslösningen med `Library`, `Book` i `book.py` och samarbete mellan object.

Försök först göra övningarna själv innan du jämför med facit. Lösningen är ett giltigt sätt att göra det på, inte nödvändigtvis det enda rätta.
