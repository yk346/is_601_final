# app/schemas/calculation.py

from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class CalculationBase(BaseModel):
    """
    Base schema with common Calculation fields.
    Use this for shared logic/validation across create/update schemas.
    """
    type: str = Field(
        ...,
        description="Type of calculation (e.g. 'addition', 'subtraction', 'multiplication', 'division')",
        example="addition"
    )
    inputs: List[float] = Field(
        ...,
        description="List of numeric inputs for the calculation.",
        example=[10.5, 3, 2]
    )

    model_config = ConfigDict(from_attributes=True)


class CalculationCreate(CalculationBase):
    """
    Schema for creating a new Calculation.
    Usually requires a user_id to link the calculation to a user.
    """
    user_id: UUID = Field(
        ...,
        description="UUID of the user who owns this calculation",
        example="123e4567-e89b-12d3-a456-426614174000"
    )


class CalculationUpdate(BaseModel):
    """
    Schema for updating an existing Calculation.
    You might only allow updating the inputs, for example.
    """
    inputs: Optional[List[float]] = Field(
        None,
        description="Updated list of numeric inputs for the calculation.",
        example=[42, 7]
    )

    model_config = ConfigDict(from_attributes=True)


class CalculationResponse(CalculationBase):
    """
    Schema for reading a Calculation from the database.
    Includes fields like ID, timestamps, and user_id.
    """
    id: UUID = Field(
        ...,
        description="Unique UUID of the calculation",
        example="123e4567-e89b-12d3-a456-426614174999"
    )
    user_id: UUID = Field(
        ...,
        description="UUID of the user who owns this calculation",
        example="123e4567-e89b-12d3-a456-426614174000"
    )
    created_at: datetime = Field(..., description="Time when the calculation was created")
    updated_at: datetime = Field(..., description="Time when the calculation was last updated")

    # If you want to expose the result directly, you could add something like:
    # result: Optional[float] = Field(None, description="Result of the calculation")

    model_config = ConfigDict(from_attributes=True)
