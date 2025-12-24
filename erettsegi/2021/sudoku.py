class Tabla:
  def __init__(self):
    self.mezo = {}
  
  def add(self, x, y, num):
    self.mezo[10 * (x - 1) + y - 1] = num
  
  def get(self, x, y):
    return self.mezo.get(10 * (x - 1) + y - 1, 0)
  
  def resztabla(self, sor, oszlop):
    __resztabla = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return __resztabla[(oszlop - 1) % 3][(sor - 1) % 3]
  
  def sorban(self, sor, szam):
    for i in range(1, 10):
      if self.get(sor, i) == szam:
        return True
    return False
  
  def oszlopban(self, oszlop, szam):
    for i in range(1, 10):
      if self.get(i, oszlop) == szam:
        return True
    return False
  
  def resztablaban(self, sor, oszlop, szam):
    s = (sor - 1) // 3 * 3 + 1
    o = (oszlop - 1) // 3 * 3 + 1
    for i in range(s, s + 3):
      for j in range(o, o + 3):
        if self.get(i, j) == szam:
          return True
    return False
  
  def kiiratas(self, sor, oszlop, szam):
    kiir = ''
    if self.get(sor, oszlop):
      kiir += 'A helyet már kitöltötték\n'
    if self.sorban(sor, szam):
      kiir += 'Az adott sorban már szerepel a szám\n'
    if self.oszlopban(oszlop, szam):
      kiir += 'Az adott oszlopban már szerepel a szám\n'
    if self.resztablaban(sor, oszlop, szam):
      kiir += 'Az adott résztáblázatban már szerepel a szám\n'
    if kiir == '':
      kiir = 'A lépés megtehető\n'
    return kiir

########################################

print('1. feladat')
filenev = input('Adja meg a bemeneti fájl nevét! ')
sor = int(input('Adja meg egy sor számát! '))
oszlop = int(input('Adja meg egy oszlop számát! '))

tabla = Tabla()
lepesek = []
with open(filenev, 'r') as f:
  for i in range(1, 10):
    row = list(map(int, f.readline().strip().split(' ')))
    for j in range(1, 10):
      tabla.add(i, j, row[j - 1])
  for i in range(4):
    lepesek.append(list(map(int, f.readline().strip().split(' '))))


print('3. feladat')
szam = tabla.get(sor, oszlop)
if szam == 0:
  szam = 'Az adott helyet még nem töltötték ki.'
print(f'Az adott helyen szereplő szám: {szam}')
print(f'A hely a(z) {tabla.resztabla(sor, oszlop)} résztáblázathoz tartozik.')

print('4. feladat')
ures = 0
for i in range(1, 10):
  for j in range(1, 10):
    if tabla.get(i, j) == 0:
      ures += 1
print(f'Az üres helyek aránya: {(ures / 81 * 100):.1f}%')

print('5. feladat')
for szam, sor, oszlop in lepesek:
  print(f'A kiválasztott sor: {sor} oszlop: {oszlop} a szám: {szam}')
  print(tabla.kiiratas(sor, oszlop, szam))
