import random

def get_random_number():
    return random.randint(1, 100)

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        raise Exception('It is not a fizzbuzz number')


num = get_random_number()
print(num)
# print(fizzbuzz(num)) # without try..except block it could rais an error
try:
    print(fizzbuzz(num))
except:
    print(f'{num} is not a fizzbuzz number.')
