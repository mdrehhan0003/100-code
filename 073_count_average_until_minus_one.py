"""Problem 73: Count Average Until Minus One."""

values = []
while True:
    try: n = float(input("Enter number (-1 to stop): "))
    except ValueError:
        print("Enter a valid number")
        continue
    if n == -1: break
    values.append(n)
print("Count:", len(values))
print("Average:", sum(values)/len(values) if values else "No numbers entered")
