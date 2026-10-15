"""Problem 41: Clock Angle."""

hour = int(input("Hour (1-12): "))
minute = int(input("Minute (0-59): "))
if not (1 <= hour <= 12 and 0 <= minute < 60): print("Invalid time")
else:
    angle = abs(30*(hour % 12) + 0.5*minute - 6*minute)
    print("Smaller angle:", min(angle, 360-angle))
