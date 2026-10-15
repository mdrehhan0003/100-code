"""Problem 32: Positive Then Even Odd."""

n = int(input("Number: "))
if n > 0: print("Positive", "-", "Even" if n % 2 == 0 else "Odd")
elif n < 0: print("Negative")
else: print("Zero")
