"""Problem 50: Reverse Number."""

n = int(input("Integer: "))
sign = -1 if n < 0 else 1
value = abs(n)
rev = 0
while value:
    rev = rev*10 + value%10
    value //= 10
print(sign*rev)
