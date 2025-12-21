class RGB:
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b

  def sum(self):
    return self.r + self.g + self.b

  def is_light(self):
    return self.sum() > 600
  
  def __str__(self):
    return f'{self.r},{self.g},{self.b}'
  
########################################

picture: list[list[RGB]] = []

# 5. feladat
def hatar(row, limit):
  rgbs = picture[row]
  for i in range(len(rgbs) - 1):
    if abs(rgbs[i].b - rgbs[i + 1].b) > limit:
      return True
  return False

# 1. feladat
with open('kep.txt', 'r') as f:
  for row in f:
    
    nums = list(map(int, row.strip().split(' ')))
    
    line = []
    for i in range(0, len(nums), 3):
      rgb = RGB(nums[i], nums[i + 1], nums[i + 2])
      line.append(rgb)
    
    picture.append(line)

print('2. feladat')
print('Kérem egy képpont adatait!')
row = int(input('Sor:')) - 1
column = int(input('Oszlop:')) - 1
print(f'A képpont színe RGB({picture[row][column]})')

print('3. feladat')
lights = 0
for row in picture:
  for rgb in row:
    lights += rgb.is_light()
print(f'A világos képpontok száma: {lights}')

print('4. feladat')
darkest = 1000
darks: list[RGB] = []
for row in picture:
  for rgb in row:
    current = rgb.sum()
    if current == darkest:
      darks.append(rgb)
    if current < darkest:
      darkest = current
      darks = [rgb]
print(f'A legsötétebb pont RGB összege: {darkest}')
print('A legsötétebb pixelek színe:')
for rgb in darks:
  print(f'RGB({rgb})')

print('6. feladat')
first, last = 0, 0
for i in range(len(picture)):
  if hatar(i, 10):
    if first == 0:
      first = i + 1
    last = i + 1
print(f'A felhő legfelső sora: {first}')
print(f'A felhő legalsó sora: {last}')
