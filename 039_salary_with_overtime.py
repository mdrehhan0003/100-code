"""Problem 39: Salary With Overtime."""

hours = float(input("Hours worked: "))
rate = float(input("Hourly rate: "))
if hours <= 40: salary = hours*rate
else: salary = 40*rate + (hours-40)*rate*1.5
print("Salary:", salary)
