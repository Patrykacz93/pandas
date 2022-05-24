Projekt z analizy danych

Poniższy projekt zwiera dane samochodowe zapisane w pliku csv. oraz funkcje napisane w języku python w celu 
wyczyszczenia pól ze zbędnych danych takich jak puste pola czy średniki. Dodatkowo zostały utworzone funkcje:

- obliczania wartości średnich, 
- zmiany typu komórek, 
- dodawana nowych kolumn do tabeli o dowolnych paramertach, 
- wyznaczania dowolnego wiersza,
- przeszukiwanie kolumny z nazwami samochodów w celu znaleznienia danych modelów,
- funkcja zamieniająca wartości kolumn Series miejscami

W ostatnim etapie podane funkcje zostały wykorzystane do przedstawienia danych na wykresach które zostaja zapisane do folderu 'charts' w formacie pdf.

Plik csv znajduje się w folderze data;

Przed uruchomieniem programu należy zainstalować odpowiednie biblioteki lub skorzystac w pliku requirements;

pip install matplotlib
pip install seaborn
pip install numpy
pip install pandas