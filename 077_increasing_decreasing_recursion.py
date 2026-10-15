"""Problem 77: Increasing Decreasing Recursion."""

def show(n):
    if n == 0: return
    show(n-1)
    print(n, end=" ")
    if n == 1: print()
    print(n, end=" ")
n = int(input("N: "))
show(max(n, 0))
print()
