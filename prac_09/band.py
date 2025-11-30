class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician."""
        self.musicians.append(musician)

    def __str__(self):
        """String representation of the band and its musicians."""
        return f"{self.name} ({', '.join(str(m) for m in self.musicians)})"

    def play(self):
        """each musician play their instrument."""
        for musician in self.musicians:
            result = musician.play()
            print(result)