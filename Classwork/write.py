filev=open("firstfile.txt","w")
print("Enter any 20 sentences:")
for x in range(20):
  sentence=input()
  filev.write(sentence+"\n")
filev.close()
