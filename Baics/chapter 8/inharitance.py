class Movies:
    def __init__(self, movieRating, production, universe):
        self.movieRating = movieRating
        self.production = production
        self.universe = universe

    def show(self):
        print(
            f"The movie is produced by {self.production}, "
            f"the rating is {self.movieRating}, "
            f"and universe is {self.universe}"
        )


class Avenger(Movies):
    def __init__(self, movieRating, production, universe, movieName, seriesNumber):
        super().__init__(movieRating, production, universe)
        self.movieName = movieName
        self.seriesNumber = seriesNumber

    def final(self):
        super().show()
        print(
            f"The movie name is {self.movieName} "
            f"and Series Number is {self.seriesNumber}"
        )


avengerInfinityWar = Avenger(
    "UA",
    "Marvel",
    "MCU",
    "Avengers: Infinity War",
    3
)

avengerInfinityWar.final()


















































# class vehicale:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")



# class car(vehicale):
#     def __init__(self, make, model, year, num_doors):
#         super().__init__(make, model, year) # calling the constructor of the parent class
#         self.num_doors = num_doors

#     def display_info(self):
#         super().display_info() # calling the method of the parent class
#         print(f"Number of doors: {self.num_doors}")

# my_car = car("Toyota", "Camry", 2020, 4)
# my_car.display_info()