# Lista 7 (Lab) Termin wysłania na SVN do 14.06.2020

Na tej liście należy korzystać z bibliotek uczenia maszynowego. Jej celem jest poznanie aktualnie wykorzystywanych narzędzi uczenia maszynowego. Wszystkie zadania wykonaj w notatniku jupyter. Proszę wysyłać tylko notatnik bez danych np. resnet50_coco_best_v2.1.0.h5 na SVN, przy wykorzystaniu ewentualnych innych danych proszę podać tylko linka.

## Zadanie 1 (10pt) Wykonaj zadanie 2 z listy 6 z wykorzystaniem Kerasa i Tensorflow. Wykonaj testy dla kilku funkcji aktywacji oraz dla wielu warstw sieci. Poeksperymentuj!
## Zadanie 2 (15pt) Wykorzystując architekturę sieci neuronowych RetinaNet Focal Loss for Dense Object Detection zaprogramuj wykrywanie obiektów. Możesz np. skorzystać z implementacji sieci w Kerasie razem z modelem uczonym na danych COCO object detection dataset. Instalacje biblioteki możesz przeprowadzić np. tak

    %pip install -q git+https://github.com/fizyr/keras-retinanet

    Pobierz nauczoną sieć w kerasie resnet50_coco_best_v2.1.0.h5 i przeprowadź wykrywanie obiektów dla COCO dataset

    labels_to_names = {
        0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane',
        5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light',
        10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench',
        14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow',
        20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack',
        25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee',
        30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite',
        34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard',
        37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass',
        41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl',
        46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli',
        51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake',
        56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed',
        60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse',
        65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave',
        69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book',
        74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear',
        78: 'hair drier', 79: 'toothbrush'}


    Przykładowy wynik jaki powinien otrzymać program. Tutaj na losowo wybranym zdjęciu ze strony ATP:

    retinanet
    Wykrywanie obiektów zrób na zdjęciu oraz z wykorzystaniem kamerki.

    import cv2
    from keras_retinanet.utils.image import read_image_bgr
    import matplotlib.pyplot as plt

    def grab_camera_snapshot(camera_id=0, fallback_filename='zdjecie.jpg'):
        camera = cv2.VideoCapture(camera_id)
        try:
            # bierzemy 15 klatek w praktyce dostajemy lepsze zdjęcia, bo
            # kamera lepiej dobierze kontrast i światło w ostatniej klatce
            for i in range(15):
                snapshot_ok, image = camera.read()
            if not snapshot_ok:
                print("Ups: could not access camera")
                if fallback_filename:
                    image = read_image_bgr(fallback_filename)
        finally:
            camera.release()
        return image

## Zadanie 3 (20pt) Zapoznaj się z różnymi modelami dostępnymi w Kerasie https://keras.io/applications/ oraz wykładem 12. Wybierz architekturę MobileNet lub Squeeze-and-Excitation network. Przeczytaj publikację i samodzielnie zaimplementuj ją w Kerasie. Postaraj się uzyskać dobrą wydajność na małych zbiorach danych np. CIFAR-10.

# Lista 6 (Lab) Termin wysłania na SVN do 24.05.2020 31.05.2020

Na tej liście nie korzystamy z bibliotek uczenia maszynowego np. keras. Jej celem jest poznanie algorytmów uczenia sieci neuronowych.

## Zadanie 1 (10pt) Zaimplementuj algorytm propagacji wstecznej przedstawiony na wykładzie 9 dla sieci neuronowej 3-4-1 (3-wejścia, 4-warstwa ukryta, 1-wyjście). Rozwiąż pokazany problem XOR. Następnie
        zamiast funkcji sigmoidalnej σ(x)=11−e−x

wykorzystaj funkcje aktywacji ReLU ReLU(x)=max(0,x).
wykorzystaj kombinacje funkcji sigmoidalnej σ
z ReLU np. warstwa ukryta ma σ a warstwa wyjściowa jest ReLU

    lub inne kombinacje. Poeksperymentuj!

Które rozwiązanie daje lepszą dokładność? Odpowiedź na to pytanie pisząc program testowy, który to pokazuje (np. po uruchomieniu w terminalu dostajemy wyniki dla różnych kombinacji z opisem). Rozwiąż ten problem również dla innych funkcji logicznych AND i OR. Dlaczego w danych wejściowych z przykładu z wykładu mamy ostatnią kolumnę z samymi jedynkami. Na to pytanie odpowiedź w komentarzu kodu źródłowego programu.

Dodatkowa uwaga: Część osób rozwiązując zadanie zauważyła (dostaje dużo pytań w tej sprawie), że możemy dostawać różne wyniki np. w implementacji z wykładu zmieniając 'sigmoid' na 'relu' i uruchamiając program za każdym razem możemy dostawać zbieżność do wektora np. [0.5, 0.5, 0.5, 0.5] lub [0, 0, 0, 0] lub to co oczekujemy czyli wartości bliskie funkcji XOR. Ten efekt to jest standardowy problem wykorzystywanych algorytmów uczenia (spadek gradientu) sieci neuronowych. Takie same wyniki otrzymamy w Kerasie (ostatni slajd) po zmianie z 'sigmoid' na 'relu' (nawet dla innych algorytmów uczenia). Po prostu wszystko zależy od wag początkowych, które w naszym przypadku (keras też tak robi) są losowe. Ale proszę zobaczyć np.

    def relu(x):
        return x * (x > 0)

    def relu_derivative(x):
        return 1. * (x > 0)

    np.random.seed(17)  # początkowy wybór wag WAŻNE

    class NeuralNetwork:
        ...
        self.eta = 0.01  # tak ważne jest zmniejszyć krok
        ...

    Przed print'ami dodajmy line z ustaleniem precyzji
        np.set_printoptions(precision=3, suppress=True)
        print(nn.output)
        print(nn.weights1)
        print(nn.weights2)

Wtedy "powinno" ładnie zbiegać do tego co oczekujemy. Po prostu wszystko zależy od początkowych wag i akurat dla np.random.seed(17) "udaje się". W innych przypadkach (inny seed) często wpada w lokalne minimum i nie wyskakuje (keras ma tak samo proszę to sprawdzić!). To nie jest tylko przypadek dla 'relu' dla przykładu z wykładu proszę tylko zmienić eta na 0.001

i już wpadniemy w [0.5, 0.5, 0.5, 0.5]. Podsumowując, wyniki warto robić nie tylko dla samych wyborów funkcji aktywacji, ale również wyboru wag i kroku eta! Ale w przypadku tego zadania i następnego wystarczy oddać tylko "dobre" przypadki, czyli dla odpowiednich wyborów np.random.seed i kroku eta przy ustalonych funkcjach aktywacji. Więcej informacji na ten temat.
## Zadanie 2 (15pt) Zaprojektuj sieć neuronową dwuwarstwową do aproksymacji funkcji np. sieć 1-5-1 lub 1-10-1 itp. i naucz ją funkcji (jedna funkcja dla jednej sieci)

    Weźmy dane wejściowe, jako próbkowana funkcja paraboliczna

    >>> x=np.linspace(-50,50,26)
    >>> y=x**2
    >>> plt.scatter(x,y)

    Sieć testuj dla wektora wejściowego

    >>> x=np.linspace(-50,50,101)
    >>> y - wynik sieci dla wejścia x
    >>> plt.scatter(x,y)

    Weźmy dane wejściowe, jako próbkowana funkcja sinus

    >>> x = np.linspace(0,2,21)
    >>> y = np.sin((3*np.pi/2) * x)
    >>> plt.scatter(x,y)

    Sieć testuj dla wektora wejściowego

    >>> x = np.linspace(0,2,161)
    >>> y = wynik sieci dla wejścia x
    >>> plt.scatter(x,y)

Dobierz też odpowiednie dla problemu funkcje aktywacji! Dokładnie σ
, ReLU lub tanh

    . W czasie uczenia pokazuj aproksymacje funkcji co np. 100 krok, czyli co 100 krok np. dla funkcji parabolicznej dla wektora x = np.linspace(-50,50,101) pokaż wynik działania sieci wykorzystując matplotlib. Dostaniemy animacje procesu uczenia sieci. Wyświetlaj jeszcze aktualny krok uczenia oraz błąd średnio-kwadratowy. Animacje procesu uczenia wykonaj dla dwóch powyższych zbiorów danych (parabola i sinus).

    Przykładowa animacja procesu uczenia dla paraboli (jaką powinien wykonywać program):
## Zadadnie 3 (20pt)* Wykonaj zadanie drugie dla sieci o trzech warstwach np. 1-10-10-1. Sam napisz algorytm propagacji wstecznej dla sieci trójwarstwowej. Jakie wyniki aproksymacji dostaniemy dla tej ,,głębszej'' sieci? 


# Lista 5 (Lab) Termin wysłania na SVN do 3.05.2020

Przy pisaniu programów (funkcji) NALEŻY stosować się do ogólnie przyjętego stylu programowania w języku Python. Proszę dokładnie przeczytać PEP 8 (tutorial, google python style) i PEP 257.

## Zadanie 1 (10pt) Napisz wykorzystując regresję liniową program, który na podstawie oceny filmów przez użytkowników będzie starał się przewidzieć ocenę innych użytkowników.
 Jako dane wykorzystamy zbiór MovieLens Latest Datasets. Dokładnie wybierzemy mniejszy zbiór, pobierz plik ml-latest-small.zip. Zadanie polega na wybraniu z pliku ratings.csv tych użytkowników (userId), którzy ocenili film 'Toy Story (1995)', który w tym pliku ma identyfikator '1' (patrz movies.csv). W tym pliku osób takich jest 215. Wtedy zgodnie z zapisem z wykładu xij będzie oceną i-tego użytkownika dla i=0,…,214, bo taki jest nasz zbiór osób, które oceniły 'Toy Story' oraz j będzie oceną j-tego filmu dla j=0,…,m. Jako j można wybrać movieId filmu, czyli np. film o movieId=42 oceniony przez użytkownika 5 (nie jest to userId, tylko piąta osoba ze zbioru 215 osób), który ocenił film jako np. 3.5 wpisujemy x[5,42]=3.5. Natomiast yi to ocena 'Toy Story' przez i-tego użytkownika. Zatem tworzymy macierz X=[xij] oraz wektor yi gdzie i=0,…,215 oraz j=0,…,m. Dla tak przygotowanych danych wykonujemy:

    regresje liniową na całym zbiorze użytkowników dla m=10,1000,10000
    
, czyli np. dla m=10 ignorujemy filmy o movieId>10
i robimy regresje dla tak okrojonego zbioru ocen. Jakie dostajemy błędy. Pokaż na wykresie.
podziel zbiór osób na tzw. zbiór treningowy oraz zbiór testowy np. weźmy i=0,…,200
to będzie zbiór treningowy i na takim zbiorze osób wykonajmy regresje natomiast później sprawdzamy już dla całości (215). Zatem ostatnie 15 ocen będziemy chcieli przewidzieć (zbiór testowy). Zrób przewidywanie dla m=10,100,200,500,1000,10000. Wyświetl wynik predykcji i wynik prawidłowy dla tych 15
osób.

Przykład danych do regresji jakie otrzymujemy dla m=10 i n=215
.
```
X = [[0.  4.  0.  0.  4.  0.  0.  0.  0.  0. ]
     [0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
     [0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
     [0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
     [0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
     [3.  0.  0.  0.  4.  0.  0.  0.  0.  0. ]
     [3.  3.  0.  0.  0.  2.  0.  0.  2.  0. ]
     [3.5 0.  0.  0.  0.  0.  0.  0.  5.  0. ]
     ...
y = [[4. ]
     [4. ]
     [4.5]
     [2.5]
     [4.5]
     [3.5]
     [4. ]
     [3.5]
     ...
```
## Zadanie 2 (15pt) Napisz system rekomendacji filmów. Systemy takie są wykorzystywane przez różne firmy np. Netflix organizował konkurs na opracowanie algorytmu, który będzie przewidywał ocenę użytkownika (Netflix Prize). W zadaniu tym zaimplementujemy podobny system, który jednak zamiast przewidywania będzie na podstawie preferencji użytkownika rekomendował filmy, które najprawdopodobniej mu się spodobają. Istnieje wiele sposobów, aby taki system napisać, dla zainteresowanych bardziej tematem proponuje zobaczyć np. Recommendation Systems. W tym zadaniu wybierzemy w miarę prosty i łatwy do implementacji system rekomendacji. Sformalizujmy problem. Załóżmy, że mamy macierz oceny, gdzie wiersze będą reprezentować użytkowników a kolumny filmy np. MatrixStar Wars IVAlice54Bob01John22Ada55
Patrząc na powyższą macierz widać, że kolumny pierwsza i druga mają podobne oceny stąd można wywnioskować, że filmy Matrix i Star Wars IV są (według użytkowników) podobne do siebie, czyli jeśli komuś podobał się Matrix to jest duża szansa, że będzie podobał mu się Star Wars i odwrotnie. Dlatego "podobieństwo" sformalizujemy przez wykorzystanie podobieństwa cosinusowego, czyli jeśli x=(x1,x2,…,xn) i y=(y1,y2,…,yn), wtedy: x1y1+x2y2+⋯+xnyn=x⋅y=∥x∥∥y∥cos(θ) Gdzie θ jest kątem między wektorami. Wygodniej będzie nam normalizować wektory. Wtedy x1y1+x2y2+⋯+xnyn=cos(θ). Wtedy cos(θ)

    reprezentuje podobieństwo jednego wektora do drugiego, czyli jak bardzo jedne oceny są bliskie innym. Dla naszej macierzy otrzymujemy

    >>> x = np.array([[5,0,2,5], [4,1,2,5]]).T
    >>> x
    array([[5, 4],
           [0, 1],
           [2, 2],
           [5, 5]])

    # obliczamy normę wektorów kolumnowych
    >>> np.linalg.norm(x, axis=0)
    array([7.34846923, 6.78232998])

    # obliczamy znormalizowaną macierz
    >>> x/np.linalg.norm(x, axis=0)
    array([[0.68041382, 0.58976782],
           [0.        , 0.14744196],
           [0.27216553, 0.29488391],
           [0.68041382, 0.73720978]])

    # teraz weźmy własną ocenę filmów Matrix - 4, Star Wars IV - 3
    # dla wygody zapisujemy jako wektor kolumnowy
    >>> y = [[4],[3]]

    # obliczamy podobieństwo cosinusowe z każdym użytkownikiem (skorzystamy z mnożenia macierzowego)
    >>> z=np.dot(x/np.linalg.norm(x, axis=0), np.array(y)/np.linalg.norm(y))
    >>> z
    array([[0.89819175],
           [0.08846517],
           [0.39466277],
           [0.98665692]])

    # normalizujemy otrzymany wektor (będzie on reprezentował nasz profil filmowy)
    >>> z/np.linalg.norm(z)
    array([[0.64422929],
           [0.06345177],
           [0.28307243],
           [0.70768107]])

    Teraz musimy obliczyć podobieństwo cosinusowe między naszym profilem a każdą kolumną macierzy, aby znaleźć takie filmy, które są podobne do naszego profilu. Sortujemy po otrzymanym podobieństwu i dostajemy rekomendacje. Wykorzystując nasz przykład, otrzymujemy

    >>> X = x/np.linalg.norm(x, axis=0)
    >>> Z = z/np.linalg.norm(z)
    >>> np.dot(X.T, Z)
    array([[0.99690104],
            [0.99448407]])

    Stąd dostaliśmy większą rekomendacje dla filmu Matrix (0.996) niż Star Wars IV (0.994). Co było oczywiście oczekiwane skoro nasza ocena była Matrix - 4, a Star Wars IV - 3. Możemy, teraz przejść do właściwej części zadania. Napisz system rekomendacji filmów który będzie wykorzystywał dane MovieLens Latest Datasets. Dokładnie mniejszy zbiór (który dodatkowo trochę jeszcze zmniejszymy). Pobierz plik ml-latest-small.zip. Interesować, będą nas głównie dwa pliki movies.csv oraz ratings.csv. W pliku ratings.csv mamy właściwie wszystkie dane, które będą nam potrzebne aby stworzyć macierz oceny. Ponieważ nawet w tym przypadku otrzymana macierz będzie dość duża dlatego w trakcie wczytywania danych z pliku proszę wziąć pod uwagę tylko te wiersze (z pliku ratings.csv) w których movie_id (druga kolumna) jest mniejsze od 10000 (resztę ignorujemy). Dla aktualnych danych ze strony otrzymamy, wtedy macierz mniej więcej 611x9019. Przykładowy wynik dla wybranego profilu filmowego:

    # wektor my_ratings odpowiada wektorowi y z przykładu wyżej
    my_ratings = np.zeros((9019,1))
    my_ratings[2571] = 5      # patrz movies.csv  2571 - Matrix
    my_ratings[32] = 4        # 32 - Twelve Monkeys
    my_ratings[260] = 5       # 260 - Star Wars IV
    my_ratings[1097] = 4
    my_ratings_norm = my_ratings/np.linalg.norm(my_ratings)

    ...

    # otrzymujemy wynik rekomendacji po posortowaniu
    # (cos(θ), movies_id)
    (0.8675507828468105, 260)
    (0.8362098349303669, 2571)
    (0.8227451213877744, 1196)
    (0.8002349214247857, 1210)
    (0.7458504689612442, 1097)
    (0.7286029159733108, 32)
    (0.7265369898748615, 1198)
    (0.7095672455110477, 1240)
    (0.7029872178855614, 1270)

Otrzymane reprezentacje wyświetl w postaci nazw filmów, korzystając z movies.csv. Uwaga: w rzeczywistych danych otrzymamy dużą liczbę zer, nawet całe kolumny, wtedy dostaniemy wartości NaN przy dzieleniu! Rozwiąż ten problem wykorzystując np.nan_to_num(...).
## Zadanie 3(20pt)* Napisz rekomendacje dla pełnego zbioru danych ml-latest.zip. Wykorzystaj do tego macierze rzadkie (sparse matrix) np. z pakietu scipy (lub inny sposób, który pozwala na obróbkę tak dużej ilości danych).

# Lista 4 (Lab) Termin wysłania na SVN do 12.04.2020

Przy pisaniu programów (funkcji) NALEŻY stosować się do ogólnie przyjętego stylu programowania w języku Python. Proszę dokładnie przeczytać PEP 8 (tutorial, google python style) i PEP 257.

    2020.03.30 - poprawki w zadaniach 2 i 3
    2020.04.04 - poprawki indeksów w zadaniu 5. Powinno być Z=(z0,z1,z2,…,z2n−1)

i Z∗=(z0,z1,z2,…,z2n−1)

## Zadanie 1 (5pt) Napisz dekorator, mający za zadanie
        drukować informacje o czasie wykonywania funkcji
## Zadanie 2 (5pt) Załóżmy, że mamy drzewo i reprezentujemy je na liście np. drzewo tree reprezentujemy jako

        ["1", ["2", ["4", ["8", None, None], ["9",None,None]], ["5",None,None]], ["3", ["6", None, None], ["7", None, None]]]

    Napisz funkcję która generuje w sposób losowy drzewo podanej wysokości oraz generator który przechodzi drzewo w porządku DFS i BFS.
## Zadanie 3 (5pt) Napisz klasę class Node(object) do reprezentacji pojedynczego węzła drzewa z dowolną liczbą potomków. Podobnie jak w zadaniu poprzednim napisz funkcję która generuje losowo drzewo o danej wysokości i generator który przechodzi drzewo w porządku DFS i BFS.
## Zadanie 4 (10pt) Przeciążenie funkcji (function overloading) daje możliwość wykorzystania tej samej nazwy funkcji, ale z różnymi parametrami. Na przykład w innych językach możemy napisać

      float norm(float x, float y) {            // norma Euklidesowa
        return sqrt(x*x + y*y)
      }
      float norm(float x, float y, float z) {   // norma taksówkowa
        return abs(x) + abs(y) + abs(z)
      }

    W języku Python nie ma przeciążenia funkcji, po prostu następna definicja nadpisuje poprzednią. Napisz dekorator nazwijmy go @overload, który pozwala na taką własność. Przykładowy program powinien wyglądać tak

      @overload
      def norm(x,y):
        return math.sqrt(x*x + y*y)

      @overload
      def norm(x,y,z):
        return abs(x) + abs(y) + abs(z)

      print(f"norm(2,4) = {norm(2,4)}")

      print(f"norm(2,3,4) = {norm(2,3,4)}")

    Otrzymujemy:

      norm(2,4) = 4.47213595499958
      norm(2,3,4) = 9

Wskazówka: Napisz dekorator, który wraca klasę z odpowiednio przeciążonym operatorem __call__, która przechowuje nazwy funkcji z parametrami. Do odróżnienia funkcji można wykorzystać np. getfullargspec(f).args z modułu inspect (from inspect import getfullargspec).
## Zadanie 5 (15pt)* Mnożenie dużych liczb o n cyfrach można wykonać w O(nlogn) zamiast klasycznie O(n2),dzięki szybkiej transformacie Fouriera. Napisz klasę FastBigNum do obliczania iloczynu dwóch bardzo dużych liczb. W programie zaimplementuj szybką transformatę Fouriera (FFT) oraz w klasie FastBigNum zdefiniuj __mul__ oraz __str__. Mówimy, że wektor y=(y0,y1,…,yn−1) jest dyskretną transformatą Fouriera (DFT) wektora x=(x0,x1,…,xn−1) i piszemy y=DFT(x), jeśli yk=n−1∑j=0xjωj⋅kn dla k=0,…,n−1 oraz ωn=e−2πi/n. Podobnie definiujemy odwrotną dyskretną transformatę Fouriera (DFT−1) i piszemy x=DFT−1(y), jeśli xj=1nn−1∑k=0ykω−k⋅jn dla j=0,…,n−1. Niech n∈N (w przypadku FFT n jest potęgą dwójki) oraz X i Y będą dużymi liczbami całkowitymi takimi, że: X=n−1∑j=0xj10j,Y=n−1∑j=0yj10j Algorytm mnożenia liczb Z=X⋅Y:
```
    X∗=
(x∗0,x∗1,…,x∗2n−1)= DFT2n(x0,x1,…,xn−1,0,…,0)

    Y∗=
(y∗0,y∗1,…,y∗2n−1)= DFT2n(y0,y1,…,yn−1,0,…,0)

    Z∗=
(z∗0,z∗1,…,z∗2n−1), z∗i=x∗i⋅y∗i dla i=0,1,…,2n−1

    Z=(z0,z1,…,z2n−1)=DFT−12n(Z∗)
    Z=∑2n−1i=0zi10i
```
Do testowania można na początku wykorzystać poniższą prostą implementację DFT:

    from cmath import exp
    from math import pi

    def omega(k,n):
        return exp(-2j*k*pi/n)

    def dft(x,n):
        return [sum(x[i]*omega(i*k,n) if i>> x = dft([1, 2, 3, 4, 5], 5)
    >>> x
    [(15+0j), (-2.500000000000001+3.440954801177934j), (-2.5+0.8122992405822647j), (-2.499999999999999-0.8122992405822673j), (-2.4999999999999964-3.440954801177935j)]
    >>> idft(x, 5)
    [1, 2, 3, 4, 5]

    Przykład działania całego programu:

    >>> A = '1312312231232131231231​231231231231212331233231349'
    >>> B = '1212312311223123121312​312321321231231112323123231'

    >>> a = FastBigNum(A)
    >>> b = FastBigNum(B)

    >>> print(a*b*a*b)

    253106550074562901422403​675886656138846376840320377646640
    728789005971339977090446​005669753867738453444565943594360
    601270478845270512230832​242981112065324812816791957946651
    0444942972440921967161

    Napisz trzy implementacje z różnymi algorytmami dla transformaty Fouriera. W pierwszej wykorzystaj podane kody dla dft i idft. W drugiej napisz swoją własną implementacje FFT (w języku Python). W trzeciej wykorzystaj numpy.fft. Porównaj czasy wykonywania i wklej do tabelki (plik tekstowy z wynikami np. fastbignum_benchmark.txt). Do testów wykorzystaj liczby 100 000, 500 000, 1 000 000. Na przykład możemy wygenerować liczby tak

    >>> a = ''.join([random.choice("0123456789") for i in range(500000)])
    >>> b = ''.join([random.choice("0123456789") for i in range(500000)])

    później testujemy czas wykonywania mnożenia a*b, klasycznie mnożenie można wykonać tak int(a)*int(b), aby sprawdzić, czy kod poprawnie je wykonał!.

# Lista 3 (Lab) Termin wysłania na SVN do 29.03.2020
Przy pisaniu programów (funkcji) NALEŻY stosować się do ogólnie przyjętego stylu programowania w języku Python. Proszę dokładnie przeczytać PEP 8 (tutorial, google python style) i PEP 257.

## Zadanie  1 (5pt) Załóżmy, że reprezentujemy macierze kwadratowe w Pythonie następująco (dla rozmiaru macierzy n=3):

        ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]

    Napisz funkcję wykorzystując tylko listy składane, która dokonuje transpozycji takich macierzy (dowolnych rozmiarów) oraz zwraca wynik w tej samej postaci (można to zrobić w jednej linii kodu!).
## Zadanie 2 (5pt) Napisz generator o nazwie "flatten", który przechodzi dowolną listę (również zagnieżdżoną) i podaje po kolei jej elementy: Na przykład dla listy

        l = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6 ], 7, [[9, [123, [[123]]]], 10]]

    Po wywołaniu: print(list(flatten(l))), otrzymujemy:

        [1, 2, 'a', 4, 'b', 5, 5, 5, 4, 5, 6, 7, 9, 123, 123, 10]

## Zadanie 3 (5pt) Wykorzystując, tylko listy składane (jako generatory) napisz program, który odczytuje plik tekstowy następnie pobiera ostatnią kolumnę, która zawiera informację o wielkości pliku, sumuje i wynik wyświetla na ekranie. Przykład pliku:

      127.0.0.1 -  - "GET /ply/  HTTP/1.1" 200 7587
      127.0.0.1 -  - "GET /favicon.ico HTTP/1.1" 404 133
      127.0.0.1 -  - "GET /ply/bookplug.gif" 200 23903
      127.0.0.1 -  - "GET /ply/ply.html HTTP/1.1" 200 97238
      127.0.0.1 -  - "GET /ply/example.html HTTP/1.1" 200 2359
      127.0.0.1 -  - "GET /index.html" 200 4447

    Dostajemy wynik:

        Całkowita liczba bajtów: 135667

## Zadanie 4 (5pt) Rozważmy algorytm QuickSort napisany w języku Haskell:

     qsort [] = []
     qsort (x:xs) = qsort elts_lt_x ++ [x] ++ qsort elts_greq_x
                     where
                       elts_lt_x = [y | y <- xs, y < x]
                       elts_greq_x = [y | y <- xs, y >= x]

    Napisz podobny program w języku Python wykorzystując
        składnie funkcjonalną (filter)
        operacje na listach składanych
## Zadanie 5 (5pt) Poniżej w języku OCAML napisany jest program, który generuje wszystkie podzbiory

      let rec allsubsets s =
        match s with
          [] -> [[]]
        | (a::t) -> let res = allsubsets t in
                      map (fun b -> a::b) res @ res;;

      # allsubsets [1;2;3];;
      - : int list list = [[1; 2; 3]; [1; 2]; [1; 3]; [1]; [2; 3]; [2]; [3]; []]

    Napisz podobny program w języku Python wykorzystując
        składnie funkcjonalną (map, lambda)
        operacje na listach składanych

Lista 2 (Lab) Termin wysłania na SVN do 22.03.2020

Przy pisaniu programów NALEŻY stosować się do ogólnie przyjętego stylu programowania w języku Python. Proszę dokładnie przeczytać PEP 8 (tutorial, google python style) i PEP 257.

## Zadanie 1(5pt) Napisz program, który dla danego pliku tekstowego wróci następujące informacje: liczba bajtów, liczbę słów, liczbę linii oraz maksymalną długość linii.

        $ python wordcount.py tekst.txt
        liczba bajtów: 4956
        liczba słów: 1018
        liczba linii: 528
        maksymalna długość linii: 67

## Zadanie  2  (5pt) Napisz program, który koduje oraz dekoduje dowolny plik binarny w kodzie Base64. Kod Base64 koduje w taki sposób, że każde kolejne 6 bitów z pliku kodowane jest znakiem ASCII przedstawionych w poniższej tabeli:

        tablica = 'ABCD​EFGH​IJKL​MNOP​QRST​UVWX​YZab​cdef​ghij​klmn​opqr​stuv​wxyz​0123​4567​89+/'

    Na przykład: słowo "Python" kodujemy jako "UHl0aG9u"

        |         P      |       y       |       t       |
        + - - - - - - - -|- - - - - - - -|- - - - - - - -| ...
        : 0 1 0 1 0 0 0 0|0 1 1 1 1 0 0 1|0 1 1 1 0 1 0 0| ...
        + - - - - - -|- -|- - - -|- - - - - -|  ...
        :     U      |     H     |      l    |  ...

        Kodowanie:
          $ python base64.py --encode plik.bin plik-enc.txt
        Dekodowanie:
          $ python base64.py --decode plik-enc.txt plik.bin

Uwaga: Proszę napisać podstawowe funkcje kodujące i dekodujące bez korzystania np. z biblioteki base64 (lub innych realizujących to zadanie).
## Zadanie 3 (5pt) Napisz program, który zamienia wszystkie nazwy w danym katalogu oraz wszystkich podkatalogach na małe litery. Jako parametr podajemy katalog (zobacz moduł os).

        $ python tolower.py ./

## Zadanie 4 (10pt) Napisz program, który w danym katalogu znajdzie wszystkie pliki, które powtarzają się więcej niż raz (zobacz os, help(os.walk)). Weź pod uwagę, że pliki mogą mieć różne nazwy, ale tą samą zawartość, dlatego przyjmujemy, że dwa pliki są takie same, jeśli mają taką samą wielkość oraz taką samą wartość funkcji haszującej. Przykład użycia funkcji haszujących

        $ python
        >>> import hashlib
        >>> hashlib.md5('python'​.encode())​.hexdigest()
        '23eeeb4347bdd26bfc6b7ee9a3b755dd'
        >>> hashlib.sha512('python'.encode()).hexdigest()
        'ecc579811​643b170​cbd88fd0d0e3​23d1e1ac​c7cef8f73​483a70abea01a89 ...

    Na wyjściu program wyświetla listę wszystkich plików, które się powtarzają (nazwy plików wraz ze ścieżką)

        $ python repchecker.py ./
        ---------------------------------
        ./plik1.txt
        ./katalog1/plik5.txt
        ./katalog3/plik1.dat
        ---------------------------------
        ./plik3.txt
        ./katalog2/plik2.txt
        ---------------------------------

## Zadanie 5 (15pt)* Napisz program, który szyfruje i deszyfruje dany plik algorytm RSA. Do sprawdzania, czy dana liczba jest pierwsza wykorzystaj dowolny test pierwszości np. test Millera-Rabina. W programie powinna być możliwość generowania kluczy do szyfrowania i deszyfrowania plików (key.pub - klucz publiczny, key.prv - klucz prywatny). Np.

        $ python rsa.py --gen-keys 128
        $ ls
        rsa.py key.pub key.prv

    Klucze mogą być dowolnie długie np. bits=128 bitowe, czyli p i q mają wtedy długość int(log(2)/log(10)*(bits)) cyfr. Przy uruchomianiu programu z parametrem --encrypt oraz ciągiem znaków do zakodowania wynik zostaje wyświetlony na standardowym wyjściu (kodowanie korzysta z klucza key.pub, jeśli kluczy nie ma to wyświetlony zostaje błąd):

        $ python rsa.py --encrypt Python
        21437302530112407657289772777280768429

    Dekodowanie odbywa się podobnie (dekodowanie korzysta z klucza key.prv):

        $ python rsa.py --decrypt 21437302530112407657289772777280768429
        Python



# Lista 1 (Lab) Termin wysłania na SVN do 8.03.2020
## Zadanie 1 _(5pt)_

Napisz funkcję, który wyświetla trójkąt Pascala o zadanej wysokości
```
                1
              1   1
            1   2   1
          1   3   3   1
        1   4   6   4   1
      .....................
```
## Zadanie 2 _(5pt)_

Napisz funkcję `primes(n)` zwracająca listę liczb pierwszych nie większych niż $n$ np.

## Zadanie 3 _(5pt)_

Napisz funkcje, która usuwa wszystkie powtarzające się elementy z listy (tak, że każdy element występuje tylko raz) np. z listy `[1,1,2,2,2,3,3,5,5,5,4,4,4,0]` dostajemy `[1,2,3,5,4,0]`.


## Zadanie 4 _(10pt)_

Napisz funkcję `prime_factors(n)`, która rozkłada $n$ na czynniki pierwsze i jako wynik wraca listę par $[(p_1,\alpha_1), (p_2,\alpha_2), \ldots, (p_k, \alpha_k)]$ taką, że $p_1^{\alpha_1}p_2^{\alpha_2}\ldots p_k^{\alpha_k}$.

## Zadanie 5 _(10pt)_

Napisz funkcję `fraczero(n)` liczącą silnie $n!$ dla $n$ od $0$ do $10000$ oraz jako wynik wraca liczbę zer na końcu $n!$.

## Zadanie 6 _(10pt)_

Napisz program, który generuje liczbę $20$ liczb losowych (rozkład jednostajny) od $1$ do $100$
* Wyświetl listę wygenerowanych liczb
* Wyświetl średnią
* Wyświetl największą i najmniejszą wartość
* Wyświetl drugą największą i drugą najmniejszą wartość na liście
* Wyświetl ile jest liczb parzystych na liście
 

## Zadanie 7 _(10pt)_

Załóżmy, że mamy następującą listę: `L = ['aababacaa', 'cabaabcca', 'aaabbcbacb', 'acababbaab', ...]` wygenerowaną losowo tzn. lista zawiera losowe ciągi znaków o zadanej długości z liter `'a'`, `'b'` i `'c'`. Takie wzorce występują w wielu miejscach np. sekwencje DNA. Użytkownik zawiera swój (wzorzec) ciąg znaków z literami i pustymi miejscami oznaczonymi przez `'*'` np. `"a**a******"`. Wykorzystaj słownik z kluczami zawierającymi indeksy znaków różnych od `'*'` i wartościami liter z wzorca. Napisz program, który znajduje wszystkie sekwencje z listy, które pasuje do podanego wzorca.

## Zadanie 8 _(10pt)_

Napisz program, który konwerteruje liczby rzymskie na liczby arabskie. Do zapisu liczb rzymskich używa
się 7 liter: `I=1`, `V=5`, `X=10`, `L=50`, `C=100`, `D=500`, `M=1000`. Opis algorytmu zamiany z i na system rzymski można znaleźć np. [tutaj](http://www.algorytm.org/algorytmy-arytmetyczne/zamiana-z-i-na-system-rzymski.html)

## Zadanie 9* _(5pt)_

Napisz program kalkulator, który pobiera wprowadzone wartości oraz funkcje z klawiatury następnie podaje wynik. W przypadku błędnych danych zgłasza błąd.


## Zadanie 10* _(10pt)_

Napisz program, który rysuje na ekranie w trybie znakowym wykres funkcji zmiennej $x$. Wskazówka: utwórz  ,,tablicę dwuwymiarową'' o wymiarach 80x24 i narysuj wykres w tej tablicy. Następnie wynik wyświetl na ekranie.

```
        Podaj funkcje f(x) = sin(x)
        Podaj początek przedziału a = -pi
        Podaj koniec przedziału b = pi
                                                |
                                                |
                                                |              ***********
                                                |           ***           ***
                                                |         **                 **
                                                |        *                     *
                                                |      **                       **
                                                |     *                           *
                                                |   **                             **
                                                |  *                                 *
                                                | *                                   *
                                                |*                                     *
        ----------------------------------------|---------------------------------------
          *                                   * |
           *                                 *  |
            **                             **   |
              *                           *     |
               **                       **      |
                 *                     *        |
                  **                 **         |
                    ***           ***           |
                       ***** *****              |
                            *                   |
                                                |
```
Przykładowa sesja:
```
    Kalkulator
    [1]: 2+5*10
        52
    [2]: sin(0.5)+cos(0.3)
        1.434762027729809
    [3]: 2^100
        1267650600228229401496703205376
```

Przykładowy kod pobierania danych od użytkownika:

```
    x = input('Podaj x = ')
```
```
In [ ]:   primes(6)
Out [ ]: [2, 3, 5]
```
