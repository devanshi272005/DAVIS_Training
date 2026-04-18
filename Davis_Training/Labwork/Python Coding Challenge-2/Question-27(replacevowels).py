#replacing  vowels
s = input("Enter a word:")
res=""
for i in s:
    res += "*" if i.lower() in "aeiou" else i
print(res)
