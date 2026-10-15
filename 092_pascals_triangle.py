"""Problem 92: Pascals Triangle."""

n = int(input("Rows: "))
for i in range(n):
    print(" "*(n-i-1), end="")
    value = 1
    for j in range(i+1):
        print(value, end=" ")
        value = value*(i-j)//(j+1) if j < i else 1
    print()
