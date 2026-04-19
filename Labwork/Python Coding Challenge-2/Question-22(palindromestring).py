#checks whether a string is palindrome or not
s = input("Enter a string:")
print("Yes" if s==s[::-1] else "No")
