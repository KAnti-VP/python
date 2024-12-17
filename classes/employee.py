# Employee(name: Alice, age: 28, gender: female, height: 165)
# Employee(name: Luca, age: 31, gender: male, height: 182)

class Employee:
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
    
    def __str__(self):
        return f'Employee(name: {self.name}, age: {self.age}, gender: {self.gender}, height: {self.height})'

print('1-2. feladat')
employees = []
with open('employees.txt', 'r') as f:
    name, age, gender, height = 0, 1, 2, 3
    for row in f:
        data = row.strip().split(', ')
        employees.append(Employee(data[name], int(data[age]), data[gender], int(data[height])))

print('3. feladat')
for employee in employees:
    print(employee)

print('4. feladat')
for employee in employees:
    if employee.gender == 'female':
        print(employee)

print('5. feladat')
for employee in employees:
    if employee.height > 175:
        print(employee)

print('6. feladat')
employee = '\nLuca, 31, male, 182'
with open('employees.txt', 'a') as f:
    f.write(employee)
