import unittest
from portfolio import Portfolio

class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.my_folio = Portfolio()

    def tearDown(self):
        pass

    def test_buy_a_share(self):
        self.my_folio.buy('ABC', 1)
        self.assertEqual(self.my_folio._holdings['ABC'], 1)

    def test_is_empty(self):
        self.assertTrue(self.my_folio.is_empty)

    def test_is_not_empty(self):
        self.my_folio.buy('ABC', 1)
        self.assertFalse(self.my_folio.is_empty)

    def test_sell_a_share(self):
        pass

if __name__ == '__main__':
    unittest.main()