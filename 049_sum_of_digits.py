"""Problem 49: Sum Of Digits."""

n = abs(int(input("Integer: ")))
total = 0
while n:
    total += n % 10
    n //= 10
print("Digit sum:", total)
