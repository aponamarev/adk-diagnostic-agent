from google.adk.agents.callback_context import CallbackContext

from core.default_messages import DiagnosticDefaultMessages
from core.diagnostic_types.diagnostic_schema import collect_missing_information
from core.settings import diagnostic_settings


def update_missing_information(callback_context: CallbackContext) -> None:
    """Update the missing information tag in the callback context."""
    state = callback_context.state
    missing_information = collect_missing_information(state)
    if missing_information:
        content = "The following information is missing: " + ", ".join(
            missing_information
        )
        state[diagnostic_settings.missing_information_field] = content
    else:
        state[diagnostic_settings.missing_information_field] = (
            DiagnosticDefaultMessages.ALL_INFORMATION_COLLECTED.value
        )


def initialize_state(callback_context: CallbackContext) -> None:
    """Lazy initialization of the diagnostic information fields."""
    state = callback_context.state
    if diagnostic_settings.diagnostic_field not in state:
        state[diagnostic_settings.diagnostic_field] = {}
    if diagnostic_settings.missing_information_field not in state:
        update_missing_information(callback_context)
