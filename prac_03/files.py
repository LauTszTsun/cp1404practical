#1.
name = input("What is your name? ")
Filename = "names.txt"
out_file = open(Filename, "w")
out_file.write(name)
out_file.close()
