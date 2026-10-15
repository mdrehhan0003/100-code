"""Problem 102: Alphabet Pyramid."""

n = int(input("Rows in upper half: "))
for i in range(1, n+1):
    left = "".join(chr(64+j) for j in range(1, i+1))
    right = "".join(chr(64+j) for j in range(i-1, 0, -1))
    print(" "*(n-i) + left + right)
for i in range(n-1, 0, -1):
    left = "".join(chr(64+j) for j in range(1, i+1))
    right = "".join(chr(64+j) for j in range(i-1, 0, -1))
    print(" "*(n-i) + left + right)
