"""Problem 51: Number Palindrome."""

n = input("Integer: ").strip()
print("Palindrome" if n == n[::-1] else "Not a palindrome")
