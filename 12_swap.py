a = int(input("enter the value a: "))
b = int(input("enter the value b: "))
print("before swapping: a=",a, "b=", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("after swapping: a=",a, "b=", b)