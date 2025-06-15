import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create an instance of SimpleCalculator before each test."""
        self.calc = SimpleCalculator()

    # --- Test Addition ---
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)                 # Pos + Pos
        self.assertEqual(self.calc.add(-1, 1), 0)                # Neg + Pos = 0
        self.assertEqual(self.calc.add(0, 0), 0)                 # 0 + 0
        self.assertEqual(self.calc.add(-5, -7), -12)             # Neg + Neg
        self.assertAlmostEqual(self.calc.add(1.1, 2.2), 3.3)     # Float addition

    # --- Test Subtraction ---
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)           # Pos - Pos
        self.assertEqual(self.calc.subtract(-1, -1), 0)          # Neg - Neg = 0
        self.assertEqual(self.calc.subtract(0, 10), -10)         # 0 - Pos
        self.assertEqual(self.calc.subtract(5, 10), -5)          # Smaller - Larger
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)  # Float subtraction

    # --- Test Multiplication ---
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)           # Pos * Pos
        self.assertEqual(self.calc.multiply(-2, 3), -6)          # Neg * Pos
        self.assertEqual(self.calc.multiply(0, 100), 0)          # 0 * X
        self.assertEqual(self.calc.multiply(-2, -3), 6)          # Neg * Neg
        self.assertAlmostEqual(self.calc.multiply(1.5, 2), 3.0)  # Float multiplication

    # --- Test Division ---
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)             # Pos / Pos
        self.assertEqual(self.calc.divide(-9, 3), -3)            # Neg / Pos
        self.assertEqual(self.calc.divide(0, 5), 0)              # 0 / X
        self.assertIsNone(self.calc.divide(5, 0))                # Division by zero

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)      # Float result
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333)

if __name__ == '__main__':
    unittest.main()
