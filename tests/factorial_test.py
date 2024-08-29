import unittest
from src.factorial import factorial


class FactorialTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1) , "Factorial of 0 should be 1!"

    def test_some_numbers(self):
        self.assertEqual(factorial(2), 2), "The factorial of 2 is not equal to 2!"
        self.assertEqual(factorial(3), 6), "The factorial of 3 is not equal to 6!"
        self.assertEqual(factorial(40), 24), "The factorial of 40 is not equal to 24!"

if __name__ == '__main__':
    unittest.main()