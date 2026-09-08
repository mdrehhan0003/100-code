a = int(input('ente a: '))
b = int(input( "enter b: "))
c = int (input( "enter c: "))

if a == 0:
    print("Not a quadratic equation")
else:
    d = b * b - 4 * a * c

    if d > 0:
        root1 = (-b + d ** 0.5) / (2 * a)
        root2 = (-b - d ** 0.5) / (2 * a)
        print("Real and distinct roots")
        print(root1, root2)

    elif d == 0:
        root = -b / (2 * a)
        print("Real and equal roots")
        print(root)

    else:
        root1 = (-b + cmath.sqrt(d)) / (2 * a)
        root2 = (-b - cmath.sqrt(d)) / (2 * a)
        print("Imaginary roots")
        print(root1, root2)
