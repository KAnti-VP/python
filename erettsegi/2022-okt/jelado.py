class Jel:
  def __init__(self, ora, perc, mp, x, y):
    self.ido = ora * 3600 + perc * 60 + mp
    self.x = x
    self.y = y
  
  def eltelt(self, other):
    return abs(self.ido - other.ido)
  
  def copy(self):
    ora = self.ido // 3600
    perc = (self.ido - ora * 3600) // 60
    mp = self.ido % 60
    return Jel(ora, perc, mp, self.x, self.y)
  
  def elmozdulas(self, other):
    return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
  
  def max_elteres(self, other):
    return max(abs(self.x - other.x), abs(self.y - other.y))
  
  def get_ido(self):
    ora = self.ido // 3600
    perc = (self.ido - ora * 3600) // 60
    mp = self.ido % 60
    return f'{ora} {perc} {mp}'
  
  ########################################

jelek: list[Jel] = []
with open('alapvizsgafeladatok\\jel.txt', 'r') as f:
  for row in f:
    jel = list(map(int, row.strip().split(' ')))
    jelek.append(Jel(jel[0], jel[1], jel[2], jel[3], jel[4]))

print('2. feladat')
sorszam = int(input('Adja meg a jel sorszámát! ')) - 1
jel = jelek[sorszam]
print(f'x={jel.x} y={jel.y}')

print('4. feladat')
ido = jelek[0].eltelt(jelek[-1])
ora = ido // 3600
perc = (ido - ora * 3600) // 60
mp = ido % 60
print(f'Időtartam: {ora}:{perc}:{mp}')

print('5. feladat')
x0, y0, x1, y1 = jelek[0].x, jelek[0].y, jelek[0].x, jelek[0].y
for jel in jelek:
  x0 = min(x0, jel.x)
  y0 = min(y0, jel.y)
  x1 = max(x1, jel.x)
  y1 = max(y1, jel.y)
print(f'Bal alsó: {x0} {y0}, jobb felső: {x1} {y1}')

print('6. feladat')
jel = jelek[0]
elmozdulas = 0
for kovetkezo in jelek[1:]:
  elmozdulas += jel.elmozdulas(kovetkezo)
  jel = kovetkezo
print(f'Elmozdulás: {elmozdulas:.3f} egység')

# 7. feladat
adatok = []
elozo = jelek[0]
for jel in jelek[1:]:
  elteres = jel.max_elteres(elozo) // 10 - 1
  idoelteres = jel.eltelt(elozo) // 300 - 1
  if elteres > idoelteres and elteres > 0:
    adatok.append(f'{jel.get_ido()} koordináta-eltérés {elteres}')
  elif elteres < idoelteres and idoelteres > 0:
    adatok.append(f'{jel.get_ido()} időeltérés {idoelteres}')
  elif elteres == idoelteres and elteres > 0:
    adatok.append(f'{jel.get_ido()} idő- és koordináta-eltérés {elteres + idoelteres}')

  elozo = jel

with open('kimaradt.txt', 'w', encoding='utf-8') as f:
  f.write('\n'.join(adatok))
