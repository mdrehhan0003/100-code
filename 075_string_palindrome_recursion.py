"""Problem 75: String Palindrome Recursion."""

def is_palindrome(s):
    if len(s) <= 1: return True
    if s[0] != s[-1]: return False
    return is_palindrome(s[1:-1])
s = input("String: ")
print("Palindrome" if is_palindrome(s) else "Not a palindrome")
