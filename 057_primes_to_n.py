"""Problem 57: Primes To N."""

n = int(input("N: "))
for x in range(2, n+1):
    prime = True
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            prime = False
            break
    if prime: print(x, end=" ")
print()
