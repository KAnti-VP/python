def good_job():
    '''
    Visszaad egy egyszerű, pozitív üzenetet.

    A függvény nem vesz át paramétereket, és egy előre meghatározott üzenetet ad vissza.

    @return: str - Az üzenet: Hi, it's a nice job!
    '''
    # a kód helye
    

def two_times(txt):
    '''
    A megadott szöveget (string) megtisztítja a környező whitespace karakterektől,
    majd kétszer összefűzi őket egy szóközzel elválasztva. Az eredményt visszaadja.

    @param txt: str - A bemeneti szöveg, amelyet feldolgozunk.
    @return: str - A megtisztított szöveg kétszer, szóközzel elválasztva.
    '''
    # a kód helye
    

def area(length, width):
    '''
    Számítja egy téglalap területét a megadott hosszúság és szélesség alapján.
    Ha valemely paraméter értéke 0 vagy negatív, 0-t ad vissza.

    @param length: float - A téglalap hossza.
    @param width: float - A téglalap szélessége.
    @return: float - A téglalap területe vagy 0, ha érvénytelen adatok vannak.
    '''
    # a kód helye


def is_vowel(letter):
    '''
    Ellenőrzi, hogy a megadott karakter magánhangzó-e (kis- és nagybetűk esetén is).

    @param letter: str - Egyetlen karakter, amit ellenőrizni szeretnénk.
    @return: bool - True, ha a karakter magánhangzó, különben False.
    '''
    # a kód helye
    

def sum_events(array):
    '''
    Összeadja egy lista összes páros számát.

    @param array: list - Számokat tartalmazó lista.
    @return: int - A lista páros elemeinek összege.
    '''
    # a kód helye


if __name__ == '__main__':
    pont = 0
    pont += good_job() == "Hi, it's a nice job!"
    pont += two_times('text') == 'text text'
    pont += two_times('right ') == 'right right'
    pont += two_times(' left') == 'left left'
    pont += two_times(' both ') == 'both both'
    pont += two_times(' ') == ' '
    pont += two_times('') == ' '
    pont += area(2, 3) == 6
    pont += area(2, 1.5) == 3
    pont += area(-2, 3) == 0
    pont += area(2, -3) == 0
    pont += area(-2, -3) == 0
    for c in 'aeioub.cAYEXIOUB':
        pont += is_vowel(c) == True
    pont += sum_events([0,1,0,2,0,3,0,4,0,5]) == 6
    pont += sum_events([0,1,3,5,7,9]) == 0
    pont += sum_events([0,2,4,6,8]) == 20
    pont += sum_events([0,1,0,1,0,1,0,1,0,1]) == 0
    pont += sum_events([-2,2,-4,4,-6,6]) == 0
    pont += sum_events([]) == 0

    print(f'Össz pontszám: {pont}')
    szazalek = pont / 28 * 100
    print(f'Százalék: {szazalek:.2f}\nJegy: ', end='')
    if szazalek >= 85:
        print(5)
    elif 85 > szazalek >= 70:
        print(4)
    elif 70 > szazalek >= 55:
        print(3)
    elif 55 > szazalek >= 40:
        print(2)
    else:
        print(1)
