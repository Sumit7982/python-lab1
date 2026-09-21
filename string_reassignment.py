# Function to change the first character
def change_string(s):
    # Create a new string with X as the first character
    s = "X" + s[1:]
    
    # Print the changed string inside the function
    print("Inside:", s)

# Create a string
my_string = "Hello"

# Print string before function call
print("Before:", my_string)

# Call the function
change_string(my_string)

# Check the original string
print("After:", my_string)

#output
#Before: Hello
#Inside: Xello
#After: Hello
