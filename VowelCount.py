def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in vowels:
        count += s.count(i)
    
    return count
s = "hello world"
result = count_vowels(s)
print(f"The number of vowels in '{example_string}' is: {result}")
