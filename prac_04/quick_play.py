import random

# Constants
NUMBERS_PER_LINE = 6
MINIUM_NUMBER = 1
MAXIMUM_NUMBER = 45
def main():
    """Quick Picks program - generate sets of random numbers."""
    number_of_quick_picks = int(input("How many quick picks? "))

    # Input validation
    while number_of_quick_picks < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input("How many quick picks? "))

    # Generate and print each quick pick
    for _ in range(number_of_quick_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MINIUM_NUMBER, MAXIMUM_NUMBER)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))

main()
