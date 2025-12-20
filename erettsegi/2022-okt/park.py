class Row:
  def __init__(self, start, end, color):
    self.start = start
    self.end = end
    self.color = color
  
  def __str__(self):
    return f'{self.start} {self.end} {self.color}'

########################################

def both_side(rows: list[Row], beds):
  result = []
  for i in range(len(rows)):
    if (rows[i].start == 1 and rows[i].end == beds) or rows[i].start > rows[i].end:
      result.append(f'{i + 1}')
  return result


def bed_in_offers(bed, rows: list[Row], beds_number):
  count = 0
  colors = []
  for row in rows:
    if row.start <= row.end:
      if bed in range(row.start, row.end + 1):
        count += 1
        if row.color not in colors:
          colors.append(row.color)
    else:
      if bed in range(row.start, beds_number + 1) or bed in range(1, row.end + 1):
        count += 1
        if row.color not in colors:
          colors.append(row.color)
  return (count, colors)


def implantation(rows: list[Row], beds):
  numbers = set()
  summa = 0
  for row in rows:
    if row.start <= row.end:
      s = set(range(row.start, row.end + 1))
      numbers |= s
      summa += len(s)
    else:
      s = set(range(row.start, beds + 1))
      s |= set(range(1, row.end + 1))
      numbers |= s
      summa += len(s)
  if len(numbers) == beds:
    print(f'Átszervezéssel megoldható a beültetés.')
  elif summa >= beds:
    print('Átszervezéssel megoldható a beültetés.')
  else:
    print('A beültetés nem oldható meg.')


def planting(garden, color, flowerbed, offer):
  if flowerbed not in garden:
    garden[flowerbed] = f'{color} {offer}'
  return garden


def writeFile(rows: list[Row], beds_number):
  data = {}
  for i in range(len(rows)):
    if rows[i].start <= rows[i].end:
      for index in range(rows[i].start, rows[i].end + 1):
        if index not in data:
          data[index] = f'{rows[i].color} {i + 1}'
      continue
    
    for index in range(rows[i].start, beds_number + 1):
      data = planting(data, rows[i].color, index, i + 1)
    for index in range(1, rows[i].end + 1):
      data = planting(data, rows[i].color, index, i + 1)
  
  content = []
  for i in range(1, beds_number + 1):
      content.append(data.get(i, f'# 0'))
  with open('szinek.txt', 'w') as f:
    f.write('\n'.join(content))
  

print('1. feladat')
print('Adat beolvasása')
offers: list[Row] = []
flowerbed = 0
with open('felajanlas.txt', 'r') as f:
  flowerbed = int(f.readline())
  for line in f:
    data = line.strip().split(' ')
    row = Row(int(data[0]), int(data[1]), data[2])
    # print(row)
    offers.append(row)

print('2. feladat')
print(f'A felajánlások száma: {len(offers)}')

print('3. feladat')
ultetok = both_side(offers, flowerbed)
print(f'A bejárat mindkét oldalán ültetők: {' '.join(ultetok)}')

print('4. feladat')
bed = int(input('Adja meg az ágyás sorszámát! '))
count, colors = bed_in_offers(bed, offers, flowerbed)
print(f'A felajánlók száma: {count}')
if len(colors):
  print(f'A virágágyás színe, ha csak az első ültet: {colors[0]}')
else:
  print('Ezt az ágyást nem ültetik be.')
print(f'A virágágyás színei: {' '.join(colors)}')

print('5. feladat')
implantation(offers, flowerbed)

print('6. feladat')

writeFile(offers, flowerbed)
