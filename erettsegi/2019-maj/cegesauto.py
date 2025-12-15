class Auto:
  def __init__(self, nap, ora_perc, rendszam, szemely_azonosito, km_szamlalo, ki_be_hajtas):
    self.nap = nap
    self.ora_perc = ora_perc
    self.rendszam = rendszam
    self.szemely_azonosito = szemely_azonosito
    self.km_szamlalo= km_szamlalo
    self.ki_be_hajtas = ki_be_hajtas
  
  def __str__(self):
    return f'{self.ora_perc} {self.rendszam} {self.szemely_azonosito} {'be' if self.ki_be_hajtas else 'ki'}'


def readAutok():
  cars: list[Auto] = []
  with open('autok.txt', 'r') as f:
    for row in f:
      car = row.strip().split(' ')
      cars.append(Auto(int(car[0]), car[1], car[2], int(car[3]), int(car[4]), int(car[5])))
  return cars

def utolso_auto(cars: list[Auto]):
  for i in range(len(cars) - 1, -1, -1):
    if cars[i].ki_be_hajtas == 0:
      print(f'{cars[i].nap}. nap rendszám: {cars[i].rendszam}')
      break

def menetlevel(cars: list[Auto]):
  rendszam = input('Rendszám: ')
  with open(f'{rendszam}_menetlevel.txt', 'a', encoding='utf-8') as f:
    for car in cars:
      if car.rendszam == rendszam:
        if car.ki_be_hajtas:
          f.write(f'\t\t{car.nap:>2}. {car.ora_perc}\t\t{car.km_szamlalo} km\n')
        else:
          f.write(f'{car.szemely_azonosito}\t\t{car.nap:>2}. {car.ora_perc}\t\t{car.km_szamlalo} km')
  print('Menetlevél kész.')

def napi_forgalom(cars: list[Auto]):
  nap = int(input('Nap: '))
  for car in cars:
    if car.nap == nap:
      print(car)

def kintmaradt_autok(cars: list[Auto]):
  kiniek = []
  for car in cars:
    if car.ki_be_hajtas == 0:
      kiniek.append(car.rendszam)
    else:
      kiniek.remove(car.rendszam)
  print(f'A hónap végén {len(kiniek)} autót nem hoztak vissza.')

def megtett_tavolsag(cars: list[Auto]):
  futott = {}
  for car in cars:
    if car.rendszam not in futott:
      futott[car.rendszam] = {'start': car.km_szamlalo, 'end': car.km_szamlalo}
    else:
      futott[car.rendszam]['end'] = car.km_szamlalo
  
  for key in sorted(futott.keys()):
    print(f'{key} {futott[key]['end'] - futott[key]['start']} km')

def leghosszabb_tavolsag(cars: list[Auto]):
  leghosszabb = []
  maxtav = 0
  uton = {}
  for car in cars:
    if car.rendszam not in uton:
      uton[car.rendszam] = car.km_szamlalo
    else:
      tav = car.km_szamlalo - uton[car.rendszam]
      uton.pop(car.rendszam)
      if maxtav == tav:
        leghosszabb.append({'szemely': car.szemely_azonosito, 'km': tav})
      if maxtav < tav:
        maxtav = tav
        leghosszabb = [{'szemely': car.szemely_azonosito, 'km': tav}]
  for leg in leghosszabb:
    print(f'Leghosszabb út: {leg['km']} km, személy: {leg['szemely']}')


print('1. feladat')
autok = readAutok()

print('2. feladat')
utolso_auto(autok)

print('3. feladat')
napi_forgalom(autok)

print('4. feladat')
kintmaradt_autok(autok)

print('5. feladat')
megtett_tavolsag(autok)

print('6. feladat')
leghosszabb_tavolsag(autok)

print('7. feladat')
menetlevel(autok)
