# Reflektion – Biblioteket

Skriv kort med egna ord. Om du inte hann ett steg, skriv det i stället för att gissa.

1. Vilka steg hann du? Vad var svårast att förstå?

2. Vad är skillnaden mellan `Book` och `Library`?

3. Vad ändras när en bok lånas? Var låg informationen i dictionary-versionen respektive i `Book`-versionen?

4. Vad lagrar `Library` i `self.books`? Vad syftar `self` på i `Library.add_book()` och vad syftar parametern `book` på?

5. Varför skapas ingen ny, självständig kopia av en `Book` när du lägger till den i `Library`?

6. Varför kan `count_available()` rimligen tillhöra `Library`, och varför kan `borrow()` rimligen tillhöra `Book`?

7. Hur kan ett object anropa en method på ett annat object? Ge ett exempel från labben.

8. Varför returnerar `borrow()` `False` om boken redan är lånad? Vad händer med bokens `is_borrowed` då?

9. Vad gör `__init__` när du skapar `second = Book("Another Title", "Another Author")`? Vilket object syftar `self` på i `first.borrow()`?

10. Vilket fel fick du när du tog bort `self` ur `borrow`? Vad lärde du dig av felmeddelandet?
