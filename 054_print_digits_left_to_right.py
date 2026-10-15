"""Problem 54: Print Digits Left To Right."""

n = input("Integer: ").strip()
digits = n.lstrip("-")
print(*digits, sep=" ")
