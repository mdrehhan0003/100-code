"""Problem 72: Binary To Decimal."""

binary = input("Binary number: ").strip()
if binary and all(ch in "01" for ch in binary): print("Decimal:", int(binary, 2))
else: print("Invalid binary number")
