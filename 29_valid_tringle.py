### Python Program

a = int(input('ente a'))
b = int(input( "enter b "))
c = int (input( "enter c"))

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")