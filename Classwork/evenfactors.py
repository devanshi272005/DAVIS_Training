# to display even factors
num=int(input("enter the number:"))
print("the even factors are:")
for i in range(1,num+1):
  if num % i==0:
    if i%2==0:
      print(i)