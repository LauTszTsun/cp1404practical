CURRENT_YEAR = 2025
VINTAGE_AGE = 50
class Guitar:
    def __init__(self, name="", year= 0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare guitars by year (older = smaller)."""
        return self.year < other.year