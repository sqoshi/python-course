###Task 01
Program przeiwduję oceny użytkowników na podsatwie określonej ilości danych. Regresja Liniowa.
1. a - regresja liniową na całym zbiorze użytkowników dla m=10,1000,10000. Błędy widoczne na grafach po włączeniu opcji --graphs.
2. b - Za pomocą regresji liniowej na zbiorze treningowym wyznaczamy predykcję wartości zbioru testowego.
Przewidywanie dla m=10,100,200,500,1000,10000. Wyświetlony zostaje wynik predykcji dla 15 wymaganych użytkowników. Addytywnie graf pod --graphs.
#### Uruchamianie
options dla a oraz b:
 1. --graphs  umieszczenie tej opcji w argumentach umożliwia wizualizację.
 2. --round   zaokrągla otrzymae wyniki do 0,5 oraz ogranicza ich zakres na <1,5>

np.:
~~~
python3 Task_01.py a --graphs --round
python3 Task_01.py a --graphs 
python3 Task_01.py b --graphs 
~~~

###Task 02
System przewidujący rekomendację dla użytkownika na podstawie ich kilku ocen, addytywnie proste gui w tkinter.
#### Uruchamianie
~~~
python3 Task_02.py
~~~