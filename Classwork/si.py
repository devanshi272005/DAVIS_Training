def calculateSi(p,r,t):
  return((p*r*t)/100)
principal=float(input("Enter principal(in Rs.):"))
rate=float(input("Enter rate (in %):"))
time=int(input("Enter time(in years):"))
print("Simple Interest(in Rs.)",calculateSi(principal,rate,time))
