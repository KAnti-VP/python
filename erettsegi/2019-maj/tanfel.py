class Beosztas:
  def __init__(self, tanar, tantargy, osztaly, ora):
    self.tanar = tanar
    self.tantargy = tantargy
    self.osztaly = osztaly
    self.ora = ora
  
  def __str__(self):
    return f'{self.tanar} óra: {self.tantargy} osztály: {self.osztaly} óraszám: {self.ora}'
  

def read_eosztas():
  rows = []
  with open('apalvizsgafeladatok\\beosztas.txt', 'r') as f:
    rows = f.readlines()
  content = []
  for i in range(0, len(rows), 4):
    content.append(Beosztas(rows[i].strip(), rows[i + 1].strip(), rows[i + 2].strip(), int(rows[i + 3].strip())))
  return content

def ossz_oraszam(beosztas: list[Beosztas]):
  ossz_ora = 0
  for b in beosztas:
    ossz_ora += b.ora
  print(f'Az iskolában a heti összóraszám: {ossz_ora}')

def heti_oraszam(beosztas: list[Beosztas]):
  oraszam = 0
  tanar = input('Egy tanár neve= ')
  for b in beosztas:
    if b.tanar == tanar:
      oraszam += b.ora
  print(f'A tanár heti óraszáma: {oraszam}')

def osztalyfonokok(beosztas: list[Beosztas]):
  osztalyfonokok = []
  for b in beosztas:
      if b.tantargy == 'osztalyfonoki':
        osztalyfonokok.append(f'{b.osztaly} - {b.tanar}')
  with open('of.txt', 'a') as f:
    f.write('\n'.join(osztalyfonokok))

def csoportbontas_e(beosztas: list[Beosztas]):
  osztaly = input('Osztály= ').strip().split('.')[0]
  tantargy = input('Tantárgy= ')
  for b in beosztas:
    if b.tantargy == tantargy and osztaly in b.osztaly:
      return 'Csoportbontásban tanulják.'
  return 'Nem csoportbontásban tanulják.'

def tanarok_szama(beosztas: list[Beosztas]):
  tanarok = []
  for b in beosztas:
    if b.tanar not in tanarok:
      tanarok.append(b.tanar)
  print(f'Az iskolában {len(tanarok)} tanár tanít.')

print('1. feladat')
beosztas = read_eosztas()

print('2. feladat')
print(f'A fájlban {len(beosztas)} bejegyzés van. ')

print('3. feladat')
ossz_oraszam(beosztas)

print('4. feladat')
heti_oraszam(beosztas)

print('5. feladat')
# osztalyfonokok(beosztas)

print('6. feladat')
print(csoportbontas_e(beosztas))

print('7. feladat')
tanarok_szama(beosztas)