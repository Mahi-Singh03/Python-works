listOfWord=["bad","badest"]

with open ("files/A9.txt","r") as file:
    data=file.read()
    for i in listOfWord:
        if i in data:
            data=data.replace(i,"*"*len(i))

with open ("files/A9.txt","w") as file:
    file.write(data)