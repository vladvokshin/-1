import kods

def test_r_string():
    if kods.r_string("hello world") == "dlrow olleh":
        print("Test r_string('hello world') is OK")
    else:
        print("Test r_string('hello world') is Fail")

    if kods.r_string("12345") == "54321":
        print("Test r_string('12345') is OK")
    else:
        print("Test r_string('12345') is Fail")

    if kods.r_string("") == "":
        print("Test r_string('') is OK")
    else:
        print("Test r_string('') is Fail")

    if kods.r_string("a") == "a":
        print("Test r_string('a') is OK")
    else:
        print("Test r_string('a') is Fail")


test_r_string()




def test_remove_duplicates():
    if kods.remove_duplicates("hello") == "helo":
        print("Test remove_duplicates('hello') is OK")
    else:
        print("Test remove_duplicates('hello') is Fail")

    if kods.remove_duplicates("aabbcc") == "abc":
        print("Test remove_duplicates('aabbcc') is OK")
    else:
        print("Test remove_duplicates('aabbcc') is Fail")

    if kods.remove_duplicates("") == "":
        print("Test remove_duplicates('') is OK")
    else:
        print("Test remove_duplicates('') is Fail")

    if kods.remove_duplicates("abcabc") == "abc":
        print("Test remove_duplicates('abcabc') is OK")
    else:
        print("Test remove_duplicates('abcabc') is Fail")

    if kods.remove_duplicates("aaa") == "a":
        print("Test remove_duplicates('aaa') is OK")
    else:
        print("Test remove_duplicates('aaa') is Fail")



test_remove_duplicates()




def test_is_palindrome():
    if kods.is_palindrome("racecar") == True:
        print("Test is_palindrome('racecar') is OK")
    else:
        print("Test is_palindrome('racecar') is Fail")

    if kods.is_palindrome("hello") == False:
        print("Test is_palindrome('hello') is OK")
    else:
        print("Test is_palindrome('hello') is Fail")

    if kods.is_palindrome("A man a plan a canal Panama") == True:
        print("Test is_palindrome('A man a plan a canal Panama') is OK")
    else:
        print("Test is_palindrome('A man a plan a canal Panama') is Fail")

    if kods.is_palindrome("") == True:
        print("Test is_palindrome('') is OK")
    else:
        print("Test is_palindrome('') is Fail")

    if kods.is_palindrome("a") == True:
        print("Test is_palindrome('a') is OK")
    else:
        print("Test is_palindrome('a') is Fail")


test_is_palindrome()


def test_find_vowels():
    if kods.find_vowels("hello") == ['e', 'o']:
        print("Test find_vowels('hello') is OK")
    else:
        print("Test find_vowels('hello') is Fail")

    if kods.find_vowels("world") == ['o']:
        print("Test find_vowels('world') is OK")
    else:
        print("Test find_vowels('world') is Fail")

    if kods.find_vowels("привет") == ['и', 'е']:
        print("Test find_vowels('привет') is OK")
    else:
        print("Test find_vowels('привет') is Fail")

    if kods.find_vowels("") == []:
        print("Test find_vowels('') is OK")
    else:
        print("Test find_vowels('') is Fail")

    if kods.find_vowels("AEIOU") == ['a', 'e', 'i', 'o', 'u']:
        print("Test find_vowels('AEIOU') is OK")
    else:
        print("Test find_vowels('AEIOU') is Fail")

test_find_vowels()
