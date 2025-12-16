import random

def veletlen_szamok():
  szamok = []
  for _ in range(3):
    szamok.append(random.randint(1, 6))
  return szamok

n = int(input('Hány alkalommal legyen feldobás? '))
anni, panni = 0, 0
for _ in range(n):
  szamok = veletlen_szamok()
  osszeg = sum(szamok)
  nyert = 'Panni'
  if osszeg < 10:
    nyert = 'Anni'
    anni += 1
  else:
    panni += 1
  print(f'Dobás: {' + '.join(map(str, szamok))} = {osszeg}\tNyert: {nyert}')
print(f'A játék során {anni} alkalommal Anni, {panni} alkalommal Panni nyert.')
      