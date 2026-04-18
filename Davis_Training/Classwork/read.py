filev=open("firstfile.txt","r")
if(filev):
  data=filev.read()
  print(data)
  print("No of characters:",len(data))
  filev.close()
else:
  print("unable to open the file")