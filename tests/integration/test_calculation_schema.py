# tests/unit/test_calculation_schema.py

import pytest
from pydantic import ValidationError
from uuid import uuid4
from datetime import datetime

from app.schemas.calculation import (
    CalculationCreate,
    CalculationUpdate,
    CalculationResponse
)


def test_calculation_create_valid():
    """Test creating a valid CalculationCreate schema."""
    data = {
        "type": "addition",
        "inputs": [10.5, 3.0],
        "user_id": uuid4()
    }
    calc = CalculationCreate(**data)
    assert calc.type == "addition"
    assert calc.inputs == [10.5, 3.0]
    assert calc.user_id is not None


def test_calculation_create_missing_type():
    """Test CalculationCreate fails if 'type' is missing."""
    data = {
        "inputs": [10.5, 3.0],
        "user_id": uuid4()
    }
    with pytest.raises(ValidationError) as exc_info:
        CalculationCreate(**data)

    assert "type\n  Field required" in str(exc_info.value)


def test_calculation_create_missing_inputs():
    """Test CalculationCreate fails if 'inputs' is missing."""
    data = {
        "type": "multiplication",
        "user_id": uuid4()
    }
    with pytest.raises(ValidationError) as exc_info:
        CalculationCreate(**data)

    assert "inputs\n  Field required" in str(exc_info.value)

def test_calculation_create_invalid_inputs():
    """Test CalculationCreate fails if 'inputs' is not a list of floats."""
    data = {
        "type": "division",
        "inputs": "not-a-list",
        "user_id": uuid4()
    }
    with pytest.raises(ValidationError) as exc_info:
        CalculationCreate(**data)

    error_message = str(exc_info.value)
    # Now we match a substring of the new Pydantic 2.x error:
    assert "Input should be a valid list" in error_message, error_message


def test_calculation_create_unsupported_type():
    """Test a scenario for an unsupported type if you had custom validation (optional)."""
    # NOTE: If your schema does not restrict 'type' to certain values,
    # this won't fail at the Pydantic level. But you might have a separate
    # check for allowed calculation types. This is just an example.
    data = {
        "type": "square_root",
        "inputs": [25],
        "user_id": uuid4()
    }
    calc = CalculationCreate(**data)
    assert calc.type == "square_root"


def test_calculation_update_valid():
    """Test a valid partial update with CalculationUpdate."""
    data = {
        "inputs": [42.0, 7.0]
    }
    calc_update = CalculationUpdate(**data)
    assert calc_update.inputs == [42.0, 7.0]


def test_calculation_update_no_fields():
    """Test that an empty update is allowed (i.e., no fields) if that's your desired behavior."""
    calc_update = CalculationUpdate()
    assert calc_update.inputs is None


def test_calculation_response_valid():
    """Test creating a valid CalculationResponse schema."""
    data = {
        "id": uuid4(),
        "user_id": uuid4(),
        "type": "subtraction",
        "inputs": [20, 5],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    calc_response = CalculationResponse(**data)
    assert calc_response.id is not None
    assert calc_response.user_id is not None
    assert calc_response.type == "subtraction"
    assert calc_response.inputs == [20, 5]
