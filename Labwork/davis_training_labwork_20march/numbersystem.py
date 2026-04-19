def classify_number(num):
    if num > 0:
        print(num, "is Positive")
    elif num < 0:
        print(num, "is Negative")
    else:
        print(num, "is Zero")

    # Nested if
    if num != 0:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

numbers = [10, -5, 0, 7, 8]

for num in numbers:
    classify_number(num)
    print()