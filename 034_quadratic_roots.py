"""Problem 34: Quadratic Roots."""

import math
a, b, c = map(float, input("Enter coefficients a b c: ").split())
if a == 0:
    print("Not a quadratic equation")
else:
    d = b*b - 4*a*c
    if d > 0: print("Two real roots:", (-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a))
    elif d == 0: print("Equal real roots:", -b/(2*a))
    else: print("Complex roots:", complex(-b/(2*a), math.sqrt(-d)/(2*a)), complex(-b/(2*a), -math.sqrt(-d)/(2*a)))
