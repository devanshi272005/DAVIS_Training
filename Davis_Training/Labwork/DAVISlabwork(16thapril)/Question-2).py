#students report filter
with open("student.txt", "w") as f:
    f.write("Alice,85,New York\n")
    f.write("Bob,70,Los Angeles\n")
    f.write("Charlie,92,Chicago\n")
    f.write("David,60,Houston\n")
    f.write("Eve,78,Phoenix\n")
with open("student.txt", "r") as source:
    with open("output.txt", "w") as destination:
        for line in source:
            data = line.strip().split(",")
            name = data[0]
            marks = float(data[1])
            city = data[2]
            if marks > 75:
                destination.write(line)
print("Students with marks > 75 % copied successfully!")