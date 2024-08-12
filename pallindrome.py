def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
   
    s = s.lower()
   
    return s == reverse_string(s)
palindrome1 = "racecar"
palindrome2 = "hello"
print(f"Is '{palindrome1}' a palindrome? {is_palindrome(palindrome1)}")  
print(f"Is '{palindrome2}' a palindrome? {is_palindrome(palindrome2)}") 
