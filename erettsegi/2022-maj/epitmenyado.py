class Telek:
  def __init__(self, tulaj, utca, hazszam, adosav, terulet):
    self.tulaj = tulaj
    self.utca = utca
    self.hazszam = hazszam
    self.adosav = adosav
    self.terulet = terulet

########################################

fizetendo = {'A': 0, 'B': 0, 'C': 0}
telkek: list[Telek] = []

def ado(adosav, terulet):
  adoosszeg = fizetendo[adosav] * terulet
  return adoosszeg if adoosszeg > 10000 else 0


with open('alapvizsgafeladatok\\utca.txt', 'r') as f:
  fizetendo['A'], fizetendo['B'], fizetendo['C'] = list(map(int, f.readline().strip().split(' ')))
  for sor in f:
    t = sor.strip().split(' ')
    telkek.append(Telek(t[0], t[1], t[2], t[3], int(t[4])))

print(f'2. feladat. A mintában {len(telkek)} telek szerepel.')

print(f'3. feladat.', end=' ')
adoszam = input('Egy tulajdonos adószáma: ')
cim = ''
for telek in telkek:
  if telek.tulaj == adoszam:
    cim = f'{telek.utca} utca {telek.hazszam}'
    print(cim)
if cim == '':
  print('Nem szerepel az adatállományban.')

print('5. feladat')
adoosszegek = {}
telekszam = {}
for telek in telkek:
  adoosszegek[telek.adosav] = adoosszegek.get(telek.adosav, 0) + ado(telek.adosav, telek.terulet)
  telekszam[telek.adosav] = telekszam.get(telek.adosav, 0) + 1

for sav in 'ABC':
  print(f'{sav} sávba {telekszam[sav]} telek esik, az adó {adoosszegek[sav]} Ft.')

print('6. feladat. A több sávba sorolt utcák:')
utcak = {'A': set(), 'B': set(), 'C': set()}
for telek in telkek:
  utcak[telek.adosav].add(telek.utca)
# print(utcak)
for utca in sorted(utcak['A'] & utcak['B'] | utcak['A'] & utcak['C'] | utcak['B'] & utcak['C']):
  print(utca)

# 7. feladat
tulajok = {}
for telek in telkek:
  tulajok[telek.tulaj] = tulajok.get(telek.tulaj, 0) + ado(telek.adosav, telek.terulet)

sorok = []
for tulaj in sorted(tulajok.keys()):
  sorok.append(f'{tulaj} {tulajok[tulaj]}')
with open('fizetendo.txt', 'w') as f:
  f.write('\n'.join(sorok))
