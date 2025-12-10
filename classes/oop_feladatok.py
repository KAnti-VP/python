'''1. Egyszerű osztály és objektum
Hozz létre egy Szemely osztályt, amelynek vannak nev és eletkor attribútumai.
Készíts egy példányt, és írd ki az attribútumait.'''
class Szemely:
    def __init__(self, nev, eletkor) -> None:
        self.nev = nev
        self.eletkor = eletkor

# Példány létrehozása
szemely1 = Szemely("Anna", 25)
print(szemely1.nev)       # Anna
print(szemely1.eletkor)   # 25


'''2. Metódus hozzáadása
Bővítsd a Valaki osztályt egy bemutatkozas() metódussal, ami visszaadja a következő szöveget:
"Sziasztok, [név] vagyok, és [életkor] éves."
Hozz létre egy objektumot és hívd meg a metódust.'''
class Valaki:
    def __init__(self, nev, eletkor):
        self.nev = nev
        self.eletkor = eletkor

    def bemutatkozas(self):
        return f"Sziasztok, {self.nev} vagyok, és {self.eletkor} éves."

szemely1 = Valaki("Bob", 30)
print(szemely1.bemutatkozas())


'''3. Alapértelmezett értékek
Hozz létre egy Auto osztályt marka és evjarat attribútumokkal.
A marka alapértelmezett értéke legyen "Ismeretlen".
Hozz létre két objektumot: az egyiknek adj meg értékeket, a másik maradjon alapértelmezett.'''
class Auto:
    def __init__(self, marka="Ismeretlen", evjarat=None):
        self.marka = marka
        self.evjarat = evjarat

auto1 = Auto("Toyota", 2020)
auto2 = Auto()

print(auto1.marka, auto1.evjarat)  # Toyota 2020
print(auto2.marka, auto2.evjarat)  # Ismeretlen None


'''4. Getter és Setter
Készíts egy Szamologep osztályt egy ertek attribútummal.
Hozz létre getter és setter metódusokat az ertek eléréséhez és módosításához.
A setter ellenőrizze, hogy a megadott érték szám legyen.'''
class Szamologep:
    def __init__(self, ertek=0):
        self.__ertek = ertek

    def get_ertek(self):
        return self.__ertek

    def set_ertek(self, uj_ertek):
        if isinstance(uj_ertek, (int, float)):
            self.__ertek = uj_ertek
        else:
            print("Hiba: csak szám adható meg.")

sz = Szamologep()
sz.set_ertek(10)
print(sz.get_ertek())  # 10
sz.set_ertek("szoveg") # Hiba: csak szám adható meg.


'''5. Osztályszintű attribútum
Készíts egy Diak osztályt nev attribútummal, és egy osztályszintű diakok_szama változót, ami számolja a létrehozott diákok számát.'''
class Diak:
    diakok_szama = 0

    def __init__(self, nev):
        self.nev = nev
        Diak.diakok_szama += 1

d1 = Diak("Anna")
d2 = Diak("Béla")
print(Diak.diakok_szama)  # 2


'''6. Öröklődés
Hozz létre egy Allat osztályt nev és hang attribútumokkal, és egy hangot_ad() metódust.
Készíts belőle Kutya és Macska osztályokat, mindkettő örökölje az Allat osztályt, és a hangjukat adja vissza.'''
class Allat:
    def __init__(self, nev, hang):
        self.nev = nev
        self.hang = hang

    def hangot_ad(self):
        return self.hang

class Kutya(Allat):
    def __init__(self, nev):
        super().__init__(nev, "Vau")

class Macska(Allat):
    def __init__(self, nev):
        super().__init__(nev, "Miau")

k = Kutya("Bodri")
m = Macska("Cirmi")
print(k.hangot_ad())  # Vau
print(m.hangot_ad())  # Miau


'''7. Speciális metódusok
Készíts egy Pont osztályt x és y koordinátákkal.
Implementáld a __str__ metódust, hogy [x, y] formátumban írja ki a pontot.
Implementáld a __add__ metódust, hogy két pont összeadható legyen.'''
class Pont:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __add__(self, masik):
        return Pont(self.x + masik.x, self.y + masik.y)

p1 = Pont(2, 3)
p2 = Pont(4, 5)
p3 = p1 + p2
print(p3)  # [6, 8]


'''8. Kompozíció
Készíts egy Konyv osztályt cim és szerzo attribútumokkal.
A szerzo egy Szerzo osztály példánya legyen, amelynek nev és eletkor attribútumai vannak.'''
class Szerzo:
    def __init__(self, nev, eletkor):
        self.nev = nev
        self.eletkor = eletkor

class Konyv:
    def __init__(self, cim, szerzo):
        self.cim = cim
        self.szerzo = szerzo

iro = Szerzo("J.K. Rowling", 57)
konyv1 = Konyv("Harry Potter", iro)
print(konyv1.cim)             # Harry Potter
print(konyv1.szerzo.nev)      # J.K. Rowling


'''9. Statikus metódus
Készíts egy Matematika osztályt, amiben van egy statikus osszeg(a, b) metódus, ami visszaadja a két szám összegét.
Hívd meg a metódust osztálypéldány létrehozása nélkül.'''
class Matematika:
    @staticmethod
    def osszeg(a, b):
        return a + b

print(Matematika.osszeg(5, 7))  # 12


'''10. Összetett feladat
Készíts egy BankSzamla osztályt:
tulajdonos és egyenleg attribútumokkal.
Metódusok: befizet(osszeg), kivesz(osszeg), egyenleg_lekérdez().
Implementálj egy egyszerű hibakezelést: ne lehessen negatív összeget kivenni.'''
class BankSzamla:
    def __init__(self, tulajdonos, egyenleg=0):
        self.tulajdonos = tulajdonos
        self.egyenleg = egyenleg

    def befizet(self, osszeg):
        if osszeg > 0:
            self.egyenleg += osszeg
        else:
            print("Hiba: pozitív összeget fizethet be.")

    def kivesz(self, osszeg):
        if 0 < osszeg <= self.egyenleg:
            self.egyenleg -= osszeg
        else:
            print("Hiba: nem lehet negatív vagy nagyobb összeget kivenni, mint az egyenleg.")

    def egyenleg_lekérdez(self):
        return self.egyenleg

szamla = BankSzamla("Anna")
szamla.befizet(1000)
szamla.kivesz(200)
print(szamla.egyenleg_lekérdez())  # 800
szamla.kivesz(1000)                # Hiba
