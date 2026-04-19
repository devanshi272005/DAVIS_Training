#email extractor
import re

emails = []

with open("source.txt", "r") as file:
    for line in file:
        found = re.findall(r'\S+@\S+', line)  # Find emails
        emails.extend(found)

# Save emails into destination file
with open("destination.txt", "w") as out:
    for email in emails:
        out.write(email + "\n")

print("Emails extracted to destination.txt")