#count frequency of elements using dictionary
l = list(map(int,input("Enter a list:").split()))
d={}
for i in l:
    d[i]=d.get(i,0)+1
print(d)