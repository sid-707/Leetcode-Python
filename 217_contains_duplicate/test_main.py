import unittest
from main import contains_duplicate


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEquals(contains_duplicate([1, 2, 3, 1]), True)

    def test_2(self):
        self.assertEquals(contains_duplicate([1, 2, 3, 4]), False)

    def test_3(self):
        self.assertEquals(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)


if __name__ == "__main__":
    unittest.main()
