import os

if not os.path.exists("source.txt"):
    with open("source.txt", "w") as src_file:
        src_file.write("This is some sample content for source.txt.\n")
    print("Created 'source.txt' with sample content.")

with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    for line in src:
        dest.write(line)
print("File copied successfully using with statement!")