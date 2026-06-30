# # Parent Class
# class Movies:
#     def __init__(self, title, actors, budget):
#         self.title = title
#         self.actors = actors
#         self.budget = budget

#     def info(self):
#         print(f"Movie Title: {self.title}")
#         print(f"Actors: {self.actors}")
#         print(f"Budget: {self.budget}")


# # Child Class 1
# class Action(Movies):
#     def __init__(self, title, actors, budget, hero, villain):
#         super().__init__(title, actors, budget)
#         self.hero = hero
#         self.villain = villain

#     def details(self):
#         self.info()
#         print(f"Hero: {self.hero}")
#         print(f"Villain: {self.villain}")


# # Child Class 2
# class Comedy(Movies):
#     def __init__(self, title, actors, budget, comedian):
#         super().__init__(title, actors, budget)
#         self.comedian = comedian

#     def details(self):
#         self.info()
#         print(f"Lead Comedian: {self.comedian}")


# # Objects
# movie1 = Action(
#     "Captain America: Civil War",
#     "Chris Evans, Robert Downey Jr.",
#     "250 Million USD",
#     "Captain America",
#     "Iron Man"
# )

# movie2 = Comedy(
#     "3 Idiots",
#     "Aamir Khan, R. Madhavan, Sharman Joshi",
#     "55 Crore INR",
#     "Aamir Khan"
# )

# # Display Details
# print("----- Action Movie -----")
# movie1.details()

# print("\n----- Comedy Movie -----")
# movie2.details()



# Simple inhariatnce
# class parent:
#     def speak(self):
#         print("hi")

# class child(parent):
#     def talk(self):
#         print("talk")

# mahi=child()
# mahi.speak() # acessing the parents class method 











# multiple inharitance

# class parent1:
#     def fun1 (slef):
#         print("this is the function form the parent 1")


# class parent2:
#     def fun2 (slef):
#         print("this is the function form the parent 2")


# class parent3:
#     def fun3 (slef):
#         print("this is the function form the parent 3")


# class child(parent1,parent2,parent3):
#     def fun4 (slef):
#         print("this is the function from the child")


# mahi=child()
# mahi.fun4() #calling the main class mehtod
# mahi.fun1() #calling the parent function for parent1
# mahi.fun2() #calling the parent function for parent2









#MRO

# class mother:

#     def language(self):
#         print("Hindi")

# class father:

#     def language(self):
#         print("Pujabi")


# #MRO cheacks from left to righ
# # class Child(father, mother):    #Punjabi
# #     pass


# class Child(mother, father):    #Hindi
#     pass
# mahi=Child()

# mahi.language()















#multilevel inheritance


# class dada_ji:
#     def ashivad(slef):
#         print("hmesha khsh raho")


# class papaji (dada_ji):

#     def blessing(slef):
#         print("be happy")

# class neyane(papaji):
#     pass


# mahi=neyane()

# mahi.ashivad()









#hierarchical inheritance


# class parent:
#     def ashirwad(self):
#         print("jite raho")



# class boy(parent):
#     pass

# class girl(parent):
#     pass


# mahi=boy()
# mani=girl()


# mahi.ashirwad()
# mani.ashirwad()












# use of supper function
#super function is use to run the constructor of the parent class

# class parent:
#     def __init__ (slef):
#         print("this is the parent constructor")
    
# class child(parent):
#     def __init__(slef):
#         super().__init__()    # super is used to run the parents class constructor
#         print("this is the child constructor")

# mahi=child()