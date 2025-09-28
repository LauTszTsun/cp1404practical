mini_length = 10
def main():
    password = get_password()
    asterisk = print_asterisk(password)
    print (asterisk)

def get_password():
    """get password from user"""
    password = input("Enter a password: ")
    while len(password) < mini_length:
        print(f"Password need to be more than {mini_length} characters.")
        password = input("Enter a password again: ")
    return password

def print_asterisk(password):
    return "*" * len(password)




main()
