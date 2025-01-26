import unittest

class MathUtils:
    def __init__(self):
        self.a = None
        self.b = None

    def add(self, a, b):
        self.a = a
        self.b = b
        return self.a + self.b

    def subtract(self, a, b):
        self.a = a
        self.b = b
        return self.a - self.b

    def multiply(self, a, b):
        self.a = a
        self.b = b
        return self.a * self.b

    def divide(self, a, b):
        self.a = a
        self.b = b
        if self.b == 0:
            raise ValueError("Division by zero is not allowed.")
        return self.a / self.b


class TestMathUtils(unittest.TestCase):
    def setUp(self):
        self.math_utils = MathUtils()

    def test_add(self):
        result = self.math_utils.add(5, 7)
        self.assertEqual(result, 12)

    def test_subtract(self):
        result = self.math_utils.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = self.math_utils.multiply(3, 6)
        self.assertEqual(result, 18)

    def test_divide(self):
        result = self.math_utils.divide(8, 2)
        self.assertEqual(result, 4.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.math_utils.divide(8, 0)


if __name__ == "__main__":
    unittest.main()
