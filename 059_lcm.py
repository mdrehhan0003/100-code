"""Problem 59: Lcm."""

import math
a, b = map(int, input("Enter two integers: ").split())
print("LCM:", abs(a*b)//math.gcd(a,b) if a and b else 0)
