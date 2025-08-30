import unittest
from scrabble_score import Scrabble

class ScrabbleTest(unittest.TestCase):
    def test_empty_word_scores_zero(self):
        self.assertEqual(0, Scrabble("").score())

    def test_whitespace_scores_zero(self):
        self.assertEqual(0, Scrabble(" \t\n").score())

    def test_nil_scores_zero(self):
        self.assertEqual(0, Scrabble(None).score())

    def test_scores_very_short_word(self):
        self.assertEqual(1, Scrabble("a").score())

    def test_scores_other_very_short_word(self):
        self.assertEqual(4, Scrabble("f").score())

    def test_simple_word_scores_the_number_of_letters(self):
        self.assertEqual(6, Scrabble("street").score())

    def test_complicated_word_scores_more(self):
        self.assertEqual(22, Scrabble("quirky").score())

    def test_scores_are_case_insensitive(self):
        self.assertEqual(41, Scrabble("OXYPHENBUTAZONE").score())

    def test_convenient_scoring(self):
        self.assertEqual(13, Scrabble.calculate_score("alacrity"))

if __name__ == "__main__":
    unittest.main()