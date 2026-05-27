# reding the content from the file and cheack if the mahi is present in the file or not

# with open("mahi.txt","r") as file:

#     content = file.read()

#     if ("mahi" in content):
#         print("Mahi is present in the file.")
#     else:
#         print("Mahi is not present in the file.")








# creating the content of the file
# c=input("enter the content to update the file: ")
# def data():

#     # creating data.txt file and writing the content to the file
#     with open("data.txt","w") as file:
#         file.write(c)
#         print("file updated successfully")


# data()





# Creating the code to update the file if it has the specific word 

# c=input("enter the name you want to replace in the file: ")

# with open ("data.txt","r") as f:
#     content = f.read()
#     old_value="MAHI"
#     if(old_value in content):
#         with open("data.txt","w") as f:
#             new_content = content.replace(old_value, c)
#             f.write(new_content)
#             print("file updated successfully")
#     else:
#         print("the word is not present in the file")






import os

# creating multiple file for tables 1 to n
n=int(input("enter the number of tables you want to create: "))

if not os.path.exists("tables"):
    os.makedirs("tables")

for i in range(1, n+1):
    with open (f"tables/table_{i}.txt","w") as file:
        for j in range(1,11):
            file.write(f"{i} x {j} = {i*j}\n")




