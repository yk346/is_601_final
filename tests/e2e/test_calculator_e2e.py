# # test_calculator_e2e

import pytest
import re
from uuid import uuid4
from playwright.sync_api import Page, expect

@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:8000"

@pytest.fixture(scope="function")
def create_and_login_user(page: Page, base_url: str):
    username = f"e2euser_{uuid4().hex[:8]}"
    password = "TestPass123!"

    # Register new user
    page.goto(f"{base_url}/login")
    page.click("text=Register")
    page.fill("#first_name", "Test")
    page.fill("#last_name", "User")
    page.fill("#email", f"{username}@example.com")
    page.fill("#username", username)
    page.fill("#password", password)
    page.fill("#confirm_password", password)
    page.click("button:has-text('Create Account')")

    # Wait for redirect to login
    expect(page).to_have_url(re.compile(".*/login.*"))

    # Login
    page.fill("#username", username)
    page.fill("#password", password)
    page.click("button:has-text('Sign in')")

    # Wait for dashboard
    expect(page).to_have_url(re.compile(".*/dashboard.*"))

    return {
        "username": username,
        "password": password
    }

def test_register_and_login(page: Page, create_and_login_user):
    # After login, ensure dashboard URL
    expect(page).to_have_url(re.compile(".*/dashboard.*"))

def test_unauthorized_access_redirect(page: Page):
    # Try accessing dashboard directly without logging in
    page.goto("http://localhost:8000/dashboard")

    # Confirm redirection to login
    expect(page).to_have_url(re.compile(".*/login"))

    # Validate login form is visible
    expect(page.locator("input[name='username']")).to_be_visible()
    expect(page.locator("input[name='password']")).to_be_visible()


def test_create_addition_calculation(page: Page, create_and_login_user):
    expect(page).to_have_url(re.compile(".*/dashboard.*"))

    # Fill out the calculation form
    page.click("text=New Calculation")
    page.select_option("#calcType", "addition")
    page.fill("#calcInputs", "3, 6, 8")
    page.click("button:has-text('Calculate')")

    # Wait for the new result to appear in the table
    row = page.locator("table tbody tr").first  # First row of the history table
    result_cell = row.locator("td").nth(2)  # 3rd column (0-based index)

    expect(result_cell).to_have_text("17")

def test_invalid_input_handling(page: Page, create_and_login_user):
    expect(page).to_have_url(re.compile(".*/dashboard.*"))
    page.click("text=New Calculation")
    page.select_option("#calcType", "addition")
    page.fill("#calcInputs", "abc, 5")
    page.click("button:has-text('Calculate')")

    # Wait for error alert to appear (not immediately fail if it's briefly visible)
    error = page.locator("#errorAlert")

    # Wait until it's attached to DOM and becomes visible
    error.wait_for(state="visible", timeout=3000)

    # Optionally assert content if needed
    expect(error).to_contain_text("Please enter at least two valid numbers")

def test_calculation_deletion_confirm_and_cancel(page: Page, create_and_login_user):
    expect(page).to_have_url(re.compile(".*/dashboard.*"))

    # Create a new calculation
    page.click("text=New Calculation")
    page.select_option("#calcType", "addition")
    page.fill("#calcInputs", "3, 7")
    page.click("button:has-text('Calculate')")

    # Wait for success
    expect(page.locator("#successAlert")).to_be_visible()

    # Back on dashboard
    expect(page).to_have_url(re.compile(".*/dashboard.*"))

    # Find the row with result "10"
    row = page.locator("tr", has_text="10")
    expect(row).to_be_visible()

    # ----------------------------
    # ❌ First test: Click "Cancel"
    # ----------------------------

    def cancel_dialog(dialog):
        assert dialog.type == "confirm"
        assert "Are you sure you want to delete this calculation?" in dialog.message
        dialog.dismiss()  # Clicks "Cancel"

    page.once("dialog", cancel_dialog)

    # Click Delete
    row.locator("button:has-text('Delete')").click()

    # Make sure the row is still there
    expect(row).to_be_visible()

    # ----------------------------
    # ✅ Second test: Click "OK"
    # ----------------------------

    def accept_dialog(dialog):
        assert dialog.type == "confirm"
        assert "Are you sure you want to delete this calculation?" in dialog.message
        dialog.accept()  # Clicks "OK"

    page.once("dialog", accept_dialog)

    # Click Delete again
    row.locator("button:has-text('Delete')").click()

    # Expect success message
    expect(page.locator("#successAlert")).to_be_visible(timeout=3000)

    # Confirm row is gone
    expect(page.locator("tr", has_text="10")).not_to_be_visible(timeout=3000)


@pytest.mark.e2e
def test_right_associative_exponentiation(page: Page, create_and_login_user):
    # Confirm we're on the dashboard
    expect(page).to_have_url(re.compile(".*/dashboard.*"))

    # Open new calculation form
    page.click("text=New Calculation")

    # Select exponentiation operation
    page.select_option("#calcType", "exponentiation")

    # Fill in right-associative inputs: 2 ** (2 ** 3) = 256
    page.fill("#calcInputs", "2, 2, 3")

    # Click calculate
    page.click("button:has-text('Calculate')")

    # Get the first row in the result table
    row = page.locator("table tbody tr").first
    result_cell = row.locator("td").nth(2)  # 3rd column (0-based)

    # Verify the result is 256
    expect(result_cell).to_have_text("256")

@pytest.mark.e2e
def test_exponentiation_two_numbers(page: Page, create_and_login_user):
    expect(page).to_have_url(re.compile(".*/dashboard.*"))
    page.click("text=New Calculation")
    page.select_option("#calcType", "exponentiation")
    page.fill("#calcInputs", "2, 3")  # 2^3 = 8
    page.click("button:has-text('Calculate')")
    result = page.locator("table tbody tr").first.locator("td").nth(2)
    expect(result).to_have_text("8")


@pytest.mark.e2e
def test_exponentiation_zero_power(page: Page, create_and_login_user):
    expect(page).to_have_url(re.compile(".*/dashboard.*"))
    page.click("text=New Calculation")
    page.select_option("#calcType", "exponentiation")
    page.fill("#calcInputs", "5, 0")  # 5^0 = 1
    page.click("button:has-text('Calculate')")
    result = page.locator("table tbody tr").first.locator("td").nth(2)
    expect(result).to_have_text("1")


@pytest.mark.e2e
def test_exponentiation_negative_exponent(page: Page, create_and_login_user):
    expect(page).to_have_url(re.compile(".*/dashboard.*"))
    page.click("text=New Calculation")
    page.select_option("#calcType", "exponentiation")
    page.fill("#calcInputs", "2, -2")  # 2^-2 = 0.25
    page.click("button:has-text('Calculate')")
    result = page.locator("table tbody tr").first.locator("td").nth(2)
    expect(result).to_have_text("0.25")


@pytest.mark.e2e
def test_exponentiation_with_floats(page: Page, create_and_login_user):
    expect(page).to_have_url(re.compile(r".*/dashboard.*"))

    page.click("text=New Calculation")
    page.select_option("#calcType", "exponentiation")
    page.fill("#calcInputs", "9, 0.5")  # sqrt(9) = 3.0
    page.click("button:has-text('Calculate')")

    result_cell = page.locator("table tbody tr").first.locator("td").nth(2)
    result_cell.wait_for(timeout=3000)

    actual_text = result_cell.inner_text()
    assert actual_text in ["3", "3.0"], f"Unexpected result: {actual_text}"

#Negative Cases
@pytest.mark.e2e
def test_exponentiation_non_numeric_input(page: Page, create_and_login_user):
    page.click("text=New Calculation")
    page.select_option("#calcType", "exponentiation")
    page.fill("#calcInputs", "2, foo")
    page.click("button:has-text('Calculate')")
    error = page.locator("#errorAlert")
    error.wait_for(state="visible")
    expect(error).to_contain_text("Please enter at least two valid numbers")


@pytest.mark.e2e
def test_exponentiation_empty_input(page: Page, create_and_login_user):
    page.click("text=New Calculation")
    page.select_option("#calcType", "exponentiation")
    page.fill("#calcInputs", "")
    page.click("button:has-text('Calculate')")
    error = page.locator("#errorAlert")
    error.wait_for(state="visible")
    expect(error).to_contain_text("Please enter at least two valid numbers")


@pytest.mark.e2e
def test_exponentiation_single_input(page: Page, create_and_login_user):
    page.click("text=New Calculation")
    page.select_option("#calcType", "exponentiation")
    page.fill("#calcInputs", "2")
    page.click("button:has-text('Calculate')")
    error = page.locator("#errorAlert")
    error.wait_for(state="visible")
    expect(error).to_contain_text("Please enter at least two valid numbers")


@pytest.mark.e2e
def test_modulo_operation_multinumber_input(page: Page, create_and_login_user):
    # Ensure we're on the dashboard
    expect(page).to_have_url(re.compile(".*/dashboard.*"))

    # Navigate to new calculation
    page.click("text=New Calculation")

    # Select modulo operation
    page.select_option("#calcType", "modulo")

    # Example: (100 % 30 % 7) = (100 % 30 = 10, then 10 % 7 = 3)
    page.fill("#calcInputs", "100, 30, 7")

    # Click calculate
    page.click("button:has-text('Calculate')")

    # Wait for result
    row = page.locator("table tbody tr").first
    result_cell = row.locator("td").nth(2)

    # Validate final result
    expect(result_cell).to_have_text("3")

@pytest.mark.e2e
def test_modulo_by_zero_error(page: Page, create_and_login_user):
    expect(page).to_have_url(re.compile(".*/dashboard.*"))

    # Trigger new calculation flow
    page.click("text=New Calculation")
    page.select_option("#calcType", "modulo")
    page.fill("#calcInputs", "5, 0")  # Invalid input
    page.click("button:has-text('Calculate')")

    # Wait for error alert
    error = page.locator("#errorAlert")
    error.wait_for(state="visible", timeout=3000)

    # Assertion (match backend message exactly)
    expect(error).to_contain_text("Cannot perform modulo by zero")

@pytest.mark.e2e
def test_modulo_with_single_input_error(page: Page, create_and_login_user):
    expect(page).to_have_url(re.compile(".*/dashboard.*"))

    page.click("text=New Calculation")
    page.select_option("#calcType", "modulo")
    page.fill("#calcInputs", "42")  # Only one number
    page.click("button:has-text('Calculate')")

    error = page.locator("#errorAlert")
    error.wait_for(state="visible", timeout=3000)

    # Just use a partial string match
    expect(error).to_contain_text("enter at least two")


@pytest.mark.e2e
def test_modulo_with_invalid_input(page: Page, create_and_login_user):
    expect(page).to_have_url(re.compile(".*/dashboard.*"))

    page.click("text=New Calculation")
    page.select_option("#calcType", "modulo")
    page.fill("#calcInputs", "abc, 5")
    page.click("button:has-text('Calculate')")

    error = page.locator("#errorAlert")
    error.wait_for(state="visible", timeout=3000)

    expect(error).to_contain_text("Please enter at least two valid numbers")
