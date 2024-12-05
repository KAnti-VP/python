print('1. feladat')
print('Adatok beolvasása a fájlból')
uvegek = []
with open('uvegek.txt', 'r') as f:
    uvegek = list(map(int, f.read().strip().split(', ')))
# print(uvegek)

print('2. feladat')
jam_amount = int(input('Mari néni lekvárja (dl): '))
# print(lekvar_mennyiseg)

print('3. feladat')
maximum = max(uvegek)
print(f'A legnagyobb üveg: {maximum} dl és {uvegek.index(maximum) + 1}. a sorban.')

print('4. feladat')
jam_capacity = sum(uvegek)
text_output = 'Elegendő üveg volt.' if jam_capacity >= jam_amount else 'Maradt lekvár.'
print(text_output)
