import unittest
import kods
class TestRString(unittest.TestCase):
    def test_r_string(self):
        self.assertEqual(kods.r_string("Hello word"), "drow olleH")

if __name__ == '__main__':
    unittest.main()

class TestRString(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(kods.remove_duplicates("Hello world"), "Helo wrd")

if __name__ == '__main__':
    unittest.main()


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(kods.is_palindrome("А роза упала на лапу Азора"))
        self.assertTrue(kods.is_palindrome("Madam"))
        self.assertTrue(kods.is_palindrome("level"))
        self.assertTrue(kods.is_palindrome("12321"))

    def test_not_palindrome(self):
        self.assertFalse(kods.is_palindrome("Hello"))
        self.assertFalse(kods.is_palindrome("Python"))
        self.assertFalse(kods.is_palindrome("12345"))

    def test_empty_string(self):
        self.assertTrue(kods.is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(kods.is_palindrome("a"))
        self.assertTrue(kods.is_palindrome("1"))

if __name__ == '__main__':
    unittest.main()



class TestFindVowels(unittest.TestCase):

    def test_find_vowels(self):
        self.assertEqual(kods.find_vowels("Hello"), ['e', 'o'])
        self.assertEqual(kods.find_vowels("Python"), ['o'])
        self.assertEqual(kods.find_vowels("Привет"), ['и', 'е'])
        self.assertEqual(kods.find_vowels("Аэрофотосъёмка"), ['а', 'э', 'о', 'о', 'о', 'ё', 'а'])

    def test_no_vowels(self):
        self.assertEqual(kods.find_vowels("xyz"), [])
        self.assertEqual(kods.find_vowels("Крк"), [])

    def test_empty_string(self):
        self.assertEqual(kods.find_vowels(""), [])

    def test_all_vowels(self):
        self.assertEqual(kods.find_vowels("aeiouаеёиоуыэюя"), ['a', 'e', 'i', 'o', 'u', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'])

if __name__ == '__main__':
    unittest.main()
