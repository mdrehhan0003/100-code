"""Problem 55: Factorial."""

n = int(input("N: "))
if n < 0: print("Factorial is undefined for negative integers")
else:
    result = 1
    for i in range(2, n+1): result *= i
    print(result)
