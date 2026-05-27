with open("Mahi-Singh.txt", "a") as f:
    data1 = " new data appended"
    data2 = "\nnew data appended in the new line"

    f.writelines([data1, data2])