"""Problem 63: Power Without Pow."""

x = float(input("Base x: "))
n = int(input("Integer exponent n: "))
result = 1
for _ in range(abs(n)): result *= x
if n < 0:
    if result == 0: print("Undefined: zero cannot have a negative exponent")
    else: print(1/result)
else: print(result)
