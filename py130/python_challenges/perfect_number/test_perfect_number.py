import unittest
from perfect_number import PerfectNumber

class PerfectNumberTest(unittest.TestCase):
    def test_initialize_perfect_number(self):
        try:
            PerfectNumber.classify(-1)
            self.fail("Expected exception not raised")
        except ValueError as e:
            self.assertEqual(str(e), "Input must be a positive integer")

    def test_classify_deficient(self):
        result = PerfectNumber.classify(13)
        self.assertEqual(result, "deficient")

    def test_classify_perfect(self):
        result = PerfectNumber.classify(28)
        self.assertEqual(result, "perfect")

    def test_classify_abundant(self):
        result = PerfectNumber.classify(12)
        self.assertEqual(result, "abundant")

if __name__ == "__main__":
    unittest.main()