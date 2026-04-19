#find the duplicates 
s = input("Enter a character")
seen=set()
dup=set()
for i in s:
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)
print(*dup)
