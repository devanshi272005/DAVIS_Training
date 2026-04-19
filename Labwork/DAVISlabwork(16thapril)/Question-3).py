#word frequency counter
import string
# Dictionary to store frequency
word_count = {}
with open("source.txt", "r") as file:
    for line in file:
        # Remove punctuation and convert to lowercase
        line = line.translate(str.maketrans('', '', string.punctuation)).lower()
        words = line.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
for word, count in word_count.items():
    print(word, ":", count)