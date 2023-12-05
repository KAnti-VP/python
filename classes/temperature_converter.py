class TemperatureConverter:
    __to_cels = 5 / 9
    __to_fahr = 9 / 5

    def __init__(self):
        pass

    def to_celsius(self, degree):
        return round((degree - 32) * type(self).__to_cels, 2)

    def to_fahrenheit(self, degree):
        return round(degree * type(self).__to_fahr + 32, 2)


tc = TemperatureConverter()
print(tc.to_celsius(100))
print(tc.to_fahrenheit(20))