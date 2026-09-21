# Function to calculate factorial
def factorial(n):
    # Start factorial with 1
    fact = 1

    # Loop from 1 to n
    for i in range(1, n + 1):
        # Multiply fact by i
        fact = fact * i

    # Return the factorial value
    return fact


# Take a number from user
n = int(input("Enter a number: "))

# Call the function
result = factorial(n)

# Print the factorial
print("Factorial:", result)

#output
#Enter a number: 5
#Factorial: 120
