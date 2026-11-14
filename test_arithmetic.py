import unittest
from arithmetic import add, multiply

class ArithmeticTests(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative(self):
        self.assertEqual(add(-2, 3), 1)
    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(9, 0), 0)
    def test_multiply_two_negatives(self):
        self.assertEqual(multiply(-2, -3), 6)

if __name__ == "__main__":
    unittest.main()
