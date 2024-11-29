from  math import pi

def pi_digits(number):
    result = {}
    for digit in str(number):
        if digit.isdigit(): 
            num = int(digit)
            if num in result:
                result[int(num)] += 1
            else:
                result[int(num)] = 1
    return result

print(pi)
print(pi_digits(pi))
