# Function to add a new entry
def add_entry(d):
    # Add a new key-value pair
    d["age"] = 20

# Create a dictionary
my_dict = {"name": "Sumit"}

# Print dictionary before function call
print("Before:", my_dict)

# Call the function
add_entry(my_dict)

# Print dictionary after function call
print("After:", my_dict)

#output
#Before: {'name': 'Sumit'}
#After: {'name': 'Sumit', 'age': 20}
