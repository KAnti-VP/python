print('1. feladat')
aktivitas = input('Adja meg az aktivitását: ')
print('2. feladat')
ertek = {'U': 1, 'G': 1, 'F': 2, 'K': 10}
tavolsag = 0
for betu in aktivitas:
  tavolsag += ertek[betu]
print(f'Az elért távolság: {tavolsag} km.')
print('3. feladat')
jutalom = True
for betu in 'UGFK':
  jutalom &= betu in aktivitas
if jutalom:
  print('Bravó! Jutalma még 10 km.')
  tavolsag += 10
else:
  print('Nem jár jutalom.')
print('4. feladat')
if tavolsag >= 40:
  print(f'Eredménye: {tavolsag} km. Gratulálok, kihívás teljesítve!')
else:
  print(f'Eredménye: {tavolsag} km. Legközelebb sikerül!')
