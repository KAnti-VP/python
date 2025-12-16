taj = input('Kérem a TAJ-számot: ')
ellenorzoszam = int(taj[-1])
print(f'Az ellenőrzőszámjegy: {ellenorzoszam}')

osszeg = 0
szorzo = [3, 7]
for i in range(len(taj[ : -1])):
  szorzat = szorzo[i % 2] * int(taj[i])
  osszeg += szorzat
  
print(f'A szorzatok összege: {osszeg}')
if osszeg % 10 == ellenorzoszam:
  print('Helyes a szám!')
else:
  print('Hibás a szám!')
