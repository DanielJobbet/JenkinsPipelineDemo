import src.factorial as factorial

def test_zero(self):
    assert factorial(0) == 1, "Factorial of 0 should be 1!"

def test_some_numbers(self):
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
