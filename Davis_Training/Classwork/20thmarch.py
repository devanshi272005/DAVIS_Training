numbers = [12, 45, 7, 23, 89, 34, 2, 67, 10, 50]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] < numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Sorted list in descending order:", numbers)