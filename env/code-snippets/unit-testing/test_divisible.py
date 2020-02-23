import unittest
from divisible import divisible_by

class DivisibleTestCase(unittest.TestCase):
    # it has to start with test_
    def test_divisble_by(self):
        self.assertFalse(divisible_by(8,3))
        self.assertTrue(divisible_by(8,2))

if __name__ == "__main__":
    unittest.main()