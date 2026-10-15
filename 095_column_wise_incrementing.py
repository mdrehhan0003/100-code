"""Problem 95: Column Wise Incrementing."""

n = int(input("Rows: "))
for i in range(1, n+1): print("".join(str(j) for j in range(1, i+1)))
