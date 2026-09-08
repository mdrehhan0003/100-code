n = int(input("enterr : "))

a = n // 100
b = (n // 10) % 10
c = n % 10

if a**3 + b**3 + c**3 == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
