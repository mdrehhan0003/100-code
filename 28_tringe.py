a = int(input('ente a'))
b = int(input( "enter b "))
c = int (input( "enter c"))

if a + b <= c or a + c <= b or b + c <= a:
    print("Not a triangle")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
