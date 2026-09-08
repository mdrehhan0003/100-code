hours = float(input("enter hours: "))
rate = float(input("enter rate: "))

if hours <= 40:
    salary = hours * rate
else:
    overtime = hours - 40
    salary = (40 * rate) + (overtime * rate * 1.5)

print("Salary =", salary)
