"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit_result = c_to_f(celsius)
            print(f"Result: {fahrenheit_result:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius_result= f_to_c(fahrenheit)
            print(f"Result: {celsius_result:.2f} C")
        else:
            print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

def c_to_f(celsius):
    """convert celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


def f_to_c(fahrenheit):
    """convert farenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)

main()