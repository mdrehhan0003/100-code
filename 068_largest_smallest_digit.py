"""Problem 68: Largest Smallest Digit."""

digits = [int(d) for d in str(abs(int(input("Integer: "))))]
print("Largest digit:", max(digits))
print("Smallest digit:", min(digits))
