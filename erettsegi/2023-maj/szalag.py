class Rekesz:
  def __init__(self, mikor, honnam, hova, tomeg):
    self.mikor = mikor
    self.honnam = honnam
    self.hova = hova
    self.tomeg = tomeg
  
  def elhalad_0_elott(self):
    return self.honnam != 0 and self.hova != 0 and self.honnam > self.hova
    
  def __str__(self):
    return f'Honnam: {self.honnam} Hova: {self.hova}'

########################################

def tav(szalaghossz, indulashelye, erkezeshelye):
  if indulashelye <= erkezeshelye:
    return erkezeshelye - indulashelye
  return szalaghossz - indulashelye + erkezeshelye

szalag: list[Rekesz] = []
szalaghossz, ido = 0, 0
with open('szallit.txt', 'r') as f:
  szalaghossz, ido = map(int, f.readline().strip().split(' '))
  for sor in f:
    rekesz = Rekesz(*list(map(int, sor.strip().split(' '))))
    szalag.append(rekesz)

print('2. feladat')
sor = int(input('Adja meg, melyik adatsorra kíváncsi! ')) - 1
print(szalag[sor])

print('4. feladat')
tavolsag = 0
rekeszek = ''
for i in range(len(szalag)):
  ut = tav(szalaghossz, szalag[i].honnam, szalag[i].hova)
  if ut == tavolsag:
    rekeszek += f'{i + 1} '
  if ut > tavolsag:
    tavolsag = ut
    rekeszek = f'{i + 1} '
print(f'A legnagyobb távolság: {tavolsag}')
print(f'A maximális távolságú szállítások sorszáma: {rekeszek}')

print('5. feladat')
ossztomeg = 0
for rekesz in szalag:
  if rekesz.elhalad_0_elott():
    ossztomeg += rekesz.tomeg
print(f'A kezdőpont előtt elhaladó rekeszek össztömege: {ossztomeg}')

print('6. feladat')
idopont = int(input('Adja meg a kívánt időpontot! '))
rekeszek = ''
for i in range(len(szalag)):
  rekesz = szalag[i]
  ut = tav(szalaghossz, rekesz.honnam, rekesz.hova)
  if rekesz.mikor <= idopont < rekesz.mikor + ut * ido:
    rekeszek += f'{i + 1} '
print(f'A szállított rekeszek halmaza: {rekeszek}')

# 7. feladat
tomeg = {}
for rekesz in szalag:
  tomeg[rekesz.honnam] = tomeg.get(rekesz.honnam, 0) + rekesz.tomeg
sorok = []
for key in sorted(tomeg.keys()):
    sorok.append(f'{key} {tomeg[key]}')
with open('tomeg.txt', 'w') as f:
  f.write('\n'.join(sorok))