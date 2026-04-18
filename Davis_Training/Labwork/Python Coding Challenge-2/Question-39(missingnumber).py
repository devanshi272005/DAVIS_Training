#find the missing number
l = list(map(int,input("Enter a number:").split()))
n = max(l)
print(sum(range(1,n+1))-sum(l))