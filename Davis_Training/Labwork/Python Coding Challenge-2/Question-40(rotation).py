#rotate a list
l = list(map(int,input("Enter a list:").split()))
print([l[-1]]+l[:-1])