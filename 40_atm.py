balance = float(input("enter balance: "))
amount = float(input("enter amount"))

if amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Insufficient balance")
elif balance - amount < 500:
    print("Withdrawal rejected: Minimum balance required")
else:
    balance -= amount
    print("Withdrawal approved")
    print("Remaining balance =", balance)
