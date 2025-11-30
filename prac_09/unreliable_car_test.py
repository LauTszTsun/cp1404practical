from unreliable_car import UnreliableCar

def main():
    """Test the unreliable car class."""
    # Create cars with different reliability values
    good_car = UnreliableCar("Good", 100, 90)
    bad_car = UnreliableCar("Bad", 100, 9)

    # Attempts to drive both cars multiple times
    for i in range(1, 20):
        print(f"Attempt {i}: Try to drive {i} km")
        print(f"{good_car.name:12} drove {good_car.drive(i):3} km ")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):3} km ")

    # Print the result after attempts
    print(good_car)
    print(bad_car)



main()