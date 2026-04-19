#Program to count number of vowels in a file
file = open("firstfile.txt", "r")
content = file.read()
vowel_count = 0
vowels = "aeiouAEIOU"
for char in content:
    if char in vowels:
        vowel_count += 1
print("Number of vowels in the file:", vowel_count)