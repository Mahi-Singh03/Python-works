class Movies:
    def __init__(self, actors, mode, budget, collection):
        self.actors = actors
        self.mode = mode
        self.budget = budget
        self.collection = collection

    def info(self):
        print(
            f"Each movie always has actors {self.actors}, "
            f"is released in {self.mode}, "
            f"has a budget of {self.budget}, "
            f"and a collection of {self.collection}."
        )


class Action(Movies):
    def __init__(self, super_villain, powers, superhero,
                 actors, mode, budget, collection):
        super().__init__(actors, mode, budget, collection)
        self.super_villain = super_villain
        self.powers = powers
        self.superhero = superhero

    def details(self):
        super().info()
        print(
            f"\nThe action movie has a superhero {self.superhero} "
            f"with the power {self.powers} "
            f"to face the super villain {self.super_villain}."
        )


civilwar = Action(
    "Iron Man",
    "Super Serum",
    "Captain America",
    "Robert Downey Jr., Chris Evans",
    "Theaters",
    "200M",
    "900M"
)

civilwar.details()