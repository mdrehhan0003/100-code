"""Problem 100: Reverse Alphabet Triangle."""

n = int(input("Rows: "))
for i in range(n, 0, -1): print("".join(chr(64+j) for j in range(1, i+1)))
