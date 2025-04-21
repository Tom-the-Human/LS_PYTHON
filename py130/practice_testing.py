import unittest

class TestPractice(unittest.TestCase):
    def setUp(self):
        self.value = 101
        
        class Numeric:
            pass

    # 1
    def test_oddness(self):
        self.assertTrue(self.value % 2 != 0, "Not an odd number!")

    # 2
    def test_xyz(self):
        self.value = 'XYZ'
        self.assertEqual(self.value.lower(), 'xyz')

    # 3
    def test_not_none(self):
        self.value = None
        self.assertIsNone(self.value)

    # 4
    def test_membership(self):
        self.value = 'xyz'
        lst = [self.value]
        self.assertIn(self.value, lst)

    # 5
    def test_no_membership(self):
        lst = ['x', 'yz']
        self.assertNotIn('xyz', lst)

    # 6
    # def test_experience(self):
    #     # commented out because requires extra setup
    #     with self.assertRaises(NoExperienceError):
    #         employee.hire

    # 7
    # def test_is_numeric(self):
    #     self.assertIsInstance(self.value, Numeric)

    # 8
    # def test_same_obj(self):
    #     lst = ['abc', 11]
    #     self.assertIs(lst, list.process())

if __name__ == "__main__":
    unittest.main()