"""
'id': {
    'entry_time': 12000
    'entry_speed': 80
    'exit_time': 12800
    'exit_speed': 85
}
"""


def convert_to_seconds(hours, minutes):
    return int(hours) * 3600 + int(minutes) * 60


def get_formatted_time(seconds):
    hours = seconds // 3600
    minutes = (seconds - 3600 * hours) // 60
    return f'{hours}:{minutes}'


print('1. feladat')
id = 0
hours = 1
minutes = 2
speed = 3
cars = {}
with open('jeladas.txt', 'r') as f:
    for row in f:
        car = row.strip().split(' ')
        if car[id] not in list(cars.keys()):
            cars[car[id]] = {
                'entry_time': convert_to_seconds(car[hours], car[minutes]),
                'entry_speed': int(car[speed])
            }
        else:
            cars[car[id]]['exit_time'] = convert_to_seconds(car[hours], car[minutes])
            cars[car[id]]['exit_speed'] = int(car[speed])
print('Adatok beolvasása')

print('2. feladat')
last_id = ''
last_time = 0
for id in cars:
    if last_time < cars[id]['entry_time']:
        last_time = cars[id]['entry_time']
        last_id = id
    if 'exit_time' in cars[id].keys() and last_time < cars[id]['exit_time']:
        last_time = cars[id]['exit_time']
        last_id = id
print(f"Az utolsó jeladás időpontja {get_formatted_time(last_time)}, a jármű rendszáma {last_id}")

print('3. feladat')
first_id = list(cars.keys())[0]
print(f'Az első jármű: {first_id}')
dates = f"{get_formatted_time(cars[first_id]['entry_time'])}"
dates += f" {get_formatted_time(cars[first_id]['exit_time'])}" if 'exit_time' in list(cars[first_id].keys()) else ''
print(f'Jeladásainak időpontjai: {dates}')

print('4. feladat')
hour = input('Kérem, adja meg az órát: ')
minute = input('Kérem, adja meg a percet: ')
current_time = convert_to_seconds(hour, minute)
sign_number = 0
for id in cars:
    if current_time <= cars[id]['entry_time']:
        sign_number += 1
    if 'exit_time' in cars[id].keys() and current_time <= cars[id]['exit_time']:
        sign_number += 1
print(f'A jeladások száma: {sign_number}')

print('5. feladat')
max_speed = 0
for id in cars:
    if max_speed < cars[id]['entry_speed']:
        max_speed = cars[id]['entry_speed']
    if 'exit_speed' in cars[id].keys() and max_speed < cars[id]['exit_speed']:
        max_speed = cars[id]['exit_speed']
speed_cars = []
for id in cars:
    if max_speed == cars[id]['entry_speed'] or ('exit_speed' in cars[id].keys() and max_speed < cars[id]['exit_speed']):
        if id not in speed_cars:
            speed_cars.append(id)
print(f'A legnagyobb sebesség km/h: {max_speed}')
print(f"A járművek: {' '.join(speed_cars)}")

print('6. feladat')
car_id = input('Kérem, adja meg a rendszámot: ')
if car_id in cars:
    print(f"{get_formatted_time(cars[car_id]['entry_time'])} 0.0 km")
    if 'exit_time' in cars[car_id].keys():
        distance = (cars[car_id]['exit_time'] - cars[car_id]['entry_time']) / 3600 * cars[car_id]['entry_speed']
        print(f"{get_formatted_time(cars[car_id]['exit_time'])} {distance:.1f} km")
else:
    print('Az adott rendszámmal nem haladt el autó.')

print('7. feladat')
content = []
for id in cars:
    row = f"{id} {get_formatted_time(cars[id]['entry_time'])}"
    if 'exit_time' in cars[id].keys():
        row += f" {get_formatted_time(cars[id]['exit_time'])}"
    row = row.replace(':', ' ')
    content.append(row)
with open('ido.txt', 'a') as f:
    f.write('\n'.join(content))
