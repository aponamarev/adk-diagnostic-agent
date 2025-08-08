from pydantic import BaseModel, Field

from .invalid_response import InvalidResponseType


class ChiefComplaintType(BaseModel):
    """The primary reason the patient is seeking medical attention."""

    complaint: str = Field(
        description="The primary reason the patient is seeking medical attention.",
        default=InvalidResponseType.NO_RESPONSE.value,
    )
    onset: str = Field(
        description="When did it start? Was it sudden or gradual?",
        default=InvalidResponseType.NO_RESPONSE.value,
    )
    severity: int = Field(
        description="On a scale of 1 to 10, how bad is it?",
        default=InvalidResponseType.NO_SEVERITY.value,
    )
