# 1. Olvasd be az employees2.txt fájl tartalmát.
# 2. Hozz létre Employee példányokat, melyek a txt fáj tartalmának felelnek meg.
# 3. Írasd ki az  employeekat  az alábbi példa szerint:
# Employee(name: John Smith, position: Software Engineer, salary: 75000)
# 4. Írsd ki a Managereket
# 5. Írsd ki a legalább 75000-et keresőket
# 6. Add hozzá a fájlhoz az alábbi munkavállalót:
# Employee(name: Eliot Wolf, position: Scrum Master, salary: 78000)

class Employee:
    def __init__(self, firstname, lastname, position, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f'Employee(name: {self.firstname} {self.lastname}, position: {self.position}, salary: {self.salary})'

print('1-2. feladat')
employees = []
with open('employees2.txt', 'r') as f:
    firstname, lastname, position, salary = 0, 1, 2, 3
    f.readline()
    for row in f:
        data = row.strip().split('\t')
        employees.append(Employee(data[firstname], data[lastname], data[position], int(data[salary])))

print('3. feladat')
for employee in employees:
    print(employee)

print('4. feladat')
for employee in employees:
    if 'Manager' in employee.position:
        print(employee)

print('5. feladat')
for employee in employees:
    if employee.salary >= 75000:
        print(employee)

print('6. feladat')
employee = '\nEliot\tWolf\tScrum Master\t78000'
with open('employees2.txt', 'a') as f:
    f.write(employee)
