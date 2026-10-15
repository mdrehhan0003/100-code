"""Problem 31: Days In Month."""

import calendar
month = int(input("Month (1-12): "))
year = int(input("Year: "))
print(calendar.monthrange(year, month)[1] if 1 <= month <= 12 else "Invalid month")
