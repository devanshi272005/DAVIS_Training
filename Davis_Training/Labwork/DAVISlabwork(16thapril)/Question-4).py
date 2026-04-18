#remove duplicate lines
seen = set()

with open("source.txt", "r") as file, open("destination.txt", "w") as out:
    for line in file:
        if line not in seen:   # Check for uniqueness
            out.write(line)
            seen.add(line)

print("Duplicates removed and saved in destination.txt")