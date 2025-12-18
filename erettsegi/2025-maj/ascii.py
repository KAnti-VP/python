def atalakit(code):
  sor = ''
  for i in range(0, len(code), 2):
    sor += int(code[i]) * code[i + 1]
  return sor
    
def fajl_hossz(filenev):
  tartalom = ''
  with open(filenev, 'r') as f:
    for sor in f:
      tartalom += sor.replace('\n', '').replace('\r', '')
  return len(tartalom)

print('1. feladat')
konyv = []
with open('konyv.txt', 'r') as f:
  for sor in f:   
    konyv.append(sor[:-1])
print('\n'.join(konyv))

print('2. feladat')
ismetles = int(input('Kérem adja meg az ismétlések számát: '))
max_len = 0
for sor in konyv:
  if max_len < len(sor):
    max_len = len(sor)

for sor in konyv:
  print(f'{sor}{(max_len - len(sor)) * " "} | ' * ismetles)

print('4. feladat')
abra = []
with open('szg_t.txt', 'r') as f:
  for sor in f:
    abra.append(atalakit(sor[: -1]))
print('\n'.join(abra))
with open('szg.txt', 'w') as f:
  f.write('\n'.join(abra))

print('5. feladat')
tomoritett = input('Kérem adja meg a tömörített ábra fájlnevét: ')
tomoritetlen = input('Kérem adja meg a tömörítetlen ábra fájlnevét: ')
tomoritett_hossz = fajl_hossz(tomoritett)
tomoritetlen_hossz = fajl_hossz(tomoritetlen)
print(f'A karakterek száma a tömörített állományban: {tomoritett_hossz}')
print(f'A karakterek száma a tömörítetlen állományban: {tomoritetlen_hossz}')
print(f'A tömörítési arány: {(tomoritett_hossz / tomoritetlen_hossz):.2f}')

print('6. feladat')
sorok_szama = 0
max_hossz = 0
blokkok = 0
with open('konyv_t.txt', 'r') as f:
  for sor in f:
      sorok_szama += 1
      blokkok += len(sor.replace('\n', '').replace('\r', '')) // 2
      if max_hossz < len(sor):
        max_hossz = len(sor)
print(f'Az ábra magassága sorokban: {sorok_szama}')
print(f'Az ábra szélessége karakterekben: {max_hossz}')
print(f'A blokkok száma: {blokkok}')
