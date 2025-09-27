import math
mini_length = 10

password = input("Enter a password: ")


while len(password) < mini_length:
    print(f"Password must be at least {mini_length} characters long.")
    password = input("Enter a password: ")


print("*" * len(password))
