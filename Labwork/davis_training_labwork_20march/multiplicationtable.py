def print_table(num):
    if num < 0:
        print("Negative number not allowed")
        return
    
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

num = int(input("Enter number: "))
print_table(num)