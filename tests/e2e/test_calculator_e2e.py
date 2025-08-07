# # test_calculator_e2e
# import pytest
# from playwright.sync_api import Page, expect

# @pytest.fixture(scope="session")
# def base_url():
#     return "http://localhost:8000"

# def test_register_and_login(page: Page, base_url: str):
#     username = f"e2euser"
#     password = "TestPass123!"

#     page.goto(f"{base_url}/login")
#     page.click("text=Register")

#     page.fill("#first_name", "Test")
#     page.fill("#last_name", "User")
#     page.fill("#email", f"{username}@example.com")
#     page.fill("#username", username)
#     page.fill("#password", password)
#     page.fill("#confirm_password", password)

#     page.click("button:has-text('Create Account')")
#     page.wait_for_url("**/login")

#     page.fill("#username", username)
#     page.fill("#password", password)
#     page.click("button:has-text('Sign in')")

#     page.wait_for_url("**/dashboard")
#     assert "/dashboard" in page.url


# @pytest.fixture(scope="function")
# def login(page: Page, base_url: str):
#     # You need an existing user for this test
#     username = f"e2euser"  # Must be in DB
#     password = "SecurePass123!"

#     page.goto(f"{base_url}/login")
#     page.fill("#username", username)
#     page.fill("#password", password)
#     page.click("button:has-text('Sign in')")
#     page.wait_for_url("**/dashboard")
#     expect(page).to_have_url(lambda url: "/dashboard" in url)
    
# def test_create_addition_calculation(page: Page, login):
#     page.click("text=New Calculation")
#     page.select_option("#calcType", "addition")
#     page.fill("#calcInputs", "5, 10, 15")
#     page.click("button:has-text('Calculate')")
#     expect(page.locator("text=Result")).to_contain_text("30")

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

