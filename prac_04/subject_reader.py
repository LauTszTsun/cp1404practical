"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    subject_data = load_data(FILENAME)
    display_subject_details(subject_data)


def load_data(filename=FILENAME):
    data = []
    with open(filename, "r") as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data


def display_subject_details(data):

    for subject_code, lecturer, student_count in data:
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")

main()