"""Problem 29: Valid Triangle."""

a, b, c = map(float, input("Enter three sides: ").split())
print("Valid triangle" if min(a,b,c) > 0 and a+b > c and a+c > b and b+c > a else "Invalid triangle")
