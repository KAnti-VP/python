osvenyek = []
dobasok = []

with open('alapvizsgafeladatok\\osvenyek.txt', 'r') as f:
  for sor in f:
    osvenyek.append(sor.strip())

with open('alapvizsgafeladatok\\dobasok.txt', 'r') as f:
  dobasok = list(map(int, f.readline().strip().split(' ')))

print('2. feladat')
print(f'A dobások száma: {len(dobasok)}')
print(f'Az ösvények száma: {len(osvenyek)}')

print('3. feladat')
sorszam = 0
max_hossz =0
for i in range(len(osvenyek)):
  if len(osvenyek[i]) > max_hossz:
    max_hossz = len(osvenyek[i])
    sorszam = i + 1
print(f'Az egyik leghosszabb a(z) {sorszam}. ösvény, hossza: {max_hossz}')

print('4. feladat')
sorszam = int(input('Adja meg egy ösvény sorszámát! ')) - 1
jatekosszam = int(input('Adja meg a játékosok számát! '))
osveny = osvenyek[sorszam]

print('5. feladat')
statisztika = {'M': osveny.count('M'), 'V': osveny.count('V'), 'E': osveny.count('E')}
for key in statisztika:
  if statisztika[key]:
    print(f'{key}: {statisztika[key]} darab')

# 6. feladat
with open('kulonleges.txt', 'a') as f:
  for i in range(len(osveny)):
    if osveny[1] in 'EV':
      f.write(f'{i + 1}\t{osveny[i]}\n')

print('7. feladat')
hely = {}
for i in range(0, len(dobasok), jatekosszam):
  for jatekos in range(1, jatekosszam + 1):
    hely[jatekos] = hely.get(jatekos, 0) + dobasok[i + jatekos - 1]
  if max(hely.values()) >= len(osveny):
    break
nyertesek = []
for jatekos in hely:
  if hely[jatekos] >= len(osveny):
    nyertesek.append(f'{jatekos}')
print(f'A játék a(z) {(i // jatekosszam) + 1}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {', '.join(nyertesek)} ')

print('8. feladat')
hely = {}
bonusz = {'M': 1, 'E': 2, 'V': 0}
for i in range(0, len(dobasok), jatekosszam):
  for jatekos in range(1, jatekosszam + 1):
    dobas = dobasok[i + jatekos - 1]
    hely[jatekos] = hely.get(jatekos, 0) + dobas
    if hely[jatekos] < len(osveny):
      hely[jatekos] += dobas * bonusz[osveny[hely[jatekos]]]
  if max(hely.values()) >= len(osveny):
    break
nyertesek = []
for jatekos in hely:
  if hely[jatekos] >= len(osveny):
    nyertesek.append(f'{jatekos}')
print(f'Nyertes(ek): {' '.join(nyertesek)}')
print('A többiek pozíciója:')
for key, value in hely.items():
  if str(key) not in nyertesek:
    print(f'{key}. játékos, {value}. mező')

print(len(osveny), hely)
