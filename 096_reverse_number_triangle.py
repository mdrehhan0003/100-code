"""Problem 96: Reverse Number Triangle."""

n = int(input("Rows: "))
for i in range(n, 0, -1): print("".join(str(j) for j in range(i, 0, -1)))
