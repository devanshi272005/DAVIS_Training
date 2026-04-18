#tail implementation
n = int(input("Enter number of last lines: "))
with open("source.txt", "r") as file:
    lines = file.readlines()
for line in lines[-n:]:
    print(line.strip())