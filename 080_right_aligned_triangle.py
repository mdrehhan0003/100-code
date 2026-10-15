"""Problem 80: Right Aligned Triangle."""

n = int(input("Rows: "))
for i in range(1, n+1): print(" "*(n-i) + "*"*i)
