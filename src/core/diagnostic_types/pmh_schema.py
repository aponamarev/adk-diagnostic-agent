"""Pydantic model for the patient's past medical history."""

from pydantic import Field

from .base_schema import BaseSchema


class PastMedicalHistorySchema(BaseSchema):
    """The patient's past medical history."""

    chronic_illnesses: list[str] | None = Field(
        default=None,
        description="The patient's chronic illnesses.",
    )
    past_surgeries: list[str] | None = Field(
        default=None,
        description="The patient's past surgeries.",
    )
    major_accidents: list[str] | None = Field(
        default=None,
        description="The patient's major accidents or injuries.",
    )
