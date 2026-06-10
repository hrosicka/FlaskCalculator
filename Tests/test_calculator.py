import unittest
from decimal import Decimal
import sys

# Setting the path to the module to be tested
sys.path.append("../FlaskCalculator")
from main import Calculator, validate_input


class TestCalculator(unittest.TestCase):

    def test_add(self):
        calc = Calculator(Decimal("2"), Decimal("7"), "add")
        self.assertEqual(calc.calculate(), Decimal("9"))

    def test_subtract(self):
        calc = Calculator(Decimal("5"), Decimal("-3"), "subtract")
        self.assertEqual(calc.calculate(), Decimal("8"))

    def test_multiply(self):
        calc = Calculator(Decimal("-2"), Decimal("-3"), "multiply")
        self.assertEqual(calc.calculate(), Decimal("6"))

    def test_divide(self):
        calc = Calculator(Decimal("16"), Decimal("2.5"), "divide")
        self.assertEqual(calc.calculate(), Decimal("6.4"))

    def test_divide_by_zero(self):
        calc = Calculator(Decimal("96"), Decimal("0"), "divide")
        self.assertEqual(calc.calculate(), "Division by zero is not allowed.")

    def test_invalid_operation(self):
        calc = Calculator(Decimal("6"), Decimal("3"), "invalid")
        self.assertEqual(calc.calculate(), "Invalid operation.")


class TestValidateInput(unittest.TestCase):

    def test_valid_input(self):
        num1, num2 = validate_input("2", "-93.5")
        self.assertEqual(num1, Decimal("2"))
        self.assertEqual(num2, Decimal("-93.5"))

    def test_invalid_input(self):
        num1, num2 = validate_input("abc", "3.5")
        self.assertIsNone(num1)
        self.assertIsNone(num2)

        num1, num2 = validate_input("2", "test")
        self.assertIsNone(num1)
        self.assertIsNone(num2)

        num1, num2 = validate_input("abc", "xyz")
        self.assertIsNone(num1)
        self.assertIsNone(num2)


if __name__ == "__main__":
    unittest.main()
