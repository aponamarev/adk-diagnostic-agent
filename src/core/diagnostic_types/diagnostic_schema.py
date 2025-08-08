from google.adk.sessions.state import State
from pydantic import Field

from core.diagnostic_types.medications_and_allergies_schema import (
    MedicationsAndAllergiesSchema,
)
from core.diagnostic_types.pmh_schema import PastMedicalHistorySchema
from core.settings import diagnostic_settings

from .base_schema import BaseSchema
from .chief_complaint_schema import ChiefComplaintSchema


class DiagnosticSchema(BaseSchema):
    """The schema for the diagnostic information."""

    chief_complaint: ChiefComplaintSchema = Field(
        default=ChiefComplaintSchema(),
        description="The primary reason the patient is seeking medical attention.",
    )
    past_medical_history: PastMedicalHistorySchema = Field(
        default=PastMedicalHistorySchema(),
        description="The patient's past medical history.",
    )
    medications_and_allergies: MedicationsAndAllergiesSchema = Field(
        default=MedicationsAndAllergiesSchema(),
        description="The patient's medications and allergies.",
    )
    # TODO: Fine-tune prompt for question generation for better user experience
    #         before adding SocialHistry
    # social_history: SocialHistorySchema = Field(
    #     default=SocialHistorySchema(),
    #     description="The patient's social history.",
    # )


def collect_missing_information(
    state: State,
) -> set[str]:
    """Return required keys that are absent from ctx.state (existence check only)."""
    required_fields = DiagnosticSchema.flatten_names()

    missing_keys = set()
    for field_name in required_fields:
        diagnostic_field_name = f"{diagnostic_settings.diagnostic_field}:{field_name}"
        container = state
        value = None
        for key in diagnostic_field_name.split(":"):
            value = container.get(key, {})
            container = value
        if value is None or value == {}:
            missing_keys.add(field_name)

    return missing_keys


__all__ = ["DiagnosticSchema", "collect_missing_information"]
