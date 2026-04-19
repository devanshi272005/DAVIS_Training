#file merge with line numbers
# Read source file twice (simulating two files if needed)
with open("source.txt", "r") as f1, open("source.txt", "r") as f2:
    lines = f1.readlines() + f2.readlines()

# Write merged content with line numbers
with open("destination.txt", "w") as out:
    for i, line in enumerate(lines, start=1):
        out.write(f"{i}. {line}")

print("Files merged with line numbers into destination.txt")