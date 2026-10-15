"""Problem 89: Sequential Number Triangle."""

n = int(input("Rows: "))
value = 1
for i in range(1, n+1):
    row = []
    for _ in range(i):
        row.append(str(value)); value += 1
    print(" ".join(row))
