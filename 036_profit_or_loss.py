"""Problem 36: Profit Or Loss."""

cp, sp = map(float, input("Cost price and selling price: ").split())
if sp > cp: print("Profit:", sp-cp)
elif sp < cp: print("Loss:", cp-sp)
else: print("No profit, no loss")
