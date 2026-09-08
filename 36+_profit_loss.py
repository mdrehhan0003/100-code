cp = float(input())
sp = float(input())

if sp > cp:
    print("Profit =", sp - cp)
elif sp < cp:
    print("Loss =", cp - sp)
else:
    print("No Profit No Loss")
