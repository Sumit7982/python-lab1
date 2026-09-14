numbers = []  # Create an empty list to store numbers

for i in range(10):  # Repeat 10 times
    n = int(input("enter a integer:"))  # Take an integer as input
    numbers.append(n)  # Add the number to the list

total = 0  # Initialize total as 0

for n in numbers:  # Go through each number in the list
    total = total + n  # Add each number to total

average = total / 10  # Calculate the average

print("sum:", total)  # Display the sum
print("average:", average)  # Display the average
