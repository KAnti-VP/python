# Car(brand: Toyota, model: Corolla, color: White, year: 2020)
# Car(brand: BYD, model: Seal, color: White, year: 2024)

class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
    
    def __str__(self):
        return f'Car(brand: {self.brand}, model: {self.model}, color: {self.color}, year: {self.year})'

print('1-2. feladat')    
cars = []
with open('cars2.txt', 'r') as f:
    brand, model, color, year = 0, 1, 2, 3
    f.readline()
    for row in f:
        car = row.strip().split('\t')
        cars.append(Car(car[brand], car[model], car[color], car[year]))

print('3. feladat')
for car in cars:
    print(car)

print('4. feladat')
newest = cars[0]
for car in cars:
    if car.year > newest.year:
        newest = car
print(newest)

print('5. feladat')
for car in cars:
    if car.color == 'Black':
        print(car)

print('6. feladat')
car = '\nBYD\tSeal\tWhite\t2024'
with open('cars2.txt', 'a') as f:
    f.write(car)
