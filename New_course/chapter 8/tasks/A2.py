class human:
    name="unknown"
    age=0
    result="un-declared"

    def __init__(self,name,age,result):
        self.name=name
        self.age=age
        self.result=result
    
    def greeting (self):
        print(f"my name is {self.name}, i am {self.age} years old and i am {self.result} in my exams")

    @staticmethod # this keyword is used when you want to  pass the complete method without passing the complete object (self)
    def print ():
        print("mahi")



mahi= human("mahi",89,"Pass")
mahi.greeting()
mahi.print()
