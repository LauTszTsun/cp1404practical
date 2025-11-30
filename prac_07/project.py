"""Project class for project management program."""

class Project:
    """Represent a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = start_date      # datetime.date object
        self.priority = priority          # int
        self.cost_estimate = cost_estimate  # float
        self.completion_percentage = completion_percentage  # int

    def __str__(self):
        """Return string representation of a Project (matches sample output)."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare Projects by priority so we can sort them."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if project is 100% complete."""
        return self.completion_percentage >= 100
