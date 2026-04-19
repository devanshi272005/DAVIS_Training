#reverse file content
with open("source.txt", "r") as file:
    lines = file.readlines()

# Reverse lines
lines.reverse()

with open("destination.txt", "w") as out:
    out.writelines(lines)

print("Reversed content saved in destination.txt")