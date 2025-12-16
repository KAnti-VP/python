import random

def lift_helyzet(start, cel):
  irany = '-'
  if start > cel:
    irany = 'L'
  if start < cel:
    irany = 'F'
  return f'{start} {irany} ({cel})'

def lift_haladas(start, cel, emelet):
  if start <= emelet <= cel:
    return abs(start - emelet)
  return abs(start - cel) + abs(cel - emelet)

def teszt(start, cel, emelet):
  print(f'A lift helyzete: {lift_helyzet(start, cel)}')
  print(f'Adja meg a szintet, ahonnan hívja a liftet! Szint: {emelet}')
  print(f'A liftnek {lift_haladas(start, cel, emelet)} emeletet kell haladnia a hívóig.')
  print('-' * 40)

start_szint = random.randint(0, 10)
cel_szint = random.randint(0, 10)
print(f'A lift helyzete: {lift_helyzet(start_szint, cel_szint)}')
szint = int(input('Adja meg a szintet, ahonnan hívja a liftet! Szint: '))
print(f'A liftnek {lift_haladas(start_szint, cel_szint, szint)} emeletet kell haladnia a hívóig.')
print('-' * 40)

teszt(7, 0, 8)
teszt(1, 3, 0)
teszt(4, 4, 9)
teszt(0, 10, 3)