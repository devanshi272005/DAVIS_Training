#count numbers greater than 50 in a list
l = eval(input("Enter numbers:"))
count = 0
for i in l:
    if i > 50:
        count += 1
print(count)
