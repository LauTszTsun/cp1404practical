menu = "(G)et a valid score\n(P)rint result\n(S)how stars\nQ)uit"
def main():
    print(menu)
    score = 0
    choice = (input("Enter your choice: ")).upper()
    while choice != "Q":
        if choice == "G" :
            score = get_valid_score()
        elif choice == "P" :
            print(f"Your score is:{get_score_result(score)}"    )
        elif choice == "S" :
            print("*" * score)
        else :
            print("Invalid choice")
        print(menu)
        choice = (input("Enter your choice: ")).upper()
    print("Thank you for playing!")
def get_valid_score():
    """get score and return to score"""
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter your score: "))
    return score
def get_score_result(score):
    """Return the result on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()