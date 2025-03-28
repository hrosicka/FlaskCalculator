from flask import Flask, render_template, request
from decimal import Decimal, InvalidOperation
from loguru import logger
import sys

app = Flask(__name__)

# Configure Loguru
logger.add("file_{time}.log", rotation="1 day", retention="7 days", level="INFO")
logger.add(sys.stdout, level="INFO")

class Calculator:
    """Class for performing arithmetic calculations."""

    OPERATIONS = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Division by zero is not allowed.",
    }

    def __init__(self, num1, num2, operation):
        """Initialize calculator with numbers and operation."""
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def calculate(self):
        """Perform calculation based on the operation."""
        operation_func = self.OPERATIONS.get(self.operation)
        if operation_func:
            try:
                result = operation_func(self.num1, self.num2)
                logger.info(f"Calculation performed: {self.num1} {self.operation} {self.num2} = {result}")
                return result
            except Exception as e:
                logger.error(f"Error during calculation: {e}")
                return "An error occurred during calculation."
        return "Invalid operation."
    
def validate_input(num1, num2):
    """Validate input numbers."""
    try:
        return Decimal(num1), Decimal(num2)
    except (InvalidOperation, TypeError, ValueError):
        return None, None


@app.route("/", methods=["GET", "POST"])
def calculator():
    """Route for calculator functionality."""
    result = None
    error = None

    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operation = request.form.get("operation")

        validated_num1, validated_num2 = validate_input(num1, num2)

        if validated_num1 is None or validated_num2 is None:
            error = "Invalid input. Please enter valid numbers."
        else:
            calc = Calculator(validated_num1, validated_num2, operation)
            result = calc.calculate()

    return render_template("calculator.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)