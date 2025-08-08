"""Pydantic model for the patient's social history."""

from pydantic import Field

from .base_schema import BaseSchema


class SocialHistorySchema(BaseSchema):
    """The patient's social history."""

    occupation: str | None = Field(
        default=None,
        description="The patient's occupation.",
    )
    illicit_substances: str | None = Field(
        default=None,
        description="The patient's tobacco, alcohol, and illicit substances use.",
    )
    diet: str | None = Field(
        default=None,
        description="The patient's diet.",
    )
    exercise: str | None = Field(
        default=None,
        description="The patient's exercise.",
    )
