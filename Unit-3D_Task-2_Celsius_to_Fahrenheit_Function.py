# Celsius to Fahrenheit Using Function

def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = convert_temperature(celsius)

print("Temperature in Fahrenheit:", fahrenheit)