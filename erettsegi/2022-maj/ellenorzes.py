class Jel:
  def __init__(self, rendszam, be_ora, be_perc, be_mp, be_emp, ki_ora, ki_perc, ki_mp, ki_emp):
    self.rendszam = rendszam
    self.belep = (be_ora * 3600 + be_perc * 60 + be_mp) * 1000 + be_emp
    self.kilep = (ki_ora * 3600 + ki_perc * 60 + ki_mp) * 1000 + ki_emp
  
  def sebesseg(self):
    ido = (self.kilep - self.belep) / 3600_000
    return 10 / ido

########################################

jelek: list[Jel] = []
with open('meresek.txt', 'r') as f:
  for sor in f:
    jl = sor.strip().split(' ')
    jel = Jel(jl[0], int(jl[1]), int(jl[2]), int(jl[3]), int(jl[4]), int(jl[5]), int(jl[6]), int(jl[7]), int(jl[8]))
    jelek.append(jel)

print('2. feladat')
print(f'A mérés során {len(jelek)} jármű adatait rögzítették.')

print('3. feladat')
szamlalo = 0
for jel in jelek:
  if jel.kilep < 9 * 3600_000:
    szamlalo += 1
  else:
    break
print(f'9 óra előtt {szamlalo} jármű haladt el a végponti mérőnél.')

print('4. feladat')
ido = input('Adjon meg egy óra és perc értéket! ')
ora, perc = list(map(int, ido.strip().split(' ')))
be = (ora * 3600 + perc * 60) * 1000
ki = be + 60_000
belepo = 0
for jel in jelek:
  if jel.belep >= ki:
    break
  if jel.belep >= be:
    belepo += 1
uton = 0
for jel in jelek:
  if jel.belep < ki  and  jel.kilep >= be:
    uton += 1
    # print(jel.ido(jel.belep), jel.ido(jel.kilep))
print(f'\ta. A kezdeti méréspontnál elhaladt járművek száma: {belepo}')
print(f'\tb. A forgalomsűrűs: {uton / 10}')

print('5. feladat')
leggyorsabb = jelek[0]
for jel in jelek:
  if jel.sebesseg() > leggyorsabb.sebesseg():
    leggyorsabb = jel
lehagyott = 0
for jel in jelek:
  if jel.belep < leggyorsabb.belep and jel.kilep > leggyorsabb.kilep:
    lehagyott += 1
print('A legnagyobb sebességgel haladó jármű')
print(f'\trendszáma: {leggyorsabb.rendszam}')
print(f'\tátlagsebessége: {int(leggyorsabb.sebesseg())} km/h')
print(f'\táltal lehagyott járművek száma: {lehagyott}')

print('6. feladat')
gyorshajtok = 0
buntetes = []
for jel in jelek:
  sebesseg = jel.sebesseg()
  if sebesseg > 90:
    gyorshajtok += 1
  if 104 < sebesseg <= 121:
    buntetes.append(f'{jel.rendszam}\t{int(sebesseg)} km/h\t30000 Ft')
  if 121 < sebesseg <= 136:
    buntetes.append(f'{jel.rendszam}\t{int(sebesseg)} km/h\t45000 Ft')
  if 136 < sebesseg < 151:
    buntetes.append(f'{jel.rendszam}\t{int(sebesseg)} km/h\t60000 Ft')
  if 151 < sebesseg:
    buntetes.append(f'{jel.rendszam}\t{int(sebesseg)} km/h\t200000 Ft')
print(f'A járművek {(gyorshajtok / len(jelek) * 100):.2f}%-a volt gyorshajtó.')

# 7. feladat
with open('buntetes.txt', 'w') as f:
  f.write('\n'.join(buntetes))
print('A fájl elkészült.')
