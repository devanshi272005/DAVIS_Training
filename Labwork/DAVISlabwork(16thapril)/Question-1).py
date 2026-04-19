#copy contents of one file into another
with open("source.txt", "w") as f:
    f.write("This is some sample content.\n")
source = open("source.txt", "r")
destination = open("destination.txt", "w")
content = source.read()
destination.write(content)
source.close()
destination.close()
print("File content copied successfully!")