#compare two files
# Comparing source.txt with destination.txt
with open("source.txt", "r") as f1, open("destination.txt", "r") as f2:
    lines1 = set(f1.readlines())
    lines2 = set(f2.readlines())

difference = lines1 - lines2

print("Lines in source.txt but not in destination.txt:")
for line in difference:
    print(line.strip())