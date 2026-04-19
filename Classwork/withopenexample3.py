# Create article.txt with some sample content
with open("article.txt", "w") as f:
    f.write("This is a sample article. It contains sample text for word counting.")

import string

# Dictionary to store frequency
word_count = {}

with open("article.txt", "r") as file:
    for line in file:
        # Remove punctuation and convert to lowercase
        line = line.translate(str.maketrans('', '', string.punctuation)).lower()
        words = line.split()

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

# Print result
for word, count in word_count.items():
    print(word, ":", count)