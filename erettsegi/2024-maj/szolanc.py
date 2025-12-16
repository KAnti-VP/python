def szo_bekeres(sorszam):
  szo = input(f'{sorszam}. szó: ')
  return szo

def helyes_a(szavak, szo):
  if len(szo) != 6:
    print('A karakterek száma téves! ')
    return False
  if len(szavak) > 0 and szavak[-1][-1] != szo[0]:
    print('Nem illeszkedett! ')
    return False
  return True

def ertekelo(szoszam):
  if szoszam > 5:
    return 'haladó'
  if 2 < szoszam:
    return 'közepes'
  return 'kezdő'

szavak = []
szo = szo_bekeres(len(szavak) + 1)
while helyes_a(szavak, szo):
  szavak.append(szo)
  szo = szo_bekeres(len(szavak) + 1)

print()
print(f'Helyes lépések száma: {len(szavak)}')
print(f'Szint: {ertekelo(len(szavak))}')