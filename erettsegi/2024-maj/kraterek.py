class Krater:
  def __init__(self, x, y, r, name):
    self.x = x
    self.y = y
    self.r = r
    self.name = name
  
  def distance(self, other):
    return ((other.x-self.x)*(other.x-self.x)+(other.y-self.y)*(other.y-self.y)) ** 0.5
  
  def is_separated(self, other):
    distance = self.distance(other)
    return distance > (self.r + other.r)
  
  def is_included(self, other):
    distance = self.distance(other)
    radius_diff = abs(self.r - other.r)
    return distance < radius_diff

  def get_area(self):
    return round(self.r **2 * 3.14, 2)

  def __str__(self):
    return f'A(z) {self.name} középpontja X={self.x} Y={self.y} sugara R={self.r}.'
  
########################################

def read_file():
  rows = []
  with open('felszin_tpont.txt', 'r') as f:
    for row in f:
      data = row.strip().split('\t')
      rows.append(Krater(float(data[0]), float(data[1]), float(data[2]), data[3]))
  return rows

def get_krater_by_name(kraters: list[Krater], name: str):
  for krater in kraters:
    if krater.name == name:
      return krater
  return None

def get_max_radius(kraters: list[Krater]):
  name = ''
  radius = 0
  for k in kraters:
    if k.r > radius:
      radius = k.r
      name = k.name
  return f'{name} {radius}'

def get_seperated(kraters: list[Krater], krater: Krater):
  result = []
  for k in kraters:
    if krater.is_separated(k):
      result.append(k.name)
  return result

def included_kraters(kraters: list[Krater]):
  for i in range(len(kraters) - 1):
    this = kraters[i]
    for j in range(i + 1, len(kraters)):
      other = kraters[j]
      if this.is_included(other):
        print(f'A(z) {this.name} kráter tartalmazza a(z) {other.name}.')

def save_kraters_area(kraters: list[Krater]):
  rows = []
  for k in kraters:
    rows.append(f'{k.get_area()}\t{k.name}')
  with open('terulet.txt', 'w') as f:
    f.write('\n'.join(rows))


print('1. feladat')
kraterek = read_file()
# for k in kraterek:
#   print(k)
print('Adatok beolvasása.')

print('2. feladat')
print(f'A kráterek száma: {len(kraterek)}')

print('3. feladat')
nev = input('Kérem egy kráter nevét: ')
krater = get_krater_by_name(kraterek, nev)
if krater:
  print(krater)
else:
  print('Nincs ilyen nevű kráter.')

print('4. feladat')
print(f'A legnagyobb kráter neve és sugara: {get_max_radius(kraterek)}')

print('6. feladat')
nev = input('Kérem egy kráter nevét: ')
krater = get_krater_by_name(kraterek, nev)
print(f'Nincs közös része: {", ".join(get_seperated(kraterek, krater))}.')

print('7. feladat')
included_kraters(kraterek)

print('8. feladat')
save_kraters_area(kraterek)
