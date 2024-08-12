def are_anagrams(s1, s2):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
  #  s1 = s1.replace(" ", "").lower()
  #  s2 = s2.replace(" ", "").lower()
    
    # Sort both strings and compare
    return sorted(s1) == sorted(s2)

# Example usage
s1 = "listen"
s2 = "silent"
result = are_anagrams(string1, string2)
print(f"'{string1}' and '{string2}' are anagrams: {result}")
