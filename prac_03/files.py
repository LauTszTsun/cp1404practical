#1.
from fileinput import close

name = input("What is your name? ")
Filename = "names.txt"
out_file = open(Filename, "w")
out_file.write(name)
out_file.close()

#2.
in_file = open("names.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}")
in_file.close()

#3.
with open("numbers.txt", "r") as in_file:

    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
result = number1 + number2
print(result)