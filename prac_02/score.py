"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random
from random import randint
def main():
    """Ask for their score"""
    score = float(input("Enter your score: "))
    result = get_score_result(score)
    print(result)
    random_score = randint (0, 100)
    print(f"Random score: {random_score}")
    print(get_score_result(random_score))


def get_score_result(score):
    """Return the result on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
main()