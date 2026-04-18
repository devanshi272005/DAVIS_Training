# function to check number is even or odd
def numberCheck(num):
  if num%2==0:
    return "Even Number"
  else:
    return "Odd Number"
a=int(input("enter a number:"))
result=numberCheck(a)
print(result)