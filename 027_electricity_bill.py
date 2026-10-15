"""Problem 27: Electricity Bill."""

units = float(input("Electricity units: "))
# Illustrative slabs: first 100 at 1.5, next 100 at 2.5, above 200 at 4.0.
if units < 0: print("Invalid units")
else:
    bill = min(units, 100)*1.5 + max(min(units-100, 100), 0)*2.5 + max(units-200, 0)*4
    print("Electricity bill:", bill)
