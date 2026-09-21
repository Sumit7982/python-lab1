# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    # Apply the Celsius to Fahrenheit formula
    f = (c * 9 / 5) + 32

    # Return Fahrenheit value
    return f


# Take Celsius temperature from user
c = float(input("Enter temperature in Celsius: "))

# Call the function
result = celsius_to_fahrenheit(c)

# Print the Fahrenheit temperature
print("Temperature in Fahrenheit:", result)

#output
#Enter temperature in Celsius: 25
#Temperature in Fahrenheit: 77.0
