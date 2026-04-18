#calculation of leap year
y = int(input())
if (y%4==0 and y%100!=0) or y%400==0:
    print("Leap Year")   #yes it's a leap year
else:
    print("Not Leap Year")
