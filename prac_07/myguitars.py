from guitar import Guitar


def main():
    """Read guitars, allow adding new ones, and save all to file."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("These are your existing guitars:")
    display_guitars(guitars)

    add_new_guitars(guitars)
    save_guitars(filename, guitars)

    print(f"\nAll guitars saved to {filename}")
    print("\nSorted by year:")
    guitars.sort()
    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Show all guitars in a list."""
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    """Ask the user to add new guitars."""
    print("\nAdd new guitars (press Enter to stop):")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} added.")
        name = input("Name: ")


def save_guitars(filename, guitars):
    """Write all guitars back to the CSV file."""
    with open(filename, "w") as out_file:
        out_file.write("Name,Year,Cost\n")
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()
