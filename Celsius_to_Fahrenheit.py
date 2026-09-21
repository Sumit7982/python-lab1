def celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f

c = float(input("Enter temperature in Celsius: "))

result = celsius_to_fahrenheit(c)

print("Temperature in Fahrenheit:", result)