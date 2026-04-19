#file encryption
shift = 3
with open("source.txt", "r") as file:
    data = file.read()
encrypted = ""
for char in data:
    if char.isalpha():
        # Shift letters
        if char.isupper():
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
    else:
        encrypted += char
with open("destination.txt", "w") as out:
    out.write(encrypted)
print("Encrypted content saved in destination.txt")