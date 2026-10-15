"""Problem 38: Three Digit Armstrong."""

n = int(input("Three-digit number: "))
if not 100 <= abs(n) <= 999: print("Please enter a three-digit number")
else:
    total = sum(int(d)**3 for d in str(abs(n)))
    print("Armstrong number" if total == abs(n) else "Not an Armstrong number")
