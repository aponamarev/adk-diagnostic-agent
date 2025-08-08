"""Pydantic model for the patient's chief complaint details."""

from pydantic import Field

from .base_schema import BaseSchema


class ChiefComplaintSchema(BaseSchema):
    """The primary reason the patient is seeking medical attention."""

    complaint: str | None = Field(
        default=None,
        description="The primary reason the patient is seeking medical attention.",
    )
    onset: str | None = Field(
        default=None,
        description="When did it start? Was it sudden or gradual?",
    )
    alleviating_factors: list[str] | None = Field(
        default=None,
        description="What makes it better or worse?",
    )
    severity: int | None = Field(
        default=None, description="On a scale of 1 to 10, how bad is it?"
    )
