#find longest line
longest_line = ""
max_length = 0

with open("source.txt", "r") as file:
    for line in file:
        if len(line) > max_length:
            max_length = len(line)
            longest_line = line

print("Longest Line:", longest_line.strip())
print("Length:", max_length)