"""Pydantic model for the patient's medications and allergies."""

from pydantic import Field

from .base_schema import BaseSchema


class MedicationsAndAllergiesSchema(BaseSchema):
    """The patient's medications and allergies."""

    medications: list[str] | None = Field(
        default=None,
        description="The patient's medications.",
    )
    allergies: list[str] | None = Field(
        default=None,
        description="The patient's allergies.",
    )
