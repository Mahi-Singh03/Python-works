# Parent Class
class Movies:
    def __init__(self, title, actors, budget):
        self.title = title
        self.actors = actors
        self.budget = budget

    def info(self):
        print(f"Movie Title: {self.title}")
        print(f"Actors: {self.actors}")
        print(f"Budget: {self.budget}")


# Child Class 1
class Action(Movies):
    def __init__(self, title, actors, budget, hero, villain):
        super().__init__(title, actors, budget)
        self.hero = hero
        self.villain = villain

    def details(self):
        self.info()
        print(f"Hero: {self.hero}")
        print(f"Villain: {self.villain}")


# Child Class 2
class Comedy(Movies):
    def __init__(self, title, actors, budget, comedian):
        super().__init__(title, actors, budget)
        self.comedian = comedian

    def details(self):
        self.info()
        print(f"Lead Comedian: {self.comedian}")


# Objects
movie1 = Action(
    "Captain America: Civil War",
    "Chris Evans, Robert Downey Jr.",
    "250 Million USD",
    "Captain America",
    "Iron Man"
)

movie2 = Comedy(
    "3 Idiots",
    "Aamir Khan, R. Madhavan, Sharman Joshi",
    "55 Crore INR",
    "Aamir Khan"
)

# Display Details
print("----- Action Movie -----")
movie1.details()

print("\n----- Comedy Movie -----")
movie2.details()