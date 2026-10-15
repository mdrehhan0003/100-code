"""Problem 71: Decimal To Binary."""

n = int(input("Non-negative decimal integer: "))
if n < 0: print("Enter a non-negative integer")
elif n == 0: print("Binary: 0")
else:
    bits = ""
    while n:
        bits = str(n % 2) + bits
        n //= 2
    print("Binary:", bits)
