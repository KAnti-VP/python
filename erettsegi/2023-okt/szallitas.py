print('1. feladat')
targyak = []
with open('tomeg.txt', 'r') as f:
  sor = f.readline()
  targyak = list(map(int, sor.strip().split(', ')))
print(targyak)
print('2. feladat')
print(f'A tárgyak tömegének összege: {sum(targyak)} kg')

print('3. feladat')
doboz = 0
dobozok = []
for targy in targyak:
  if doboz + targy <= 20:
    doboz += targy
  else:
    dobozok.append(doboz)
    doboz = targy
if doboz > 0:
  dobozok.append(doboz)
print(f'A dobozok tartalmának tömege (kg): {' '.join(map(str, dobozok))}')
print(f'A szükséges dobozok száma: {len(dobozok)}')
