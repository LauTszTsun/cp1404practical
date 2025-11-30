class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Store the details for a programming language."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"
    def _str_(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"