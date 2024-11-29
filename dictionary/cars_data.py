data = [
    {'type' : 'Audi', 'color': 'red', 'year': 2021, 'price': 3_490_000},
    {'type' : 'Audi', 'color': 'blue', 'year': 2022, 'price': 3_499_000},
    {'type' : 'BMW', 'color': 'yellow', 'year': 2021, 'price': 3_990_000},
    {'type' : 'Lexus', 'color': 'red', 'year': 2022, 'price': 3_999_000},
    {'type' : 'Mercedes', 'color': 'bue', 'year': 2021, 'price': 4_490_000},
    {'type' : 'Mercedes', 'color': 'black', 'year': 2022, 'price': 4_450_000},
    {'type' : 'BMW', 'color': 'red', 'year': 2021, 'price': 2_490_000},
    {'type' : 'VW', 'color': 'red', 'year': 2022, 'price': 2_450_000},
    {'type' : 'Lexus', 'color': 'black', 'year': 2021, 'price': 5_490_000},
    {'type' : 'Mercedes', 'color': 'blue', 'year': 2022, 'price': 5_450_000},
]

def print_car(car):
    print(f"{car['type']} \t color: {car['color']} \tyear: {car['year']} \tprice: {car['price']:_}")

def print_red_cars(cars):
    for car in cars:
        if car['color'] == 'red':
            print_car(car)

def get_most_expensive_car(cars):
    result = cars[0]
    for car in cars:
        if car['price'] > result['price']:
            result = car
    return result

def print_type(car_type, cars):
    is_any = False
    for car in cars:
        if car.get('type') == car_type:
            print_car(car)
            is_any = True
    if not is_any:
        print(f'No car type {car_type}.')


print('\nRed cars:')
print_red_cars(data)

most_expensive_car = get_most_expensive_car(data)
print('\nMost expensive car:')
print_car(most_expensive_car)

print('\nMercedes cars:')
print_type('Mercedes', data)

print('\nToyota cars:')
print_type('Toyota', data)
