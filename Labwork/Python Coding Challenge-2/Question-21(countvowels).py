s = input("Enter a word:")
print(sum(1 for i in s if i.lower() in "aeiou"))
