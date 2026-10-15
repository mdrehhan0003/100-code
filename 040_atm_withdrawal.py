"""Problem 40: Atm Withdrawal."""

balance = float(input("Account balance: "))
amount = float(input("Withdrawal amount: "))
minimum = float(input("Minimum balance to maintain: "))
if amount <= 0: print("Invalid amount")
elif amount > balance: print("Rejected: insufficient balance")
elif balance-amount < minimum: print("Rejected: minimum balance rule")
else: print("Approved. Remaining balance:", balance-amount)
