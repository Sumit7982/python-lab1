# Function to reassign the dictionary
def reassign_dict(d):
    # Create a new dictionary and assign it to d
    d = {"city": "Delhi"}

# Create the original dictionary
my_dict = {"name": "Sumit"}

# Print dictionary before function call
print("Before:", my_dict)

# Call the function
reassign_dict(my_dict)

# Check the original dictionary
print("After:", my_dict)

#output
#Before: {'name': 'Sumit'}
#After: {'name': 'Sumit'}
