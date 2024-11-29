import random

def get_random_number():
    return random.randint(1, 100)

def is_even(number):
    if number % 3 == 0:
        raise Exception('Divisible by 3')
    return number % 2 == 0

num = get_random_number()
try:
    print(is_even(num), num)
except:
    print(f'The {num} is divisible by 3')
