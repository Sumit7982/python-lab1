# Function to find the maximum of two numbers
def maximum(a, b):
    # Check if a is greater than b
    if a > b:
        return a
    else:
        # Otherwise, return b
        return b

# Take first number from user
x = int(input("Enter first number: "))

# Take second number from user
y = int(input("Enter second number: "))

# Call the function
result = maximum(x, y)

# Print the greater number
print("Maximum:", result)

#output
#Enter first number: 25
#Enter second number: 40
#Maximum: 40
