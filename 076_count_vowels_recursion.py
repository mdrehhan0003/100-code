"""Problem 76: Count Vowels Recursion."""

def count_vowels(s):
    if not s: return 0
    return (1 if s[0].lower() in "aeiou" else 0) + count_vowels(s[1:])
s = input("String: ")
print("Vowel count:", count_vowels(s))
