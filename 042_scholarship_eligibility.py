"""Problem 42: Scholarship Eligibility."""

marks = float(input("Marks (%): "))
attendance = float(input("Attendance (%): "))
income = float(input("Annual family income: "))
# Example criteria; adjust if your assignment specifies different thresholds.
eligible = marks >= 85 and attendance >= 75 and income <= 250000
print("Eligible for scholarship" if eligible else "Not eligible")
