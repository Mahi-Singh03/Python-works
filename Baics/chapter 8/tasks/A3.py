class students:
    name="student"
    classs="radom"
    reult=bool
    def __init__(self,name,classs,reult):
        self.name=name
        self.classs=classs
        self.reult=reult

    def printData (self):
        print(f"my name is {self.name}. i am from class {self.classs}, and my result is {self.reult}")
    

mahi=students("mahi","BSc",True)
Monika=students("monika" , "BSc",True)

Monika.printData()