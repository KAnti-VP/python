to = []
sorokszama, oszlopokszama = 0, 0
with open('melyseg.txt', 'r') as f:
  sorokszama = int(f.readline().strip())
  oszlopokszama = int(f.readline().strip())
  for i in range(sorokszama):
    to.append(list(map(int, f.readline().strip().split(' '))))

print('2. feladat')
sor = int(input(f'A mérés sorának azonosítója=')) - 1
oszlop = int(input(f'A mérés oszlopának azonosítója=')) - 1
print(f'A mért mélység az adott helyen {to[sor][oszlop]} dm')

print('3. feladat')
felszin = 0
melyseg = 0
legmelyebb = 0
melysegek = []
for i in range(sorokszama):
  for j in range(oszlopokszama):
    if to[i][j] != 0:
      felszin += 1
      melyseg += to[i][j]
    
    if legmelyebb == to[i][j]:
      melysegek.append((i + 1, j + 1))
    if legmelyebb < to[i][j]:
      legmelyebb = to[i][j]
      melysegek = [(i + 1, j + 1)]
    
print(f'A tó felszíne: {felszin} m2, átlagos mélysége: {(melyseg / 10 / felszin):.2f} m')

print('4. feladat')
print(f'A tó legnagyobb mélysége: {legmelyebb} dm')
print('A legmélyebb helyek sor-oszlop koordinátái:')
for s, o in melysegek:
  print(f'({s}; {o})', end=' ')
print()

print('5. feladat')
partvonal = 0
for i in range(1, sorokszama - 1):
  for j in range(1, oszlopokszama - 1):
    if to[i][j] != 0 and to[i+1][j] == 0:
      partvonal += 1
    if to[i-1][j] == 0 and to[i][j] != 0:
      partvonal += 1
    if to[i][j-1] == 0 and to[i][j] != 0:
      partvonal += 1
    if to[i][j] != 0 and to[i][j+1] == 0:
      partvonal += 1
print(f'A tó partvonala {partvonal} m hosszú')

print('6. feladat')
oszlop = int(input('A vizsgált szelvény oszlopának azonosítója=')) - 1
for i in range(sorokszama):
  print(f'{str(i + 1).zfill(2)}{round(to[i][oszlop] / 10) * '*'}')
