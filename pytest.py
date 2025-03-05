import pytest
import kods


def test_r_string():
    assert kods.r_string("hello") == "olleh"

    assert kods.r_string("") == ""

    assert kods.r_string("a") == "a"

    assert kods.r_string("hello world") == "dlrow olleh"

    assert kods.r_string("123!@#") == "#@!321"

    assert kods.r_string("привет") == "тевирп"

if __name__ == '__main__':
    pytest.main()



def test_remove_duplicates():

    assert kods.remove_duplicates("abcdef") == "abcdef"

    assert kods.remove_duplicates("aabbcc") == "abc"

    assert kods.remove_duplicates("") == ""

    assert kods.remove_duplicates("aaaaa") == "a"

    assert kods.remove_duplicates("hello world") == "helo wrd"

    assert kods.remove_duplicates("112233!!@@##") == "123!@#"

    assert kods.remove_duplicates("привет привет") == "привет "

if __name__ == '__main__':
    pytest.main()


def test_is_palindrome():

    assert kods.is_palindrome("racecar") == True

    assert kods.is_palindrome("A man a plan a canal Panama") == True

    assert kods.is_palindrome("") == True

    assert kods.is_palindrome("hello") == False

    assert kods.is_palindrome("Madam") == True

    assert kods.is_palindrome("12321") == True

    assert kods.is_palindrome("12345") == False

    assert kods.is_palindrome("шалаш") == True

    assert kods.is_palindrome("привет") == False

if __name__ == '__main__':
    pytest.main()


def test_find_vowels():

    assert kods.find_vowels("aeiou") == ["a", "e", "i", "o", "u"]

    assert kods.find_vowels("аеёиоуыэюя") == ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

    assert kods.find_vowels("hello world") == ["e", "o", "o"]

    assert kods.find_vowels("привет мир") == ["и", "е", "и"]

    assert kods.find_vowels("") == []

    assert kods.find_vowels("bcdfg") == []

    assert kods.find_vowels("бвгджз") == []

    assert kods.find_vowels("AEIOU") == ["a", "e", "i", "o", "u"]

    assert kods.find_vowels("АЕЁИОУЫЭЮЯ") == ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

    assert kods.find_vowels("123!@# aeiou") == ["a", "e", "i", "o", "u"]

if __name__ == '__main__':
    pytest.main()
