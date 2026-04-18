filev=open("firstfile.txt","w")
sentences=[]
print("Enter any five sentence:")
for x in range(5):
  sentence=input()
  sentences.append(sentence)
filev.writelines(sentences)
print("Data succeessfully written")
filev.close()