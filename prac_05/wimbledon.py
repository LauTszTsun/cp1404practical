"""
Word Occurrences
Estimate: 55 minutes
Actual:   70 minutes
"""
"""
CP1404/CP5632 Practical
Wimbledon Gentlemen's Singles Champions
Estimate time: (your estimate)
Actual time: (your actual time)
"""



"""
CP1404/CP5632 Practical
Wimbledon Gentlemen's Singles Champions
Estimate time: (your estimate)
Actual time: (your actual time)
"""

import csv

def main():
    filename = "wimbledon.csv"
    champions_count = {}
    countries = set()
    with open(filename, "r", encoding="utf-8-sig", newline="") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # skip header
        for row in reader:
            year = row[0]
            country = row[1]   # Champion's country
            champion = row[2]  # Champion's name
            champions_count[champion] = champions_count.get(champion, 0) + 1
            countries.add(country)
    sorted_champions = []
    champions_copy = champions_count.copy()
    while champions_copy:
        max_wins = -1
        max_champion = ""
        for champ, wins in champions_copy.items():
            if wins > max_wins:
                max_wins = wins
                max_champion = champ
        sorted_champions.append((max_champion, max_wins))
        champions_copy.pop(max_champion)
    print("Wimbledon Champions:")
    for champion, wins in sorted_champions:
        print(f"{champion} {wins}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))
main()
