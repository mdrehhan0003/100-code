a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number : "))
if a < b and b > c :
    print( b," is large")
elif c > a and c > b :
    print(c," is large")
else: 
    print(a," is large ")
