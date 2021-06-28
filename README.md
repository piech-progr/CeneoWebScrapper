<br>
#### Projekt powstał w ramach zajęć PP2
<br>
##### Aplikacja ma na celu pobieranie i wyświetlanie opinii wybranego produktu z serwisu Ceneo.pl
##### Została napisana przy użyciu języka Python, JavaScript, HTML oraz CSS.
##### Korzysta z bibliotek: Flask, Flask-Markdown, Flask WTForms, Jinja, Beautifulsoup4, Requests, SweetAlert.
##### Podczas tworzenia aplikacji zastosowano podejście obiektowe

<br>

##### Etap 1. Pobranie składowych pojedynczych opiii
- pobranie kodu pojedynczej strony z opiniami
- wyodrębnienie z kodu strony pojedynczej opinii
- pobranie do pojedynczych zmiennych poszczególnych składowych na podstawie selektorów
- obsługa błędów
- dobranie typów danych do wartości zmiennych


##### Etap 2. Ekstrakcja wszystkich opinii o produkcie z pojedynczej strony
- zapis składowych pojedynczej opinii do słownika
- zdefiniowanie listydo przechowywania wszystkich opinii o danym produkcie
- dodanie pętli, która wykonuje operację ekstracji dla wszystkich opinii pobranych z pojedynczej strony

##### Etap 3. Ekstrakcja wszystkich opinii o produkcie z wszystkich stron
- dodanie pętli, która pobiera i analizuje kolejne strony z opiniami o produkcie
- dodanie możliwości podania kodu produktu "z klawiatury"
- dodanie zapisu wszystkich opinii o produkcie do pliku .json

##### Etap 4. Refactoring
- zdefiniowanie funkcji do ekstrakcji pojedynczego elementu opinii
- przygotowanie słownika opisującego składowe opinii wraz z ich selektorami
- tworzenie słownika reprezentującego pojedyncząopinię przy wykorzstaniu wyrażenia słownikowego (dictionary comprehension)

##### Etap 5. DataFrame i statystyki
- wyświetlenie listy produktów, dla których pobrane zostały opinie
- wczytanie opinii o wskazanym produkcie do obiektu DataFrame
- obliczenie podstawowych statystyk
    * średnia ocena produktu
    * liczba opinii o produkcie
    * liczba opinii dla których podana została liczba zalet
    * liczba opinii dla których podana została liczba wad

##### Etap 6. Rysowanie wykresów opartych o dane z pobranych opinii
- wykres słupkowy/kolumnowy obrazujący częstość występowania opinii z poszczególnymi ocenami
- wykres kołowy obrazujący udział poszczególnych rodzajów rekomendacji w zbiorze opinii

##### Etap 7. Stworzenie webowej wersji aplikacji
- stworzenie strukturalnej wersji projektu
- zainstalowanie biblioteki Flask
- zainstalowanie biblioteki Jinja
- dodanie routingów
- stworzenie szablonu strony opartego na technologii bootstrap

##### Etap 8. Praca własna
- stworzenie contentu na stronie głównej przy użyciu biblioteki Flask Markdown
- stworzenie walidacji wpisywanego kodu ekstrakcji za pomocą biblioteki WTForms
- dodanie animowanych komunikatów o błędzie za pomocą biblioteki SweetAlert
- poprawa wizualnego widoku strony
    * edycja navbara
    * stworzenie footera
    * zmiana szaty graficznej
- dodanie contentu na podstronie o autorze
- dodanie biblioteki Pandas
- dodanie przycisku pobierania

