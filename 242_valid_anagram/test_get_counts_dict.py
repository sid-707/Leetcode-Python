import unittest
from get_counts_dict import get_counts_dict


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertDictEqual(
            get_counts_dict("anagram"), {"a": 3, "n": 1, "g": 1, "m": 1, "r": 1}
        )

    def test_2(self):
        self.assertDictEqual(
            get_counts_dict("nagaram"), {"a": 3, "n": 1, "g": 1, "m": 1, "r": 1}
        )

    def test_3(self):
        self.assertDictEqual(get_counts_dict("car"), {"a": 1, "c": 1, "r": 1})

    def test_4(self):
        self.assertDictEqual(get_counts_dict("rat"), {"a": 1, "r": 1, "t": 1})


if __name__ == "__main__":
    unittest.main()
