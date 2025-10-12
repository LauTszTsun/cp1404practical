import random

# Constants
NUMBERS_PER_LINE = 6
MINIUM_NUMBER = 1
MAXIMUM_NUMBER = 45
def main():

        number_of_picks = int(input("How many quick picks? "))

        for _ in range(number_of_picks):
            quick_pick = generate_quick_pick()
            # Print each number in the pick, right-aligned in a width of 2
            print(" ".join(f"{number:2}" for number in quick_pick))

def generate_quick_pick():

        numbers = []
        while len(numbers) < NUMBERS_PER_LINE:
            number = random.randint(MINIUM_NUMBER, MAXIMUM_NUMBER)
            if number not in numbers:
                numbers.append(number)
        numbers.sort()
        return numbers
main()
