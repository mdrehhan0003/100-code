"""Problem 26: Day Of Week."""

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
n = int(input("Day number (1-7): "))
print(days[n-1] if 1 <= n <= 7 else "Invalid day number")
