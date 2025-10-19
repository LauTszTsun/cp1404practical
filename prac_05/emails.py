"""
Word Occurrences
Estimate: 35 minutes
Actual:   45 minutes
"""
"""
CP1404/CP5632 Practical
Store users' emails (keys) and names (values) in a dictionary.
Estimate time: (your estimate)
Actual time: (your actual time)
"""

def main():
    """Store emails and names in a dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation not in ("", "y", "yes"):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")
def extract_name(email):
    """Extract a name from the given email address."""
    # Split at '@' to remove domain, then split by '.' or '_' and capitalize each part
    name_part = email.split('@')[0]
    parts = name_part.replace('.', ' ').replace('_', ' ').split()
    name = ' '.join(parts).title()
    return name
main()
