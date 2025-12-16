class Jel:
  def __init__(self, rendszam, ora, perc, sebesseg):
    self.rendszam = rendszam
    self.ora = ora
    self.perc = perc
    self.sebesseg = sebesseg
  
  def __str__(self):
    return f'{self.rendszam} {self.ora} {self.perc} {self.sebesseg}'

###################################################################

def beolvasas():
  with open('jeladat.txt', 'r') as f:
    adatok = []
    for sor in f:
      adat = sor.strip().split('\t')
      adatok.append(Jel(adat[0], int(adat[1]), int(adat[2]), int(adat[3])))
  return adatok


def printJelek(jelek):
  for jel in jelek:
    print(jel)


def utolso_jeladas(jel: Jel):
  print(f'Az utolsó jeladás időpontja {jel.ora}:{jel.perc}, a jármű rendszáma {jel.rendszam}')


def elso_jarmu_jeladasai(jelek:list[Jel]):
  rendszam = jelek[0].rendszam
  print(f'Az első jármű: {rendszam}')
  print('Jeladásainak időpontjai: ', end='')
  for jel in jelek:
    if jel.rendszam == rendszam:
      print(f'{jel.ora}:{jel.perc}', end=' ')
  print()


def jeladasok_szama(jelek:list[Jel]):
  ora = int(input('Kérem, adja meg az órát: '))
  perc = int(input('Kérem, adja meg a percet: '))
  jelszam = 0
  for jel in jelek:
    if jel.ora == ora and jel.perc == perc:
      jelszam += 1
  print(f'A jeladások száma: {jelszam}')


def legnagyobb_sebesseg(jelek:list[Jel]):
  autok = set()
  max_sebesseg = 0
  for jel in jelek:
    if jel.sebesseg == max_sebesseg:
      autok.add(jel.rendszam)
    if jel.sebesseg > max_sebesseg:
      max_sebesseg = jel.sebesseg
      autok = {jel.rendszam}
  print(f'A legnagyobb sebesség km/h: {max_sebesseg}')
  print(f'A járművek: {' '.join(sorted(autok))}')


def jarmu_jeladasai(jelek:list[Jel]):
  rendszam = input('Kérem, adja meg a rendszámot: ')
  van_auto = False 
  elozo_idopont = 0
  ut = 0
  for jel in jelek:
    if jel.rendszam == rendszam:
      idopont = jel.ora * 60 + jel.perc
      ut += (idopont - elozo_idopont) / 60 * jel.sebesseg
      if van_auto == False:
        ut = 0
        van_auto = True
      elozo_idopont = idopont
      print(f'{jel.ora}:{jel.perc} {ut:.1f} km')

  if not van_auto:
    print(f'Nem szerepel az adtok között {rendszam} rendszámmal jármű.')
        

def jarmu_be_ki_lepes(jelek:list[Jel]):
  autok = {}
  for jel in jelek:
    if jel.rendszam in autok:
      autok[jel.rendszam]['ki'] = f'{jel.ora} {jel.perc}'
    else:
      autok[jel.rendszam] = {'be': f'{jel.ora} {jel.perc}'}
  
  adatok = []
  for key in sorted(autok.keys()):
    adatok.append(f'{key} {autok[key]['be']} {autok[key]['ki']}')

  with open('ido.txt', 'w') as f:
    f.write('\n'.join(adatok))


print('1. feladat')
jelek = beolvasas()
# printJelek(jelek)
print('Adatok beolvasása a fájlból.')

print('2. feladat')
utolso_jeladas(jelek[-1])

print('3. feladat')
elso_jarmu_jeladasai(jelek)

print('4. feladat')
jeladasok_szama(jelek)

print('5. feladat')
legnagyobb_sebesseg(jelek)

print('6. feladat')
jarmu_jeladasai(jelek)

print('7. feladat')

jarmu_be_ki_lepes(jelek)
