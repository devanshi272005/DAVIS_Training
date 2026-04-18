#find the longest word
s = input("Enter a word:").split()
print(max(s,key=len))