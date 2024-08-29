import unittest
import src.factorial as factorial


class FactorialTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1) , "Factorial of 0 should be 1!"

    def test_some_numbers(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)

if __name__ == '__main__':
    unittest.main()