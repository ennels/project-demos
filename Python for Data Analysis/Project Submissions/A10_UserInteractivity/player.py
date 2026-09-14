class Player():
    def __init__(self, name, jersey, atbats, hits):
        self.name = name
        self.jersey = jersey
        self.atbats = atbats
        self.hits = hits

    def batting_average(self):
        if self.atbats > 0:
            return self.hits / self.atbats
        return 0.0

    def display(self):
        avg = self.batting_average()
        print(f"\t{self.jersey}\t{self.name}\t\t{self.atbats}\t{self.hits}\t{avg:.3f}")
