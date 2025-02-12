from datetime import datetime, timezone
import requests
import pytest

@pytest.fixture
def base_url(fastapi_server: str) -> str:
    """
    Returns the FastAPI server base URL without a trailing slash.
    """
    return fastapi_server.rstrip("/")

def test_health_endpoint(base_url: str):
    """
    Verify that the /health endpoint returns {"status": "ok"}.
    """
    url = f"{base_url}/health"
    response = requests.get(url)
    assert response.status_code == 200, (
        f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
    )
    assert response.json() == {"status": "ok"}, "Unexpected response from /health."

def test_user_registration(base_url: str):
    """
    Test the user registration endpoint by posting valid user data and verifying
    that the response contains the expected fields.
    """
    url = f"{base_url}/auth/register"
    payload = {
        "first_name": "Alice",
        "last_name": "Smith",
        "email": "alice.smith@example.com",
        "username": "alicesmith",
        "password": "SecurePass123!",
        "confirm_password": "SecurePass123!"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201, (
        f"Expected 201 but got {response.status_code}. Response: {response.text}"
    )
    data = response.json()
    for key in ["id", "username", "email", "first_name", "last_name", "is_active", "is_verified"]:
        assert key in data, f"Field '{key}' missing in registration response."
    assert data["username"] == "alicesmith"
    assert data["email"] == "alice.smith@example.com"
    assert data["first_name"] == "Alice"
    assert data["last_name"] == "Smith"
    assert data["is_active"] is True
    assert data["is_verified"] is False

def _parse_datetime(dt_str: str) -> datetime:
    """Helper function to parse datetime strings from API responses."""
    if dt_str.endswith('Z'):
        dt_str = dt_str.replace('Z', '+00:00')
    return datetime.fromisoformat(dt_str)

def test_user_login(base_url: str):
    """
    Test the user login endpoint by:
      - Registering a new user
      - Logging in with that user's credentials
      - Verifying that the response contains tokens and user details
      - Verifying the token structure and data types
    """
    reg_url = f"{base_url}/auth/register"
    login_url = f"{base_url}/auth/login"
    
    # Test user data
    test_user = {
        "first_name": "Bob",
        "last_name": "Jones",
        "email": "bob.jones@example.com",
        "username": "bobjones",
        "password": "SecurePass123!",
        "confirm_password": "SecurePass123!"
    }
    
    # Step 1: Register a new user
    reg_response = requests.post(reg_url, json=test_user)
    assert reg_response.status_code == 201, f"User registration failed: {reg_response.text}"
    
    # Step 2: Login with the registered user
    login_payload = {
        "username": test_user["username"],
        "password": test_user["password"]
    }
    login_response = requests.post(login_url, json=login_payload)
    
    # Step 3: Verify response status
    assert login_response.status_code == 200, f"Login failed: {login_response.text}"
    
    # Step 4: Verify response structure
    login_data = login_response.json()
    
    # Required fields in TokenResponse
    required_fields = {
        "access_token": str,
        "refresh_token": str,
        "token_type": str,
        "expires_at": str,  # ISO format datetime string
        "user_id": str,     # UUID string
        "username": str,
        "email": str,
        "first_name": str,
        "last_name": str,
        "is_active": bool,
        "is_verified": bool
    }
    
    # Verify all required fields exist and have correct types
    for field, expected_type in required_fields.items():
        assert field in login_data, f"Missing field: {field}"
        assert isinstance(login_data[field], expected_type), \
            f"Field {field} has wrong type. Expected {expected_type}, got {type(login_data[field])}"
    
    # Step 5: Verify token format
    assert login_data["token_type"].lower() == "bearer", "Token type should be 'bearer'"
    assert len(login_data["access_token"]) > 0, "Access token should not be empty"
    assert len(login_data["refresh_token"]) > 0, "Refresh token should not be empty"
    
    # Step 6: Verify user data matches registration
    assert login_data["username"] == test_user["username"]
    assert login_data["email"] == test_user["email"]
    assert login_data["first_name"] == test_user["first_name"]
    assert login_data["last_name"] == test_user["last_name"]
    assert login_data["is_active"] is True
    
    # Step 7: Verify expires_at is a valid future datetime
    # Ensure we're comparing timezone-aware datetimes
    expires_at = _parse_datetime(login_data["expires_at"])
    current_time = datetime.now(timezone.utc)
    
    assert expires_at.tzinfo is not None, "expires_at should be timezone-aware"
    assert current_time.tzinfo is not None, "current_time should be timezone-aware"
    assert expires_at > current_time, "Token expiration should be in the future"