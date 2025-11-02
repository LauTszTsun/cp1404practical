from prac_06.guitar import Guitar

def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            # Decide vintage label using normal if block
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"

            # Print with f-string (easy to read)
            print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:,.2f}{vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")