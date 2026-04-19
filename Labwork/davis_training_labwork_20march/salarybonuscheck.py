def calculate_bonus(salary, years):
    if years >= 10:
        bonus = 0.20 * salary
    elif years >= 5:
        bonus = 0.10 * salary
    else:
        bonus = 0.05 * salary
    
    return bonus

n = int(input("Enter number of employees: "))

for i in range(n):
    salary = float(input("Enter salary: "))
    years = int(input("Enter experience: "))
    
    bonus = calculate_bonus(salary, years)
    print("Bonus:", bonus)