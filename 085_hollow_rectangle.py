"""Problem 85: Hollow Rectangle."""

rows = int(input("Rows: "))
cols = int(input("Columns: "))
for i in range(rows):
    if i == 0 or i == rows-1: print("*"*cols)
    else: print("*" + " "*(max(cols-2, 0)) + ("*" if cols > 1 else ""))
