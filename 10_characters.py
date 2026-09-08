x = input("enter the charecter")
if 'A' <= x <= 'Z' :
    print("upper case")
elif 'a' <= x <= 'z' :
    print('lower case')
elif '0' <= x <= '9' :
    print("digit")
else:
    print("special character")