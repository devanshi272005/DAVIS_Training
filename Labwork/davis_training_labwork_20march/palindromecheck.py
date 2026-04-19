def is_palindrome(s):
    original = s
    reversed_str = ""

    for char in s:
        reversed_str = char + reversed_str

    if original == reversed_str:
        print("Palindrome")
    else:
        print("Not Palindrome")

value = input("Enter string/number: ")
is_palindrome(value)