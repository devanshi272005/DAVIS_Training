#check whether it's a prime or not
def prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print("Prime" if prime(7) else "Not Prime")