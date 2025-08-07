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
