import unittest
from sum_of_multiples import SumOfMultiples

class SumTest(unittest.TestCase):
    def test_sum_to_1(self):
        self.assertEqual(0, SumOfMultiples.sum_up_to(1))

    def test_sum_to_3(self):
        self.assertEqual(3, SumOfMultiples.sum_up_to(4))

    def test_sum_to_10(self):
        self.assertEqual(23, SumOfMultiples.sum_up_to(10))

    def test_sum_to_100(self):
        self.assertEqual(2_318, SumOfMultiples.sum_up_to(100))

    def test_sum_to_1000(self):
        self.assertEqual(233_168, SumOfMultiples.sum_up_to(1000))

    def test_configurable_7_13_17_to_20(self):
        self.assertEqual(51, SumOfMultiples(7, 13, 17).to(20))

    def test_configurable_4_6_to_15(self):
        self.assertEqual(30, SumOfMultiples(4, 6).to(15))

    def test_configurable_5_6_8_to_150(self):
        self.assertEqual(4419, SumOfMultiples(5, 6, 8).to(150))

    def test_configurable_43_47_to_10000(self):
        self.assertEqual(2_203_160, SumOfMultiples(43, 47).to(10_000))

if __name__ == "__main__":
    unittest.main()