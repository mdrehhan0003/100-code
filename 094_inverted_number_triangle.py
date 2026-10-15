"""Problem 94: Inverted Number Triangle."""

n = int(input("Rows: "))
for i in range(n, 0, -1): print("".join(str(j) for j in range(1, i+1)))
