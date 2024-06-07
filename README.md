# PPY
Jakub Jankiewicz
s25463

Dokumentacja Projektu: Gra "Escaperom" w Pythonie

# Opis Projektu
gracz eksploruje różne pokoje zamku, rozwiązując zagadki, aby przechodzić do kolejnych pomieszczeń i ostatecznie znaleźć wyjście. Gra oferuje funkcje zapisu i wczytywania stanu gry.

# Pliki w Projekcie
main.py: Główny skrypt uruchamiający grę i obsługujący interakcje gracza.
gameplay.py: Skrypt definiujący główną logikę gry.
pokoj.py: Skrypt definiujący klasę pokoju i obsługę zagadek.
zagadka.py: Skrypt definiujący klasę zagadki.

# Opcje Gry
Nawigacja: Gracz porusza się między pokojami używając komend north, south, east, west.
Rozwiązywanie zagadek: Gracz musi rozwiązać zagadki w pokojach, aby przejść dalej.
Zapis gry: Gracz może zapisać stan gry wpisując save.
Wczytanie gry: Gracz może wczytać stan gry wpisując load.
Wyjście z gry: Gracz może wyjść z gry wpisując quit.

# Opis Funkcjonalności

## Moduł Gameplay

### Główny Skrypt Gry (main.py)
- `gameplay = Gameplay()`: Tworzy nową instancję gry.
- `gameplay.start()`: Rozpoczyna grę, wywołując metodę `start()` klasy `Gameplay`.

### Klasa Gameplay
- `__init__(self)`: Inicjalizuje nową grę poprzez utworzenie pokoi za pomocą metody `createRooms()`.
- `createRooms(self)`: Tworzy pokoje, definiuje ich połączenia oraz losuje zagadki dla poszczególnych pokojów.
- `start(self)`: Rozpoczyna rozgrywkę, wyświetlając powitanie i kontrolując przebieg gry.
- `saveGameplay(self, filename)`: Zapisuje stan gry do pliku za pomocą biblioteki `pickle`.
- `loadGameplay(filename)`: Wczytuje stan gry z pliku za pomocą biblioteki `pickle`.

### Funkcje Klasowe
- `saveGameplay(self, filename)`: Metoda zapisująca stan gry do pliku.
- `loadGameplay(filename)`: Metoda wczytująca stan gry z pliku.

## Moduł Pokój (pokoj.py)

### Klasa Pokoj
- `__init__(self, name, description)`: Inicjalizuje pokój z określoną nazwą, opisem oraz losowo wybraną zagadką.
- `addRelation(self, direction, room)`: Dodaje połączenie z innym pokojem w określonym kierunku.
- `getRelation(self, direction)`: Zwraca pokój połączony z obecnym w określonym kierunku.
- `hasQuest(self)`: Sprawdza, czy pokój ma zagadkę do rozwiązania.
- `solve_puzzle(self, answer)`: Rozwiązuje zagadkę w pokoju, sprawdzając odpowiedź gracza.

## Moduł Zagadka (zagadka.py)

### Klasa Zagadka
- `__init__(self, question, answer)`: Inicjalizuje zagadkę z zadanym pytaniem i odpowiedzią.
- `solve(self, givenAnswer)`: Sprawdza, czy odpowiedź gracza zgadza się z odpowiedzią na zagadkę (ignoruje wielkość liter).


# Wymagania
Python 3.x
# Struktura Kodu
main.py
python

# Uwagi
Gra oferuje interaktywny sposób na eksplorację zamku i rozwiązywanie zagadek.
Funkcje zapisu i wczytywania gry pozwalają na przerwanie i kontynuowanie rozgrywki w dowolnym momencie.
Przykłady zagadek mogą być rozszerzone o dodatkowe pytania i odpowiedzi, aby zwiększyć różnorodność gry.
