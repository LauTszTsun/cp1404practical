from guitar import Guitar


def main():
    """Read guitars from file and display them sorted by year."""
    guitars = []

    # Read file
    with open("guitars.csv", "r") as in_file:
        in_file.readline()  # Skip header if there is one
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))

    print("All guitars:")
    for guitar in guitars:
        print(guitar)

    # Sort by year
    guitars.sort()

    print("\nSorted by year:")
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
