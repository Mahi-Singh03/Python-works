wordTofFind="mahi"

with open ("files/A10.txt","r") as file:
    data=file.readlines()
    for index , line in enumerate (data,start=1):
        if wordTofFind in line:
            print(f"word found at line number {index}")