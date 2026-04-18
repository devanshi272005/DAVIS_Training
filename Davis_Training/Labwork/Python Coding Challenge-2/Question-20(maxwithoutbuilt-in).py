#find the maximum value
l = list(map(int,input("Enter a list:").split()))
mx = l[0]
for i in l:
    if i>mx: mx=i
print(mx)
