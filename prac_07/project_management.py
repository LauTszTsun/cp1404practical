"""
Word Occurrences
Estimate: 40 minutes
Actual:   80 minutes
"""
import datetime
from project import Project
DEFAULT_FILENAME = "projects.txt"
def main():
    """Run Management program."""
    projects = load_projects(DEFAULT_FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    MENU = ("- (L)oad projects\n"
            "- (S)ave projects\n"
            "- (D)isplay projects\n"
            "- (F)ilter projects by date\n"
            "- (A)dd new project\n"
            "- (U)pdate project\n"
            "- (Q)uit")
    print(MENU)
    choice = input(">>> ").strip().lower()

    while choice != "q":
        if choice == "l":
            filename = input("Filename to load from: ").strip()
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "s":
            filename = input("Filename to save to: ").strip()
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").strip().lower()

    save_text = input(f"Would you like to save to {DEFAULT_FILENAME}? ").strip().lower()
    if save_text.startswith("y"):
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")
def load_projects(filename):
    """Load projects from a tab-delimited file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split("\t")
            if len(parts) != 5:
                continue
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects
def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            date_string = project.start_date.strftime("%d/%m/%Y")
            out_file.write(f"{project.name}\t{date_string}\t{project.priority}\t"
                           f"{project.cost_estimate}\t{project.completion_percentage}\n")

def sort_by_start_date(project):
    """Return a project's start date."""
    return project.start_date

def display_projects(projects):
    """Display incomplete and completed projects."""
    incomplete = [p for p in projects if p.completion_percentage < 100]
    complete = [p for p in projects if p.completion_percentage >= 100]
    incomplete.sort()
    complete.sort()
    print("Incomplete projects: ")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects: ")
    for project in complete:
        print(f"  {project}")
def filter_projects_by_date(projects):
    """Display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ").strip()
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format")
        return
    filtered = [p for p in projects if p.start_date >= filter_date]
    filtered.sort(key=sort_by_start_date)
    for project in filtered:
        print(project)
def add_new_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    date_string = input("Start date (dd/mm/yy): ").strip()
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
def update_project(projects):
    """Update a project's completion or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
    except (ValueError, IndexError):
        print("Invalid project choice")
        return
    print(project)
    new_percentage = input("New Percentage: ").strip()
    if new_percentage != "":
        project.completion_percentage = int(new_percentage)

    new_priority = input("New Priority: ").strip()
    if new_priority != "":
        project.priority = int(new_priority)
if __name__ == "__main__":
    main()