from flask import Flask, render_template, request
from flask_restx import Api, Resource, fields, abort
from decimal import Decimal, InvalidOperation
from loguru import logger
import sys
from typing import Optional

# Initialize Flask application
app = Flask(__name__)

# Initialize Flask-RESTx API
api = Api(
    app,
    version="1.0",
    title="Calculator API",
    description="A simple calculator API with basic arithmetic operations",
    prefix="/api",
    doc="/api/",
)

# Configure Loguru for logging
logger.add("file_{time}.log", rotation="1 day", retention="7 days", level="INFO")
logger.add(sys.stdout, level="INFO")

# Define operation constants
ADD = "add"
SUBTRACT = "subtract"
MULTIPLY = "multiply"
DIVIDE = "divide"


class DivisionByZeroError(Exception):
    """Custom exception for division by zero."""

    pass


class InvalidOperationError(Exception):
    """Custom exception for invalid operation."""

    pass


class Calculator:
    """
    A class for performing basic arithmetic calculations.
    """

    OPERATIONS = {
        ADD: lambda x, y: x + y,
        SUBTRACT: lambda x, y: x - y,
        MULTIPLY: lambda x, y: x * y,
        DIVIDE: lambda x, y: (
            x / y if y != 0 else DivisionByZeroError("Division by zero is not allowed.")
        ),
    }

    def __init__(self, num1: Decimal, num2: Decimal, operation: str):
        """
        Initializes the Calculator instance with two numbers and an operation.

        Args:
            num1 (Decimal): The first number for the calculation.
            num2 (Decimal): The second number for the calculation.
            operation (str): The operation to perform (add, subtract, multiply, divide).
        Raises:
            InvalidOperationError: If the provided operation is invalid.
        """
        if operation not in self.OPERATIONS:
            raise InvalidOperationError(f"Invalid operation: {operation}")
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def calculate(self) -> Decimal:
        """
        Performs the calculation based on the provided operation.

        Returns:
            Decimal: The result of the calculation.
        Raises:
            DivisionByZeroError: If division by zero is attempted.
        """
        operation_func = self.OPERATIONS[self.operation]
        logger.info(f"Calculation performed: {self.num1} {self.operation} {self.num2}")
        return operation_func(self.num1, self.num2)


def validate_input(num_str: str) -> Optional[Decimal]:
    """
    Validates if the input string can be converted to a Decimal number.

    Args:
        num_str (str): The input number as a string.

    Returns:
        Optional[Decimal]: The validated Decimal number, or None if validation fails.
    """
    try:
        return Decimal(num_str)
    except (InvalidOperation, TypeError, ValueError):
        return None


# Define the namespace for the calculator API
ns = api.namespace("calculate", description="Basic arithmetic operations")

# Define the data transfer object (DTO) for the calculator input
calculator_model = api.model(
    "CalculatorInput",
    {
        "num1": fields.String(required=True, description="First number"),
        "num2": fields.String(required=True, description="Second number"),
        "operation": fields.String(
            required=True,
            description=f"Operation ({ADD}, {SUBTRACT}, {MULTIPLY}, {DIVIDE})",
        ),
    },
)

# Define the data transfer object (DTO) for the calculation result
result_model = api.model(
    "Result", {"result": fields.String(description="Calculation result")}
)


@ns.route("/")
class Calculation(Resource):
    """
    Resource representing the calculation endpoint.
    """

    @ns.expect(calculator_model)
    @ns.marshal_with(result_model)
    def post(self):
        """
        Performs a calculation based on the provided input.
        """
        data = api.payload
        num1_str = data.get("num1")
        num2_str = data.get("num2")
        operation = data.get("operation")

        validated_num1 = validate_input(num1_str)
        validated_num2 = validate_input(num2_str)

        if validated_num1 is None or validated_num2 is None:
            abort(400, "Invalid input. Please enter valid numbers.")

        try:
            calc = Calculator(validated_num1, validated_num2, operation)
            result = calc.calculate()
            return {"result": str(result)}
        except DivisionByZeroError as e:
            abort(400, str(e))
        except InvalidOperationError as e:
            abort(400, str(e))


@app.route("/", methods=["GET", "POST"])
def calculator_ui():
    """
    Route for the calculator web user interface.
    Handles both GET requests for displaying the form and POST requests for performing calculations.
    """
    result = None
    error = None

    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operation = request.form.get("operation")

        validated_num1 = validate_input(num1)
        validated_num2 = validate_input(num2)

        if validated_num1 is None or validated_num2 is None:
            error = "Invalid input. Please enter valid numbers."
        else:
            try:
                calc = Calculator(validated_num1, validated_num2, operation)
                result = calc.calculate()
            except DivisionByZeroError as e:
                error = str(e)
            except InvalidOperationError as e:
                error = str(e)

    return render_template("calculator.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
