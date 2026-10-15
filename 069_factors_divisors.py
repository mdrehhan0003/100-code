"""Problem 69: Factors Divisors."""

n = int(input("Positive integer: "))
if n <= 0: print("Enter a positive integer")
else: print("Factors:", [i for i in range(1, n+1) if n % i == 0])
