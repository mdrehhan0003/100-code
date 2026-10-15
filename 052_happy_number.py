"""Problem 52: Happy Number."""

n = abs(int(input("Number: ")))
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = sum(int(d)**2 for d in str(n))
print("Happy number" if n == 1 else "Not a happy number")
