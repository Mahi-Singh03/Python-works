# Protected Members
# declared with the _variable
# A protected variable is meant for internal use, but Python does not strictly prevent access.



# class boy:
#     def __init__(self):
#         self._marks=90    #declaring a proteted variable


# mahi=boy()
# print(mahi._marks) #90   you can get this output








# private member
# declated with the double _

# class boy:
#     def __init__(self):
#         self.__marks=90    #declaring a proteted variable


# mahi=boy()
# print(mahi._marks) # you gets an error








#Accessing Private Variables (Not Recommended)
#Although private variables are hidden, Python still stores them.


# class emp:
#     def __init__(slef):
#         slef.__sallery=500000

# mahi=emp()

# print(mahi._emp__sallery) # you cant acess direclty but there is a turn around







#acessing the private data member
#using getter method
#this method return the private method


# class emp:
#     def __init__(self):
#         self.__sallery=8989898

#     def method_to_get_the_private_member(self):  #this is the mehtod you can use to acess the method
#         return self.__sallery
    
# mahi=emp()

# print(mahi.method_to_get_the_private_member())











# class emp:
#     def __init__(self):
#         self.___sallery=10000
    
#     #new value setter:
#     def new_value_setter (self,sallery):
#         self.___sallery=sallery

#     #getter function

#     def get_value(self):
#         return self.___sallery
    


# mahi=emp()

# print(mahi.get_value())
# mahi.new_value_setter(20)
# print(mahi.get_value())





# class subject:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__result = "not declared"

#         if marks <= 100 and marks >= 0:
#             self.__marks = marks
#         else:
#             print("Value is not valid")

#     # setter function
#     def Set_Value(self, result):
#         self.__result = result

#     # getter function for both result and marks
#     def Get_value(self):
#         return self.__result, self.__marks


# hindi = subject("mahi",89)

# print(hindi.Get_value())

# hindi.Set_Value("pass")

# print(hindi.Get_value())





# class Student:

#     def __init__(self):
#         self.__marks = 90

#     @property
#     def marks(self):
#         return self.__marks

#     @marks.setter
#     def marks(self, value):

#         if 0 <= value <= 100:
#             self.__marks = value
#         else:
#             print("Invalid Marks")

# student1 = Student()

# student1.marks = 989

# print(student1.marks)








# class password:
#     __password="2012"

#     @property                           #using the property we can use this way
#     def geetPassword(self):
#         return self.__password
    
#     #regulare way:


#     def getPasswordInRegularWay(self):
#         return self.__password

# mainn=password()

# print(mainn.geetPassword)  #for property method
# print(mainn.getPasswordInRegularWay()) #for regular way













#property Setter 

class Bank:

    def __init__(self):
        self.__password = "admin123"

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password


pass1 = Bank()

pass1.password = "new password 123"

print(pass1.password)












