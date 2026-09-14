# Take list input from the user
my_list = list(map(int, input("Enter list elements separated by spaces: ").split()))

# Create an empty list to store unique elements
unique_list = []

# Go through each element of the original list
for item in my_list:
    # Check if the element is not already in the unique list
    if item not in unique_list:
        # Add the element to the unique list
        unique_list.append(item)

# Display the list after removing duplicates
print("List after removing duplicates:", unique_list)
