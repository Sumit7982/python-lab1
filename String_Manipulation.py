s = input("Enter a string ")  # Take a string as input from the user

print("Uppercase:", s.upper())  # Convert the string to uppercase

print("lowercase:", s.lower())  # Convert the string to lowercase

print("Reverse:", s[::-1])  # Reverse the string

count = 0  # Initialize the vowel count to 0

for ch in s:  # Check each character in the string
    if ch.lower() in "aeiou":  # Check if the character is a vowel
        count += 1  # Increase the vowel count by 1

print("number of vowels:", count)  # Display the total number of vowels
