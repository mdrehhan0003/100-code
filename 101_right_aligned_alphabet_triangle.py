"""Problem 101: Right Aligned Alphabet Triangle."""

n = int(input("Rows: "))
for i in range(1, n+1): print(" "*(n-i) + "".join(chr(64+j) for j in range(1, i+1)))
