# Simple Web Calculator with Flask

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Language](https://img.shields.io/badge/language-Python-blue.svg)
![GitHub stars](https://img.shields.io/github/stars/hrosicka/FlaskCalculator.svg?style=social&label=Star)
![GitHub issues](https://img.shields.io/github/issues/hrosicka/FlaskCalculator)
![Repo size](https://img.shields.io/github/repo-size/hrosicka/FlaskCalculator)
![Last Commit](https://img.shields.io/github/last-commit/hrosicka/FlaskCalculator)

- This repository contains a clean and user-friendly web calculator built with Flask, HTML, and CSS. 
- It's designed to be simple to use while providing a modern and intuitive interface.

  ![](https://github.com/hrosicka/FlaskCalculator/blob/master/doc/Calculator1.PNG)

## Features

-   **Basic Arithmetic Operations:** Perform addition, subtraction, multiplication, and division.
-   **User-Friendly Interface:** Clean and modern design with a focus on usability.
-   **Input Validation:** Handles invalid input and division by zero errors gracefully.
-   **Responsive Design:** Looks great on various screen sizes.
-   **Google Fonts Integration:** Uses Roboto font for a polished look.
-   **RESTful API:** Provides an API for performing calculations programmatically.
-   **Swagger Documentation:** Automatically generated API documentation using Flask-RESTx, accessible through a web interface.
-   **Unit Tests:** Includes comprehensive unit tests to ensure the reliability of the backend calculation logic and input validation.
-   **Logging:** Implements logging using Loguru to track application activity and errors.


## Technologies Used

-   **Flask:** A lightweight Python web framework.
-   **HTML:** For structuring the web page.
-   **CSS:** For styling and layout.
-   **Google Fonts:** For beautiful typography (Roboto).
-   **Decimal:** Python's `Decimal` type for precise arithmetic calculations.
-   **Loguru:** A Python logging library for structured and informative logs.
-   **unittest:** Python's built-in testing framework for writing and running unit tests.

## Getting Started

1.  **Clone the repository:**

    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install Flask Flask-RESTx Loguru
    ```

4.  **Run the application:**

    ```bash
    python app.py
    ```

5.  **Open your browser:**
    -   **Web Interface:** Navigate to `http://127.0.0.1:5000/` to use the web calculator.
    -   **Swagger UI:** Navigate to `http://127.0.0.1:5000/api/` to access the automatically generated API documentation and try out the API endpoints.

## Usage

### Web Interface

Simply enter two numbers in the respective fields, select the desired operation from the dropdown, and click the "Calculate" button to get the result. The application will handle any invalid input (non-numeric values) and division by zero errors, displaying an appropriate message.

### REST API

The calculator exposes a RESTful API under the `/api` prefix. You can interact with the calculator programmatically by sending a `POST` request to the `/api/calculate/` endpoint with a JSON payload containing the following fields:

-   `num1`: The first number (as a string).
-   `num2`: The second number (as a string).
-   `operation`: The operation to perform (a string: "add", "subtract", "multiply", or "divide").

**Example using `curl`:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"num1": "10", "num2": "5", "operation": "add"}' [http://127.0.0.1:5000/api/calculate/](http://127.0.0.1:5000/api/calculate/)
```

The API will return a JSON response with the result of the calculation as a string. It also handles invalid input and division by zero, returning appropriate error messages with an HTTP status code of 400.

## Unit Tests

Unit tests are included to verify the functionality of the Calculator class and the validate_input function.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy calculating! 🚀
