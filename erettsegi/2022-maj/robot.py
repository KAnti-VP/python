parancs = input('Kérem a robot parancsait: ')
betuk = {'E': 0, 'D': 0, 'K':0, 'N': 0}
for betu in parancs:
    betuk[betu] += 1
for b in betuk:
    print(f'{b} betűk száma: {betuk[b]}')
uj_parancs = ''
if betuk['E'] > betuk['D']:
    uj_parancs += 'E' * (betuk['E'] - betuk['D'])
else:
    uj_parancs += 'D' * (betuk['D'] - betuk['E'])
if betuk['K'] > betuk['N']:
    uj_parancs += 'K' * (betuk['K'] - betuk['N'])
else:
    uj_parancs += 'N' * (betuk['N'] - betuk['K'])
print(f'Egy legrövidebb út parancsszava: {uj_parancs}')