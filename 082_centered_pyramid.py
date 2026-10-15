"""Problem 82: Centered Pyramid."""

n = int(input("Rows: "))
for i in range(1, n+1): print(" "*(n-i) + "*"*(2*i-1))
