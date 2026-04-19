#second largest
l = list(map(int,input("Enter a list:").split()))
l = list(set(l))
l.sort()
print(l[-2])