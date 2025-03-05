def r_string(text):
    return text[::-1]

def remove_duplicates(text_1):
    result = []
    seen = set()
    for char in text_1:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return "".join(result)

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def find_vowels(s):
    vowels = set("aeiouаеёиоуыэюя")
    s = s.lower()
    found_vowels = [char for char in s if char in vowels]
    return found_vowels
