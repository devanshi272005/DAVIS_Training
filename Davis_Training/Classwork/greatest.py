# to find out the greatest number
num=int(input("enter the number:"))
max=0
while(num>0):
  digit=num % 10
  if(digit>max):
    max=digit
  num=num//10
print("the greatest number is:",max)