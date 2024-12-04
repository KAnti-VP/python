def get_file_as_list(file_name):
    rows = []
    with open(file_name, 'r') as f:
        for row in f:
            str_data = row.strip().split(', ')
            rows.append(str_data)
    return rows

def set_file_content(file_name, rows):
    with open(file_name, 'w') as f:
        rows = [', '.join(row) for row in rows]
        f.write('\n'.join(rows))


print('1. feladat')
lista = get_file_as_list('fibonacci.txt')

print('2. feladat')
for row in lista:
    print(' '.join(row))

print('3. feladat')
for i in range(len(lista)):
    row = lista[i]
    for _ in range(2):
        a = row[-1]
        b = row[-2]
        new_value = int(a) + int(b)
        row.append(str(new_value))
    lista[i] = row

print('4. feladat')
set_file_content('fibonacci.txt', lista)
 
