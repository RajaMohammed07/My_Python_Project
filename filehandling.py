file=open("filehandling.txt","w")
file.write("This is a file handling example.\n")
file.write("We are writing to a file using Python.\n")
file.close()


file=open("filehandling.txt","a")
file.write("This is an additional line in the file.\n")
file.close()

file=open("filehandling.txt","r")
print(file.read())
file.close()

with open("filehandling.txt","r") as file:
    for line in file:
        print(line.strip())