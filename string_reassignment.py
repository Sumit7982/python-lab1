def change_string(s):
    s = "X" + s[1:]
    print("Inside:", s)

my_string = "Hello"

print("Before:", my_string)

change_string(my_string)

print("After:", my_string)