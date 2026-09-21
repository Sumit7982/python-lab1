# Function to remove the last element
def remove_last(lst):
    lst.pop()

# Create a list
my_list = [10, 20, 30, 40]

# Print list before function call
print("Before:", my_list)

# Call the function
remove_last(my_list)

# Print list after function call
print("After:", my_list)

#output
#Before: [10, 20, 30, 40]
#After: [10, 20, 30]
