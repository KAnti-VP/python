class DistanceConverter:
    __to_miles = 0.621371
    __to_kms = 1.609344

    def __init__(self):
        pass

    def miles_to_kilometers(self, miles):
        return round(miles * type(self).__to_kms, 2)

    def kilometers_to_miles(self, kms):
        return round(kms * type(self).__to_miles, 2)

conv = DistanceConverter()
print(conv.kilometers_to_miles(100))
print(conv.miles_to_kilometers(100))