"""Problem 66: Sum Even Odd Separately."""

n = int(input("N: "))
even_sum = sum(i for i in range(1, n+1) if i % 2 == 0)
odd_sum = sum(i for i in range(1, n+1) if i % 2 != 0)
print("Even sum:", even_sum)
print("Odd sum:", odd_sum)
