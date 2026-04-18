filev=open("firstfile.txt","w")
print("Enter any five sentence:")
for x in range(5):
  sentence=input()
  filev.write(sentence+"\n")
filev.close()
