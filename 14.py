n = int(input("enter the number : "))
k = int(input("enter bit : "))
if n & ( 1 << k):
    print("kth  bit is set")
else:
    print("kth bit is not set")