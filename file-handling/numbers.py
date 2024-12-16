def else_feladat():
    with open('./sources/numbers.txt', 'r') as f:
        numbers = []
        for row in f:
            nums = row.strip().split(', ')
            # print( list( map(int, nums) ) )
            szamok = []
            for num in nums:
                szamok.append( int(num) )
            numbers.append(szamok)
        return numbers

def legkisebbek(nums):
    for row in nums:
        print(min(row))

def osszegek(nums):
    for row in nums:
        print(sum(row))

def fajlbairas():
    szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    with open('./files/numbers.txt', 'a') as f:

        new_line = '\n' + ', '.join(list(map(str, szamok)))
        f.write(new_line)

print('1. feladat - fájl olvasása')
numbers = else_feladat()

# print(numbers)

print('2. feladat - legkisebb kiíratása')
legkisebbek(numbers)

print('3. feladat - sorok összege')
osszegek(numbers)

print('4. feladat - számok hozzáadása a fájlhoz')
fajlbairas()
