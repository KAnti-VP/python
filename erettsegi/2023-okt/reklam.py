class Rendeles:
  def __init__(self, nap, hely, darab):
    self.nap = nap
    self.hely = hely
    self.darab = darab
  
  def __str__(self):
    return f'{self.nap} {self.hely} {self.darab}'

########################################

def fajlolvasas():
  adatok = []
  with open('rendel.txt', 'r') as f:
    for sor in f:
      adat = sor.strip().split(' ')
      rendeles = Rendeles(int(adat[0]), adat[1], int(adat[2]))
      adatok.append(rendeles)
  return adatok
  
def napi_rendeles(adatok: list[Rendeles], nap):
  darab = 0
  for rendeles in adatok:
    if rendeles.nap == nap:
      darab += 1
    if rendeles.nap > nap:
      break
  return darab

def max_rendeles(adatok: list[Rendeles]):
  maximum = adatok[0]
  for rendeles in adatok:
    if rendeles.darab > maximum.darab:
      maximum = rendeles
  return maximum

def osszes(adatok: list[Rendeles], varos, nap):
  darab = 0
  for rendeles in adatok:
    if rendeles.hely == varos and rendeles.nap == nap:
      darab += rendeles.darab
    if rendeles.nap > nap:
      break
  return darab

print('1. feladat')
rendelesek: list[Rendeles] = fajlolvasas()

print('2. feladat')
print(f'A rendelések száma: {len(rendelesek)}')

print('3. feladat')
nap = int(input('Kérem, adjon meg egy napot: '))
print(f'A rendelések száma az adott napon: {napi_rendeles(rendelesek, nap)}')

print('4. feladat')
napok = set()
for rendeles in rendelesek:
  if rendeles.hely == 'NR':
    napok.add(rendeles.nap)

nem_volt_rendeles = 30 - len(napok)
if nem_volt_rendeles > 0:
  print(f'{nem_volt_rendeles} nap nem volt a reklámban nem érintett városból rendelés')
else:
  print('Minden nap volt rendelés a reklámban nem érintett városból')

print('5. feladat')
rendeles: Rendeles = max_rendeles(rendelesek)
print(f'A legnagyobb darabszám: {rendeles.darab}, a rendelés napja: {rendeles.nap}')

print('7. feladat')
print(f'A rendelt termékek darabszáma a 21. napon PL: {osszes(rendelesek, 'PL', 21)} TV: {osszes(rendelesek, 'TV', 21)} NR: {osszes(rendelesek, 'NR', 21)}')

print('8. feladat')
heti = {'PL': [0, 0, 0], 'TV': [0, 0, 0], 'NR': [0, 0, 0]}
for rendeles in rendelesek:
  heti[rendeles.hely][(rendeles.nap - 1) // 10] += 1
rows = [
  'Napok\t1..10\t11..20\t21..30',
  f'PL\t{heti['PL'][0]}\t{heti['PL'][1]}\t{heti['PL'][2]}',
  f'TV\t{heti['TV'][0]}\t{heti['TV'][1]}\t{heti['TV'][2]}',
  f'NR\t{heti['NR'][0]}\t{heti['NR'][1]}\t{heti['NR'][2]}'
]
content = '\n'.join(rows)
with open('kampany.txt', 'w') as f:
  f.write(content)
  print(content)

