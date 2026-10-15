"""Problem 30: Simple Calculator."""

a = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Second number: "))
if op == "+": print(a+b)
elif op == "-": print(a-b)
elif op == "*": print(a*b)
elif op == "/" and b != 0: print(a/b)
elif op == "/": print("Cannot divide by zero")
else: print("Invalid operator")
