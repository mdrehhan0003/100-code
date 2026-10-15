"""Problem 91: Alternating 1 0 Triangle."""

n = int(input("Rows: "))
for i in range(1, n+1):
    print("".join("1" if j % 2 == 0 else "0" for j in range(i)))
