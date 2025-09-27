import math
mini_length = 10

password = input("Enter a password: ")


while len(password) < mini_length:
    print(f"Password need to be more than {mini_length} characters.")
    password = input("Enter a password again: ")


print("*" * len(password))
