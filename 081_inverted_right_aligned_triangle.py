"""Problem 81: Inverted Right Aligned Triangle."""

n = int(input("Rows: "))
for i in range(n, 0, -1): print(" "*(n-i) + "*"*i)
