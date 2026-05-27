import os

limit=int(input("enter the upper limit of the tables: "))





def write_tables(n):
    for i in range (1,n+1):
        with open (f"tables/table{i}.txt","w") as file:
            for j in range (1,5):
                data=(f"{i} X {j} = {i*j}\n")
                file.write(data)

                
    




def create_folder():
    if not os.path.exists("tables"):
        os.makedirs("tables")
        write_tables(limit)
    else:
        write_tables(limit)


create_folder()
