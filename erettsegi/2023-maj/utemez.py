class Tabor:
  def __init__(self, start_ho, start_nap, end_ho, end_nap, diakok, tema):
    self.start_ho = start_ho
    self.start_nap = start_nap
    self.end_ho = end_ho
    self.end_nap = end_nap
    self.diakok = diakok
    self.tema = tema
  
  def __str__(self):
    return f'{self.start_ho}.{str(self.start_nap).zfill(2)}-{self.end_ho}.{str(self.end_nap).zfill(2)} {self.tema}'
  
########################################

def fajlolvasas():
  taborok = []
  with open('taborok.txt', 'r') as f:
    for sor in f:
      t = sor.strip().split('\t')
      tabor = Tabor(int(t[0]), int(t[1]), int(t[2]), int(t[3]), t[4], t[5])
      taborok.append(tabor)
  return taborok

def legnepszerubb_tabor(taborok: list[Tabor]):
  legnepszerubb = []
  resztvevok = 0
  for tabor in taborok:
    if resztvevok == len(tabor.diakok):
      legnepszerubb.append(f'{tabor.start_ho} {tabor.start_nap} {tabor.tema}')
    if resztvevok < len(tabor.diakok):
      resztvevok = len(tabor.diakok)
      legnepszerubb = [f'{tabor.start_ho} {tabor.start_nap} {tabor.tema}']
  return '\n'.join(legnepszerubb)

def sorszam(honap, nap):
  if honap == 6:
    return nap - 15
  if honap == 7:
    return nap + 15
  if honap == 8:
    return nap + 15 + 31

def zajlo_taborok(taborok: list[Tabor]):
  ho = int(input('ho: '))
  nap = int(input('nap: '))
  aktualis_nap = sorszam(ho, nap)
  szamlalo = 0
  for t in taborok:
    if sorszam(t.start_ho, t.start_nap) <= aktualis_nap <= sorszam(t.end_ho, t.end_nap):
      szamlalo += 1
  print(f'Ekkor éppen {szamlalo} tábor tart.')

print('1. feladat')
taborok: list[Tabor] = fajlolvasas()

print('2. feladat')
print(f'Az adatsorok száma: {len(taborok)}')
print(f'Az először rögzített tábor témája: {taborok[0].tema}')
print(f'Az utoljára rögzített tábor témája: {taborok[-1].tema}')

print('3. feladat')
for tabor in taborok:
  if tabor.tema == 'zenei':
    print(f'Zenei tábor kezdődik {tabor.start_ho}. hó {tabor.start_nap}. napján.')

print('4. feladat')
print('Legnépszerűbbek:')
print(legnepszerubb_tabor(taborok))

print('6. feladat')
zajlo_taborok(taborok)

print('7. feladat')
