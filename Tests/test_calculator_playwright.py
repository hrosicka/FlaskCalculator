# This file contains Playwright tests for a simple calculator web application.
#         """
#         Performs the calculation based on the initialized numbers and operation.
#         pytest --snapshot-update
#         """
import pytest
from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:5000"


def test_addition(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "5")
    page.fill("#num2", "3")
    page.select_option("#operation", "add")
    page.click("input[type='submit']")
    result = page.locator(".result-box p")
    expect(result).to_have_text("8")


def test_subtraction(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "10")
    page.fill("#num2", "4")
    page.select_option("#operation", "subtract")
    page.click("input[type='submit']")
    result = page.locator(".result-box p")
    expect(result).to_have_text("6")


def test_multiplication(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "6")
    page.fill("#num2", "7")
    page.select_option("#operation", "multiply")
    page.click("input[type='submit']")
    result = page.locator(".result-box p")
    expect(result).to_have_text("42")


def test_division(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "15")
    page.fill("#num2", "3")
    page.select_option("#operation", "divide")
    page.click("input[type='submit']")
    result = page.locator(".result-box p")
    expect(result).to_have_text("5")


def test_division_by_zero(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "10")
    page.fill("#num2", "0")
    page.select_option("#operation", "divide")
    page.click("input[type='submit']")
    error = page.locator(".result-box p")
    expect(error).to_have_text("Division by zero is not allowed.")


def test_decimal_numbers_addition(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "2.5")
    page.fill("#num2", "1.5")
    page.select_option("#operation", "add")
    page.click("input[type='submit']")
    result = page.locator(".result-box p")
    expect(result).to_have_text("4.0")


def test_negative_numbers_subtraction(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "-5")
    page.fill("#num2", "-2")
    page.select_option("#operation", "subtract")
    page.click("input[type='submit']")
    result = page.locator(".result-box p")
    expect(result).to_have_text("-3")


def test_large_numbers_multiplication(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "1000000")
    page.fill("#num2", "2000")
    page.select_option("#operation", "multiply")
    page.click("input[type='submit']")
    result = page.locator(".result-box p")
    expect(result).to_have_text("2000000000")


def test_decimal_and_negative_multiplication(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "3.14")
    page.fill("#num2", "-2")
    page.select_option("#operation", "multiply")
    page.click("input[type='submit']")
    result = page.locator(".result-box p")
    expect(result).to_have_text("-6.28")


def test_decimal_division(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "7.5")
    page.fill("#num2", "2.5")
    page.select_option("#operation", "divide")
    page.click("input[type='submit']")
    result = page.locator(".result-box p")
    expect(result).to_have_text("3")


def test_empty_first_number(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "")
    page.fill("#num2", "5")
    page.click("input[type='submit']")
    error = page.locator(".result-box p")
    expect(error).to_have_text("Invalid input. Please enter valid numbers.")


def test_empty_second_number(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "10")
    page.fill("#num2", "")
    page.click("input[type='submit']")
    error = page.locator(".result-box p")
    expect(error).to_have_text("Invalid input. Please enter valid numbers.")


def test_both_numbers_empty(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "")
    page.fill("#num2", "")
    page.click("input[type='submit']")
    error = page.locator(".result-box p")
    expect(error).to_have_text("Invalid input. Please enter valid numbers.")


def test_decimal_input_whole_number_result_addition(page: Page):
    page.goto(BASE_URL)
    page.fill("#num1", "2.5")
    page.fill("#num2", "2.5")
    page.select_option("#operation", "add")
    page.click("input[type='submit']")
    result = page.locator(".result-box p")
    expect(result).to_have_text("5.0")


def test_calculator_layout(page: Page, snapshot):
    page.goto(BASE_URL)
    screenshot = page.screenshot()
    snapshot.assert_match(screenshot, "calculator_initial_layout.png")
