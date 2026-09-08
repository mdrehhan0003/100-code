n = int(input("enter the number: "))
if n % 3 and n % 5 == 0:
    print('divisible by both 2 and 5 ')
elif n % 3 == 0:
    print("DIVISABLE BY 3")
elif n % 5 == 0:
    print("divisable by 5")
else:
    print("nither duivisible by 3 or 5 a")
