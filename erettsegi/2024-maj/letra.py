print('1. feladat')
dobasok = []
with open('dobasok.txt', 'r') as f:
    dobasok = list(map(int, f.readline().strip().split(', ')))
print('Adatok beolvasása')

print('2. feladat')
sum = 0
mezok = []
visszalepes = 0
for dobas in dobasok:
    sum += dobas
    if sum % 10 == 0:
        sum -= 3
        visszalepes += 1
    mezok.append(str(sum))
print(' '.join(mezok))

print('3. feladat')
print(f'A játék során {visszalepes} alkalommal lépett létrára.')

print('4. feladat')
output_text = 'A játékot befejezte.' if int(mezok[-1]) >= 45 else 'A játékot abbahagyta.'
print(output_text)
