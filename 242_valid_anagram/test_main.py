import unittest
from main import valid_anagram


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(valid_anagram("anagram", "nagaram"), True)

    def test_2(self):
        self.assertEqual(valid_anagram("rat", "car"), False)


if __name__ == "__main__":
    unittest.main()
