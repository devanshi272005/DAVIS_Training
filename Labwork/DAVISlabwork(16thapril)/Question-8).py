#keyword search tool
keyword = input("Enter keyword to search: ")

with open("source.txt", "r") as file:
    for line in file:
        if keyword.lower() in line.lower():  # Case-insensitive search
            print(line.strip())