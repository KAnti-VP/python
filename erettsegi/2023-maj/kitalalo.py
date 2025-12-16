import random

szavak = []
with open('szavak.txt', 'r') as f:
  szavak = f.readline().strip().split(', ')

for i in range(len(szavak)):
  szavak[i] = szavak[i][1:-1]
# print(szavak)

# 2. feladat
rejtett = random.choice(szavak)
print(rejtett)

# 3. feladat
tipp = input('Kérem a tippet: ')
szamlalo = 1
while tipp != 'stop':
  if tipp == rejtett:
    break
  eredmeny = ''
  for i in range(6):
    if tipp[i] == rejtett[i]:
      eredmeny += tipp[i]
    else:
      eredmeny += '.'
  print(f'Az eredmény: {eredmeny}\n')
  szamlalo += 1
  tipp = input('Kérem a tippet: ')

# 4. feladat
if tipp == rejtett:
  print(f'{szamlalo} tippeléssel sikerült kitalálni.')
