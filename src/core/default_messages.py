"""Application wide default messages that are used by various agents."""

from enum import Enum


class DiagnosticDefaultMessages(Enum):
    """Default messages for the diagnostic collection agent."""

    ALL_INFORMATION_COLLECTED = (
        "All required information for the diagnosis is collected!"
    )
