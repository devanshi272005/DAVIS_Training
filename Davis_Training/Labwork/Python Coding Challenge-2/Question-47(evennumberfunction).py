#function to return all even numbers
def even(l):
    return [i for i in l if i%2==0]
print(even([1,2,3,4]))