"""Problem 104: Hollow Diamond Rectangle."""

n = int(input("Rows (at least 3): "))
if n < 3: print("Use at least 3 rows")
else:
    for i in range(n):
        if i == 0 or i == n-1: print("*"*(n+2))
        else:
            inner = min(i, n-1-i)
            print("*"*inner + "*" + " "*(n-2*inner) + "*" + "*"*inner)
