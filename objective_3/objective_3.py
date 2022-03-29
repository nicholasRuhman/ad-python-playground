# Implement a function named 'convert' that takes a temperature in degrees Fahrenheit
# and returns the temperature converted to Celsius, rounded to one decimal place.
#
def convert(F):
    return round((F - 32) * 5 / 9, 1)
