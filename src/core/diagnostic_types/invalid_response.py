from enum import Enum


class InvalidResponseType(Enum):
    """The type of invalid response from the user."""

    NO_RESPONSE = "no_response"
    INVALID_RESPONSE = "invalid_response"
    NOT_RELEVANT = "not_relevant"
    NO_SEVERITY = -1
